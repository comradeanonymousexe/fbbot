import re


commands = ['-ta','-te','-setname','-echo','-send','-notify']
commands_dict = {key:False for key in commands }


# commands that be truncated from 'text'
#====Have to implement error handling logics====#

def process_command(text):

    text = text.lower()

    for prefix in commands_dict:
        commands_dict[prefix] = text.startswith(prefix)

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


#print(process_command("-te Mew"))