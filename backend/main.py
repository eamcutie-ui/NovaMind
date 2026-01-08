"""
NovaMind Backend Elite
Author: NovaMind
Level: Production-grade
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.ai_module import NovaMindAI

# Initialize FastAPI
app = FastAPI(
    title="NovaMind API",
    description="Elite AI Chat Backend",
    version="1.0.0"
)

# Enable frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For mobile testing, change in prod
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI Engine
ai_engine = NovaMindAI()


@app.get("/")
def root():
    """Basic health check"""
    return {"status": "success", "message": "NovaMind backend running!"}


@app.get("/chat")
def chat(message: str = Query(..., min_length=1, description="User message")):
    """
    Chat endpoint
    Example: /chat?message=Hello
    """
    try:
        response = ai_engine.chat(message)
        return response
    except Exception as e:
        return {"status": "error", "response": str(e)}


@app.get("/info")
def info():
    """Returns AI engine info"""
    return {
        "engine": ai_engine.__class__.__name__,
        "version": ai_engine.version,
        "personality": ai_engine.personality
    }
