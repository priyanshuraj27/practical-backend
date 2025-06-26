import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash")

async def get_gemini_response(message: str) -> str:
    prompt = (
        "You are Sakhi, a friendly and helpful chatbot designed for rural Indian women. "
        "Use a mix of Hindi and simple English. Give short, clear, encouraging replies "
        "to help them with saving, earning, investing, planning, or learning about money.\n\n"
        f"User message: {message}"
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Sorry, I'm having trouble responding right now."
