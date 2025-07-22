from dataLoader.dataLoaderCSV import DataLoaderCSV
from cleaner.splitData import SplitData
from builder.naiveBayesBuilder import NaiveBayesBuilder
from classifier.naiveBayesClassifier import NaiveBayesClassifier
from builder.validator import Validator
from logHandler.logConfig import LogConfig

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
        model = self.trainer.extract_ratios_with_pandas()
        self.logger.info(f"Model extracted: {model}")

        self.evaluator = Validator(label, model)
        self.evaluator.Validator_train(x_test, y_test)
        self.logger.info("Model evaluation completed")

        self.predictor = NaiveBayesClassifier(label, model)

        sample = {
            "age": "youth",
            "income": "medium",
            "student": "yes",
            "credit_rating": "fair",
            "job": "part_time",
            "married": "no",
            "Buy_Computer": "yes"
        }

        result = self.predictor.predictor(sample)
        self.logger.info(f"Prediction result: {result}")
        print("Prediction result:", result)


if __name__ == "__main__":
    manager = Manager()
    manager.run()
