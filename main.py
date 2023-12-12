# from data_loader import PolygonFinancialDataLoader
# from preprocess import FinancialsDataPreprocessor

from data_loader.polygon_data_loader import PolygonFinancialsDataLoader
from data_loader.nasdaq_data_loader import (
    NASDAQSymbolsDataLoader,
    NYSESymbolsDataLoader,
    AMEXSymbolsDataLoader,
)
from data_loader.constants import TICKERS


def main():
    data_loader = NASDAQSymbolsDataLoader()
    print(data_loader.save_dir_path)
    data_loader.download()
    # data_loader.run()

    # preprocessor = FinancialsDataPreprocessor()
    # preprocessor.run()


if __name__ == "__main__":
    main()
