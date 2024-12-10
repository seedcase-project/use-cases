import os

import requests

def download_data_custom():
    """Downloads a data file after asking for the location of the source (url or folder).

    This is the more advanced of the download data scripts. It will ask for the resource 
    name first, then create the data-raw folder with .gitignore file if it finds that they
    do not already exist. 
    There shouldn't be a need to edit the script if it is copied to a new data resource.

    Args:
        url: the url for the data file entered by the user.
        folder: the folder path for the data file entered by the user.

    Returns:
        No return as such, but a file is fetched and stored in the repo.

    Raises:
        If the user doesn't specify either a folder or a url it will abort.
    """

# folder_name = 'male-seed-beetle' For Testing Delete Later

folder_name = input("Enter the name of the main folder for the project: ")

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_dir, '..', '..', folder_name, 'data-raw')

file_path = os.path.join(folder_path, '.gitignore')

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
else:
    pass

if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write('*')
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
    folder = input("Write the full path and filename here: ") 
    # for testing /Users/au157729/Downloads/Beetle.txt

    file_path = os.path.join(folder_path, 'data.csv')
    with open(folder, 'rb') as source_file:
        with open(file_path, 'wb') as dest_file:
            dest_file.write(source_file.read())

else:
    print("Did you type either 'u' or 'f' ")
