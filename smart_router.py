from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def route(user_input):
    prompt = f"""
You are an intent classifier for an AI assistant.

Classify the user input into ONE of these categories:

- jobs
- rota
- de_coach
- ai

Rules:
- jobs → job related queries
- rota → schedule/shift/work timing
- de_coach → SQL, Python, DBT, Airflow learning questions
- ai → anything else

User input: {user_input}

Return ONLY one word.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You classify user intent."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip().lower()