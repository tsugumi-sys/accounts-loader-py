# from data_loader import PolygonFinancialDataLoader
# from preprocess import FinancialsDataPreprocessor

from data_loader.polygon_data_loader import PolygonDataLoader


def main():
    data_loader = PolygonDataLoader()
    print(data_loader.save_dir_path)
    # data_loader.run()

    # preprocessor = FinancialsDataPreprocessor()
    # preprocessor.run()


if __name__ == "__main__":
    main()
