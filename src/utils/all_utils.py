import yaml
import os
import json
import logging



def read_yaml(path_to_yaml: str)->dict:
    with open(path_to_yaml, "r") as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"read yaml file from {path_to_yaml}")

    return content

def create_directory(dirs: list):
    for dir in dirs:
        os.makedirs(dir,exist_ok =True)
        logging.info(f"created directory {dir}")

def save_local_df(data,data_path, index = False, sep = ","):
    data.to_csv(data_path,index =index,sep=sep)
    logging.info(f"data frame saved at {data_path}")


def store_reports(report: dict, report_path: str, indent=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indent)
    logging.info(f"report saved at {report_path} ")