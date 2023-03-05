MONGO_URI = "mongodb://193.164.17.141:27017"
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
MONGO_DBNAME = 'images'
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'qDpIu8CY4w8X'
schema = {'id': {
    'type': 'integer',
},
    'img': {
        'type': 'text'
    },
    'tag': {
        'type': 'text'
    }

}
images = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'image',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'tag'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}
DOMAIN = {'images': images}

