import os
import google.generativeai as genai
import json
import re


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not set in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

async def generate_business_idea(skill: str) -> dict:
    prompt = (
        f"Suggest one income-generating business idea for a woman in India skilled in \"{skill}\".\n"
        f"Return in this exact JSON format:\n\n"
        f"{{\n"
        f"  \"id\": \"1\",\n"
        f"  \"title\": \"...\",\n"
        f"  \"description\": \"...\",\n"
        f"  \"skillsNeeded\": [\"...\", \"...\"],\n"
        f"  \"earningPotential in rupees\": \"...\",\n"
        f"  \"startupTips\": \"...\",\n"
        f"  \"requiredMaterials\": \"...\"\n"
        f"}}\n\n"
        f"Return only valid JSON. Do not include markdown, explanation, or any other text."
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # ✅ Strip any markdown blocks like ```json
        clean_text = re.sub(r"```json|```", "", text).strip()

        return json.loads(clean_text)

    except Exception as e:
        return {
            "error": "Could not parse Gemini response",
            "details": str(e),
            "raw": text if 'text' in locals() else ''
        }
