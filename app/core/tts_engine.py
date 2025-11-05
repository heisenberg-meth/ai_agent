import requests
from app.config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID

def synthesize_speech(text, filename="output.wav"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    data = {"text": text}

    r = requests.post(url, json=data, headers=headers)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename
