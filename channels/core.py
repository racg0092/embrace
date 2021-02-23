"""Channel class definition ."""
import os
import sys
from eprint.main import printBWG, printHelpDocs, printResult
import collections

class Channel:


    def sharedCommandsMapping(self):
        self.COMMANDS_MAP['help'] = self.help


    def open(self):
        # initialize local commands
        self.sharedCommandsMapping()
        # import evaluation function
        from evaluate.commands import eval
        # start inifinite loop since this is interactive mode
        while True:
            commands = printBWG(self.name).split(' ')
            execute = eval(commands) # evaluate
            if isinstance(execute, collections.Callable): # if execut is a function execute it
                result = execute(self.COMMANDS_MAP)
                if result is not None:
                    printResult(result)
            else:
                if execute is not None:
                    printResult(execute)


    def help(self):
        """help: Provides a list of all available commands and their uses.

        NOTE: 
            This is just the current channel help section. You will have to change
            channesl to see their respectives sections.
        """
        print('\n')
        [printHelpDocs(self.COMMANDS_MAP[cmd].__doc__) for cmd in self.COMMANDS_MAP if self.COMMANDS_MAP[cmd].__doc__ is not None]

