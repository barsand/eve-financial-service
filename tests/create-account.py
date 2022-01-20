import sys
import random
import requests
import datetime


if __name__ == '__main__':
    res = requests.post('http://127.0.0.1:5000/accounts', json={
        'user': sys.argv[1],
        'starting_balance': '%.2f' % random.uniform(0, 1000),
        'name': 'stocks-%d' % int(datetime.datetime.utcnow().timestamp()),
        'type': 'Investment'
    })
    if '--silent' in sys.argv:
        try:
            print(res.json()['_id'])
        except Exception:
            if '--debug' in sys.argv:
                import ipdb
                ipdb.set_trace()
            else:
                pass
    else:
        import json
        print(json.dumps(res.json(), indent=4))
