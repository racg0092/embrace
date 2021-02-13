import sys
import os
from eprint.main import printBWG

# channel name
channel = os.path.basename(__file__).replace('.py', '')


def init():
    while True:
        command = printBWG(channel)

        if command == '.exit':
            break
        