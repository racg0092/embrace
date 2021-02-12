#!/usr/bin/env python3
import sys
import presentation
import os
from evaluate import commands as cmd

presentation.Welcome()




while True and sys.argv.__len__() <= 1:
    command = input('>> ')
    
    #if command is exit end REPL
    if command == '.exit':
        break

    # check if command is invalid
    elif command not in cmd.COMMANDS_MAP:
        print(f'\n{command} is not a valid command. Type [help] to get a list of available commands or [.exit] to end REPL.\n')
    
    # if command is valid run command
    elif command in cmd.COMMANDS_MAP:
        result = cmd.runCommand(command)
        if result is not None:
            print(result)
    else:
        print('Unable to process request. Unexpected Error')

if __name__ == "__main__" and sys.argv.__len__() > 1:
    cmd.runCommands(sys.argv[1:])
     
