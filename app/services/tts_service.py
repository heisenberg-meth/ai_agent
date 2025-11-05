import openai
from app.config import OPENAI_API_KEY
import base64

openai.api_key = OPENAI_API_KEY

async def convert(text: str) -> bytes:
    try:
        response = openai.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        )
        return response.audio  # already base64-encoded PCM
    except Exception as e:
        print(f"TTS Error: {e}")
        return b""
