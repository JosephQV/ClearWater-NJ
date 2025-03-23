from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
import json

from shared_config import USER_DATA_FILE, COLORS
from water_system_databases import get_all_counties, get_all_municipalities, get_water_system_by_municipality


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


class UserDataForm(FloatLayout):
    username = StringProperty("")
    email = StringProperty("")
    municipality = StringProperty("Select Municipality")
    county = StringProperty("Select County")
    water_system = StringProperty("Select Water System")
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
        user_data = get_user_data()
        self.username = user_data["username"]
        self.email = user_data["email"]
        
        if user_data["municipality"] != "": 
            self.municipality = user_data["municipality"] 
        else:
            self.municipality = "Select Municipality"
            
        if user_data["county"] != "": 
            self.county = user_data["county"] 
        else: 
            self.county = "Select County"
            
        if user_data["water_system"] != "": 
            self.water_system = user_data["water_system"]
        else:
            self.water_system = "Select Water System"
    
    def submit_user_data(self):
        user_data = get_user_data()
        user_data["username"] = self.username
        user_data["email"] = self.email
        user_data["municipality"] = self.municipality
        user_data["county"] = self.county
        user_data["water_system"] = self.water_system
        
        with open(USER_DATA_FILE, "w") as file:
            json.dump(user_data, file)
        
        return user_data


class CountyDropDown(Button):
    dropdown = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        
        all_counties = get_all_counties()
        
        self.dropdown = DropDown()
        
        for county in all_counties:
            btn = Button(
                text=county, 
                size_hint_y=None, 
                height=40,
                background_color=COLORS["tertiary"]["hex"],
                background_normal="",
                background_down="",
                color="#FFFFFF"
            )
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

            self.dropdown.add_widget(btn)

        self.bind(on_release=self.dropdown.open)
        
        def process_selection(instance, municipality):
            setattr(self, 'text', municipality)
            
        self.dropdown.bind(on_select=process_selection)
        

class MunicipalityDropDown(Button):
    county_filter = StringProperty("")
    dropdown = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def create_selection(self):
        all_municipalities = get_all_municipalities()
        
        self.dropdown = DropDown()
        
        if self.county_filter != "":
        
            for index, row in all_municipalities[all_municipalities["COUNTY_NAME_COMMON"] == self.county_filter + " County"].iterrows():
                print(row)
                btn = Button(
                    text=row["MUNICIPALITY_NAME_NJ-1040"], 
                    size_hint_y=None, 
                    height=40,
                    background_color=COLORS["tertiary"]["hex"],
                    background_down="",
                    background_normal="",
                    color="#FFFFFF"
                )
                btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

                self.dropdown.add_widget(btn)

        self.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))
        
        
class WaterSystemDropDown(Button):
    municipality_filter = StringProperty("")
    dropdown = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def create_selection(self):
        water_systems = get_water_system_by_municipality(self.municipality_filter)
        print(water_systems)
        
        self.dropdown = DropDown()
        
        if self.county_filter != "":
        
            for index, row in water_systems.iterrows():
                print(row)
                btn = Button(
                    text=row["Water System Name"].title(), 
                    size_hint_y=None, 
                    height=40,
                    background_color=COLORS["tertiary"]["hex"],
                    background_down="",
                    background_normal="",
                    color="#FFFFFF"
                )
                btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

                self.dropdown.add_widget(btn)

        self.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))
            

if __name__ == "__main__":
    u = get_user_data()
    print(u)
    u["water_tests"].append({"date": 123, "scores": [1, 2, 3]})
    print(u)   
    with open(USER_DATA_FILE, "w") as file:
        json.dump(u, file)     
    