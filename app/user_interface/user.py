from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder

from app.interface_controllers.user_controller import UserController, UserDataController
from app.models.water_system_data import get_all_counties, get_all_municipalities, get_all_water_systems, get_water_system_by_municipality

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/user.kv")


class UserScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = UserController()


class UserDataScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = UserDataController()

    def get_user_data_form_items(self):
        items = [
            {
                "type": "Text",
                "label_text": "Username"
            },
            {
                "type": "Text",
                "label_text": "Email"
            },
            {
                "type": "Dropdown",
                "label_text": "County",
                "options": get_all_counties()
            },
            {
                "type": "Dropdown",
                "label_text": "Municipality",
                "options": get_all_municipalities()["MUNICIPALITY_NAME_COMMON"]
            },
            {
                "type": "Dropdown",
                "label_text": "Water System",
                "options": get_all_water_systems()["PWS Name"]
            }
        ]
        return items
        
    
    
    