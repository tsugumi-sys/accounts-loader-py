from data_loader.base_data_loader import BaseDataLoader


class PolygonDataLoader(BaseDataLoader):
    def __init__(self, save_dir_path="polygon"):
        super().__init__(save_dir_path)
