import os
import pandas as pd 
from videogamesforecasting.logging import logger
import yaml
from sqlalchemy import create_engine

class DataIngestion:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as config_file:
            self.config = yaml.safe_load(config_file)["data_ingestion"]

        self.source_config = self.config["source"]
        self.destination_config = self.config["destination"]

    def connect_to_mysql(self):
        engine = create_engine(
            f"mysql+pymysql://{self.source_config['username']}:{self.source_config['password']}@{self.source_config['host']}:{self.source_config['port']}/{self.source_config['database']}"
        )
        return engine.connect()

    def fetch_data_from_mysql(self):
        connection = self.connect_to_mysql()
        query = self.source_config["query"]
        data = pd.read_sql(query, connection)
        connection.close()
        return data

    def save_to_csv(self, data):
        path = self.destination_config["path"]
        include_column_names = self.destination_config.get("include_column_names", False)

        data.to_csv(path, index=False, header=include_column_names)

    def run_ingestion(self):
        data = self.fetch_data_from_mysql()
        self.save_to_csv(data)
        path = self.destination_config["path"]
        file=os.path.split(path)[1]

        logger.info(f"{file} is saved")