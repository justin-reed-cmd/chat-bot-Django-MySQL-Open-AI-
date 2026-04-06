import PyPDF2

def read_resume(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    return text


# Send message to OpenAI

import os

from openai import OpenAI


# def get_ai_reply(message):
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         return "Auto-reply unavailable because OPENAI_API_KEY is not configured."

#     client = OpenAI(api_key=api_key)
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", 
#             "content": """
#             You are a friendly chatbot representing Justin Reed.

#             Justin is a software engineer with a passion for technology and innovation. 
#             He enjoys helping others and is always eager to learn new things. 
#             When responding to messages, please be polite, helpful, and concise. 
#             If you don't know the answer to a question, it's okay to say so. 
#             Always maintain a positive and respectful tone in your replies.

#             Answer the message as if you were Justin, using a friendly and approachable style.
#             """
#             },
#             {"role": "user", "content": message}
#         ]
#     )

#     return response.choices[0].message.content

from openai import OpenAI

client = OpenAI()

def get_ai_reply(message):
    resume_text = read_resume("resume.pdf")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
                You are Marcus's assistant.

                Here is Marcus's resume:
                {resume_text}

                Answer using this information.
                """
            },
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content