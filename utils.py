import re
import requests

commands = ['-ta','-te','-setname','-echo','-send','-notify','-dcsend']
commands_dict = {key:False for key in commands }

#implement error handling for each command
# commands that be truncated from 'text'
#====Have to implement error handling logics====#

def process_command(text):

    text = text.lower()

    for prefix in commands_dict:
        commands_dict[prefix] = text.startswith(prefix) #--BUG: two commands with same starting string cant be assigned

    #=============just a gibberish RegEx thing from chatgpt================#

    cmd_pattern = "|".join(map(re.escape, commands))

    main_text = re.sub(f"^(?:{cmd_pattern})\\s*", "", text)



    return [main_text, commands_dict] 


#==== Slice the text, to determine Name and Message. Currently works with '-send' functionality 
def text_slice(text):

    sections = text.split(',',1)

    name = sections[0].strip()
    message = sections[1].strip()

    return name, message



def send_dc(message):

    webhook_url = "https://discord.com/api/webhooks/1167926983880102008/3HRwYf9haP63G_RTXvfhRbCFvHGwFU2E4Xtjta2BUiWRmYcFCXxvpHkJF9T0mRxmFT32"

    data = {
        "content": message
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        return 1
    else:
        return 0



#print(process_command("-te Mew"))