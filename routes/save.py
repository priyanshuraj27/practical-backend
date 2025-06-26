from fastapi import APIRouter, Body
from gemini.save_client import generate_saving_plan

router = APIRouter()

@router.post("/")
async def save_route(
    goal: str = Body(..., embed=True),
    targetAmount: int = Body(..., embed=True),
    durationMonths: int = Body(..., embed=True)
):
    return await generate_saving_plan(goal, targetAmount, durationMonths)
