from keys import api, secret_key
from binance.um_futures import UMFutures
import ta
import pandas as pd
from time import sleep
from binance.error import ClientError


client = UMFutures(key=api, secret=secret_key)

tp = 0.01   # Take profit
sl = 0.01   # Stop loss
volume = 50 # Volume in USDT
leverage = 10
type = 'ISOLATED' # Isolated margin


def get_balance_usdt():
    try:
        response = client.balance(recvWindow=6000)
        print(response)
        for asset in response:
            if asset['asset'] == 'USDT':
                return float(asset['balance'])

    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )


print(get_balance_usdt())


# Task: Fix API keys
