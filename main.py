
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD', 
  'symbol': 'BTC'
  
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters, headers=headers)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)