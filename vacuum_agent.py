# Simple reflex vacuum agent

def agent(room):
    if room == "Dirty":
        return "Suck"
    return "Move"


rooms = {"A": "Dirty", "B": "Clean"}
location = "A"

for step in range(4):
    action = agent(rooms[location])

    print("Location:", location, "| Room:", rooms[location], "| Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"
    else:
        location = "B" if location == "A" else "A"

print("Final rooms:", rooms)
