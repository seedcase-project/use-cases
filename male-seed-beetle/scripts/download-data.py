from pathlib import Path

import requests

#testing:
url = 'https://datadryad.org/stash/downloads/file_stream/30903'

def download_data(url: str):
    """Downloads a data file from a given URL.

    This is the most basic of the download data scripts. It requires that the url for 
    the data is provided as an argument, as well as the folder name 
    for the data resource. It also creates the data-raw folder if that doesn't already
    exist, and creates a .gitignore file in the folder if that doesn't exist.
    There are two things that need to be edited when the script is copied to a new
    folder, the name of the folder in the folder_path variable and the url for the data.

    Args:
        url: the url for the data file given as an argument.

    Returns:
        No return as such, but a file is fetched and saved to the relevant folder in the repo.

    Raises:
        No error messages for now, but will need one if it can't find the file.
    """

script_dir = Path(__file__).resolve().parent.parent #testing male-seed-beetle returned with print(f'{script_dir}')

folder_path = script_dir / 'data-raw' #testing male-seed-beetle/data-raw returned with print(f'{folder_path}')

raw_data = requests.get(url, allow_redirects=True)

file_path = folder_path / 'data.csv'

with open(file_path, 'wb') as file:
    file.write(raw_data.content) 
