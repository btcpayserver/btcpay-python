# btcpay-python


## Pairing
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


## Creating a client
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
