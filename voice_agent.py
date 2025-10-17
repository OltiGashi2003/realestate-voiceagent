from dotenv import load_dotenv
import logging

from livekit import agents, api
from livekit.agents import (
    AgentSession,
    Agent,
    RunContext,
    function_tool,
    get_job_context,
    cli,
    WorkerOptions,
)
from livekit.plugins import google
from system_prompts import SYSTEM_PROMPT, GREETING_PROMPT
from property_database import (
    search_properties,
    get_property_by_id,
    get_districts,
    get_property_types,
)

load_dotenv(".env.local")
logger = logging.getLogger("immobilien-agent")
logger.setLevel(logging.INFO)


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=SYSTEM_PROMPT,
        )

    async def hangup(self):
        """Helper function to hang up the call by deleting the room"""
        job_ctx = get_job_context()
        await job_ctx.api.room.delete_room(
            api.DeleteRoomRequest(room=job_ctx.room.name)
        )

    @function_tool
    async def search_immobilien(
        self,
        context: RunContext,
        listing_type: str = None,
        property_type: str = None,
        district: str = None,
        min_price: int = None,
        max_price: int = None,
        min_rooms: float = None,
        max_rooms: float = None,
    ) -> str:
        """Suche nach Immobilien basierend auf Kriterien.

        Args:
            listing_type: "Miete" oder "Kauf"
            property_type: "Wohnung", "Haus", "Penthouse", oder "Reihenhaus"
            district: Stadtteil Name (z.B. "Zentrum", "Haunwöhr", "Nordwest")
            min_price: Mindestpreis (monatlich für Miete, Kaufpreis für Kauf)
            max_price: Höchstpreis
            min_rooms: Mindestanzahl Zimmer
            max_rooms: Höchstanzahl Zimmer
        """
        logger.info(f"Searching properties: type={listing_type}, property={property_type}, district={district}")
        
        results = search_properties(
            listing_type=listing_type,
            property_type=property_type,
            district=district,
            min_price=min_price,
            max_price=max_price,
            min_rooms=min_rooms,
            max_rooms=max_rooms,
        )
        
        if not results:
            return "Leider keine Immobilien gefunden, die Ihren Kriterien entsprechen."
        
        # Format results for the LLM
        response = f"Ich habe {len(results)} Immobilien gefunden:\n\n"
        for prop in results[:5]:  # Limit to first 5 results
            response += f"ID: {prop.id} - {prop.title}\n"
            response += f"  {prop.type} in {prop.district}\n"
            response += f"  {prop.rooms} Zimmer, {prop.size}m²\n"
            response += f"  Preis: {prop.price}€ ({prop.listing_type})\n"
            response += f"  Verfügbar: {'Ja' if prop.available else 'Nein'}\n\n"
        
        if len(results) > 5:
            response += f"...und {len(results) - 5} weitere Immobilien."
        
        return response

    @function_tool
    async def get_immobilie_details(
        self,
        context: RunContext,
        property_id: str
    ) -> str:
        """Hole detaillierte Informationen zu einer bestimmten Immobilie.

        Args:
            property_id: Die ID der Immobilie (z.B. "A001", "H003")
        """
        logger.info(f"Getting property details for: {property_id}")
        
        prop = get_property_by_id(property_id)
        
        if not prop:
            return f"Immobilie mit ID {property_id} nicht gefunden."
        
        # Format detailed information
        response = f"{prop.title}\n\n"
        response += f"Typ: {prop.type}\n"
        response += f"Adresse: {prop.address}, {prop.district}\n"
        response += f"Zimmer: {prop.rooms} ({prop.bedrooms} Schlafzimmer)\n"
        response += f"Größe: {prop.size}m²\n"
        response += f"Preis: {prop.price}€ ({prop.listing_type})\n"
        response += f"Badezimmer: {prop.bathrooms}\n"
        response += f"Verfügbar: {'Ja' if prop.available else 'Nein'}\n\n"
        response += f"Ausstattung: {', '.join(prop.features)}\n\n"
        response += f"Beschreibung: {prop.description}"
        
        return response

    @function_tool
    async def get_available_districts(self, context: RunContext) -> str:
        """Hole eine Liste aller verfügbaren Stadtteile in Ingolstadt."""
        districts = get_districts()
        return f"Verfügbare Stadtteile: {', '.join(districts)}"

    @function_tool
    async def end_call(self, context: RunContext) -> None:
        """Called when the user wants to end the call"""
        logger.info(f"ending the call")
        
        # let the agent finish speaking
        current_speech = context.session.current_speech
        if current_speech:
            await current_speech.wait_for_playout()
        
        await self.hangup()

    @function_tool
    async def detected_answering_machine(self, context: RunContext) -> None:
        """Called when the call reaches voicemail. Use this tool AFTER you hear the voicemail greeting"""
        logger.info(f"detected answering machine")
        await self.hangup()


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()
    
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Kore",
            temperature=0.8,
            instructions=SYSTEM_PROMPT,
            language="de-DE",
        ),
        # Detect when user is away/inactive for 30 seconds
        user_away_timeout=30.0,
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
    )

    await session.generate_reply(
        instructions=GREETING_PROMPT
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))