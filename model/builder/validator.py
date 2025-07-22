import pandas as pd
from classifier.naiveBayesClassifier import NaiveBayesClassifier


class Validator:
    def __init__(self,label,modal):
        self.modal = modal
        self.label = pd.Series(label)

    def Validator_train(self, x_test, y_test):
        correct = 0
        total = len(y_test)
        for i in range(total):
            simplePred = x_test.iloc[i].to_dict()

            true_label = y_test.iloc[i]
            pred = self.ValidatorPred(simplePred)

            if pred == true_label:
                correct += 1

        accuracy = correct / total
        print(f"Final Accuracy: {accuracy:.2f}")



    def ValidatorPred(self,dataPred):

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








