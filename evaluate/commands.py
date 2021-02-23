import sys
import os
from channels import listing as channels
from eprint.main import printHelpDocs
from data import getData as embrace
from presentation import Welcome



def help():
    """.help: Print global help docs
    """
    [printHelpDocs(_commands_map[cmd].__doc__) for cmd in _commands_map if _commands_map[cmd].__doc__ is not None]


def get():
    """Returns a list of global commands
    """
    return _commands_map


def getChannels():
    """.channels: Prints a list of available channels
    """
    [print(channel) for channel in channels.get()]


def exit():
    """.exit: Terminates embrace
    """
    sys.exit()


def version():
    """version: Returns Embrace current version.
    """
    return ''.join(['v', embrace('package.json')["version"]])


# clears screen
def clear():
    """clear: Clears the screen
    """
    os.system('clear')


def getCommandList():
    return _commadList


# global commands dictionary
_commands_map = {
    '.channels': getChannels,
    '.help': help,
    '.exit': exit,
    '.clear': clear,
    '.version': version,
    '.whoami': Welcome
}


def eval(commandList):
    _commandList = iter(commandList)
    while True:
        try:
            command = next(_commandList)
            return pathIdentification(command)
        except StopIteration:
            break





def pathIdentification(command):
    if str(command).startswith('.'):
        return golbalCommandScope(command)

    elif str(command).startswith('@'):
        channelSwitch(command)
    else:
        return localCommandScope(command)

        


def golbalCommandScope(command):
    if command in _commands_map:
        result = _commands_map[command]()
        if result is not None:
            return result
    else:
        return f'{command} is not recognized as a global command'


def channelSwitch(channel):
    channels_list = channels.get()
    if channel in channels_list:
        channels_list[channel].open()
    else:
        print(f'{channel} was not found. You will be redirected to the main channel.')
        print('\nAvailable channels')
        _commands_map['.channels']()
        channels.get()['@embrace'].open()


def localCommandScope(command):
    def x(commands_map):
        if command in commands_map:
            result = commands_map[command]()
            return result
        else:
            return f'{command} was not recognize as local command'
    return x
    

