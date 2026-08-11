"""
The "after" version — YOUR file to complete.

Fill in the three functions marked with # TODO. Everything else (CLI wiring,
imports) is already done for you. Do not hardcode any path, format string, or
threshold value anywhere in this file — if you find yourself typing a literal
number or file path outside of a default/example, it belongs in the config
file instead.

Run with:
    python src/pipeline.py --config config/pipeline.yaml
"""
import argparse
import csv
import json
from pathlib import Path
import yaml

REQUIRED_KEYS = ["input_path", "input_format", "high_value_threshold", "output_path"]


def load_config(path):
    """Load a YAML config file and validate required keys are present.

    Must raise ValueError naming the specific missing key if REQUIRED_KEYS
    are not all present. Do not let this fail with a bare KeyError later.
    """
    # implemented
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
        raise ValueError("The following keys are missing in the config {missed}")


def load_transactions(path, fmt):
    """Load transactions from `path`, using `fmt` ("csv" or "json") to decide
    how to parse it — not by sniffing the file extension.

    Must return a list of dicts. Every dict must have at least "amount"
    (str or float) and "is_fraud" (str "True"/"False" or bool).
    Raise ValueError for any fmt other than "csv" or "json".
    """
    if fmt not in ['csv','json']:
        raise ValueError(f"{fmt} is not compatable")

    if fmt!=Path(path).suffix[1:]:
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




def run_pipeline(config):
    """Load data per `config`, compute the same summary fields as
    pipeline_hardcoded.py (n_transactions, total_amount, fraud_rate,
    n_high_value, high_value_threshold), and write them as JSON to
    config["output_path"]. Return the report dict as well.
    """
    # TODO: implement
    raise NotImplementedError("run_pipeline is not implemented yet")


def main():
    parser = argparse.ArgumentParser(description="Config-driven fraud transaction summary pipeline")
    parser.add_argument("--config", required=True, help="Path to a YAML config file")
    args = parser.parse_args()

    config = load_config(args.config)
    report = run_pipeline(config)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
