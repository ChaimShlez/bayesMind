import numbers

import pandas as pd

class NaiveBayesPredictor:

        def __init__(self,model,label):
            self.model = model

            if isinstance(label, dict):
                self.label = pd.Series(label)
            else:
                self.label = label

        def safe_sum_series(self, label):
            total = 0
            for item in label.values:
                if isinstance(item, numbers.Number):
                    total += item
                elif isinstance(item, dict):
                    total += sum(v for v in item.values() if isinstance(v, numbers.Number))
            return total

        def predictor(self, dataPred):

            result_model = self.model
            print([type(v) for v in self.label.values])
            label=self.label

            total = self.safe_sum_series(label)
            probs = {}
            for label in self.label.index:
                prob = self.label[label] / total
                for feature, value in dataPred.items():
                    if feature in result_model and value in result_model[feature] and label in result_model[feature][value]:
                        p_val = result_model[feature][value][label]
                        prob *= p_val
                probs[label] = prob

            print(max(probs, key=probs.get))
            return max(probs, key=probs.get)

