import os
from abc import ABC, abstractmethod

from data_loader.constants import RAW_DATA_DIR


class BaseDataLoader(ABC):
    SAVE_ROOT_DIR = RAW_DATA_DIR

    def __init__(self, save_dir: str):
        if save_dir is None:
            raise ValueError("`save_dir` should be str, instead of None.")
        self.save_dir = save_dir
        os.makedirs(self.save_dir_path, exist_ok=True)

    @property
    def save_dir_path(self):
        return os.path.join(self.SAVE_ROOT_DIR, self.save_dir)

    @abstractmethod
    def download(self, *args, **kwargs):
        pass
