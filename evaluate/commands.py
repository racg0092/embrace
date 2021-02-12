import sys
import os
import json
from data import getData as embrace

# channels
from channels.scaffolding import scaffold

def help():
    print('Coming soon...')

def version():
    return ''.join(['v', embrace()["version"]])

def printChannels():
    print('\n')
    for channel in COMMANDS_MAP:
        if channel.startswith('@'):
            print(channel)
    print('\n')

# clears screen
def clear():
    os.system('clear')


# map of commands
COMMANDS_MAP = {
    'help': help,
    '-h': help,
    'version': version,
    '-v': version,
    'clear': clear,
    'cls': clear,
    'channels': printChannels,
    '@scaffold': scaffold.init
}


# runs the command map to the dictionary
# this function is used for interactive REPL
def runCommand(command):
    return COMMANDS_MAP[command]()


# runs all commands map to the directory
# 
def runCommands(commands):
    for command in commands:
        if command in COMMANDS_MAP:
            result = COMMANDS_MAP[command]()
            if result is not None:
                print(result)



