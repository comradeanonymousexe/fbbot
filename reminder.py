import json

jsonF = "reminder.json"


#====Have to implement error handling logics====#

def name_entry(name, author_id):
    
    with open(jsonF, "r") as json_file:
        data = json.load(json_file)


    #=== No name conflict====#
    if name in data["users"]:
        return 0

    data["users"][name] = {}
    data["users"][name]["facebook"] = author_id
    data["users"][name]["discord"] = None

    with open(jsonF, "w") as json_file:
        json.dump(data, json_file, indent=4)


    return 1


#=== This was for the debugging functionality "-send"===#
#=== "-send" works fine, converting it to actual extract_id(), allowing only names as argument

def extract_id(name):

    try:

        # -> parts of -send functionalities are commented out <- #
         #---first argument is name, rest are messages- gotta pretty it up---#
        #name,message = argument_slice(text)
        

        with open(jsonF,"r") as json_file:
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



