import requests
import json

# Replace with your cron-job.org API key and Discord webhook URL
api_key = 'uz6qTIE8bKu+GqoDOWxwea21CoFU8tdsCr9x8Y7Er80='
webhook_url = 'https://discord.com/api/webhooks/1167926983880102008/3HRwYf9haP63G_RTXvfhRbCFvHGwFU2E4Xtjta2BUiWRmYcFCXxvpHkJF9T0mRxmFT32'

# Define the message you want to send
message = {
    'content': 'Delta `schedule success`',
}

# Define the scheduled time in the cron-job.org format (e.g., '15 * * * *')
scheduled_time = '15 * * * *'  # Replace with your desired schedule

# Create the cron-job.org task
task_data = {
    'job': {
        'url': webhook_url,
        'requestMethod': 1,  # Set the request method to "POST"
        'extendedData':{
            'body': json.dumps(message)
        },
        'schedule': {
            'timezone': 'Asia/Dhaka',
            'hours': [-1],
            'mdays': [-1],
            'minutes': [30],
            'months': [-1],
            'wdays': [-1]
        },
        'enabled': True,
    }
}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# Make a PUT request to create the task
response = requests.put('https://api.cron-job.org/jobs', data=json.dumps(task_data), headers=headers)

if response.status_code == 200:
    print(f'Task scheduled successfully: {response.json()}')
else:
    print(f'Failed to schedule task. Status code: {response.status_code}')
    print(response.text)