from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from app.interface_controllers.resources_controller import ResourcesController
from data.app_config import ICON_PATH

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/resources.kv")

    
class ResourcesScreen(Screen):
    controller = ObjectProperty(None)
    educational_resources_list = ObjectProperty(None)
    contaminant_resources_list = ObjectProperty(None)
    tool_resources_list = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = ResourcesController()
        
    def get_resource_feed_items(self, resource_category):
        if self.controller is None: self.controller = ResourcesController()
        resources = self.controller.get_in_app_resources(resource_category)
        items = []
        for index, row in resources.iterrows():
            items.append({
                "title": row["Display Name"],
                "subtitle_1": "",
                "subtitle_2": "",
                "subtitle_3": "",
                "description": "",
                "submit_action": "open external link",
                "link": row["Link"],
                "image": f"{ICON_PATH}/{row["Image"]}"
            })
        return items
        
        



    

        