import os
import eve
import sys
import hooks
import pymongo
import settings


def check_db_conn():
    try:
        mongo_uri = os.environ['MONGO_URI']
        mongo_client = pymongo.MongoClient(mongo_uri)
        mongo_client.admin.command('ismaster')

    except KeyError:
        sys.exit('environment variable MONGO_URI must be set (use mongodb://127.0.0.1:27017'
                 'for local mongo instance, for example).')
    except pymongo.errors.InvalidURI:
        sys.exit('please specify a valid mongo URI')
    except pymongo.errors.ConnectionFailure as e:
        print(e.args)
        sys.exit('\nfailed to connect to the database')
    return


check_db_conn()

app = eve.Eve(settings={
    'DOMAIN': settings.DOMAIN
})

app.on_inserted_transactions = hooks.balance.handle_inserted_transactions
app.on_updated_transactions = hooks.balance.handle_updated_transactions
app.on_deleted_item_transactions = hooks.balance.handle_deleted_transactions


if __name__ == '__main__':
    app.run()
