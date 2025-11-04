from dotenv import load_dotenv
import logging

from livekit import agents
from livekit.agents import (
    AgentSession,
    Agent,
    RunContext,
    function_tool,
    cli,
    WorkerOptions,
)
from livekit.plugins import deepgram, openai, cartesia, silero
from demo_prompts import SYSTEM_PROMPT, GREETING_PROMPT

load_dotenv(".env.local")
logger = logging.getLogger("dr-immobilien-demo")
logger.setLevel(logging.INFO)


class ImmobilienAgent(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=SYSTEM_PROMPT)
    
    async def on_enter(self):
        """Called when agent becomes active - start the conversation"""
        await self.session.generate_reply(instructions=GREETING_PROMPT)
    
    @function_tool
    async def get_firmeninfos(self, context: RunContext) -> str:
        """Zeige Firmeninformationen von DR Immobilien"""
        return """DR Immobilien & Partners GmbH
Milchstraße 9, 85049 Ingolstadt

Öffnungszeiten:
Montag-Donnerstag: 08:30-17:30 Uhr
Freitag: 08:30-12:00 Uhr
Samstag-Sonntag: Geschlossen

E-Mail: info@richarz-immobilien.de"""
    
    @function_tool
    async def kontakt_aufnehmen(
        self,
        context: RunContext,
        name: str,
        telefon: str,
        anliegen: str,
    ) -> str:
        """
        Nimm Kontaktdaten eines Interessenten auf.
        
        Args:
            name: Name des Kunden
            telefon: Telefonnummer
            anliegen: Was möchte der Kunde (z.B. "Wohnung mieten", "Haus kaufen")
        """
        logger.info(f"Kontakt: {name}, Tel: {telefon}, Anliegen: {anliegen}")
        return f"Vielen Dank {name}! Wir melden uns bei Ihnen unter {telefon} bezüglich '{anliegen}'."


async def entrypoint(ctx: agents.JobContext):
    """Main entrypoint for the demo voice agent"""
    logger.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect()
    
    # Create agent session (Context7 Method 2: Plugin classes for language support)
    session = AgentSession(
        vad=silero.VAD.load(),
        stt=deepgram.STT(
            model="nova-3",
            language="de",  # German language
            detect_language=False,
        ),
        llm=openai.LLM(
            model="gpt-4o-mini",
            temperature=0.7,
        ),
        tts=cartesia.TTS(
            model="sonic-2",
            voice="b9de4a89-2257-424b-94c2-db18ba68c81a",  # German female voice
            language="de",  # German language for numbers and text
        ),
    )
    
    await session.start(
        room=ctx.room,
        agent=ImmobilienAgent(),
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
