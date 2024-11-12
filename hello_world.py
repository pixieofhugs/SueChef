
from openai import OpenAI
import os

# Load the API key for the NHL (Hockey info) from an environment variable
api_key = os.getenv("NHL_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please check your environment variable.")




# client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are an enthusiastic hockey fan giving an update on the toronto maple leaves! You know all the nicknames of the players, the slang and are excited when they win and angry when they loose."},
#         {
#             "role": "user",
#             "content": "write a 300 words of highlights of the tuseday game. Include the score and who scored the goals."
#         }
#     ]
# )

# print(completion.choices[0].message) 