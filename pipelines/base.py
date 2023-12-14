import os
from abc import ABC, abstractmethod

from pipelines.common import PIPELINE_DATA_DIR


class Pipeline(ABC):
    def __init__(self, save_dir: str):
        if save_dir is None:
            raise ValueError("`save_dir` should ne str, snstead of None.")
        self.save_dir = save_dir
        os.makedirs(self.save_dir_path, exist_ok=True)

    @property
    def save_dir_path(self):
        return os.path.join(PIPELINE_DATA_DIR, self.save_dir)

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
