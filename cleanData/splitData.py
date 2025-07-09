from sklearn.model_selection import train_test_split
import pandas as pd

class SplitData:
    def __init__(self,data):
        self.data=data

    def extract_train_test_split(self):
        col = self.data.columns[-1]
        data_label=col.value_counts().to_dict()
        return data_label

    def split(self):
        col = self.data.columns[-1]

        x = self.data.drop(columns=col)
        y = self.data[col]

        split_index = int(len(self.data) * 0.7)

        x_train = x[:split_index]
        y_train = y[:split_index]

        x_test = x[split_index:]
        y_test = y[split_index:]
        df_data = pd.concat([x_train, y_train], axis=1)
        return df_data, y_train, y_test
