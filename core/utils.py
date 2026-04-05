# Send message to OpenAI

from openai import OpenAI

client = OpenAI()

def get_ai_reply(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly chatbot."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content