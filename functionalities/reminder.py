import json

userF = "users.json"
taskF = "tasks.json"


#====Have to implement error handling logics====#

def name_entry(name, author_id):
    
    with open(userF, "r") as json_file:
        data = json.load(json_file)


    #=== No name conflict====#
    if name in data["users"]:
        return 0

    data["users"][name] = {}
    data["users"][name]["facebook"] = author_id
    data["users"][name]["discord"] = None

    with open(userF, "w") as json_file:
        json.dump(data, json_file, indent=4)


    return 1


#=== This was for the debugging functionality "-send"===#
#=== "-send" works fine, converting it to actual extract_id(), allowing only names as argument

def extract_id(name):

    try:

        with open(userF,"r") as json_file:
            data = json.load(json_file)

        users = data.get('users',{})
        recipient = users.get(name)

        if recipient is not None:
            recipient_id = recipient.get('facebook')
            return 1,recipient_id

        else:
            return 0,"I couldn't find the user :("
            

    except Exception as e:
        return 0,e





#---debug---#
def process_reminder(text):

    user_blocks = text.strip().split("\n\n")

    user_data = {}  # Dictionary to store user data

    for block in user_blocks:

        lines = block.strip().split("\n")
        username = lines[0]
        tasks = lines[1:]  # The rest of the lines contain tasks and times

        user_data[username] = []

        for task_line in tasks:

            if ":" in task_line:
                task, time = task_line.split(":")
                task = task.strip()
                time = time.strip()

            else:
                task = task_line.strip()
                time = "everyday"

            user_data[username].append({"task": task, "time": time})

#---take out---#


    return user_data



def sort_reminder(task_list):

    def key_func(task):
        if task["time"] == "everyday":
            return (0, 0, 0)
        else:
            date_parts = task["time"].split('-')
            year = int(date_parts[2])
            month = int(date_parts[1])
            day = int(date_parts[0])
            return (1, year, month, day)

    return sorted(task_list, key=key_func)



def submit_reminder(user_data):

    for user, tasks in user_data.items():  
        user_data[user] = sort_reminder(tasks)

    with open(taskF, 'r') as json_file:
        existing_data = json.load(json_file)


    existing_data["user_data"] = user_data


    with open(taskF, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    return 1


