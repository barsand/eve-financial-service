import sys
import requests


if __name__ == '__main__':
    res = requests.post('http://127.0.0.1:5000/accounts', json={
        'user_id': sys.argv[1],
        'name': 'stocks',
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
