# btcpay-python

## Install
```shell
pip3 install btcpay-python
```
If you were a user of the prior unofficial client library for Python, you would need to uninstall it first:
```shell
pip3 uninstall btcpay
pip3 install btcpay-python
```
This library is fully backward compatibile with the prior unofficial library; no code changes are needed.

## Pairing to your server:
To connect your website with your BTCPay server, you must first pair your application to BTCPay. To do this you will need to generate a Access token as follows:

1. On your BTCPay server, browse to Stores > Store settings > Access tokens > Create new token
2. Fill in the form:
    Label: <anything that will help you remember what this pairing is used for>
    Public key: leave blank
    Facade: 'merchant'
3. Click save and then copy the 7 digit pairing code from the success page

After you have the access token, you are ready to use the client library to create a client object.

## The "easy method" to create a new BTCPay client
Use the pairing code obtained above as follows:
```python
from btcpay import BTCPayClient

client = BTCPayClient.create_client(host='https://btcpay.example.com', code=<pairing-code>)
```

## Uses for the client object you just created above

You'll probably only ever need the `create_invoice` and `get_invoice` methods, but the client object also has other methods, such as those for getting and setting custom rate information.

### Create invoice
See bitpay api documentation: https://bitpay.com/api#resource-Invoices
```python
new_invoice = client.create_invoice({"price": 20, "currency": "USD"})
```

### Get invoice
```python
fetched_invoice = client.get_invoice(<invoice-id>)
```

### Get rates
```python
client.get_rates()
```

### Create specific rate
```python
client.get_rate('USD')
```

## Storing the client object for later

You do not need to store any tokens or private keys. Simply `pickle` the client object and save it to your persistent storage method (Redis, SQLAlchemy, MongoDB, etc). Do not use `shelve` or a file for storage, as concurrent access could corrupt the static file. Pull the client object from persistent storage later, unpickle it, and perform any of the methods above on it which you may need. You must save the object to persistent storage if you wish for the pairing to persist beyond the limited time your code is in memory.

## Creating a client the manual way (not necessary if you used the 'easy' method above)

If you prefer to create the client object manually (as was the only way in the prior unofficial library), you can do so as follows. This is unnecessary for most developers and is preserved primarily to maintain backward compatibility with both the prior unofficial library and also compatibility with Bitpay.

* Generate and save private key:
```python
import btcpay.crypto
privkey = btcpay.crypto.generate_privkey()
```
* Create client:
```python
from btcpay import BTCPayClient
client = BTCPayClient(host='http://hostname', pem=privkey)
```
* On BTCPay server > shop > access tokens > create new token, copy pairing code:
* Pair client to server and save returned token:
```python
client.pair_client(<pairing-code>)
>>> {'merchant': "xdr9vw3v5wc0w90859v45"}
```
* Recreate client:
```python
client = BTCPayClient(
    host='http://hostname',
    pem=privkey,
    tokens={'merchant': "xdr9vw3v5wc0w90859v45"}
)
```
