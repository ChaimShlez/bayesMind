from fastapi import FastAPI
from dataLoader.dataLoaderCSV import DataLoaderCSV

from cleaner.splitData import SplitData
from builder.naiveBayesBuilder import NaiveBayesBuilder
from builder.validator import Validator
from logHandler.logConfig import LogConfig

app = FastAPI()

@app.get("/model")
def build_and_return_model():
    logger = LogConfig.get_logger("manager")
    logger.info("Building model now")

    extractor = DataLoaderCSV()
    data = extractor.read_data()

    splitter = SplitData(data)
    label = splitter.extract_label()
    df_data, x_test, y_test = splitter.split_from_test_modal()

    trainer = NaiveBayesBuilder(df_data, label)
    modal_naive = trainer.extract_ratios_with_pandas()

    validator = Validator(label, modal_naive)
    validator.Validator_train(x_test, y_test)

    logger.info("Returning built model and label")
    return {"model": modal_naive, "label": label}
