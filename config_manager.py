import json

CONFIG_FILE = ".config"


def create_config_file():
    """
    This function creates a configuration file with an empty list of users and a list of prices.
    """
    config = {"users": [], "prices": [{"stop": 0.2, "move": 0.5}]}
    save_config(config)


def load_config() -> dict:
    """
    This function loads a configuration file and returns its contents as a dictionary, creating the file
    if it doesn't exist.
    :return: The function `load_config()` returns a dictionary object that is loaded from a JSON file
    specified by the `CONFIG_FILE` constant. If the file is not found, the function calls
    `create_config_file()` to create a new configuration file and then recursively calls `load_config()`
    to load the newly created file.
    """
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        create_config_file()
        return load_config()


def save_config(config):
    """
    This function saves a configuration object to a file in JSON format with indentation.

    :param config: The `config` parameter is a dictionary object that contains configuration settings or
    parameters that need to be saved to a file. The function `save_config` takes this dictionary object
    and writes it to a file in JSON format with indentation for readability. The name of the file is
    specified by the `CONFIG_FILE
    """
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
