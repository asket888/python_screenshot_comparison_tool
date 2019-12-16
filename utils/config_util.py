import json


def get_env(env: str):
    if env.upper() == "USA":
        return _read_config("config.json", "USA")
    elif env.upper() == "LAT":
        return _read_config("config.json", "LAT")
    elif env.upper() == "RUS":
        return _read_config("config.json", "RUS")
    else:
        raise TypeError("Unexpected Env. Check your config.json file variables")


def _read_config(file, tag):
    with open(file) as json_file:
        as_dict = json.load(json_file)[tag]
        return as_dict
