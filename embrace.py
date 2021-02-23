#!/usr/bin/env python3
import sys
import presentation
import subprocess
from channels.embrace import embrace
from evaluate import commands
 
# welcome screen
presentation.Welcome()


# if not arguments present start interactive REPL
if len(sys.argv) <= 1:
    embrace.open()


# if arguments present run commands as they are
if __name__ == "__main__" and len(sys.argv) > 1:
    commands.eval(sys.argv[1:])
    print('\nRun embrace without argument to start interacte REPL')
