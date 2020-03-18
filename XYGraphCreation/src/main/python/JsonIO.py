

import json

class JsonIO:
    
    @staticmethod
    def read(jsonFilePath):
        with open(jsonFilePath) as jsonFile:
            return json.load(jsonFile)