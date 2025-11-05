from twilio.rest import Client
from app.config import TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER, NGROK_URL

client = Client(TWILIO_SID, TWILIO_TOKEN)

def start_outbound_call(to_number: str):
    call = client.calls.create(
        to=to_number,
        from_=TWILIO_NUMBER,
        twiml=f"""
        <Response>
          <Say>This call may be recorded for quality purposes.</Say>
          <Connect>
            <Stream url="{NGROK_URL.replace('http', 'wss')}/stream" />
          </Connect>
        </Response>
        """
    )
    return {"sid": call.sid, "status": call.status}
