import sys
import requests


if __name__ == '__main__':
    transaction_url = 'http://127.0.0.1:5000/transactions/%s' % sys.argv[1]
    res = requests.get(transaction_url)
    res = requests.patch(
        transaction_url,
        json={'amount': sys.argv[2]},
        headers={'If-Match': res.json().get('_etag')}
    )
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
