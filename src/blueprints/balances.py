import os
import bson
import flask
import pymongo
import collections


balances = flask.Blueprint('balances', __name__)


@balances.route('/user/<user_id>/balances/accounts', methods=['GET'])
def report_transactions_grouped_by_account(user_id):
    # TODO check why does db.transactions.find({'account.user_id': <user_id>}) isn't working.
    client = pymongo.MongoClient(os.environ['MONGO_URI'])

    date2account2transactions = collections.defaultdict(lambda: collections.defaultdict(list))
    account_info = collections.defaultdict(dict)

    for account in client['eve']['accounts'].find({'user': bson.ObjectId(user_id)}):
        curr_account_id = str(account['_id'])
        account_info[curr_account_id]['starting_balance'] = account['starting_balance']
        account_info[curr_account_id]['name'] = account['name']
        account_info[curr_account_id]['type'] = account['type']

        for transaction in client['eve']['transactions'].find({'account': account['_id']}):
            curr_date_strf = transaction['date'].strftime('%Y/%m/%d')
            date2account2transactions[curr_date_strf][curr_account_id].append(
                    transaction['amount'])

    account2latest_balance = dict()
    for account_id, account_data in account_info.items():
        account2latest_balance[account_id] = account_data['starting_balance']

    balance = collections.defaultdict(dict)
    for date in sorted(date2account2transactions.keys()):
        for account_id, account_data in account_info.items():

            account2latest_balance[account_id] += \
                    sum(date2account2transactions[date][account_id])
            balance[date][account_id] = account2latest_balance[account_id]

    balance_table = list()
    balance_table.append('\t'.join(['Account', 'Name', 'Type', 'Date', 'Balance']))
    for date, account_balances in balance.items():
        for account_id in sorted(account_balances.keys()):
            balance_table.append('\t'.join([
                account_id,
                account_info[account_id]['name'],
                account_info[account_id]['type'],
                date,
                '%.2f' % balance[date][account_id]
            ]))
        balance_table.append('\n')

    return '\n'.join(balance_table)
