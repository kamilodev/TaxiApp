import json

CONFIG_FILE = ".config"


def create_config_file():
    config = {"users": [], "prices": [{"stop": 0.2, "move": 0.5}]}
    save_config(config)


def load_config() -> dict:
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        create_config_file()
        return load_config()


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
