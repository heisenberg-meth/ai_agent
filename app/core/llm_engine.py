from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a polite, natural-sounding AI voice agent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
