import logging
from JsonManager import JsonManager
import os
import subprocess
import argparse
import sys
import datetime

sys.dont_write_bytecode = True

level = logging.DEBUG
format_log = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=format_log)


def main(file,ratio,execution_id):
    try:
        json_obj = JsonManager(file, execution_id, ratio)
        print(datetime.datetime.now().strftime("YYYYMMDD HH:mm:ss (%Y-%m-%d %H:%M:%S)"))
        managing_files =  json_obj.managing_json_file()
    except Exception as error:
        logging.info(error)

if __name__=="__main__":
    file = "ExecutionsID.json"
    ratio = "202104"
    execution_id = "9"

    main(file, ratio, execution_id)