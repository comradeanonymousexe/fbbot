import fbchat
import os 
from fbchat.models import *
from trnslt import *
from utils import *
from reminder import *



email = os.environ.get('fb_login_email')
password = os.environ.get('fb_login_psd')


#====Have to implement error handling logics====#

# Subclass of Client to handle messages
class Bot(fbchat.Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
      
       #===Dont talk to yourself===#
        if author_id == self.uid:
            return

        #===point out the command and extract the arguments. File: utils.py===#
        text, commands = process_command(message_object.text)
        

        #===HANDLE COMMANDS===#

        #---Translate and Echo (for debugging) File: trnslt.py ---#
        if commands['-ta']:

            response = translate_arabic_to_english(text)
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)


        if commands['-te']:
            response = translate_english_to_arabic(text)
            self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)


        if commands['-echo']:

            self.send(Message(text=text), thread_id=thread_id, thread_type=thread_type)



        #---take authors name as argument, registers into json. File: reminder.py---#
        #---Nicely implemented---#

        if commands['-setname']:

            try:

                ID = author_id
                status_code = name_entry(text,ID)


                if status_code:
                    response = f"Succefully registered {text}\'s name with the id of {ID}"

                else:
                    response = f"Entry {text} already exists."

                self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)

            except Exception as e:
                
                response = f"an error occured, {e}"
                self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)


        if commands['-send']:

            name, response = text_slice(text)

            if extract_id(name)[0]:

                recipient = extract_id(text)[1]

                self.send(Message(text=response), thread_id=recipient, thread_type=ThreadType.USER)
                self.send(Message(text="Done :) "), thread_id=thread_id, thread_type=thread_type)

            else:
            
                self.send(Message(text=extract_id(text)[1]), thread_id=thread_id, thread_type=thread_type)



        #---testing--#
        if commands['-notify']:

            process_reminder(text)

            self.send(Message(text="Notification enlisted soxesfully"), thread_id=thread_id, thread_type=thread_type)


        if commands['-dcsend']:

            status = send_dc(text)

            if status:
                self.send(Message(text="pathano successful, giye deekhe ashen"), thread_id=thread_id, thread_type=thread_type)

            else:
                self.send(Message(text="genjam lagse, message pouche nai"), thread_id=thread_id, thread_type=thread_type)






bot = Bot(email, password)

bot.listen()