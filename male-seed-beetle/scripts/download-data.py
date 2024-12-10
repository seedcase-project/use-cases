import os
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_dir, '..', '..', 'male-seed-beetle', 'data_raw')

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
