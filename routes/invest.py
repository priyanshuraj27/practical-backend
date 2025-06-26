from fastapi import APIRouter, Body
from gemini.invest_client import recommend_investment

router = APIRouter()

@router.post("/")
async def invest_route(
    amount: int = Body(..., embed=True),
    riskLevel: str = Body(..., embed=True)
):
    return await recommend_investment(amount, riskLevel)
