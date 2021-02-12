import sys
import os
import json

environment = 'dev'

def loadData():
    try:
        f = open('package.json', 'r')
        return json.load(f)
    except FileNotFoundError as e:
        print(f'package.json not found: {e!r}')
        raise

def getData():
    if environment == 'dev':
        return loadData()
    elif environment == 'prod':
        try:
            os.chdir(sys._MEIPASS)
            return loadData()
        except SystemError as e:
            print(f'{e!r}')
            raise
        else:
            print('Unkown error')


