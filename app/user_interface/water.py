from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, DictProperty
from kivy.lang import Builder

from data.app_config import ICON_PATH
from app.interface_controllers.water_controller import WaterContaminantSelectionController, WaterQualityController, WaterTestInputController

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/water.kv")


class WaterQualityScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = WaterQualityController()


class WaterTestInputScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = WaterTestInputController()
        
    def get_water_test_form_items(self):
        pass


class WaterContaminantSelectionScreen(Screen):
    controller = ObjectProperty(None)
    selection_form = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = WaterContaminantSelectionController()
    
    def get_contaminant_selection_form_items(self):
        if self.controller is None: self.controller = WaterContaminantSelectionController()
        contaminants = self.controller.get_all_contaminants()
        form_items = []
        # Not separating by rarity yet
        for contaminant_info in contaminants["Common"] + contaminants["Rare"] + contaminants["Very Rare"]:
            item = {
                "type": "Checkbox",
                "label_text": f"{contaminant_info["Contaminant"]}\n{contaminant_info["Contaminant Group"]}",
                "required": False
            }
            form_items.append(item)
        return form_items
        

      
        