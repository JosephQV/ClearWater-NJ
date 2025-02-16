from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
import webbrowser
import pandas as pd
import os


class ResourcesScreen(Screen):
    pass


class EducationalResourcesList(BoxLayout):
    pass
          
                
class ResourceItem(BoxLayout):
    resource_display_name = StringProperty(None)
    
    def open_resource_link(self):
        link = self.get_link(self.resource_display_name)
        if link is not None:
            webbrowser.open(link)     
    
    def get_link(self, display_name):
        file = fr"{os.curdir}\resources\InAppResources.xlsx"
        df = pd.read_excel(file)
        result = df[df["Display Name"] == display_name]
        if not result.empty:
            return result.iloc[0]["Name"]
        else:
            return None
    

        