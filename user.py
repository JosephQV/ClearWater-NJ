from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
import json

from shared_config import USER_DATA_FILE


def get_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            data = json.load(file)
            
        return data
    
    except Exception as e:
        print(str(e))
        return {"username": "", "municipality": "", "county": "", "water_tests": []}
        

class UserScreen(Screen):
    pass


class UserDataScreen(Screen):
    pass


class UserDataForm(BoxLayout):
    username = StringProperty("")
    municipality = StringProperty("")
    county = StringProperty("")
    
    def submit_user_data(self):
        user_data = {}
        with open(USER_DATA_FILE, "r") as file:
            try:
                user_data = json.load(file)
                user_data["username"] = self.username
                user_data["municipality"] = self.municipality
                user_data["county"] = self.county
            except Exception:
                user_data = {"username": self.username, "municipality": self.municipality, "county": self.county, "water_tests": []}
        
        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file)
            
        self.username = ""
        self.municipality = ""
        self.county = ""
        
        return user_data
            
        