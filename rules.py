import json

def calculate_points(event_type, event_date):

    with open("rules.json", "r") as file:
        rules = json.load(file)

    points = rules["base_points"].get(event_type, 0)

    # Weekend multiplier
    if event_date.weekday() in [5, 6]:
        points *= rules["weekend_multiplier"]

    # Cap
    points = min(
        points,
        rules["max_points_per_event"]
    )

    return points