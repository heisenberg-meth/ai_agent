import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_response(user_text: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI call agent speaking naturally with customers."},
                {"role": "user", "content": user_text}
            ],
            temperature=0.6
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM Error: {e}")
        return "I'm sorry, could you please repeat that?"
