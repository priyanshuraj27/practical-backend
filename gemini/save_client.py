import os
import google.generativeai as genai
import json
import re

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ Environment variable GEMINI_API_KEY not set!")

genai.configure(api_key=api_key)

# Gemini model instance
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

# Generate saving plan from Gemini
async def generate_saving_plan(goal: str, targetAmount: int, durationMonths: int) -> dict:
    prompt = (
        f"A woman wants to save ₹{targetAmount} in {durationMonths} months for the goal: \"{goal}\".\n"
        f"1. Calculate how much she needs to save per day, per week, and per month.\n"
        f"2. Suggest one simple saving method (formal or informal).\n"
        f"3. Return in this exact JSON format:\n\n"
        f"{{\n"
        f"  \"goal\": \"{goal}\",\n"
        f"  \"targetAmount\": \"₹{targetAmount}\",\n"
        f"  \"duration\": \"{durationMonths} months\",\n"
        f"  \"monthlySavingNeeded\": \"...\",\n"
        f"  \"weeklySavingNeeded\": \"...\",\n"
        f"  \"dailySavingNeeded\": \"...\",\n"
        f"  \"plan\": \"...\",\n"
        f"  \"recommendedPlan\": {{\n"
        f"    \"id\": \"...\",\n"
        f"    \"name\": \"...\",\n"
        f"    \"description\": \"...\",\n"
        f"    \"category\": \"...\",\n"
        f"    \"riskLevel\": \"...\",\n"
        f"    \"typicalReturns\": \"...\",\n"
        f"    \"minInvestment\": \"...\",\n"
        f"    \"lockInPeriod\": \"...\",\n"
        f"    \"taxBenefits\": \"...\",\n"
        f"    \"howToStart\": \"...\"\n"
        f"  }},\n"
        f"  \"tip\": \"...\"\n"
        f"}}\n\n"
        f"Return only valid JSON. No markdown, no explanation outside JSON."
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        clean_text = re.sub(r"```json|```", "", text).strip()
        return json.loads(clean_text)
    except Exception as e:
        return {"error": "Could not parse Gemini response", "details": str(e)}
