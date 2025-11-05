from fastapi import FastAPI
from app.routes import voice, call_routes, stream_routes

app = FastAPI(title="AI Voice Agent")

# Register routes
app.include_router(voice.router)
app.include_router(call_routes.router)
app.include_router(stream_routes.router)

@app.get("/")
async def root():
    return {"message": "AI Voice Agent API running."}
