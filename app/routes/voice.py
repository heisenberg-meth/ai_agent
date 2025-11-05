from fastapi import APIRouter, Request
from twilio.twiml.voice_response import VoiceResponse
from app.core.call_manager import process_call

router = APIRouter(prefix="/voice", tags=["voice"])

@router.post("/inbound")
async def inbound_call(request: Request):
    """Handle incoming call from Twilio webhook"""
    form = await request.form()
    audio_url = form.get("RecordingUrl")

    response_text = await process_call(audio_url)
    twiml = VoiceResponse()
    twiml.say(response_text)
    return str(twiml)

@router.post("/outbound")
async def outbound_call():
    """Trigger outbound call using Twilio API"""
    from twilio.rest import Client
    from app.config import TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER, TARGET_NUMBER

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    call = client.calls.create(
        to=TARGET_NUMBER,
        from_=TWILIO_NUMBER,
        url="https://your-domain.com/voice/inbound"
    )
    return {"status": "Call initiated", "sid": call.sid}
