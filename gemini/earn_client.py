import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
# print("Earn is called")
async def generate_business_idea(skill: str) -> dict:
    prompt = (
        f"Suggest one income-generating business idea for a woman in india skilled in \"{skill}\".\n"
        f"Return in the exact JSON format below:\n\n"
        f"{{\n"
        f"  \"id\": \"1\",\n"
        f"  \"title\": \"...\",\n"
        f"  \"description\": \"...\",\n"
        f"  \"skillsNeeded\": [\"...\", \"...\"],\n"
        f"  \"earningPotential in rupees\": \"...\",\n"
        f"  \"startupTips\": \"...\",\n"
        f"  \"requiredMaterials\": \"...\"\n"
        f"}}\n\n"
        f"Do not include any text, heading, or markdown outside the JSON."
    )

    try:
        response = model.generate_content(prompt)
        # print("🔍 Gemini RAW:", response.text)
        text = response.text.strip()
        clean = re.sub(r"```json|```", "", text).strip()
        return json.loads(clean)
    except Exception as e:
        return {"error": "Gemini failed", "details": str(e)}
