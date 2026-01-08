from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "NovaMind backend running!"}

@app.get("/chat")
def chat(message: str):
    # Placeholder response
    return {"response": f"NovaMind received: {message}"}
