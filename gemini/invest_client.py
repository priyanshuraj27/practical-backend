import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
async def recommend_investment(amount: int, riskLevel: str) -> dict:
    prompt = (
        f"Suggest a suitable investment scheme for a woman who can invest ₹{amount} monthly "
        f"with a {riskLevel} risk appetite.\n\n"
        f"Respond ONLY in this exact JSON format:\n"
        f"{{\n"
        f"  \"id\": \"...\",\n"
        f"  \"name\": \"...\",\n"
        f"  \"description\": \"...\",\n"
        f"  \"category\": \"...\",\n"
        f"  \"riskLevel\": \"...\",\n"
        f"  \"typicalReturns\": \"...\",\n"
        f"  \"minInvestment\": \"...\",\n"
        f"  \"lockInPeriod\": \"...\",\n"
        f"  \"taxBenefits\": \"...\",\n"
        f"  \"howToStart\": \"...\"\n"
        f"}}"
    )

    try:
        response = model.generate_content(prompt)
        # print("🔍 RAW RESPONSE:", response.text) 
        text = response.text.strip()
        clean_text = re.sub(r"```json|```", "", text).strip()

        return json.loads(clean_text)
    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": "Gemini failed", "details": str(e)}
