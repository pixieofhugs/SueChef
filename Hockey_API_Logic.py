import os
import requests
import json
import datetime as dt

# Load the API key for the Hockey info from an environment variable
nhl_api_key = os.getenv("NHL_API_KEY")
if not nhl_api_key:
    raise ValueError("API key not found. Please check your environment variable.")


# Use the response library to make a request to the Hockey API
url = "https://v1.hockey.api-sports.io/status"
headers = {
  'x-rapidapi-key': nhl_api_key,
  'x-rapidapi-host': 'v1.hockey.api-sports.io'

}

# This calls the API to see if I have enough API credits to preform the opperation

# First, we get the status
response = requests.request("GET", url, headers=headers)
data = response.json()

# Then we see if I have enough API credits to preform the opperation
if data["response"]["requests"]["current"] >= data["response"]["requests"]["limit_day"]:
    print("You have reached your API limit for today. Please try again tomorrow.")
    exit()

##########################################

# For now, we are going to hardcode the paramaters for leage and team because this is for my husband.
# He likes the Toronto Maple Leafs. Quite a lot! check out the API documentation to change these if you want to see another team.
url = "https://v1.hockey.api-sports.io/games"
params = {
    # TODO: Make Season dynamic. dt.datetime.now().year the season will throw an error after december becasue the season will still be 2024
    "season": "2024",
    # Go leafs Go!
    "team": "700",
    # NHL
    "league": "57",
    # The date of the game
    "date": dt.datetime.now().date()
}
# Now that we know the API loves us, we can determine if a game has happend in the last 24 hours



# We call the API to get the game data
response = requests.request("GET", url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Write the JSON data to a file with pretty formatting
    with open("game_data.json", "w") as file:
        json.dump(data, file, indent=4)  # indent=4 is the formatting magic

    print("Response saved to game_data.json.")
else:
    print("Failed to retrieve data:", response.status_code)
    exit()


####################################


# Once we have some game data, now we can get the events which happend in the game
# First, We need to get the game ID from the response

game_id = data["response"][0]["id"]


url = "https://v1.hockey.api-sports.io/games/events"
params = {
    "game": game_id
}

# Call the API to get the events
response = requests.request("GET", url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Write the JSON data to a file with pretty formatting
    with open("event_data.json", "w") as file:
        json.dump(data, file, indent=4)  # indent=4 is the formatting magic

    print("Response saved to event_data.json.")

#With that we have all the information we need to create a cool write up of the game.