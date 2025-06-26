import os
import google.generativeai as genai
import json
import re

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not set in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash")


async def recommend_investment(amount: int, riskLevel: str) -> dict:
    prompt = (
        f"A woman can invest ₹{amount} monthly and has a {riskLevel} risk appetite.\n"
        f"Suggest one suitable investment scheme.\n"
        f"Respond ONLY in this JSON format:\n\n"
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
        text = response.text.strip()

        # Strip any ```json or ``` if Gemini adds formatting
        clean_text = re.sub(r"```json|```", "", text).strip()

        return json.loads(clean_text)

    except Exception as e:
        return {
            "error": "Could not parse Gemini response",
            "details": str(e),
            "raw": text if 'text' in locals() else ''
        }
