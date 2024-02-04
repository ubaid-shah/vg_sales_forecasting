import os
from videogamesforecasting.constants import *
from videogamesforecasting.utils.common import read_yaml, create_directories
from videogamesforecasting.entity.config_entity import *
class ConfigurationManager:
    def __init__(
        self,
        # from constants
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        (create_directories([self.config.artifacts_root]))

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([os.path.split(config.destination.path)[0]])

        data_ingestion_config = DataIngestionConfig(
            s_type= config.source.type,
            host= config.source.host,
            port= config.source.port,
            database= config.source.database,
            username= config.source.username,
            password= config.source.password,
            query= config.source.query,
            d_type=config.destination.type,
            path= config.destination.path,
            include_column_names= config.destination.include_column_names
        )

        return data_ingestion_config
    

    def data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([os.path.split(config.STATUS_FILE)[0]])

        get_data_validation_config = DataValidationConfig(
            dir=config.dir,
            data_dir=config.data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return get_data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.dir])

        data_transformation_config = DataTransformationConfig(
            dir=config.dir,
            data_dir=config.data_dir
        )

        return data_transformation_config