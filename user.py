from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import StringProperty
import json

from shared_config import USER_DATA_FILE
from water_system_databases import get_all_counties, get_all_municipalities


def get_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            data = json.load(file)
            
        return data
    
    except Exception as e:
        print(str(e))
        return {"username": "", "email": "", "municipality": "", "county": "", "water_system": "", "water_tests": []}
        

class UserScreen(Screen):
    pass


class UserDataScreen(Screen):
    pass


class UserDataForm(BoxLayout):
    username = StringProperty("")
    municipality = StringProperty("")
    county = StringProperty("")
    
    def submit_user_data(self):
        user_data = get_user_data()
        user_data["username"] = self.username
        user_data["municipality"] = self.municipality
        user_data["county"] = self.county
        
        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file)
            
        self.username = ""
        self.municipality = ""
        self.county = ""
        
        return user_data


class CountyDropDown(DropDown):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        all_counties = get_all_counties()
        
        for county in all_counties:
            btn = Button(
                text=county, 
                size_hint_y=None, 
                height=44
            )
            btn.bind(on_release=lambda btn: self.select(btn.text))

            self.add_widget(btn)

        mainbutton = Button(text="Select County", size_hint=(None, None))
        mainbutton.bind(on_release=self.open)
        self.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            

if __name__ == "__main__":
    u = get_user_data()
    print(u)
    u["water_tests"].append({"date": 123, "scores": [1, 2, 3]})
    print(u)   
    with open(USER_DATA_FILE, "w") as file:
        json.dump(u, file)     
    