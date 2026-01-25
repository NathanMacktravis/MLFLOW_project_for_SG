import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib
# from ensure import ensure_annotations # Ne fonctionne plus sur python 3.12
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


# NB1: le @ensure_annotation est un décorateur qui va s'assurer que : 
# - Les arguments passés à la fonction respectent les types annotés
# - La valeur de retour correspond aussi au type annoncé

# @ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """This function reads a YAML file from the specified path and returns its contents as a ConfigBox.

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

# NB2: ConfigBox sert à transformer un dictionnaire Python (ou un YAML/JSON chargé) en un objet :
# - immuable ou quasi-immuable
# - accessible via la notation pointée (config.model.lr)
# - avec des erreurs claires si une clé n’existe pas
# Ex : Si on a un dico d = {'key1' : 'val1', 'key2' : 'val2'}, on ne peut y accéder aux valeurs avec d['key1']
# Or si on le transforme en d2 = ConfigBox({'key1' : 'val1', 'key2' : 'val2'}), on peut accéder avec d2.key1  



# @ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args: 
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



# @ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




# @ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)



# @ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")



# @ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



# @ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"



def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()



def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
