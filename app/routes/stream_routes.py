from fastapi import APIRouter, WebSocket
import json
from app.services import stt_service, llm_service, tts_service
from app.utils.audio_utils import decode_audio, encode_audio

router = APIRouter()

@router.websocket("/stream")
async def stream_handler(websocket: WebSocket):
    await websocket.accept()
    print("🟢 Twilio Stream connected")

    try:
        while True:
            msg = await websocket.receive_text()
            data = json.loads(msg)

            if data["event"] == "media":
                # Decode audio from Twilio
                audio_chunk = decode_audio(data["media"]["payload"])
                text = await stt_service.transcribe(audio_chunk)

                if text.strip():
                    print(f"Caller said: {text}")
                    reply = await llm_service.generate_response(text)
                    print(f"Agent: {reply}")
                    speech_audio = await tts_service.convert(reply)

                    await websocket.send_text(json.dumps({
                        "event": "media",
                        "media": {"payload": encode_audio(speech_audio)}
                    }))

            elif data["event"] == "stop":
                print("🔴 Stream stopped by Twilio")
                break

    except Exception as e:
        print(f"⚠️ Stream Error: {e}")
    finally:
        await websocket.close()
