import json
import logging
import os

import pandas as pd

from constants import FINANCIALS_DATA_DIR, TICKERS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class FinancialsDataPreprocessor:
    data_dir = FINANCIALS_DATA_DIR

    def run(self):
        data = {
            "ticker": [],
            "fiscal_period": [],
            "fiscal_year": [],
            "fiscal_date": [],
            "revenue": [],
            "gross_profit": [],
            "unit": [],
        }
        for ticker in TICKERS:
            logger.info(f"Preprocessing {ticker} data ...")
            raw_data = self._load_data(ticker)
            for date, item in raw_data.items():
                logger.debug(f"{'=' * 20} {date} {'=' * 20}")
                logger.debug("Fiscal Period: {}".format(item.get("fiscal_period")))
                logger.debug("Fiscal Year: {}".format(item.get("fiscal_year")))
                # Calculate revenue
                if item.get("revenues").get("formula") is not None:
                    logger.warning(
                        "formula exists on revenues: {}".format(
                            item.get("revenues").get("formula")
                        )
                    )
                logger.debug(
                    "Revenue: {} {}".format(
                        item.get("revenues").get("value"),
                        item.get("revenues").get("unit"),
                    )
                )
                # Calculate gross profit
                if item.get("gross_profit").get("formula") is not None:
                    logger.warning(
                        "formula exists on gross profit: {}".format(
                            item.get("gross_profit").get("formula")
                        )
                    )
                logger.debug(
                    "Revenue: {} {}".format(
                        item.get("gross_profit").get("value"),
                        item.get("gross_profit").get("unit"),
                    )
                )

                data["ticker"].append(ticker)
                data["fiscal_period"].append(item.get("fiscal_period"))
                data["fiscal_year"].append(item.get("fiscal_year"))
                data["fiscal_date"].append(date)
                data["revenue"].append(item.get("revenues").get("value"))
                data["gross_profit"].append(item.get("gross_profit").get("value"))
                data["unit"].append(item.get("revenues").get("unit"))
        pd.DataFrame.from_dict(data).to_csv("./financials.csv")

    def _load_data(self, ticker: str) -> dict:
        with open(os.path.join(self.data_dir, f"{ticker}.json"), "r") as f:
            data = json.load(f)
        return data


if __name__ == "__main__":
    preprocessor = FinancialsDataPreprocessor()
    preprocessor.run()
