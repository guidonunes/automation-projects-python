import sys
import clipboard
import json

SAVED_DATA = 'data.json'

def save_items(filepath, items):
    with open(filepath, 'w') as file:
        json.dump(items, file)

def load_items(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == 'save':
        # Save the clipboard data
        key = input("Enter key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
    elif command == 'load':
        print('Laoding')
    elif command == 'list':
        print('Listing')
    else:
        print('Invalid command')
print('Please provide a command')
