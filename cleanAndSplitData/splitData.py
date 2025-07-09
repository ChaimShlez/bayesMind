from sklearn.model_selection import train_test_split
import pandas as pd

class SplitData:
    def __init__(self,data):
        self.data=data

        self.label=self.extract_label()
        self.df_data, self.x_test, self.y_test=self.split_from_test_modal()

    def extract_label(self):

        col = self.data.columns[-1]
        data_label = self.data[col].value_counts().to_dict()
        # data_label = self.data.value_counts().to_dict()
        return data_label

    def split_from_test_modal(self):
        data_shuffled = self.data.sample(frac=1, random_state=42).reset_index(drop=True)

        data_no_id = data_shuffled.drop(columns=['id'])
        col = data_no_id.columns[-1]

        x = data_no_id.drop(columns=col)
        y = data_no_id[col]

        split_index = int(len(data_shuffled) * 0.7)

        x_train = x[:split_index]
        y_train = y[:split_index]

        x_test = x[split_index:]
        y_test = y[split_index:]

        # x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.33, random_state=42)

        df_data = pd.concat([x_train, y_train], axis=1)
        return df_data,  x_test, y_test
