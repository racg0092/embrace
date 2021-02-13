import sys
import os
import json
from data import getData as embrace
from presentation import Welcome
from eprint.main import printHelpDocs

# channels
from channels.scaffolding import scaffold

def help():
    """help: Provides a list of all available commands and their uses.

    NOTE: 
        This is just the @embrace channel help section. You will have to change
        channesl to see their respectives sections.
    """
    print('\n')
    for command in COMMANDS_MAP:
        if COMMANDS_MAP[command].__doc__ is not None:
            printHelpDocs(COMMANDS_MAP[command].__doc__)
    print('\n')

def version():
    """version: Returns Embrace current version.
    """
    return ''.join(['v', embrace('package.json')["version"]])

def printChannels():
    """channels: Print all the channels (services) available
    """
    print('\n')
    for channel in COMMANDS_MAP:
        if channel.startswith('@'):
            print(channel)
    print('\n')

# clears screen
def clear():
    """clear: Clears the screen
    """
    os.system('clear')


# map of commands
COMMANDS_MAP = {
    'help': help,
    'channels': printChannels,
    'clear': clear,
    '@scaffold': scaffold.init,
    'version': version,
    'whoami': Welcome
}


# runs the command map to the dictionary
# this function is used for interactive REPL
def runCommand(command):
    """Executes CLI command based on command's map

    Args:
        command: The name of the command to execute

    Returns:
        The result of the command execcution if any.
    """
    return COMMANDS_MAP[command]()


# runs all commands map to the directory
# 
def runCommands(commands):
    for command in commands:
        if command in COMMANDS_MAP:
            result = COMMANDS_MAP[command]()
            if result is not None:
                print(result)



