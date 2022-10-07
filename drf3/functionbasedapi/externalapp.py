import requests
import json

URL="http://127.0.0.1:8000/apistudent/"
#URL="http://127.0.0.1:8000/api/poststudent/"
#URL="http://127.0.0.1:8000/api/updatestudent/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    print(r.json())

def post_data():
    data={
    'name':'penaldo',
    'roll':711,
    'city':'agra',
    }
    headers={'content-Type':'application/json'}
    jsondata=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=jsondata)
    print(r.json())

def update_data():
    data={
    'id':3,
    'name':'Meghna',
    }
    headers={'content-Type':'application/json'}
    jsondata=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=jsondata)
    print(r.json())

def delete_data():
    data={
    'id':1,
    }
    headers={'content-Type':'application/json'}
    jsondata=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=jsondata)
    print(r.json())

#get_data(1)   
#post_data()
#update_data()
delete_data()