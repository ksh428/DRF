import requests
import json

# URL="http://127.0.0.1:8000/api/getstudent/"
#URL="http://127.0.0.1:8000/api/poststudent/"
URL="http://127.0.0.1:8000/api/updatestudent/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)

    r=requests.get(url=URL,data=json_data)

    print(r.json())

def post_data():
    data={
    'name':'penaldo',
    'roll':711,
    'city':'agra',
    }
    jsondata=json.dumps(data)
    r=requests.post(url=URL,data=jsondata)
    print(r.json())

def update_data():
    data={
    'id':3,
    'name':'Meghna',
    }
    jsondata=json.dumps(data)
    r=requests.put(url=URL,data=jsondata)
    print(r.json())

def delete_data():
    data={
    'id':3,
    }
    jsondata=json.dumps(data)
    r=requests.delete(url=URL,data=jsondata)
    print(r.json())

# get_data()   
post_data()
#update_data()
#delete_data()