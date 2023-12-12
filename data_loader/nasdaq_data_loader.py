# https://www.nasdaq.com/
from enum import StrEnum
import json
import logging
import os

import requests

from data_loader.base_data_loader import BaseDataLoader


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

CUSTOM_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0"
)
CUSTOM_HEADERS = {"user-agent": CUSTOM_USER_AGENT}


class Exchange(StrEnum):
    NASDAQ = "nasdaq"
    NYSE = "nyse"
    AMEX = "amex"


def symbols_api_endpoint(exchange_name: Exchange):
    return f"https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&exchange={exchange_name}&download=true"


class NASDAQSymbolsDataLoader(BaseDataLoader):
    def __init__(self, save_dir: str = "nasdaq/nasdaq/symbols"):
        super().__init__(save_dir)
        self.exchange_name = Exchange.NASDAQ

    def download(self):
        logger.info(
            f"Loading {self.exchange_name.upper()} symbols data from `https://www.nasdaq.com/`"
        )

        res = requests.get(
            symbols_api_endpoint(self.exchange_name), headers=CUSTOM_HEADERS
        )
        if res.status_code != 200:
            logger.error(
                f"Request Failed with status code: {res.status_code}. All response body is the following: {res.text}"
            )

        with open(os.path.join(self.save_dir_path, "data.json"), "w") as f:
            json.dump(res.json().get("data").get("rows"), f)


class NYSESymbolsDataLoader(BaseDataLoader):
    def __init__(self, save_dir: str = "nasdaq/nyse/symbols"):
        super().__init__(save_dir)
        self.exchange_name = Exchange.NYSE

    def download(self):
        logger.info(
            f"Loading {self.exchange_name.upper()} symbols data from `https://www.nasdaq.com/`"
        )
        res = requests.get(
            symbols_api_endpoint(self.exchange_name), headers=CUSTOM_HEADERS
        )

        if res.status_code != 200:
            logger.error(
                f"Request Failed with status code: {res.status_code}. All response body is the following: {res.text}"
            )

        with open(os.path.join(self.save_dir_path, "data.json"), "w") as f:
            json.dump(res.json().get("data").get("rows"), f)


class AMEXSymbolsDataLoader(BaseDataLoader):
    def __init__(self, save_dir: str = "nasdaq/amex/symbols"):
        super().__init__(save_dir)
        self.exchange_name = Exchange.AMEX

    def download(self):
        logger.info(
            f"Loading {self.exchange_name.upper()} symbols data from `https://www.nasdaq.com/`"
        )

        res = requests.get(
            symbols_api_endpoint(self.exchange_name), headers=CUSTOM_HEADERS
        )

        if res.status_code != 200:
            logger.error(
                f"Request Failed with status code: {res.status_code}. All response body is the following: {res.text}"
            )

        with open(os.path.join(self.save_dir_path, "data.json"), "w") as f:
            json.dump(res.json().get("data").get("rows"), f)
