import requests
import json
import os
from PIL import Image


def load_untagged():
    url = "http://127.0.0.1:5000/untagged_images"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
def load_tagged():
    import requests

    url = "http://127.0.0.1:5000/image?img=ор&tag=рф"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def get_image(tag):
    try:
        img = load_tagged()['_items']
        for i in range(len(img)):
            crate = img[i]['tag']
            if crate == tag:
                res = img[i]['img']

        img_data = requests.get(res).content
        print(img_data)
        with open('../image_name.jpg', 'wb') as handler:
            handler.write(img_data)
        return 'OK', True
    except:
        return 'get_image func failed', False



def upload_image(img, tag):
    try:
        url = 'http://127.0.0.1:5000/image'
        payload = json.dumps({'img': img, 'tag': tag})
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(url, headers=headers, data=payload)
    except:
        return 'upload_image func failed'

def upload_untagged_image(img):
    try:
        url = 'http://127.0.0.1:5000/untagged_images'
        payload = json.dumps({'img_link': img, 'tagged': 'False'})
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(url, headers=headers, data=payload)
        print(response)
    except:
        return 'download_untagged img func failed'

