schema = {
    'item_methods': ['GET', 'GET', 'PATCH', 'DELETE'],
    'resource_methods': ['POST', 'GET'],
    'schema': {
        'date': {
            'type': 'datetime',
        },
        'name': {
            'type': 'string',
            'required': True,
        },
        'amount': {
            'type': 'float',
            'required': True,
        },
        'account': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'accounts',
                'field': '_id',
                'embeddable': True
            }
        }
    }
}
