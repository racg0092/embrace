import sys
import os
import channels.core as core

# channel name
channel = os.path.basename(__file__).replace('.py', '')




class Scaffold(core.Channel):
    
    def __init__(self, name):
        self.name = name
        self.COMMANDS_MAP = {
            'electron': self.electron
        }
    

    def electron(self):
        """electron: scaffolds electron application
        """
        print('npx electron')


scaffold = Scaffold(channel)

