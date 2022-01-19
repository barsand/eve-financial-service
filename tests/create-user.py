import sys
import datetime
import requests


if __name__ == '__main__':
    res = requests.post('http://127.0.0.1:5000/users', json={
        'name': 'usename%s' % int(datetime.datetime.utcnow().timestamp())
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
