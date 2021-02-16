#!/usr/bin/env python3
import sys
import presentation
import os
import subprocess
from channels.embrace import embrace
import evaluate.commands as cmd


presentation.Welcome()


if len(sys.argv) <= 1:
    embrace.open()


if __name__ == "__main__" and len(sys.argv) > 1:
    cmd.runCommands(sys.argv[1:])
    print('\nRun embrace without argument to start interacte REPL')
