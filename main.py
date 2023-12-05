from data_loader import PolygonFinancialDataLoader
from preprocess import FinancialsDataPreprocessor


def main():
    data_loader = PolygonFinancialDataLoader()
    data_loader.run()

    preprocessor = FinancialsDataPreprocessor()
    preprocessor.run()


if __name__ == "__main__":
    main()
