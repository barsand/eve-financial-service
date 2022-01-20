import os
import pymongo


def update_account_balance(account_id, balance_offset):
    client = pymongo.MongoClient(os.environ['MONGO_URI'])
    client['eve']['accounts'].update_one(
        {'_id': account_id},
        {'$inc': {'current_balance': balance_offset}}
    )
    client.close()


def handle_inserted_transactions(items):
    for item in items:
        update_account_balance(item['account'], item['amount'])


def handle_updated_transactions(updates, original):
    update_account_balance(
        original['account'],
        original['amount'] * -1 + updates['amount']
    )


def handle_deleted_transactions(item):
    update_account_balance(item['account'], item['amount'] * -1)
