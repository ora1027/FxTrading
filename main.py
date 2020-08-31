import logging
import sys

from oanda.oanda import APIClient

import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    # print(settings.account_id)
    # print(settings.access_token)
    # print(settings.product_code)
    # print(settings.db_name)
    # print(settings.db_driver)
    # print(settings.web_port)
    # print(settings.trade_duration)
    # print(settings.back_test)
    # print(settings.use_percent)
    # print(settings.past_period)
    # print(settings.stop_limit_percent)
    # print(settings.num_ranking)

    api_client = APIClient(settings.access_token, settings.account_id)
    balance = api_client.get_balance()
    print(balance.currency)
    print(balance.available)
    ticker = api_client.get_ticker(settings.product_code)
    print(ticker.product_code)
    print(ticker.timestamp)
    print(ticker.ask)
    print(ticker.bid)
    print(ticker.volume)