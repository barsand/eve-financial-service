import sys
import random
import datetime
import requests

STOCKS = [
    'AAPL', 'MSFT', 'GOOG', 'GOOGL', 'FB', 'TSM', 'NVDA', 'ASML', 'CSCO', 'ADBE', 'AVGO',
    'ORCL', 'INTC', 'CRM', 'ACN', 'QCOM', 'TXN', 'SAP', 'AMD', 'INTU', 'INFY', 'MU', 'NOW',
    'SPGI', 'IBM'
]

date = datetime.datetime.utcnow() - datetime.timedelta(days=(5-random.randint(0, 5)))


if __name__ == '__main__':
    res = requests.post('http://127.0.0.1:5000/transactions', json={
        'date': date.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'name': 'Purchase %s' % random.choice(STOCKS),
        'amount': '%.2f' % random.uniform(-100, 100),
        'account': sys.argv[1]
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
