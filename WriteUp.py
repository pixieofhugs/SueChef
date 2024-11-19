
from openai import OpenAI
import os
import json

#This is the file which will be more text than code. 

#load in the API key
client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

# Load the text from the parsed events file
with open("parsed_events.txt", "r") as file:
    content = file.read()

user = "You are an enthusiastic hockey fan giving an update on the toronto maple leaves! You know all the nicknames of the players, the slang and are excited when they win and angry when they loose."
system = "write a 500 words of highlights of the tuseday game. Include the included information about goals and pentalties. don't forget to have fun!"
model = "gpt-4o-mini"


# use the above to create a structure message.json file
with open("message.json", "w") as file:
    file.write("[")
    json.dump({"role": "user", "content": user}, file)
    file.write(",")
    file.write("\n")
    json.dump({"role": "system", "content": system + content}, file)
    file.write("]")


client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

completion = client.chat.completions.create(
    model=model,
    messages= json.load(open("message.json"))
)

print(completion.choices[0].message)
#write the content out to file
