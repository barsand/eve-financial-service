schema = {
    'item_methods': ['GET'],
    'resource_methods': ['POST', 'GET'],
    'schema': {
        'name': {
            'type': 'string',
            'required': True,
            # For the sake of scope limitation, `User-Restricted Resource Access` will not be
            # used in this version, so this will behave like a `uniqe` entry (i.e., values are
            # unique resource-wide). Remove this rule to support the same name for different
            # users.
            'unique_to_user': True
        },
        'type': {
            'type': 'string',
            'required': True,
            # This should be replaced by a more robust setup, such as a config collection or a
            # user-managed entity if its a feature that fits the business model
            'allowed': ['Checking', 'Savings', 'Investment', ' Credit Card']
        },
        'current_balance': {
            'type': 'float',
            'default': 0
        },
        'user_id': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'users',
                'field': '_id',
            }
        }
        # An interesting field to be added here would be another `data_relation` referring to
        # transactions linked to this account. This would help processing requests that
        # require account-based grouping when providing user reports.
    }
}
