import sys
import os
import json

environment = 'dev'

def loadData(filename):
    try:
        f = open(filename, 'r')
        return json.load(f)
    except FileNotFoundError as e:
        print(f'package.json not found: {e!r}')
        raise

def getData(filename):
    if environment == 'dev':
        return loadData(filename)
    elif environment == 'prod':
        try:
            os.chdir(sys._MEIPASS)
            return loadData(filename)
        except SystemError as e:
            print(f'{e!r}')
            raise
        else:
            print('Unkown error')