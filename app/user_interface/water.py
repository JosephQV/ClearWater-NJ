from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, DictProperty, ListProperty
from kivy.lang import Builder

from data.app_config import ICON_PATH
from app.interface_controllers.water_controller import TestingKitSelectionController, WaterContaminantSelectionController, WaterQualityController, WaterTestInputController
from app.models.user_data import add_water_test

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/water.kv")


class WaterQualityScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = WaterQualityController()


class TestingKitSelectionScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = TestingKitSelectionController()
        
    def get_test_selection_feed_items(self):
        if self.controller is None: self.controller = TestingKitSelectionController()
        # list of testing kit dictionaries
        testing_kits = self.controller.get_testing_kits()
        feed_items = []
        for kit in testing_kits:
            item = {
                "image": f"{ICON_PATH}/{kit["image_source"]}", 
                "title": f"{kit["brand"]} {kit["name"]}",
                "subtitle_1": f"Manufacturer: {kit["manufacturer"]}",
                "subtitle_2": "",
                "subtitle_3": "",
                "description": f"Tested Contaminants and Parameters: {kit["contaminants_and_parameters"]}",
                "submit_action": "custom",
                "action_function": self.load_water_test_input_form_from_selections,
                "action_function_kwargs": {"contaminant_selection": kit["contaminants_and_parameters"], "test_type": kit["test_type"], "test_id": kit["ID"]}
            }
            feed_items.append(item)
        return feed_items
    
    def load_water_test_input_form_from_selections(self, contaminant_selection, test_type, test_id):
        water_input_screen = self.manager.get_screen("watertestinput_screen")
        water_input_screen.test_id = test_id
        water_input_screen.update_input_form_items(contaminant_selection, test_type)
        self.manager.switch_screens("watertestinput_screen")


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


class WaterTestInputScreen(Screen):
    controller = ObjectProperty(None)
    input_form = ObjectProperty(None)
    test_id = StringProperty("")
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = WaterTestInputController()
        
    def update_input_form_items(self, contaminant_selection, test_type):
        if self.controller is None: self.controller = WaterTestInputController()
        contaminants = self.controller.get_chosen_contaminants(contaminant_selection)
        print(contaminants)
        form_items = []
        if test_type == "qualitative":
            for contaminant, row in contaminants.iterrows():
                item = {
                    "type": "Dropdown",
                    "label_text": contaminant,
                    "options": ["Not detected", "Detected"]
                }
                form_items.append(item)
        elif test_type == "quantitative":
            for contaminant, row in contaminants.iterrows():
                item = {
                    "type": "Numeric",
                    "label_text": contaminant,
                    "value_bounds": [0.0, 100_000.0]
                }
                form_items.append(item)
                
        self.input_form.form_items = form_items
        
    def save_test_to_file(self, form_data):
        add_water_test(form_data, self.test_id)