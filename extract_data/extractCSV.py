import io

import pandas as pd

from extract_data.IExtract import IExtract


class ExtractCSV(IExtract):

    def __init__(self):
        # content  self.path='expanded_buy_computer_data.csv'
        # self.data=self.extract_data()
      pass



    def extract_data(self,content):
        file_csv = io.StringIO(content.decode("utf-8"))

        data=pd.read_csv( file_csv)
        # print(data)
        # data=data.to_dict()

        return data
