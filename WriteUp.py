
from openai import OpenAI
import os
import json

#This is the file which will be more text than code. 

#load in the API key
client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

# Load the text from the parsed events file
with open("parsed_events.txt", "r") as file:
    content = file.read()

hocky_errata = """ Here are some things you know about Hockey: 
- Each period is 20 minutes long
- Overtime is 5 minutes long
-     
    """

leafs_errata = """ Here are some things you know about the Toronto Maple Leafs:
 - John Tavares is no longer the captain, Auston Matthews is the captain
 - The team coach is Craig Berube
 - B. McMann is nicknamed Bobby "The Man" McMann
 - Very occationally, the team is called the "Buds"
 - Mitch Marner is occationally called "Shambles"
 - Auston Matthews is occationally called "Papi"
 - Morgan Rielly is occationally called "Riles" or "Captain Morgan"
 - William Nylander is occationally called "Willy" or "Nylanderthall"
 - Storlarz is occationally called "Stellaris" or "Stolie the Goalie"
 - Mathew Knies is occationally called "The Mutant"
 - John Tavares is occationally called "JT" or "Johnny Toronto". He is often called "The Amulet"
"""

user = """You are an enthusiastic hockey fan giving an update on the toronto maple leaves! You know all the nicknames of the players, 
            the slang and are excited when they win and angry when they loose."""
system = """You are announcer Joe Bowen giving a lively 500 word retelling of a Hockey game. Use highlights of the provided game using the event information. 
            Include the included information about goals and pentalties. don't forget to have fun!"""
model = "gpt-4o-mini"


# use the above to create a structure message.json file
with open("message.json", "w") as file:
    file.write("[")
    json.dump({"role": "user", "content": user}, file)
    file.write(",")
    file.write("\n")
    json.dump({"role": "system", "content": system + content}, file)
    file.write(",")
    file.write("\n")
    json.dump({"role": "system", "content": hocky_errata}, file)
    file.write(",")
    file.write("\n")
    json.dump({"role": "system", "content": leafs_errata}, file)
    file.write("]")


client = OpenAI(api_key=os.getenv("SUE_API_KEY"))

completion = client.chat.completions.create(
    model=model,
    messages= json.load(open("message.json"))
)

print(completion.choices[0].message)

# convert the comlpetion message to a string
completion_message = str(completion.choices[0].message)

# write the completion message to a file
with open("writeup.txt", "w") as file:
    file.write(completion_message)


