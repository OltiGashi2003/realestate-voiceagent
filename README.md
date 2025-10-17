# DR-Immobilien Voice Agent

A German-language LiveKit voice agent for real estate inquiries in Ingolstadt, powered by Google Gemini 2.0 Flash Experimental.

## Features

- 🎙️ **Voice Interaction**: Natural German conversations using Gemini Realtime API with "Kore" voice
- 🏠 **Property Search**: Search through apartments and houses in Ingolstadt
- 📍 **District-Based Search**: Filter properties by 9 districts in Ingolstadt
- 💰 **Advanced Filters**: Search by listing type, property type, price range, and room count
- 📞 **Call Management**: Automatic hangup detection and voicemail recognition
- 🔍 **Property Details**: Get comprehensive information about specific properties

## Project Structure

```
livekit-voice-agent/
├── voice_agent.py          # Main agent implementation
├── property_database.py    # Sample property data (20 properties)
├── system_prompts.py       # German system prompts
├── pyproject.toml          # Project dependencies
└── .env.local              # Environment variables (not tracked)
```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/OltiGashi2003/realestate-voiceagent.git
   cd realestate-voiceagent
   ```

2. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

3. **Create environment variables**:
   Create a `.env.local` file with:
   ```
   LIVEKIT_URL=your_livekit_url
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   GOOGLE_API_KEY=your_google_api_key
   ```

4. **Install dependencies**:
   ```bash
   uv sync
   ```

5. **Run the agent**:
   ```bash
   uv run voice_agent.py dev
   ```

## Property Database

The agent has access to 20 sample properties across 9 districts in Ingolstadt:
- **Districts**: Zentrum, Haunwöhr, Nordwest, Südwest, Nordost, Mailing, Etting, Friedrichshofen, Oberhaunstadt
- **Property Types**: Apartments, Houses, Penthouses, Townhouses
- **Listing Types**: Rental and Purchase options

## Function Tools

The agent provides the following tools:

- `search_immobilien()`: Search properties with filters (listing type, property type, district, price range, room count)
- `get_immobilie_details()`: Get detailed information about a specific property
- `get_available_districts()`: List all available districts in Ingolstadt
- `end_call()`: Gracefully end the conversation
- `detected_answering_machine()`: Detect and handle voicemail scenarios

## Technology Stack

- **LiveKit Agents Framework**: Voice agent infrastructure
- **Google Gemini 2.0 Flash Experimental**: Realtime voice model
- **Silero VAD**: Voice Activity Detection
- **Python 3.11+**: Core programming language
- **UV**: Fast Python package manager

## Development

Built following official LiveKit patterns from Context7 documentation:
- Function tools with `@function_tool` decorator
- StopResponse pattern for call termination
- External API pattern for property database
- Auto-discovery of function tools

## Company

**DR-Immobilien**  
Real estate services in Ingolstadt, Germany

## License

MIT License
