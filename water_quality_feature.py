from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen 
from kivy.properties import ObjectProperty 
import pandas

class WaterQualityScreen(Screen):
    pass

class WaterTestInputForm(BoxLayout):
    def __init__(self, **kwargs):
        super(WaterTestInputForm, self).__init__(**kwargs)
        
        self.contaminant_1 = ObjectProperty(None)
        self.contaminant_2 = ObjectProperty(None)
        self.contaminant_3 = ObjectProperty(None)
        self.contaminant_4 = ObjectProperty(None)
        self.contaminant_5 = ObjectProperty(None)
        
    
    def submit_button_action(self):
        print(self.contaminant_1.text)
        print(self.contaminant_2.text)
        print(self.contaminant_3.text)
        print(self.contaminant_4.text)
        print(self.contaminant_5.text)
        
        # Load data into pandas dataframe like
        # Contaminant Name  Level
        # ...               ...
        # ...               ...
        # etc.              etc.