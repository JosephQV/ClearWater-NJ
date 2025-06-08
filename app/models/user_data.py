import json
import pathlib
import logging
import datetime
import time
import requests

from data.app_config import USER_WATER_TEST_RESULTS_PATH


logger = logging.getLogger(__name__)

BASE_URL = "https://clearwater-nj-api.fly.dev"
LOGIN_URL = f"{BASE_URL}/token"
REGISTER_URL = f"{BASE_URL}/register"

USER_DATA_DEFAULT = {
    "id": "",
    "username": "",
    "full_name": "",
    "email": "",
    "county": "",
    "municipality": "",
    "water_system": "",
    "private_well": False,
    "preferred_language": "en",
    "account_created": datetime.datetime.now(),
    "num_water_tests": 0
}


class UserController:
    def __init__(self):
        self.user_data = USER_DATA_DEFAULT
        self.auth_token = None

    # Register a new user in the remote server database
    def register_new_user(
            self,
            username: str, 
            password: str,
            full_name: str,
            email: str, 
            county: str, 
            municipality: str, 
            water_system: str, 
            private_well: bool,
            preferred_language: str = "en"
        ):
        # TODO: Make a POST request to the REGISTER_URL (above) with a user data dictionary
        # in the body of the request. The dictionary should contain the fields shown above in
        # USER_DATA_DEFAULT, along with a password. These values can be taken from the arguments
        # given to this function.
        pass

    # Login using a given username and password
    def get_login_token(self, username: str, password: str):
        # TODO: Make a POST request to the LOGIN_URL (above) with the username and password
        # included in the body of the request.
        # Retrieve the authentication token from the body of the response.
        # Save this token to self.auth_token to be used in other methods.
        pass

    # Get current user record from the server
    def get_user_from_server(self) -> dict:
        if self.auth_token is not None:
            try:
                # endpoint to get current user
                url = f"{BASE_URL}/users/me"
                headers = {"Authorization": f"Bearer {self.auth_token}"}
                response = requests.get(url, headers=headers)
                return response.json()
            except Exception as e:
                logger.error(f"Failed to get current user from server: {str(e)}")
                return USER_DATA_DEFAULT
        else:
            logger.error("Must login and acquire authentication token before retrieving from server.")
            return USER_DATA_DEFAULT
    
    # Update this UserController object to be in sync (matching data) with what's on the remote server
    def sync_user_data_from_remote(self):
        self.user_data = self.get_user_from_server()

    # Update any part of the user_data given the passed dictionary (which will have some of 
    # the keys from USER_DATA_DEFAULT with new, updated values)
    def set_user_data(self, updated_user: dict):
        # TODO: Make a PATCH request to the /users/update API endpoint with the dict
        # passed to this function to update the user record on the server.
        # If the request is successful (check response), set self.user_data to the
        # updated_user.
        pass

    def get_language(self):
        return self.user_data.get("preferred_language", "en")

    def set_language(self, language_setting):
        lang_map = {
            "English": "en",
            "Español": "es"
        }
        self.user_data["preferred_language"] = lang_map[language_setting]
        self.set_user_data(self.user_data)

    # Add some metadata to the beginning of inputted test data before saving
    def prepend_metadata_to_water_test(self, test_data: dict, test_id: str):
        now = datetime.datetime.now()
        test = {
            "date": str(now.date()),
            "time": str(now.strftime("%H:%M")),
            "timestamp": now.isoformat(timespec="seconds").replace(":", "-"),
            "number_parameters_tested": len(test_data),
            "test_id": test_id,
            "test_results": test_data
        }
        return test
    
    # Save test data to a local JSON file with the timestamp and test_id in the file name
    def save_water_test_locally(self, json_test_data: dict):
        timestamp = json_test_data.get("timestamp", "")
        test_id = json_test_data.get("test_id", "")
        # E.g., 2025-06-08T15-16-25_B07WNJJVKN_test.json
        file_path = f"{USER_WATER_TEST_RESULTS_PATH}/{timestamp}_{test_id}_test.json"
        with open(file_path, "w+") as f:
            json.dump(json_test_data, f, indent=4)

    def upload_water_test(self):
        # TODO: Upload the latest submitted water test to the server.
        # Each water test is first saved locally to a JSON file and so this
        # is what will be uploaded (the actual file).
        # The file names are prepended with the timestamp of when they were
        # created, so the file names in the directory USER_WATER_TEST_RESULTS_PATH
        # can be sorted to find the most recent file. Then, this is the file that 
        # should be uploaded to the API endpoint /files/water_test/upload
        pass

    def retrieve_water_tests_from_server(self):
        # TODO: For situations where the remote server is not synced with the local
        # storage (for example, user is on a new device), we can retrieve previously
        # saved data from the remote. Complete this function to make a request to the 
        # API endpoint /files/water_test/all. This will retrieve the JSON content
        # of all submitted water tests from server storage for this user. 
        # The body of the response will be a list of JSON objects, representing the list
        # of saved tests where each test is a JSON object (a dictionary). 
        # Each retrieved water test should be saved to a JSON file locally using the above method
        # self.save_water_test_locally() on each item in the list.
        pass

    def get_all_saved_water_tests(self) -> list[dict] | None:
        # TODO: Read every JSON file in the local directory USER_WATER_TEST_RESULTS_PATH
        # and append the JSON content of each file to a list. Return this list. If
        # there are no saved test files in the directory, return None.
        pass