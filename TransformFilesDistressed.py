import logging
from JsonManager import JsonManager
import os
import subprocess
import argparse
import sys
import json

sys.dont_write_bytecode = True

level = logging.DEBUG
format_log = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=format_log)


def main(file, ratio):
    try:
        execution_id = ""

        with open(file, mode="r") as f:
            json_file = json.load(f)

        if ratio in json_file["RATIO"].keys():
            logging.info("Ratio encontrado")
            execution_id = json_file["RATIO"][ratio][-1]         
        else:
            logging.info("ERROR: Ratio não encontrado")
            sys.exit(1)
        logging.info(execution_id)
    except Exception as error:
        logging.info(error)


if __name__== "__main__":
    file = "ExecutionsID.json"
    ratio = "202211"

    main(file, ratio)