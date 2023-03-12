
import http.client
import json
import hmac
import hashlib

# conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
# payload = '/prices'

# timestamp = str(int(time.time()))
# passphase = '...'
# api_key = 'rilzSAJuTy2DsOe6'
# api_secret = 'KKia9KXG8DKpfylVXndbTZN1oyezZn59'
# request_path  = '/oracles'
# method = 'GET'
# body = ''

# message = timestamp + method + request_path + body
# signature = hmac.new(api_key.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()

 
# headers = {
#   'Content-Type': 'application/json',
#   'cb-access-key': api_key,
#   'cb-access-passphrase': passphase,
#   'cb-access-sign': signature,
#   'cb-access-timestamp': str(int(time.time())),
# }

# api_url = 'https://api.exchange.coinbase.com/oracle'

# conn.request("GET", "/oracle", payload, headers)


# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

# API Key: rilzSAJuTy2DsOe6
# API Secret: KKia9KXG8DKpfylVXndbTZN1oyezZn59
import json, hmac, hashlib, time, requests
from requests.auth import AuthBase

timestamp = str(int(time.time()))

# Create custom authentication for Coinbase API
class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time.time()))
        message = timestamp + request.method + request.path_url + (request.body or '')
        signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
        })
        return request

api_url = 'https://api.exchange.coinbase.com/v2/'
auth = CoinbaseWalletAuth(API_KEY, API_SECRET)
r = requests.get(api_url + '/oracle', auth=auth)
print(r.json())