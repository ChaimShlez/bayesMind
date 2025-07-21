import pandas as pd
from predictor.naiveBayesPredictor import NaiveBayesPredictor
class Evaluator:
    def __init__(self,label,modal):
       self.n=NaiveBayesPredictor(label,modal)

    def Evolution_train(self, x_test, y_test):
        correct = 0
        TP = FP = TN = FN = 0
        total = len(y_test)
        for i in range(total):
            simple = x_test.iloc[i].to_dict()

            true_label = y_test.iloc[i]
            pred = self.n.predictor(simple)

            if pred == true_label:
                correct += 1


            pred = str(pred).strip().lower()
            true_label = str(true_label).strip().lower()
            print(f"true: {true_label} | predicted: {pred}")

            if pred == 'yes' and true_label == 'yes':
                TP += 1
            elif pred == 'yes' and true_label == 'no':
                FP += 1
            elif pred== 'no' and true_label =='no':
                TN += 1
            elif pred== 'no' and true_label == 'yes':
                FN += 1

        accuracy = correct / total
        print(f"Final Accuracy: {accuracy:.2f}")
        return accuracy
        print(f"TP = {TP}, FP = {FP}, TN = {TN}, FN = {FN}")







