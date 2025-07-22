
import pandas as pd

class NaiveBayesBuilder:
    def __init__(self,train_df,label):

        self.data = train_df
        self.label_counts = label

        self.label_counts = pd.Series(label)
        print(self.label_counts)
        self.label_column = self.data.columns[-1]
        self.label_values = self.data[self.label_column].unique()
        self.dict_modal=self.extract_ratios_with_pandas()






    def extract_ratios_with_pandas(self):
        modal = {}

        for column in self.data.columns[:-1]:
            cross = pd.crosstab(self.data[column], self.data[self.label_column])



            amountColumns = self.data[column].nunique()
            denominator = self.label_counts + amountColumns
            smoothed = (cross + 1).div(denominator, axis=1)

            # smoothed = (cross + 1).div(self.label_counts + amountColumns, axis=1)
            modal[column] = smoothed.to_dict(orient='index')

        return modal
