import json
import sys
import logging
sys.dont_write_bytecode = True
from os.path import exists, dirname, realpath, isfile

level = logging.DEBUG
format_log = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=format_log)


class JsonManager:
    def __init__(self, file, execution_id, ratio):
        self.file = file
        self.execution_id = execution_id
        self.ratio = ratio


    def json_exists(self):
        validation = exists(self.file)
        return validation


    def create_json_file(self):
        data = {
                "RATIO":{
                    self.ratio:[self.execution_id]
                }
            }

        with open(self.file, 'w') as file:  
            json.dump(data, file)


    def managing_json_file(self):
        try:
            if self.json_exists():
                logging.info('FILE ALREADY EXISTS')
            
                with open(self.file, mode="r") as file:
                    json_file = json.load(file)

                    if self.ratio in json_file["RATIO"].keys():
                        logging.info("RATIO ALREADY EXISTS IN JSON, ADDING AN EXECUTION ID TO FILE")
                        json_file["RATIO"][self.ratio].append(self.execution_id)
                    else:
                        logging.info("RATIO DOES NOT EXISTS IN JSON, ADDING A RATIO AND EXECUTION ID TO FILE")
                        json_file["RATIO"][self.ratio] = [self.execution_id]

                    with open (self.file, 'w') as f:
                        json.dump(json_file, f, indent=2, sort_keys=False)

            else:
                logging.info("First Execution")
                self.create_json_file()
        except Exception as error:
            print(error)
