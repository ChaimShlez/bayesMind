from extract_data.extractData import ExtractData
from cleanData.splitData import SplitData
from trainer.naiveBayesTrainer import NaiveBayesTrainer
from predictor.naiveBayesPredictor import NaiveBayesPredictor
from trainer.evaluator import Evaluator
class Manager:
    def __init__(self):
        extractor=ExtractData()
        self.data=extractor.read_data()

        splitData=SplitData(self.data)
        self.train_df, self.label,self.y_test= splitData.extract_train_test_split()

        trainer_modal = NaiveBayesTrainer(self.train_df, self.label)
        trainer_modal.extract_ratios_with_pandas()

        evaluator=Evaluator(self.label,self.y_test)
        evaluator.Evolution_train(trainer_modal)
