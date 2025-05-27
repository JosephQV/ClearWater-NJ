import json
import pathlib
import logging
import datetime
import time

from data.app_config import USER_DATA_FILE


logger = logging.getLogger(__name__)


USER_DATA_TEMPLATE = {
    "username": "",
    "email": "",
    "municipality": "",
    "county": "",
    "water_system": "",
    "water_tests": [],
    "preferred_language": "en"
}


def create_user_data_file():
    try:
        user_data_file = pathlib.Path(USER_DATA_FILE)
        if not user_data_file.exists():
            with open(user_data_file, "x") as f:
                json.dump(USER_DATA_TEMPLATE, f)
        else:
            logger.info("User data file already exists. Did not overwrite.")
    except Exception as e:
        logger.error(f"Failed to create {USER_DATA_FILE}: {str(e)}")


def get_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        logger.error(f"Failed to read {USER_DATA_FILE}: {str(e)}")
        return USER_DATA_TEMPLATE


def write_user_data(user_data):
    try:
        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file)
    except Exception as e:
        logger.error(f"Failed to write {USER_DATA_FILE}: {str(e)}")
        

def get_language():
    try:
        return get_user_data()["preferred_language"]
    except Exception as e:
        logger.error(f"Failed to get language: {str(e)}")
        return "en"


def set_language(language_setting):
    lang_map = {
        "English": "en",
        "Español": "es"
    }
    user_data = get_user_data()
    user_data["preferred_language"] = lang_map[language_setting]
    write_user_data(user_data)
    

def add_water_test(test_data: dict, test_id: str):
    test = {
        "date": str(datetime.date.today()),
        "time": str(datetime.datetime.now().strftime("%H:%M")),
        "number_parameters_tested": len(test_data),
        "test_id": test_id,
        "test_results": test_data
    }
    user_data = get_user_data()
    user_data["water_tests"].append(test)
    write_user_data(user_data)