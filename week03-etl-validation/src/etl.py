"""
Extract -> Validate -> Transform -> Load pipeline for the fraud transaction
data. Run with:

    python src/etl.py --config config.yaml

(a default config.yaml pointing at data/raw_transactions.csv is provided)
"""
import argparse
import csv
import json
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expectations as exp

KNOWN_CATEGORIES = {
    "grocery", "electronics", "fuel", "travel", "restaurant",
    "online_retail", "utilities", "pharmacy", "entertainment", "atm_withdrawal",
}


def build_expectation_suite():
    """The data contract for this dataset. Each entry says which expectation
    function to run, and with what arguments. This is provided — read it to
    know exactly what your expectation functions in expectations.py need to
    handle correctly.
    """
    return [
        (exp.expect_column_not_null, {"column": "amount"}),
        (exp.expect_column_not_null, {"column": "card_id"}),
        (exp.expect_column_positive, {"column": "amount"}),
        (exp.expect_column_in_set, {"column": "merchant_category", "allowed_values": KNOWN_CATEGORIES}),
        (exp.expect_column_unique, {"column": "transaction_id"}),
    ]


def extract(input_path):
    with open(input_path, newline="") as f:
        return list(csv.DictReader(f))


def write_csv(output,rows):
    if not rows:
        return ValueError("No rows to write")
    fieldnames=list(rows[0].keys())
    with open(output,mode='w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader() 
        writer.writerows(rows)

def report_gen(vio_objs):
    Total_violations=len(vio_objs)
    violation={"expect_column_not_null":0,"expect_column_positive":0,"expect_column_in_set":0,"expect_column_unique":0}
    violation_ids={"expect_column_not_null":[],"expect_column_positive":[],"expect_column_in_set":[],"expect_column_unique":[]}
    for v in vio_objs:
        violation[v.expectation]+=1
        violation_ids[v.expectation].append(v.row_index)
    
    return {
        "n_violations" : Total_violations,
        "Expected column not null" : f"count: {violation['expect_column_not_null']} , row_indexs {violation_ids['expect_column_not_null']}",
        "Expected column positive" : f"count: {violation['expect_column_positive']} , row_indexs {violation_ids['expect_column_positive']}",
        "Expected column in set"   : f"count: {violation['expect_column_in_set']} , row_indexs {violation_ids['expect_column_in_set']}",
        "Expected column unique"   : f"count: {violation['expect_column_unique']} , row_indexs {violation_ids['expect_column_unique']}",
    }
    

def run_etl(config):
    """Implement the four ETL steps described in ASSIGNMENT.md:
    extract, validate (run every expectation in build_expectation_suite()
    and collect ALL violations, not just the first), transform (split into
    clean vs quarantined rows — a row with ANY violation is quarantined),
    load (write clean_output_path, quarantine_output_path, and
    report_output_path as described in the assignment).

    Return the validation_report dict as well as writing it to disk.
    """
    # VERIFY: implement
    rows = extract(config["input_path"])
    exp_suite=build_expectation_suite()
    vio_objs=[]
    for fn, args in exp_suite:
        vio_objs.extend(fn(rows,**args))
    
    violated_indexs=set()
    for v in vio_objs:
        violated_indexs.add(v.row_index)


    violated_rows=[]
    clean_rows=[]
    for i in range(len(rows)):
        if str(i) not in violated_indexs:
            clean_rows.append(rows[i])
        else:
            violated_rows.append(rows[i])

    write_csv(config["clean_output_path"],clean_rows)
    write_csv(config["quarantine_output_path"],violated_rows)

    report = report_gen(vio_objs)

    with open(config['report_output_path'], "w") as f:
            json.dump(report, f, indent=2)
            
    return report



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    report = run_etl(config)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
