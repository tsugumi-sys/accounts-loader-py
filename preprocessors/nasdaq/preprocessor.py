from enum import StrEnum
import json
import os

from preprocessors.base import BasePreprocessor

import pandas as pd

PRPOCESSED_NASDAQ_SYMBOLS_DATA_DIR = "nasdaq/symbols"


class Exchange(StrEnum):
    NASDAQ = "nasdaq"
    NYSE = "nyse"
    AMEX = "amex"


class NASDAQSymbolsPreprocessor(BasePreprocessor):
    def __init__(
        self,
        source_dir_path: str,
        save_dir: str = os.path.join(f"nasdaq/symbols/{Exchange.NASDAQ}"),
    ):
        super().__init__(source_dir_path, save_dir)

    def preprocess(self):
        with open(os.path.join(self.source_dir_path, "data.json"), "r") as f:
            data = json.load(f)
        symbols_data = {k: [v] for k, v in data[0].items()}
        for d in data[1:]:
            for key, value in d.items():
                symbols_data[key].append(value)
        pd.DataFrame.from_dict(symbols_data).to_csv(
            os.path.join(self.save_dir_path, "data.csv")
        )


class NYSESymbolsPreprocessor(BasePreprocessor):
    def __init__(
        self,
        source_dir_path: str,
        save_dir: str = os.path.join(f"nasdaq/symbols/{Exchange.NYSE}"),
    ):
        super().__init__(source_dir_path, save_dir)

    def preprocess(self):
        with open(os.path.join(self.source_dir_path, "data.json"), "r") as f:
            data = json.load(f)
        symbols_data = {k: [v] for k, v in data[0].items()}
        for d in data[1:]:
            for key, value in d.items():
                symbols_data[key].append(value)
        pd.DataFrame.from_dict(symbols_data).to_csv(
            os.path.join(self.save_dir_path, "data.csv")
        )


class AMEXSymbolsPreprocessor(BasePreprocessor):
    def __init__(
        self,
        source_dir_path: str,
        save_dir: str = os.path.join(f"nasdaq/symbols/{Exchange.AMEX}"),
    ):
        super().__init__(source_dir_path, save_dir)

    def preprocess(self):
        with open(os.path.join(self.source_dir_path, "data.json"), "r") as f:
            data = json.load(f)
        symbols_data = {k: [v] for k, v in data[0].items()}
        for d in data[1:]:
            for key, value in d.items():
                symbols_data[key].append(value)
        pd.DataFrame.from_dict(symbols_data).to_csv(
            os.path.join(self.save_dir_path, "data.csv")
        )
