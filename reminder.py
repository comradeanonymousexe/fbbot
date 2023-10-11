import json

jsonF = "reminder.json"

def name_entry(name, author_id):
    
    with open(jsonF, "r") as json_file:
        data = json.load(json_file)

    if "users" not in data:
        data["users"] = {}

    data["users"][name] = author_id

    with open(jsonF, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return 1