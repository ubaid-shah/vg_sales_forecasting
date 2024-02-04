from videogamesforecasting.logging import logger
import pandas as pd
import yaml

class DataValidation:
    def __init__(self, config_path="config/config.yaml",schema_filepath="schema.yaml"):
        with open(config_path, "r") as config_file:
            self.config = yaml.safe_load(config_file)["data_validation"]
        with open(schema_filepath,"r") as schema_file:
            self.schema=yaml.safe_load(schema_file)["COLUMNS"]

        self.source_config = self.config
        self.schema_config=self.schema.keys()

       
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.source_config['data_dir'])
            all_cols = list(data.columns)

            all_schema = self.schema_config

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.source_config['STATUS_FILE'], 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                    logger.info(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.source_config['STATUS_FILE'], 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                    logger.info(f"Validation Status: {validation_status}")

            return validation_status
        
        
        except Exception as e:
            raise e