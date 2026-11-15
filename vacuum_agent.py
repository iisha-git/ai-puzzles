def vacuum_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Move Right"
    return "Move Left"


def run_vacuum_world(room_a, room_b, start_location="A"):
    world = {"A": room_a, "B": room_b}
    location = start_location
    actions = []
    steps = 0
    max_steps = 20

    while steps < max_steps:
        status = world[location]
        action = vacuum_reflex_agent(location, status)
        actions.append((location, status, action))

        if action == "Suck":
            world[location] = "Clean"
        elif action == "Move Right":
            location = "B"
        elif action == "Move Left":
            location = "A"

        steps += 1

        if world["A"] == "Clean" and world["B"] == "Clean":
            break

    return world, actions


if __name__ == "__main__":
    final_world, log = run_vacuum_world("Dirty", "Dirty")

    for location, status, action in log:
        print(f"Location={location}, Status={status}, Action={action}")

    print("Final world:", final_world)

    print(
        "Rationality analysis: The agent cleans a dirty current room "
        "and moves toward the other room when the current room is clean."
    )
