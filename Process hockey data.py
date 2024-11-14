import json

# Load the game data from the JSON file
with open("game_data.json", "r") as file:
    game_data = json.load(file)

# load the event data from the JSON file
with open("event_data.json", "r") as file:
    event_data = json.load(file)


# Extract the key information about the game from the data
events = event_data.get("response", [])

# Function to parse each event
def parse_event(event):
    # Common fields
    period = event.get("period")
    minute = event.get("minute")
    team_name = event["team"]["name"]
    players = ", ".join(event.get("players", []))
    assists = ", ".join(event.get("assists", []))
    comment = event.get("comment")
    event_type = event.get("type")



    # Create formatted event string
    if event_type == "goal":
        event_str = f"[Goal] Period {period}, Minute {minute} - {team_name}\n"
        event_str += f"   Scorer: {players}\n"
        if assists:
            event_str += f"   Assists: {assists}\n"
        if comment:
            event_str += f"   Comment: {comment}\n"
    elif event_type == "penalty":
        event_str = f"[Penalty] Period {period}, Minute {minute} - {team_name}\n"
        event_str += f"   Player: {players}\n"
        event_str += f"   Penalty: {comment}\n"
    event_str += "\n"  # Add a newline after each event for readability
    return event_str


def print_event(event):
    # Print formatted event information
    if event_type == "goal":
        print(f"[Goal] Period {period}, Minute {minute} - {team_name}")
        print(f"   Scorer: {players}")
        if assists:
            print(f"   Assists: {assists}")
        if comment:
            print(f"   Comment: {comment}")
    elif event_type == "penalty":
        print(f"[Penalty] Period {period}, Minute {minute} - {team_name}")
        print(f"   Player: {players}")
        print(f"   Penalty: {comment}")
    print()

# Iterate and parse each event
for event in events:
    parse_event(event)


# dump the string of events into a file
with open("parsed_events.txt", "w") as file:
    for event in events:
        file.write(str(event) + "\n")