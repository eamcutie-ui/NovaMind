from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.ai_module import NovaMindAI
from backend.database import ChatMemory
from backend.utils import generate_user_id, check_limits, validate_tool

app = FastAPI(title="NovaMind V7 MaxElite")
ai_engine = NovaMindAI()
chat_memory = ChatMemory()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"status":"success","message":"NovaMind V7 Backend Running"}

@app.get("/chat")
def chat(user_id: str = None, message: str = Query(..., min_length=1), tool: str="chat", pro: bool=False):
    if not user_id:
        user_id = generate_user_id()
    if not check_limits(user_id, pro):
        return {"status":"error","response":"Daily limit reached!"}
    if not validate_tool(tool):
        return {"status":"error","response":"Invalid tool!"}

    chat_memory.add_message(user_id, "user", message)

    if tool == "chat" or tool == "text":
        response = ai_engine.chat_text(message)
    elif tool == "image":
        response = ai_engine.generate_image(message)
    else:
        response = "Tool not implemented yet."

    chat_memory.add_message(user_id, "ai", response)
    return {"status":"success","response":response, "history": chat_memory.get_history(user_id)}
