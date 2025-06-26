# routes/chat.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from gemini.chat_client import get_gemini_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    userId: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str

@router.post("/", response_model=ChatResponse)
async def chat_route(request: ChatRequest):
    try:
        reply = await get_gemini_response(request.message)
        return ChatResponse(reply=reply)
    except Exception as e:
        print("Gemini API Error:", e)
        raise HTTPException(status_code=500, detail="Error while generating reply from Gemini.")
