import json
import os


def read_json(path):
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)