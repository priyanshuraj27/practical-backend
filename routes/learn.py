from fastapi import APIRouter, Body
from gemini.learn_client import explain_term

router = APIRouter()

@router.post("/")
async def learn(term: str = Body(..., embed=True)):
    response = await explain_term(term)
    return response
