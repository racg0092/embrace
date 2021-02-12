import sys
import os

# channel name
channel = os.path.basename(__file__).replace('.py', '')


def init():
    while True:
        command = input(f'@{channel} >> ')

        if command == '.exit':
            break
        