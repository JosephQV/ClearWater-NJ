from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import DictProperty
from kivy.lang import Builder

import os

from models.user_data import get_user_data


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/results.kv")


class AllTestsResultsScreen(Screen):
    pass


class SingleTestResultsScreen(Screen):
    pass
        
