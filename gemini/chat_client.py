# gemini/chat_client.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model (you can switch to gemini-1.5-pro if needed)
model = genai.GenerativeModel("gemini-2.0-flash")

async def get_gemini_response(message: str) -> str:
    """
    Sends a user message to Gemini and returns the generated reply.
    """
    prompt = (
        "You are Sakhi, a friendly and helpful chatbot designed for rural Indian women. "
        "Use a mix of Hindi and simple English. Give short, clear, encouraging replies "
        "to help them with saving, earning, investing, planning, or learning about money.\n\n"
        f"User message: {message}"
    )

    try:
        response = model.generate_content(prompt)
        # print(response)
        reply_text = response.text.strip()
        return reply_text
    except Exception as e:
        print("❌ Gemini Chat Error:", str(e))
        return "Sorry, I'm having trouble responding right now."
