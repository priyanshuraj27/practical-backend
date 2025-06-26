import os
import google.generativeai as genai
import json
import re

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ Environment variable GEMINI_API_KEY not set!")

genai.configure(api_key=api_key)


model = genai.GenerativeModel("models/gemini-2.0-flash")

async def explain_term(term: str) -> dict:
    prompt = (
        f"Explain the financial term \"{term}\" in simple language for a rural Indian woman. "
        f"Respond ONLY in this JSON format:\n"
        f"{{\n"
        f"  \"term\": \"{term}\",\n"
        f"  \"definition\": \"...\",\n"
        f"  \"simpleExplanation\": \"...\",\n"
        f"  \"example\": \"...\"\n"
        f"}}"
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Remove markdown formatting if present
        clean_text = re.sub(r"```json|```", "", text).strip()

        return json.loads(clean_text)
    except Exception as e:
        return {
            "error": "Could not parse response from Gemini",
            "details": str(e),
            "raw": text if 'text' in locals() else ''
        }
