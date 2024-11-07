
from openai import OpenAI
import os


from openai import OpenAI
client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ],
    max_tokens=10
)

print(completion.choices[0].message)