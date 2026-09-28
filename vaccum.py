state = {
    "current_location": "A",
    "current_room": "Clean",
    "other_room": "Dirty"
}

def model_based_vacuum_agent(state):

    if state["current_room"] == "Dirty":
        return "Suck"

    elif state["current_room"] == "Clean":
        if state["other_room"] == "Dirty":
            if state["current_location"] == "A":
                return "Move Right"
            else:
                return "Move Left"
        else:
            return "NoOp"


action = model_based_vacuum_agent(state)
print(action)
