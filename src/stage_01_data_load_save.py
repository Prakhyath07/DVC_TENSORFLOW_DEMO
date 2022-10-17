from src.utils.all_utils import read_yaml
import argparse
import pandas as pd
import os
from src.utils.all_utils import create_directory
import shutil
from tqdm import tqdm
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)
logger = logging.basicConfig(filename=os.path.join(log_dir, "running-logs.log"),
level=logging.INFO,format=logging_str, filemode="a")

def copy_file(source,destination):
    list_of_files = os.listdir(source)
    N= len(list_of_files)
    for file in tqdm(list_of_files,total=N, desc = f"copying files from {source} to {destination}", colour="green"):
        src = os.path.join(source,file)
        dest = os.path.join(destination,file)
        shutil.copy(src,dest)
    logging.info(f"files copied from {source} to {destination}")

def get_data(config_path):
    config = read_yaml(config_path)
    source_download_dirs = config["source_download_paths"]
    local_data_dirs = config["local_data_dirs"]

    for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs,local_data_dirs),total=2, desc = "list of files", colour="red"):
        create_directory([local_data_dir])
        copy_file(source_download_dir, local_data_dir)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_args = args.parse_args()
    try:
        get_data(config_path= parsed_args.config)
        logging.info(">>>>>>>>>stage one completed<<<<<<<<<")
    except Exception as e:
        logging.exception(e)