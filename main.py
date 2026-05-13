import asyncio
import os
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents import AgentSession, Agent 
from livekit.plugins import deepgram, openai, elevenlabs, silero

# Load the free API keys from the .env file
load_dotenv()

async def entrypoint(ctx: JobContext):
    # Set up the real-time session
    session = AgentSession(
        vad=silero.VAD.load(),                        
        stt=deepgram.STT(),  
        
        # THE FIX: Updated the model to strictly use qwen-3-32b
        llm=openai.LLM(
            model="qwen-3-32b",                       # Using your permitted Qwen model
            base_url="https://litellm.digitaltribe.cloud", 
            api_key=os.getenv("LITELLM_API_KEY")      
        ),     
        
        tts=elevenlabs.TTS(                           
            voice_id="HHJcozd8AgLT2VmACyDV",
            api_key=os.getenv("ELEVEN_API_KEY"),      
            model="eleven_multilingual_v2"            
        ),
    )

    # Give the agent its personality
    agent = Agent(
        instructions="You are a helpful AI assistant with a soft, warm, and calm demeanor. Keep your responses very short and conversational."
    )

    # Start the session and connect to the room
    await session.start(room=ctx.room, agent=agent)

    # Have the agent speak first when the connection opens
    await asyncio.sleep(1)
    await session.generate_reply(instructions="Greet the user and ask how you can help them.")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
