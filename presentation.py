from data import getData as embrace

def WelcomePrettyPrint():
    print('*'*14, '  ', '**'*2)
    print('*'*14, '  ', '**'*2)
    for i in range(7):
        if i == 3 or i == 4:
            print('*'*13)
        else:
            print('**', ' '*14, '**'*2)
    print('*'*14)
    print('*'*14)


def Welcome():
    """whoami: Prints introduction banner.
    NOTE:
        This contains a welcome versiona and the software version.
    """
    message = f'Embrace v{embrace("package.json")["version"]}'
    message2 = 'Our aim is to handle repetitive tasks for you.'
    message3 = 'So you can build amazing things.'
    print('*'*(len(message2)+8))
    for i in range(3):
        if i == 0:
            out = '*'*2 + '  ' + message 
        elif i == 1:
            out = '*'*2 + '  ' + message2
        else:
            out = '*'*2 + '  ' + message3
        out = out + ' '*(len(message2) + 8 - len(out) - 4) + '  **'
        print(out)
    print('*'*(len(message2)+8))
    print('\n\n')