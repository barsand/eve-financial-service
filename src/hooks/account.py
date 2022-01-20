def handle_insert_accounts(items):
    for item in items:
        item['current_balance'] = item['starting_balance']
