from extract_data.extractData import ExtractData
from cleanAndSplitData.splitData import SplitData
from trainer.naiveBayesTrainer import NaiveBayesTrainer
from predictor.naiveBayesPredictor import NaiveBayesPredictor
from trainer.evaluator import Evaluator
class Manager:
    def __init__(self):
        extractor=ExtractData()
        self.data=extractor.read_data()

        splitData=SplitData(self.data)
        self.label=splitData.extract_label()
        self.df_data, self.x_test, self.y_test = splitData.split_from_test_modal()

        trainer_modal = NaiveBayesTrainer(self.df_data, self.label)
        modal=trainer_modal.extract_ratios_with_pandas()
        print(f"misal:{modal}")

        evaluator=Evaluator(self.label ,modal)
        evaluator.Evolution_train(self.x_test, self.y_test)

        predictor= NaiveBayesPredictor(self.label,modal)

        sample = {
            "age": "youth",
            "income": "medium",
            "student": "yes",
            "credit_rating": "fair",
            "job": "part_time",
            "married": "no",
            "Buy_Computer": "yes"
        }

        result = predictor.predictor(sample)
        print("Prediction result:", result)


