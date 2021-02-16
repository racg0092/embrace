import sys
import os




# GLOBAL SERVICES


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



