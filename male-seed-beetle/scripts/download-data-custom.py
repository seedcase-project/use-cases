import os
import requests

# Either code the name in directly, or ask every time.

# folder_name = 'male-seed-beetle'
folder_name = input("Enter the name of the main folder for the project: ")

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_dir, '..', '..', folder_name, 'data_raw')

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
else:
    pass

source = input("Where is the file stored, write either 'u' for url or 'f' for folder: ")

if source == 'u':
    url = input("Write the full url here: ")
    r = requests.get(url, allow_redirects=True)

    file_path = os.path.join(folder_path, 'data.csv')
    with open(file_path, 'wb') as file:
        file.write(r.content)

elif source == 'f':
    folder = input("Write the full path and filename here: ") # /Users/au157729/Downloads/Beetle.txt

    file_path = os.path.join(folder_path, 'data.csv')
    with open(folder, 'rb') as source_file:
        with open(file_path, 'wb') as dest_file:
            dest_file.write(source_file.read())

else:
    print("Did you type either 'u' or 'f' ")
