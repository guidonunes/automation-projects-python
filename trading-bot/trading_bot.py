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
        resp = pd.DataFrame(client.klines(symbol=symbol, interval='1h', limit=500))
        resp = resp.iloc[:, 0:6]
        resp.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        resp = resp.set_index('date')
        resp.index = pd.to_datetime(resp.index, unit='ms')
        resp = resp.astype(float)
        return resp
    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
            )
        )

print(klines('ADAUSDT'))

# Set leverage
def set_leverage(symbol, leverage):
    try:
        response = client.change_leverage(
        symbol=symbol, leverage=leverage, recvWindow=6000
        )
        print(response)
    except ClientError as error:
        print(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

def set_mode(symbol, type):
    try:
        response = client.change_margin_type(
        symbol=symbol, marginType=type, recvWindow=6000
        )
        print(response)
    except ClientError as error:
        print(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

def get_price_precision(symbol):
    response = client.exchangeInfo()['symbols']
    for elem in response:
        if elem['symbol'] == symbol:
            return elem['pricePrecision']


def get_qty_precision(symbol):
    response = client.exchangeInfo()['symbols']
    for elem in response:
        if elem['symbol'] == symbol:
            return elem['quantityPrecision']

def open_order(symbol,side):
    price = float(client.ticker_price(symbol=symbol)['price'])
    qty_precision = get_qty_precision(symbol)
    price_precision = get_price_precision(symbol)
    qty = round(volume / price, qty_precision)
    if side == 'buy':
        try:
            resp1 = client.new_order(symbol=symbol, side='BUY', type='LIMIT', quantity=qty, timeInForce='GTC', price=price)
            print(symbol, side, 'placing order')
            print(resp1)
            sleep(2)
            sl_price = round(price - price * sl, price_precision)
            resp2 = client.new_order(symbol=symbol, side='SELL', type='STOP_MARKET', quantity=qty, timeInForce='GTC', stopPrice=sl_price)
            sleep(2)
            tp_price = round(price + price * tp, price_precision)
            resp3 = client.new_order(symbol=symbol, side='SELL', type='TAKE_PROFIT_MARKET', quantity=qty, timeInForce='GTC', stopPrice=tp_price)
            sleep(2)
