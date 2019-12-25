import yaml

data = {"data": {"name": "张鹏博", "age": 18}}

with open('./Data/xx.yaml', "a", encoding="utf-8") as f:
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
