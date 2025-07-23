import pandas as pd
from base.IDataLoader import IDataLoader
from logHandler.logConfig import LogConfig



class DataLoaderCSV(IDataLoader):

    def __init__(self):
        self.logger = LogConfig.get_logger("loader")
        self.path = 'data.csv'
        self.data = self.read_data()

    def read_data(self):
        self.logger.info(f"Starting to read data from {self.path}")

        try:
            data = pd.read_csv(self.path)
            self.logger.info(f"Successfully read {len(data)} rows from {self.path}")
            return data
        except Exception as e:
            self.logger.error(f"Failed to read data from {self.path}: {e}")
            raise
