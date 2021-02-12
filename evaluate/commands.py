import sys
import os
import json

def version():
    contents = os.listdir()
    try:
        fs = open('./package.json', 'r')
        return ''.join(['v',json.load(fs)['version']])
    except FileNotFoundError as e:
        print(f'File System Error: {e!r}')
    

# clears screen
def clear():
    os.system('clear')


# map of commands
COMMANDS_MAP = {
    'help': 'help',
    '-h': 'help',
    'version': version,
    'clear': clear
}


# runs the command map to the dictionary
def runCommand(command):
    return COMMANDS_MAP[command]()





