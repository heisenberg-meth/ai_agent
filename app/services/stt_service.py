import openai
from app.config import OPENAI_API_KEY
import io
import soundfile as sf

openai.api_key = OPENAI_API_KEY

async def transcribe(audio_bytes: bytes) -> str:
    try:
        with io.BytesIO(audio_bytes) as audio_file:
            audio_file.name = "speech.wav"
            sf.write(audio_file, [], 16000, 'PCM_16')
            audio_file.seek(0)
            transcript = openai.Audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcript["text"].strip()
    except Exception as e:
        print(f"STT Error: {e}")
        return ""
