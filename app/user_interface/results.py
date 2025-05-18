from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import DictProperty
from kivy.lang import Builder

import os

from models.user_data import get_user_data


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/results.kv")


class WaterTestResultsScreen(Screen):
    pass


class WaterTestResultsWidget(BoxLayout):
    user_data = DictProperty(get_user_data())
    
    def update_results_data(self):
        self.user_data = get_user_data()
        print(self.user_data)
    
   
class AllWaterTestsScreen(Screen):
    pass


class AllWaterTestsWidget(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        water_tests = get_user_data()["water_tests"]
        
        for test in water_tests:
            result_item = WaterTestResultItem(
                test_info=test,
            )
            self.add_widget(result_item)


class WaterTestResultItem(FloatLayout):
    test_info = DictProperty({"date": "", "scores": "", "results": ""})
        
    def __init__(self, test_info, **kw):
        super().__init__(**kw)
        
        self.test_info = test_info
        
  