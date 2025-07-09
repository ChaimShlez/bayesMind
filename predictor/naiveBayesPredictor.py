import pandas as pd
from trainer.naiveBayesTrainer import NaiveBayesTrainer

class NaiveBayesPredictor:


    def __init__(self):
        self.train=NaiveBayesTrainer()
        self.label_counts=self.train.label_counts



    def Predictor(self,dataPred):
        result_modal= self.train.dict_result_modal
        total = sum(self.label_counts)
        probs = {}

        for label in self.label_counts.index:
            prob = self.label_counts[label] / total
            for feature, value in dataPred.items():
                prob *=  result_modal[feature][value][label]
            probs[label] = prob

        return max(probs, key=probs.get)
        # return probs
