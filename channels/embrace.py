import sys
import os
import channels.core as core
from presentation import Welcome

# child channels
from channels.scaffold import scaffold

# channel name
channel = os.path.basename(__file__).replace('.py', '')

class Embrace(core.Channel):
    
    def __init__(self, name):
        self.name = name
        self.COMMANDS_MAP = {
            'channels': self.printChannels,
            '@scaffold': scaffold.open,
        }

    def printChannels(self):
        """channels: Print all the channels (services) available
        """
        print('\n') # creates new line for space
        [print(channel) for channel in self.COMMANDS_MAP if channel.startswith('@')]
        print('\n') #

    
embrace = Embrace(channel)