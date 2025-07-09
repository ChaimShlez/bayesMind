import pandas as pd

class ExtractData:

    def __init__(self):
        self.path='expanded_buy_computer_data.csv'
        self.data=self.read_data()
        # self.label=self.extract_label_to_dict()
        # self.label, self.train_df, self.y_test = self.extract_train_test_split()


    def read_data(self):
        data=pd.read_csv(self.path)

        return data








# app = FastAPI()
# extractor = ExtractData()


# @app.get("/labels")
# async def get_labels():
#     return extractor.label
#
# @app.get("/data")
# async def get_data():
#     return extractor.data.to_dict(orient='records')








