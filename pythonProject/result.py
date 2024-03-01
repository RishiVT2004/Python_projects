import currencyapicom
import json
from requests import get
from pprint import PrettyPrinter


api_key = "cur_live_kJH7ttaF7rWv9gpV8GOL9bokDpim5s59VW4VBwUZ";
base_url = "https://api.currencyapi.com/"

def get_currency():
    printer = PrettyPrinter()
    client = currencyapicom.Client(api_key)
    result = client.currencies()

    endpoint = f"v3/latest?apikey={api_key}"    
    url = base_url + endpoint
    data = get(url).json()['data']

    data = list(data.items())
    data.sort()

    return data

def print_currency(currencies):
    for currency in currencies:
        name = currency['name']
        _id_ = currency['code']
        symbol = currency['symbol']

        print(f'{name} - {_id_} - {symbol}')

currency = get_currency()
print_currency(currency)

