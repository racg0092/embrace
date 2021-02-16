"""Channel class definition ."""
import os
import sys
from eprint.main import printBWG, printHelpDocs
from data import getData as embrace
from presentation import Welcome

class Channel:


    def sharedCommandsMapping(self):
        self.COMMANDS_MAP['clear'] = self.clear
        self.COMMANDS_MAP['help'] = self.help
        self.COMMANDS_MAP['version'] = self.version
        self.COMMANDS_MAP['whoami'] = Welcome
        self.COMMANDS_MAP['channels'] = self.channels
        self.COMMANDS_MAP['.exit'] = self.closeEmbrace


    def open(self):
        self.sharedCommandsMapping()

        while True:
            command = printBWG(self.name)

  
            if command.startswith('@'):
                from channels import listing
                channels = listing.get()
                if command in channels:
                    channels[command].open()
                else:
                    print(f'channel {command} does not exist')
                    print('\nList of available channels')
                    self.channels()

           
            elif command in self.COMMANDS_MAP:
                result = self.COMMANDS_MAP[command]()
                if result != None:
                    print(result)
            
            else:
                print(f'{command} is not recognized')

    
    def channels(self):
        from channels import listing
        [print(channelName) for channelName in listing.get()]
    
    # clears screen
    def clear(self):
        """clear: Clears the screen
        """
        os.system('clear')


    
    def help(self):
        """help: Provides a list of all available commands and their uses.

        NOTE: 
            This is just the current channel help section. You will have to change
            channesl to see their respectives sections.
        """
        print('\n')
        [printHelpDocs(self.COMMANDS_MAP[cmd].__doc__) for cmd in self.COMMANDS_MAP if self.COMMANDS_MAP[cmd].__doc__ is not None]


    def version(self):
        """version: Returns Embrace current version.
        """
        return ''.join(['v', embrace('package.json')["version"]])

    
    def closeEmbrace(self):
        sys.exit()


