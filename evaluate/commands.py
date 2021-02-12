import sys
import os
import json
from data import getData


def help():
    print('Coming soon...')

def version():
    return ''.join(['v', getData()["version"]])

    

# clears screen
def clear():
    os.system('clear')


# map of commands
COMMANDS_MAP = {
    'help': help,
    '-h': help,
    'version': version,
    '-v': version,
    'clear': clear
}


# runs the command map to the dictionary
def runCommand(command):
    return COMMANDS_MAP[command]()

def runCommands(commands):
    for command in commands:
        if command in COMMANDS_MAP:
            result = COMMANDS_MAP[command]()
            if result is not None:
                print(result)



