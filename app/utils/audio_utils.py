import base64

def decode_audio(b64_audio: str) -> bytes:
    return base64.b64decode(b64_audio)

def encode_audio(audio_bytes: bytes) -> str:
    return base64.b64encode(audio_bytes).decode("utf-8")
