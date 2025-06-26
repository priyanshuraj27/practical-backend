from fastapi import APIRouter, Body
from gemini.earn_client import generate_business_idea

router = APIRouter()
# print("API heated earn ")
@router.post("/")
async def earn_route(skill: str = Body(..., embed=True)):
    return await generate_business_idea(skill)
