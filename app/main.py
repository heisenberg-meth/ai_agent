from fastapi import FastAPI
from app.routes import voice

app = FastAPI(title="AI Voice Agent")

# Register  routes
app.include_router(voice.router)

@app.get("/")
async def root():
    return {"message": "AI Voice Agent API running."}
