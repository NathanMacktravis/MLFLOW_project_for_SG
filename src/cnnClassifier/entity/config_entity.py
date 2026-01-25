# création de la classe d'ingestion des données 
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # "frozen" permet de rendre l'objet de la classe immuable après sa création
class DataIngestionConfig:
    """Classe de l'ingestion des données"""
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path