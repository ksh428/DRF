#EXTERNAL APP ON CLIENT SIDE

import requests
URL="http://127.0.0.1:8000/api/"

print(requests.get(url=URL).json())