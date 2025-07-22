import json

from model.dataLoader.dataLoaderCSV import DataLoaderCSV
from model.cleaner.splitData import SplitData
from model.builder.naiveBayesBuilder import NaiveBayesBuilder
from classifier.naiveBayesClassifier import NaiveBayesClassifier
from model.builder.validator import Validator
from model.logHandler.logConfig import LogConfig

class Manager:
    def __init__(self):
        self.logger = LogConfig.get_logger("manager")
        self.extractor = DataLoaderCSV()
        self.splitter = None
        self.trainer = None
        self.evaluator = None
        self.predictor = None

    def run(self):
        self.logger.info("Manager started running")

        data = self.extractor.read_data()
        self.logger.info(f"Data loaded with {len(data)} rows")

        self.splitter = SplitData(data)
        label = self.splitter.extract_label()
        df_data, x_test, y_test = self.splitter.split_from_test_modal()
        self.logger.info("Data split into training and test sets")

        self.trainer = NaiveBayesBuilder(df_data, label)
        modal_naive = self.trainer.extract_ratios_with_pandas()

        path_model = "data_model/model.json"
        with open(path_model, "w") as f:
            json.dump(modal_naive, f)

        path_label = "data_model/label.json"
        with open(path_label, "w") as f:
            json.dump(label, f)

        self.logger.info(f"Model extracted: { modal_naive}")

        path_model = "data_model/model.json"
        path_label = "data_model/label.json"
        with open(path_model, "r") as f:
            model_dict = json.load(f)

        with open(path_label, "r") as f:
            label_dict = json.load(f)

        self.evaluator = Validator(label_dict,  model_dict)
        self.evaluator.Validator_train(x_test, y_test)
        self.logger.info("Model evaluation completed")

        # self.predictor = NaiveBayesClassifier(label, model)
        #
        # sample = {
        #     "age": "youth",
        #     "income": "medium",
        #     "student": "yes",
        #     "credit_rating": "fair",
        #     "job": "part_time",
        #     "married": "no",
        #     "Buy_Computer": "yes"
        # }
        #
        # result = self.predictor.predictor(sample)
        # self.logger.info(f"Prediction result: {result}")
        # print("Prediction result:", result)


if __name__ == "__main__":
    manager = Manager()
    manager.run()
