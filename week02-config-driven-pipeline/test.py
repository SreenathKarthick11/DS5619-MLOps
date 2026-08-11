import yaml
import csv
import json
import pprint
from pathlib import Path
REQUIRED_KEYS = ["input_path", "input_format", "high_value_threshold", "output_path"]


def load_config(path):
    """Load a YAML config file and validate required keys are present.

    Must raise ValueError naming the specific missing key if REQUIRED_KEYS
    are not all present. Do not let this fail with a bare KeyError later.
    """
    try:
        with open(path,'r') as file:
            data=yaml.load(file,Loader=yaml.SafeLoader)
    except Exception as e:
        print(f"Error occured while loading config : {e}")
        exit(1)
    
    missed=[]
    for key in REQUIRED_KEYS:
        if key not in data.keys():
            missed.append(key)

    if (missed!=[]):
        raise ValueError(f"The following keys are missing in the config {missed}")
    


def load_transactions(path, fmt):
    """Load transactions from `path`, using `fmt` ("csv" or "json") to decide
    how to parse it — not by sniffing the file extension.

    Must return a list of dicts. Every dict must have at least "amount"
    (str or float) and "is_fraud" (str "True"/"False" or bool).
    Raise ValueError for any fmt other than "csv" or "json".
    """
    if fmt not in ['csv','json']:
        raise ValueError(f"{fmt} is not compatable")
    
    if ('.'+fmt)!=Path(path).suffix:
        raise Exception(f"The format doesn't match for the file")

    if fmt == 'csv':
        try:
            with open(path,'r',newline="") as f:
                data = csv.DictReader(f)
                return list(data)
        except Exception as e:
            print(f"Error while loading csv , `check file path` : {e}")
            exit(1)
    else:
        try:
            with open(path,'r') as f:
                data = json.load(f)
                return data
        except Exception as e:
            print(f"Error while loading json , `check file path` : {e}")
            exit(1)

    raise NotImplementedError("load_transactions is not implemented yet")

# load_config('/home2/mlops/Documents/Labs/week02-config-driven-pipeline/config/pipeline.example.yaml')
print(load_transactions("/home2/mlops/Documents/Labs/week02-config-driven-pipeline/data/v1/transactions.json","csv"))