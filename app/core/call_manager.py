from app.core.asr_engine import transcribe_audio
from app.core.llm_engine import generate_response
from app.core.tts_engine import synthesize_speech

async def process_call(audio_url: str | None):
    if audio_url:
        text = transcribe_audio(audio_url)
    else:
        text = "Hello there!"  # fallback

    reply = generate_response(text)
    synthesize_speech(reply)
    return reply
