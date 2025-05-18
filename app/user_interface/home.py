from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from app.interface_controllers.home_controller import HomeController

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/home.kv")


class HomeScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = HomeController()
        
    def get_general_news_feed_items(self):
        if self.controller is None: self.controller = HomeController()
        articles = self.controller.get_recent_news(topic="general")
        items = []
        for article in articles:
            print(article)
            # items.append({
            #     "title": "",
            #     "subtitle_1": "",
            #     "subtitle_2": "",
            #     "subtitle_3": "",
            #     "description": "",
            #     "submit_action": "open external link",
            #     "link": row["Link"],
            #     "image": f"{ICON_PATH}/{row["Image"]}"
            # })
        return items