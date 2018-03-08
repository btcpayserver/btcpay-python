"""btcpay.client

BTCPay API Client.
"""

import re
import json
from urllib.parse import urlencode

import requests

from . import crypto


class BTCPayClient:
    def __init__(self, host, pem, insecure=False, tokens=None):
        self.host = host
        self.verify = not(insecure)
        self.pem = pem
        self.tokens = tokens or dict()
        self.client_id = crypto.get_sin_from_pem(pem)
        self.user_agent = 'btcpay-python'
        self.s = requests.Session()
        self.s.verify = self.verify
        self.s.headers.update(
            {'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-accept-version': '2.0.0'})

    def _create_signed_headers(self, uri, payload):
        return {
            "X-Identity": crypto.get_compressed_public_key_from_pem(self.pem),
            "X-Signature": crypto.sign(uri + payload, self.pem)
        }

    def _signed_get_request(self, path, params=None, token=None):
        token = token or list(self.tokens.values())[0]
        params = params or dict()
        params['token'] = token

        uri = self.host + path
        payload = '?' + urlencode(params)
        headers = self._create_signed_headers(uri, payload)
        r = self.s.get(uri, params=params, headers=headers)
        r.raise_for_status()
        return r.json()['data']

    def _signed_post_request(self, path, payload, token=None):
        token = token or list(self.tokens.values())[0]
        uri = self.host + path
        payload['token'] = token
        payload = json.dumps(payload)
        headers = self._create_signed_headers(uri, payload)
        r = self.s.post(uri, headers=headers, data=payload)
        r.raise_for_status()
        return r.json()['data']

    def _unsigned_request(self, path, payload=None):
        uri = self.host + path
        if payload:
            payload = json.dumps(payload)
            r = self.s.post(uri, data=payload)
        else:
            r = self.s.get(uri)
        r.raise_for_status()
        return r.json()['data']

    def get_rates(self, crypto='BTC', store_id=None):
        params = dict(
            cryptoCode=crypto
        )
        if store_id:
            params['storeID'] = store_id
        return self._signed_get_request('/rates/', params=params)

    def get_rate(self, currency, crypto='BTC', store_id=None):
        rates = self.get_rates(crypto=crypto, store_id=store_id)
        rate = [rate for rate in rates if rate['code'] == currency.upper()][0]
        return rate['rate']

    def create_invoice(self, payload, token=None):
        if re.match(r'^[A-Z]{3,3}$', payload['currency']) is None:
            raise ValueError('Currency is invalid.')
        try:
            float(payload['price'])
        except ValueError as e:
            raise ValueError('Price must be a float') from e
        return self._signed_post_request('/invoices/', payload, token=token)

    def get_invoice(self, invoice_id, token=None):
        return self._signed_get_request('/invoices/' + invoice_id, token=token)

    def pair_client(self, code):
        if re.match(r'^\w{7,7}$', code) is None:
          raise ValueError("pairing code is not legal")
        payload = {'id': self.client_id, 'pairingCode': code}
        data = self._unsigned_request('/tokens', payload)
        data = data[0]
        return {
            data['facade']: data['token']
        }

    def __repr__(self):
        return '{}({})'.format(
            type(self).__name__,
            self.host
        )
