import os
from abc import ABC, abstractmethod
from typing import Any, List

from data_loader.constants import RAW_DATA_DIR


class BaseDataLoader(ABC):
    SAVE_ROOT_DIR = RAW_DATA_DIR

    def __init__(self, save_dir_name: str):
        if save_dir_name is None:
            raise ValueError("`save_dir_name` should be str, instead of None.")
        self.save_dir_name = save_dir_name

    @property
    def save_dir_path(self):
        return os.path.join(self.SAVE_ROOT_DIR, self.save_dir_name)

    @property
    def load_data(self, tickers: List[str]):
        pass

    @abstractmethod
    def get_data(self, ticker: str) -> Any:
        pass
