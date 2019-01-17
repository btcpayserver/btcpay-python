# btcpay-python

## Install
```shell
pip3 install btcpay-python
```

## The "easy method" to create a new BTCPay client
* On BTCPay server > shop > access tokens > create new token, copy pairing code.
* Then use that code in the below Python code:
```python
from btcpay-python import BTCPayClient

client = BTCPayClient.create_client(host='https://btcpay.example.com', code=<pairing-code>)
```


## Creating a client the manual way (not necessary if you used the 'easy' method)
* Generate and save private key:
```python
import btcpay-python.crypto
privkey = btcpay.crypto.generate_privkey()
```
* Create client:
```python
from btcpay-python import BTCPayClient
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


## Get rates
```python
client.get_rates()
```


## Create specific rate
```python
client.get_rate('USD')
```


## Create invoice
See bitpay api documentation: https://bitpay.com/api#resource-Invoices
```python
client.create_invoice({"price": 20, "currency": "USD"})
```


## Get invoice
```python
client.get_invoice(<invoice-id>)
```
