from dataLoader.dataLoaderCSV import DataLoaderCSV
from cleaner.splitData import SplitData
from builder.naiveBayesBuilder import NaiveBayesBuilder
from builder.validator import Validator
from logHandler.logConfig import LogConfig

class Manager:
    def __init__(self):
        self.logger = LogConfig.get_logger("manager")
        self.validator=None

    def run(self):
        self.logger.info("Building model now")

        extractor = DataLoaderCSV()
        data = extractor.read_data()

        splitter = SplitData(data)
        label = splitter.extract_label()
        df_data, x_test, y_test = splitter.split_from_test_modal()

        trainer = NaiveBayesBuilder(df_data, label)
        modal_naive = trainer.extract_ratios_with_pandas()

        self.validator = Validator(label, modal_naive)
        self.validator.Validator_train(x_test, y_test)

        self.logger.info("Returning built model and label")
        return modal_naive, label
