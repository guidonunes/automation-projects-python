import sys
import clipboard
import json


def save_items(filepath, items):
    with open(filepath, 'w') as file:
        json.dump(items, file)

def load_items(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

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
