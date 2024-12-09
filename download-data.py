import os
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_dir, '..', 'data_raw')

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
else:
    pass

url = 'https://datadryad.org/stash/downloads/file_stream/30903'
r = requests.get(url, allow_redirects=True)

open('data.csv', 'wb').write(r.content)
