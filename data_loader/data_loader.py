import json
import logging
import time

from dotenv import dotenv_values
from polygon import RESTClient

from constants import FINANCIALS_DATA_DIR, TICKERS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PolygonFinancialDataLoader:
    tickers = TICKERS
    save_dir = FINANCIALS_DATA_DIR
    request_limit_min = 5

    def __init__(self):
        self.polygon_client = RESTClient(dotenv_values(".env").get("POLYGON_API_KEY"))

    def run(self):
        request_count = 0
        for ticker in self.tickers:
            logger.info(f"Loading {ticker} data from Polygon ...")
            finalcials_data = {}

            self._avoid_request_limit(request_count)
            request_count += 1
            for item in self._get_data(ticker):
                financial_data = {}
                financial_data["date"] = item.filing_date
                financial_data["fiscal_period"] = item.fiscal_period
                financial_data["fiscal_year"] = item.fiscal_year

                income_statement = item.financials.income_statement
                financial_data["revenues"] = {
                    "formula": income_statement.revenues.formula,
                    "label": income_statement.revenues.label,
                    "order": income_statement.revenues.order,
                    "unit": income_statement.revenues.unit,
                    "value": income_statement.revenues.value,
                    "xpath": income_statement.revenues.xpath,
                }

                financial_data["gross_profit"] = {
                    "formula": income_statement.gross_profit.formula,
                    "label": income_statement.gross_profit.label,
                    "order": income_statement.gross_profit.order,
                    "unit": income_statement.gross_profit.unit,
                    "value": income_statement.gross_profit.value,
                    "xpath": income_statement.gross_profit.xpath,
                }
                finalcials_data[item.filing_date] = financial_data

            with open(f"./data/financials/{ticker}.json", "w") as f:
                json.dump(finalcials_data, f)

    def _get_data(self, ticker: str) -> list:
        rawdata = []
        for d in self.polygon_client.vx.list_stock_financials(
            ticker=ticker, filing_date_gte="2022-01-01"
        ):
            rawdata.append(d)
        return rawdata

    def _avoid_request_limit(self, request_count: int):
        if request_count < self.request_limit_min:
            return
        if request_count % 5 != 0:
            return
        logger.info("Waiting for 90 seconds to avoid request limit")
        time.sleep(90)


if __name__ == "__main__":
    data_loader = PolygonFinancialDataLoader()
    data_loader.run()
