import sys
import clipboard
import json

# var of the json file
SAVED_ITEMS = "clipboard.json"


#function to save the data to a json file
def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)

# function to read the json file
def read_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file) # .load() will take the file and ret py dictionary of the json data
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = read_data(SAVED_ITEMS)

    if command == "save":
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_ITEMS, data)
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print("That key does not exist")
    elif command == "list":
        print(data)
    else:
        print('Unknown command.')
else:
    print("Please pass in exactly one command.")