import requests
import json


api_key = 'uz6qTIE8bKu+GqoDOWxwea21CoFU8tdsCr9x8Y7Er80='
webhook_url = 'https://discord.com/api/webhooks/1167926983880102008/3HRwYf9haP63G_RTXvfhRbCFvHGwFU2E4Xtjta2BUiWRmYcFCXxvpHkJF9T0mRxmFT32'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}



message = {
    "content": "Delta `scheduled message`",
}


# Create the cron-job.org task
task_data = {
    'job': {
        'url': webhook_url,
        'requestMethod': 1,  # Set the request method to "POST" = 1
        'extendedData':{
            'headers':{
                'Content-Type':'application/json'
            },
            'body': json.dumps(message)
        },
        'schedule': {
            'timezone': 'Asia/Dhaka',
            'hours': [0,12],
            'mdays': [-1],
            'minutes': [3],
            'months': [-1],
            'wdays': [-1]
        },
        'enabled': True,
    }
}



#response = requests.put('https://api.cron-job.org/jobs', data=json.dumps(task_data), headers=headers)

#if response.status_code == 200:
#    print(f'Task scheduled successfully: {response.json()}')
#else:
#    print(f'Failed to schedule task. Status code: {response.status_code}')
#    print(response.text)


##################

schedule= {
            'timezone': 'Asia/Dhaka',
            'hours':'', #currently unset.
            'mdays': [-1],
            'minutes': [0],
            'months': [-1],
            'wdays': [-1]
        }

#discord id will be used as title, message is their schedule message
def create_task(discordId, message, scheduleHour = [0,12]):

    schedule['hours'] = scheduleHour
    title = str(discordId)
    message = str(message)
    json_message = {"content":message}

    task_data = {
        'job': {
        'title': title,
        'url': webhook_url,
        'requestMethod': 1,
        'extendedData': {
            'headers': {
                    'Content-Type': 'application/json'
                        },
            'body': json.dumps(json_message)
                    },
        'schedule': schedule,  # Use the provided schedule argument
        'enabled': True,
                }
        }    

    response = requests.put('https://api.cron-job.org/jobs', data=json.dumps(task_data), headers=headers)

    if response.status_code == 200:
        return f'Task was created successfully'

    else:
        return f'Failed to register task. Status Code: {response.status_code}'


def update_task(discordId, message):

    pass



# Test-----
message = '''
mahdi
create python
cry
learn jsx
'''

print(create_task("mahdi",message,[7,10]))
# Test for task creating success


















####################




def schedule_tasks(webhook_url, schedule, headers):
    # Read users.json
    with open('users.json') as users_file:
        users_data = json.load(users_file)

    # Read tasks.json
    with open('tasks.json') as tasks_file:
        tasks_data = json.load(tasks_file)

    for user, tasks in tasks_data['user_data'].items():
        discord_id = users_data['users'].get(user.lower(), {}).get('discord')
        if discord_id:
            message = f"<@{discord_id}>\n"
            for task in tasks:
                message += f"{task['task']}\n"
                if task['time'] != 'everyday':
                    message += f"{task['time']}\n"
            # Create the job with the constructed message
            json_message = {"content": message}
            task_data = {
                'job': {
                    'title': discord_id,
                    'url': webhook_url,
                    'requestMethod': 1,
                    'extendedData': {
                        'headers': {
                            'Content-Type': 'application/json'
                        },
                        'body': json.dumps(json_message)
                    },
                    'schedule': schedule,  # Use the provided schedule argument
                    'enabled': True,
                }
            }
            # Schedule the job using the task_data
            response = requests.put('https://api.cron-job.org/jobs', data=json.dumps(task_data), headers=headers)
            if response.status_code == 200:
                print(f"Job scheduled successfully for {discord_id}")
            else:
                print(f"Failed to schedule job for {discord_id}. Status code: {response.status_code}")


