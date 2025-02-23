from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
import webbrowser
import pandas as pd
import os

from shared_config import IN_APP_RESOURCES_DATA_FILE


def get_resources(category):
    df = pd.read_excel(IN_APP_RESOURCES_DATA_FILE)
    df = df[df["Category"] == category]
    
    return df
    
class ResourcesScreen(Screen):
    pass


class ResourcesWidget(BoxLayout):
    pass


class ResourcesList(GridLayout):
    category = StringProperty("")
    previous_language = StringProperty("")
    resource_items = []
        
    def add_resources(self, language):
        if language != self.previous_language:
            self.previous_language = language
            
            for item in self.resource_items:
                self.remove_widget(item)
            
            resources = get_resources(self.category)
            
            for index, resource in resources.iterrows():
                item = ResourceItem(
                        display_name=resource[f"Display Name ({language})"],
                        link=resource["Link"],
                        img_source=f"{os.curdir}/resources/icons/{resource["Image"]}"
                    )
                self.add_widget(item)
                self.resource_items.append(item)
          
          
class ResourceItem(BoxLayout):
    display_name = StringProperty("")
    link = StringProperty("")
    img_source = StringProperty("")
    
    def __init__(
        self,
        display_name,
        link,
        img_source,
        **kw
    ):
        super().__init__(**kw)
        
        self.display_name = display_name
        self.link = link
        self.img_source = img_source
    
    def open_resource_link(self):
        webbrowser.open(self.link)
    

        