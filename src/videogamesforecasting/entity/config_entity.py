from dataclasses import dataclass
from pathlib import Path
import ipaddress

@dataclass(frozen=True)
class DataIngestionConfig:
    s_type: str
    host: ipaddress.IPv4Address
    port: int
    database: str
    username: str
    password: str
    query: str
    d_type: str
    path: Path
    include_column_names: str

@dataclass(frozen=True)
class DataValidationConfig:
    dir: Path
    data_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    dir: Path
    data_dir: Path