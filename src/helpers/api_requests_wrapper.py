import requests
import json

def get_requests(url,auth,in_json):
    response=requests.get(url=url,auth=auth)
    if in_json is True:
        return response.json()
    return response

def post_requests(url,auth,payload,headers,in_json):
    post_response=requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

