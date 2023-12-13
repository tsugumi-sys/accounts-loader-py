import os
from abc import ABC, abstractmethod

from preprocessors.common import PREPROCESSED_DATA_DIR


class BasePreprocessor(ABC):
    def __init__(self, source_dir_path: str, save_dir: str):
        if save_dir is None:
            raise ValueError("`save_dir` should be str, instead of None.")
        if not os.path.exists(source_dir_path):
            raise ValueError(f"`source_dir_path`: {source_dir_path} not found")
        self.save_dir = save_dir
        os.makedirs(self.save_dir_path, exist_ok=True)
        self.source_dir_path = source_dir_path

    @property
    def save_dir_path(self):
        return os.path.join(PREPROCESSED_DATA_DIR, self.save_dir)

    @abstractmethod
    def process(self, *args, **kwargs):
        pass
