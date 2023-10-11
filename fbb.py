import fbchat
import os 
from fbchat.models import *
from trnslt import *
from utils import *
from reminder import *

#remove later
import re
import json


email = os.environ.get('fb_login_email')
password = os.environ.get('fb_login_psd')


# Subclass of Client to handle messages
class Bot(fbchat.Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        #DEBUG AREA#
        print(message_object)
        #00#

        text, commands = process_command(message_object.text)
        

        if commands['-ta']:

            response = translate_arabic_to_english(text)
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)


        if commands['-te']:
            response = translate_english_to_arabic(text)
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)


        if commands['-echo']:

            self.send(Message(text=text), thread_id=thread_id, thread_type=thread_type)


        if commands['-setname']:

            if thread_type != ThreadType.USER:
                response = "This command is only valid to be used in DMs"
                self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)
            else:
                name_entry(text,author_id)

# Only for testing, get rid of later.
        if commands['-send']:
            
            recipient = text.split()[0]
            text = re.sub(r'^' + re.escape(recipient) + r'\s*', '', text)


            with open("reminder.json", "r") as json_file:
                data = json.load(json_file)

            recipient_id = data["users"].get(recipient)

            if recipient_id:
                self.send(Message(text=text), thread_id=recipient_id, thread_type=ThreadType.USER)

            else:
                self.send(Message(text=f"User '{recipient}' not found"), thread_id=thread_id, thread_type=thread_type)
#00#








bot = Bot(email, password)


bot.listen()