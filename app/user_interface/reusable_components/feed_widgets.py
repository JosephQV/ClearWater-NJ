from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView

import os
import webbrowser
import logging


logger = logging.getLogger(__name__)


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/feed_widgets.kv")


class SmallFeedItem(BoxLayout):
    image = StringProperty("")
    title = StringProperty("Title")
    subtitle_1 = StringProperty("")
    subtitle_2 = StringProperty("")
    submit_action = StringProperty("")
    link = StringProperty("")
    
    def on_image_click(self, screen_manager):
        if self.submit_action == "open external link":
            webbrowser.open(self.link)
        elif self.submit_action == "open screen":
            pass
        
    
class LargeFeedItem(BoxLayout):
    image = StringProperty("")
    title = StringProperty("Title")
    subtitle_1 = StringProperty("")
    subtitle_2 = StringProperty("")
    subtitle_3 = StringProperty("")
    description = StringProperty("Description")
    submit_action = StringProperty("")
    link = StringProperty("")


class HorizontalFeed(ScrollView):
    feed_items = ListProperty([])
    feed_item_size = StringProperty("small")  # "small" or "large"
    layout = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.bind(feed_items=self.fill_feed)

    def fill_feed(self, *args):
        self.layout.clear_widgets()
        widgets = self.create_feed_widgets(self.feed_items)
        for widget in widgets:
            self.layout.add_widget(widget)
            
    def create_feed_widgets(self, feed_items):
        widgets = []
        for i, item in enumerate(feed_items):
            try:
                if self.feed_item_size == "small":
                    widget = SmallFeedItem(
                        image=item.get("image", ""),
                        title=item.get("title", ""),
                        subtitle_1=item.get("subtitle_1", ""),
                        subtitle_2=item.get("subtitle_2", ""),
                        submit_action=item.get("submit_action", ""),
                        link=item.get("link", ""),
                        height=self.height,
                        width=self.height
                    )
                elif self.feed_item_size == "large":
                    widget = LargeFeedItem(
                        image=item.get("image", ""),
                        title=item.get("title", ""),
                        subtitle_1=item.get("subtitle_1", ""),
                        subtitle_2=item.get("subtitle_2", ""),
                        subtitle_3=item.get("subtitle_3", ""),
                        description=item.get("description", ""),
                        submit_action=item.get("submit_action", ""),
                        link=item.get("link", ""),
                        height=self.height,
                        width=self.height
                    )
                widgets.append(widget)
            except Exception as e:
                logger.error(f"Error creating feed item #{i}: {e}")
        return widgets
            
    def expand_feed(self):
        pass
        