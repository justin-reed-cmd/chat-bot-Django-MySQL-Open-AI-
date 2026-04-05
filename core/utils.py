# Send message to OpenAI

import os

from openai import OpenAI


def get_ai_reply(message):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Auto-reply unavailable because OPENAI_API_KEY is not configured."

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly chatbot."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
