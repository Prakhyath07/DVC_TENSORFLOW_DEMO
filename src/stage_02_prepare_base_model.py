from src.utils.all_utils import read_yaml
import argparse
import pandas as pd
import os
from src.utils.all_utils import create_directory
from src.utils.models import get_VGG16_model, prepare_model
import shutil
from tqdm import tqdm
import logging
import tensorflow as tf


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)
logger = logging.basicConfig(filename=os.path.join(log_dir, "running-logs.log"),
level=logging.INFO,format=logging_str, filemode="a")



def prepare_base_model(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    
    artifacts = config["artifacts"]

    artifacts_dir = artifacts["ARTIFACTS_DIR"]
    base_model_dir = artifacts["BASE_MODEL_DIR"]
    base_model_name = artifacts["BASE_MODEL_NAME"]

    base_model_dir_path = os.path.join(artifacts_dir,base_model_dir)
    create_directory([base_model_path])

    base_model_path = os.path.join(base_model_dir_path,base_model_name)

    base_model = get_VGG16_model(input_shape=params["IMAGE_SIZE"],model_path=base_model_path)

    model =prepare_model(
        model,
        classes=params["CLASSES"],
        freeze_all = True,
        freeze_till =None,
        learning_rate = params["LEARNING_RATE"]
    )

    logging.info(f"model summayr {model.summary()}")

    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")


    parsed_args = args.parse_args()
    try:
        prepare_base_model(config_path= parsed_args.config,params_path= parsed_args.params)
        logging.info(">>>>>>>>>stage two completed<<<<<<<<<")
    except Exception as e:
        logging.exception(e)