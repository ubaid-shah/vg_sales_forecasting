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