# from data_loader import PolygonFinancialDataLoader
# from preprocess import FinancialsDataPreprocessor

from data_loader.polygon_data_loader import PolygonFinancialsDataLoader
from preprosessors.polygon_data_preprocessor import PolygonFinancialsDataPreprocessor

# from data_loader.nasdaq_data_loader import (
#     NASDAQSymbolsDataLoader,
#     NYSESymbolsDataLoader,
#     AMEXSymbolsDataLoader,
# )

TICKERS = ["NVDA", "INTC", "AVGO", "TXN", "QCOM", "AMAT", "MU", "AMD"]


def main():
    data_loader = PolygonFinancialsDataLoader()
    data_loader.download(TICKERS)
    preprocessor = PolygonFinancialsDataPreprocessor(
        source_dir_path=data_loader.save_dir_path
    )
    preprocessor.run(TICKERS)


if __name__ == "__main__":
    main()
