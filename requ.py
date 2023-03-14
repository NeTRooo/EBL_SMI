import requests
import json


def load():
    import requests

    url = "http://127.0.0.1:5000/image?img=ор&tag=рф"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def get_image(tag):
    img = load()['_items']
    for i in range(len(img)):
        crate = img[i]['tag']
        if crate == tag:
            res = img[i]['img']

    return res

print(get_image('nigger'))