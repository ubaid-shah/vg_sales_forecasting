from videogamesforecasting.config.configuration import ConfigurationManager
from videogamesforecasting.components.data_ingestion import DataIngestion
from videogamesforecasting.logging import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager=ConfigurationManager()
        config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion()
        data_ingestion.run_ingestion()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e