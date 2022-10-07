#EXTERNAL APP ON CLIENT SIDE
import json
import requests
import json

URL="http://127.0.0.1:8000/apicreate/"

data={
    'name':'Meghna',
    'roll':102,
    'city':'Durgapur',
}
jsondata=json.dumps(data)
r=requests.post(url=URL,data=jsondata)
