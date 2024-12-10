import os

import requests

def download_date():
    """Downloads a data file from a url coded directly in the script.

    This is the most basic of the download data scripts. It requires that the url for 
    the data is written into the script, as well as the folder name 
    for the data resource. It also creates the data-raw folder if that doesn't already
    exist, and creates a .gitignore file in the folder if that doesn't exist.
    There are two things that needs to be edited when the script is copied to a new
    folder, the name of the folder in the folder_path variable and the url for the data.

    Args:
        url: the url for the data file given as a hard-coded variable below.

    Returns:
        No return as such, but a file is fetched and stored in the repo.

    Raises:
        No error messages for now, but will need one if it can't find the file.
    """

script_dir = os.path.dirname(os.path.abspath(__file__)) 

folder_path = os.path.join(script_dir, '..', '..', 'male-seed-beetle', 'data-raw')

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

url = 'https://datadryad.org/stash/downloads/file_stream/30903'

r = requests.get(url, allow_redirects=True)

file_path = os.path.join(folder_path, 'data.csv')
with open(file_path, 'wb') as file:
    file.write(r.content)
