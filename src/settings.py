import models

DOMAIN = {
    'users': models.user.schema,
    'accounts': models.account.schema,
    'transactions': models.transaction.schema
}
