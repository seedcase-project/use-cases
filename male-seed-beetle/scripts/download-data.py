import os
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_dir, '..', '..', 'male-seed-beetle', 'data_raw')

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
else:
    pass

url = 'https://datadryad.org/stash/downloads/file_stream/30903'

r = requests.get(url, allow_redirects=True)

file_path = os.path.join(folder_path, 'data.csv')
with open(file_path, 'wb') as file:
    file.write(r.content)
