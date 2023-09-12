
from requests import Session
import matplotlib
import time

def getPrice (): 

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '5439fc0f-cfda-4c0b-a06a-96323ddd906e',
    }
    session = Session() 
    session.headers.update(headers) 
    response = session.get(url, params=parameters) 
    price = (response.json().get("data").get("1").get("quote").get("USD").get("price"))
    print(price)

getPrice() 


