
from openai import OpenAI
import os
import json

# Load the game data from the JSON file
with open("game_data.json", "r") as file:
    game_data = json.load(file)

# load the event data from the JSON file
with open("event_data.json", "r") as file:
    event_data = json.load(file)


# Extract the key information about the game from the data
winning_team = game_data["response"][0]["teams"][1]["home"][0]["name"][0]
print(winning_team)


#client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

# completion = client.chat.completions.create(
  #  model="gpt-4o-mini",
   # messages=[
   #     {"role": "system", "content": "You are an enthusiastic hockey fan giving an update on the toronto maple leaves! You know all the nicknames of the players, the slang and are excited when they win and angry when they loose."},
    #    {
    #        "role": "user",
    #        "content": "write a 300 words of highlights of the tuseday game. Include the score and who scored the goals."
    # }
# ]
#)

# print(completion.choices[0].message) 