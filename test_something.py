# A testing file to be used for importing any classes or functions and then calling them
# within the if-statement below. Run this file independently to test code written here.
from app.models.user_data import UserController


if __name__ == "__main__":
    user_cont = UserController()

    print(user_cont.user_data)
