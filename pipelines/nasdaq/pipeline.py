import logging
from preprocessors.nasdaq.preprocessor import (
    NASDAQSymbolsPreprocessor,
    NYSESymbolsPreprocessor,
    AMEXSymbolsPreprocessor,
)
from data_loaders.nasdaq.data_loader import NASDAQSymbolsDataLoader

from pipelines.base import Pipeline


logger = logging.getLogger(__name__)


class NASDAQSymbolsPipeline(Pipeline):
    def __init__(self, save_dir: str = "nasdaq"):
        super.__init__(save_dir)

    def run(self):
        logger.info("{} NASDAQ pipline starts {}".format("=" * 30, "=" * 30))
