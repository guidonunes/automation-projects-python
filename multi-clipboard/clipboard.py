import sys
import clipboard
import json


if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)

    if command == 'save':
        print('Saving')
    elif command == 'load':
        print('Laoding')
    elif command == 'list':
        print('Listing')
    else:
        print('Invalid command')
print('Please provide a command')
