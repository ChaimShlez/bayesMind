import pandas as pd
from trainer.naiveBayesTrainer import NaiveBayesTrainer

class NaiveBayesPredictor:

    def __init__(self,label,modal):
        self.modal=modal
        self.label = pd.Series(label)



    def predictor(self,dataPred):

        result_modal= self.modal
        t_p = pd.Series(self.label)
        total = sum(t_p)
        probs = {}
        for label in self.label.index:
            prob = self.label[label] / total

            for feature, value in dataPred.items():
                if feature in result_modal and value in result_modal[feature] and label in result_modal[feature][value]:
                    p_val = result_modal[feature][value][label]
                    prob *= p_val
            probs[label] = prob
        print(f"prods-{probs}")

        return max(probs, key=probs.get)

