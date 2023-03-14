
MONGO_URI = "mongodb://localhost:27017"


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'image': {
        'schema': {
            'img': {
                'type': 'string',
            },
            'tag': {
                'type': 'string',
            }
        }
    },
    'untagged_images': {
        'schema': {
            'img_link':{
                'type': 'string'
            },
            'tagged':{
                'type': 'string'
            }

        }
    }
}