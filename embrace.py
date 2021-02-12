#!/usr/bin/env python3
import sys
import presentation

presentation.Welcome()

while True:
    command = input('> ')
    if command == '.exit':
        break
