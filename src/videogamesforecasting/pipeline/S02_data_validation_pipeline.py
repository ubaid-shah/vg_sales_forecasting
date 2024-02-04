from videogamesforecasting.config.configuration import ConfigurationManager
from videogamesforecasting.components.data_validation import DataValidation
from videogamesforecasting.logging import logger

STAGE_NAME = "Data validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        config.data_validation_config()
        validate=DataValidation()
        validate.validate_all_columns()


if __name__=='__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")

        obj=DataValidationPipeline()
        obj.main()

        logger.info(f">>>>>> {STAGE_NAME} completed")

    except Exception as e:
        logger.exception(e)
        raise e