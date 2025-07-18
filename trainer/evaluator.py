import pandas as pd
from predictor.naiveBayesPredictor import NaiveBayesPredictor
class Evaluator:
    def __init__(self,label,modal):
       self.n=NaiveBayesPredictor(label,modal)

    def Evolution_train(self, x_test, y_test):
        correct = 0
        total = len(y_test)
        for i in range(total):
            simple = x_test.iloc[i].to_dict()

            true_label = y_test.iloc[i]
            pred = self.n.predictor(simple)

            if pred == true_label:
                correct += 1

        accuracy = correct / total
        print(f"Final Accuracy: {accuracy:.2f}")







