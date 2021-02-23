from colorama import Fore



def printBWG(channel):
    """This Function Prints to the console with an specific color schema and returns an input from the console.
    
    Arguments:
        channel: The name of the channel that is being used.
    """
    channelText = ''.join([
        Fore.BLUE, 
        f'@{channel}'
        ])
    brackets = ''.join([
        Fore.WHITE, 
        '>>'
        ]) 
    userText = ''.join([Fore.GREEN, ''])
    output = ' '.join([
        channelText, 
        brackets, 
        userText
        ])
    return input(output)


def printHelpDocs(doc):
    command = Fore.MAGENTA + doc[0:doc.index(':')]
    content = Fore.WHITE + doc[doc.index(':'):]
    print(command + content)


def printResult(value):
    print(value)