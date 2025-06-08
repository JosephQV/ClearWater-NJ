import requests
import json
import datetime
import os

BASE_URL = "https://clearwater-nj-api.fly.dev/"

USER_EXAMPLE = {
    "username": "testuser1234",
    "password": "safe_password",
    "full_name": "Albert Einstein",
    "email": "einstein@example.com",
    "county": "Union",
    "municipality": "Elizabeth",
    "water_system": "NJ American Water - Raritan",
    "private_well": False,
    "preferred_language": "en"
}
JSON_FILE_PATH = "sample_water_test.json"

# Step 1: Register a new user
def register_user():
    url = f"{BASE_URL}/register"
    payload = USER_EXAMPLE
    response = requests.post(url, json=payload)
    print("Register response:", response.status_code, response.json())

# Step 2: Log in and get the access token
def login():
    url = f"{BASE_URL}/token"
    data = {
        "username": USER_EXAMPLE["username"],
        "password": USER_EXAMPLE["password"]
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    token = response.json()["access_token"]
    print("Access Token:", token)
    return token

# Step 3: Get current user info
def get_me(token):
    url = f"{BASE_URL}/users/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("User Info:", response.json())

# Step 4: Upload a water test JSON file
def upload_water_test(token):
    url = f"{BASE_URL}/files/water_test/upload"
    headers = {"Authorization": f"Bearer {token}"}
    with open(JSON_FILE_PATH, "rb") as f:
        files = {"file": (JSON_FILE_PATH, f, "application/json")}
        response = requests.post(url, files=files, headers=headers)
    print("Upload Result:", response.status_code, response.json())

# Step 5: Get latest water test file
def get_latest_test(token):
    url = f"{BASE_URL}/files/water_test/latest"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Latest Water Test JSON:", json.dumps(response.json(), indent=2))

# Optional: Get all users (for testing)
def list_users():
    url = f"{BASE_URL}/users/all"
    response = requests.get(url)
    print("All Users:", response.json())

def get_all_tests(token):
    url = f"{BASE_URL}/files/water_test/all"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("All Water Test JSON:", json.dumps(response.json(), indent=2))

# Main sequence
if __name__ == "__main__":
    register_user()
    token = login()
    get_me(token)
    upload_water_test(token)
    get_latest_test(token)
    list_users()
    get_all_tests(token)
