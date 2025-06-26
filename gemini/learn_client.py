import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

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
    response = model.generate_content(prompt)
    text = response.text.strip()

    # Remove ```json or ``` blocks if Gemini includes them
    json_cleaned = re.sub(r"```json|```", "", text).strip()

    try:
        return json.loads(json_cleaned)
    except json.JSONDecodeError:
        return {
            "error": "Could not parse response from Gemini",
            "raw": text
        }
