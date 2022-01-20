# eve-financial-manager

RESTFul service that implements the backend API of a transaction manager's primitive
version–--where all accounts and transactions need to be added manually.

## Deployment
eve-financial-manager was developed and tested in a Unix-based environment, running Debian
GNU/Linux 11 (bullseye). The repo has a `Makefile` to facilitate installation, and deployment;
make sure you have the `build-essentials` packege installed (run `$ apt install
build-essential`). you can also check out the commands at each target denoted at the
`Makefile`.


### Preparation
A MongoDB database is needed to properly run `eve-financial-manager`. Follow [official
instructions](https://docs.mongodb.com/manual/administration/install-community/) on installing
a local instance. You can also create a cloud-based instance using database service such as
[Atlas](https://www.mongodb.com/atlas/database) to instantiate a remote version. Once you have
an instance running, export the URI to acceess the database. If you're running a local
version, for example, run:
```bash
export MONGO_URI='mongodb://127.0.0.1:27017'
```

### Installation
Simply run
```bash
$ make install
```

### Execution

Run
```bash
$ make run
```

## Usage
`eve-financial-manager` has three basic collections: `users`, `accounts` and `transactions`,
structured as follows*:

#### users

| value | type     |
|-------|----------|
| _id   | ObjectId |
| name  | string   |

#### accounts

| value            | type                                 |
|------------------|--------------------------------------|
| _id              | ObjectId                             |
| name             | string                               |
| type             | string                               |
| starting_balance | float                                |
| current_balance  | float                                |
| user             | ObjectId (link to `users` collection) |


#### transactions

| value   | type                                       |
|---------|--------------------------------------------|
| _id     | ObjectId                                   |
| date    | datetime                                   |
| namem   | string                                     |
| amount  | float                                      |
| account | ObjectId (link to  `accounts`  collection) |



* Python Eve also creates additional control fields automatically, such as `_etag`, `_updated`
  and `_created`, which are not listed.

### Adding accounts and transactions
With the API running (`$ make run`), you can either issue requests with the Python scripts
located in the `tests` directory (make sure you use an environment with
[`requests`](https://docs.python-requests.org/en/latest/) installed) and
follow these steps:

1. First of all, create a user:
```bash
$  python3 tests/create-user.py --silent
```
This command outputs an `user_id` on success.

2. Create an account, assigning the created user to it:
```bash
$  python3 tests/create-account.py `<user_id>` --silent
```
This command outputs an `account_id` on success.

3. Create a transaction, assigning the created account to it:
```bash
$  python3 tests/create-transaction.py <account_id> --silent
```
This command outputs a `transaction_id` on success.

Repeat steps 2 and 3 as many times as necessary to create multiple accounts and transactions
for a user.

Additionally, you can also update transaction amounts by running:
```bash
$  python3 tests/update-transaction.py <transaction_id> <amount> --silent
```

#### Querying
Retrieving the information from eve-financial-manager is also quite simple: all listings, filterings
and reports can be performed with simple GET requests (you can use software such as
[Postman](https://www.postman.com/), or just use your Web browser):

- See transactions filtered by date:
```
GET /transactions/?where={"date": {"$gte":"Thu, 20 Jan 2022 00:00:00 GMT", "$lte":"Thu, 21 Jan 2022 00:00:00 GMT"}}
```

- See transactions filtered by account:
```
GET /transactions/?where={"account": "<account_id>"}
```

- See transactions filtered by both date and account:
```
GET /transactions/?where={"date": {"$gte":"Thu, 20 Jan 2021 00:00:00 GMT"}}&where={"account": "<account_id>"}

```

- See balances over time grouped by account:
```
GET /user/<user_id>/balances/accounts
```

- See balances over time, by transaction:
```
GET /account/<account_id>/balances/transactions
```
