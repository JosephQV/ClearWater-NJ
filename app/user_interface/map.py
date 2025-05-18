from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder

from app.interface_controllers.map_controller import MapController

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/map.kv")


class MapScreen(Screen):
    controller = MapController()
        

class InteractiveMap(FloatLayout):
    pass
    

