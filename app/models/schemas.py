from pydantic import BaseModel

class OutboundCallRequest(BaseModel):
    to_number: str

class OutboundCallResponse(BaseModel):
    sid: str
    status: str
    