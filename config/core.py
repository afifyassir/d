from pathlib import Path

from typing import Optional, Sequence

from config_classes import AppConfig, ModelConfig, Config

from pydantic import BaseModel
from strictyaml import YAML, load

import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(FILE_PATH)
CONFIG_FILE_PATH = os.path.join(PARENT_DIR, "config.yml")
DATASET_DIR = os.path.join(PARENT_DIR, "datasets")
TRAINED_MODEL_DIR = os.path.join(PARENT_DIR, "trained_models")


def yaml_config_file_location() -> str:
    """Find the location of the configuration file.
       Return the location if found, otherwise raise an exception."""

    try:
        assert os.path.isfile(CONFIG_FILE_PATH)
        return CONFIG_FILE_PATH
    except AssertionError:
        raise Exception(f"The config file does not exist at {CONFIG_FILE_PATH!r}")



def fetching_yaml_file(file_path: Optional[str] = None) -> YAML:
    """Parse YAML containing the package configuration."""

    try:
        if not file_path:
            file_path = yaml_config_file_location()

        with open(file_path, "r") as yml_file:
            parsed_config = load(yml_file.read())
            return parsed_config
    except FileNotFoundError:
        raise OSError(f"YAML file not found")




def validate_config(parsed_config: YAML = None) -> Config:
    """Validate values of our configuration."""
    parsed_config = parsed_config or fetching_yaml_file()

    # Validate the app_config and model_config separately.
    app_config = AppConfig(**parsed_config.data)

    model_config = ModelConfig(**parsed_config.data)

    # Combine the validated app_config and model_config into a single Config object.
    config = Config(app_config=app_config, model_config=model_config)

    return config


config = validate_config()
print(FILE_PATH)
print(PARENT_DIR)
print(config)
