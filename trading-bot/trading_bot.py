from keys import api, secret_key
from binance.um_futures import UMFutures
import ta
import pandas as pd
from time import sleep
from binance.error import ClientError


client = UMFutures(key=api, secret=secret_key)

tp = 0.01   # Take profit
sl = 0.01   # Stop loss
volume = 50
leverage = 10
type = 'ISOLATED'


def get_balance_usdt():
    try:
        response = client.balance(recvWindow=6000)
        for asset in response:
            if asset['asset'] == 'USDT':
                return float(asset['balance'])

    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )


print("My balance is: ", get_balance_usdt(), " USDT")


def get_tickers_usdt():
    tickers = []
    resp = client.ticker_price()
    for ticker in resp:
        if 'USDT' in ticker['symbol']:
            tickers.append(ticker['symbol'])
    return tickers

print("Tickers: ", get_tickers_usdt())

# Get the last 1000 candles
def klines(symbol):
    try:
        resp = pd.DataFrame(client.klines(symbol=symbol, interval='1h', limit=1000))
        return resp
    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
            )
        )
