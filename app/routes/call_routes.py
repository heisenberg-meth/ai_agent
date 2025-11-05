from fastapi import APIRouter
from app.models.schemas import OutboundCallRequest, OutboundCallResponse
from app.services.twilio_service import start_outbound_call

router = APIRouter()

@router.post("/voice/outbound", response_model=OutboundCallResponse)
def make_call(request: OutboundCallRequest):
    result = start_outbound_call(request.to_number)
    return OutboundCallResponse(**result)
