import re

commands = ['-ta','-te','-set','-setname','-echo','-send']
commands_dict = {key:False for key in commands }

# commands that be truncated from 'text'
def process_command(text):
    text = text.lower()
    #just a gibberish RegEx thing from chatgpt
    cmd_pattern = "|".join(map(re.escape, commands))
    matched_cmd = re.match(f'({cmd_pattern})\\s*', text)

    while matched_cmd:

        matched_cmd = matched_cmd.group(1)
        commands_dict[matched_cmd] = True

        text = re.sub(matched_cmd, "", text)


    return [text, commands_dict]