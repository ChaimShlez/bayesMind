from extract_data.extractData import ExtractData
import pandas as pd

class NaiveBayesTrainer:
    def __init__(self,train_df,label):

        self.data = train_df
        self.label_counts = label
        # self.y_test=df.y_test
        self.label_counts = pd.Series(label)
        self.label_column = self.data.columns[-1]
        self.label_values = self.data[self.label_column].unique()
        self.dict_modal=self.extract_ratios_with_pandas()






    def extract_ratios_with_pandas(self):
        modal = {}

        for column in self.data.columns[1:-1]:
            cross = pd.crosstab(self.data[column], self.data[self.label_column])

            for val in self.label_values:
                if val not in cross.columns:
                    cross[val] = 0

            amountColumns = self.data[column].nunique()
            smoothed = (cross + 1).div(self.label_counts + amountColumns, axis=1)
            modal[column] = smoothed.to_dict(orient='index')

        return modal
