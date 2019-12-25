import os

import yaml


class GetData:
    def get_datas(self, yaml_file):
        with open("./Data" + os.sep + yaml_file, 'r', encoding="utf-8") as f:
            return yaml.safe_load(f)
