from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.lang.builder import Builder

from app.models.user_data import set_language
from app.interface_controllers.settings_controller import SettingsController

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/settings.kv")


class SettingsScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = SettingsController()
        
    def get_settings_form_items(self):
        language_setting = {
            "type": "Dropdown",
            "label_text": "Language",
            "options": ["English", "Español"]
        }
        return [language_setting]

    def update_settings(self, settings):
        set_language(settings["Language"])
