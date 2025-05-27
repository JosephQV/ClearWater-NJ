import os
import logging

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import FadeTransition, NoTransition, SlideTransition
from kivy.uix.button import Button
from kivy.lang.builder import Builder

from data.app_config import IMAGES
from app.themes.colors import PRIMARY_THEME_COLOR


logger = logging.getLogger(__name__)


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/navigation.kv")


# Creating a class that sub-classes the kivy ScreenManager class for maintaing behavior
# between multiple screens.
class WindowManager(ScreenManager):
    prev_screen_hist = ListProperty("")
           
    def __init__(self, **kw):
        super(WindowManager, self).__init__(**kw)
        self.transition = NoTransition()
        
    def switch_screens(self, next_screen, transition=None):
        if next_screen not in self.screen_names:
            logger.error(f"Error switching screens, '{next_screen}' does not exist.")
            return
        prev_screen = self.current
        try:
            if transition == None:
                self.current = next_screen
            elif transition == "right":
                self.transition = SlideTransition()
                self.transition.direction = "right"
                self.current = next_screen
                self.transition = NoTransition()
            elif transition == "left":
                self.transition = SlideTransition()
                self.transition.direction = "left"
                self.current = next_screen
                self.transition = NoTransition()
            elif transition == "up":
                self.transition = SlideTransition()
                self.transition.direction = "up"
                self.current = next_screen
                self.transition = NoTransition()
            elif transition == "down":
                self.transition = SlideTransition()
                self.transition.direction = "down"
                self.current = next_screen
                self.transition = NoTransition()
            elif transition == "fade":
                self.transition = FadeTransition()
                self.current = next_screen
                self.transition = NoTransition()
        except Exception as e:
            logger.error(f"Error switching screens: {e}")
        self.prev_screen_hist.append(prev_screen)
    
    def go_back(self):
        try:
            prev_screen = self.prev_screen_hist[-1]
            self.prev_screen_hist = self.prev_screen_hist[:-1]
            self.current = prev_screen
        except Exception as e:
            logger.error(f"Error switching to previous screen: {e}\nScreen history: {self.prev_screen_hist}")
    

# This class represents a navigation bar at the bottom of the screen used to switch between screens.
# It sub-classes the kivy GridLayout container widget. The buttons for it are defined in the screennavigation.kv file.
# Each screen will have this component at the bottom.
class ScreenNavigationBar(GridLayout):
    # These properties are mapped to the corresponding button in the navigation
    # bar so that the selection status (which screen is being navigated to) can be known
    # by the class.
    mywater_btn = ObjectProperty(None)
    map_btn = ObjectProperty(None)
    home_btn = ObjectProperty(None)
    resources_btn = ObjectProperty(None)
    communication_btn = ObjectProperty(None)
    
    default_icon_paths = [IMAGES["mywater"], IMAGES["map"], IMAGES["home"], IMAGES["resources"], IMAGES["communication"]]
    selected_icon_paths = [IMAGES["mywater_selected"], IMAGES["map_selected"], IMAGES["home_selected"], IMAGES["resources_selected"], IMAGES["communication_selected"]]
                
    def color_buttons(self, calling_screen):
        match calling_screen:
            case "waterquality_screen":
                current = self.mywater_btn
            case "resources_screen":
                current = self.resources_btn
            case "home_screen": 
                current = self.home_btn
            case "communication_screen":
                current = self.communication_btn
            case "map_screen":
                current = self.map_btn
            case _:
                print("Error: screen not found")
        for i, btn in enumerate([self.mywater_btn, self.map_btn, self.home_btn, self.resources_btn, self.communication_btn]):
            if btn is None:
                continue
            elif btn == current:
                btn.color = PRIMARY_THEME_COLOR
                img = btn.children[0]
                img.source = self.selected_icon_paths[i]
            else:
                btn.color = "#000000"
                img = btn.children[0]
                img.source = self.default_icon_paths[i]
                
                
class NavigationButton(Button):
    button_text = StringProperty("")
    screen = StringProperty("")
    image_source = StringProperty("")
        

class UserMenuNavigation(BoxLayout):
    pass
        

class BackMenuBar(BoxLayout):
    title_text = StringProperty("")
    

class TextPreview(BoxLayout):
    title = StringProperty("")
    body = StringProperty("")
    button_text = StringProperty("Go")
    target_screen = StringProperty("")

    def navigate(self, screen_manager):
        if hasattr(screen_manager, "switch_screens"):
            screen_manager.switch_screens(self.target_screen)


class ImagePreview(BoxLayout):
    image_source = StringProperty("")
    caption = StringProperty("")
    target_screen = StringProperty("")

    def navigate(self, screen_manager):
        if hasattr(screen_manager, "switch_screens"):
            screen_manager.switch_screens(self.target_screen)


class NavigationHub(ScrollView):
    items = ListProperty([])
    screen_manager = ObjectProperty(None)
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(items=self.populate_items)

    def populate_items(self, *args):
        if not self.layout:
            return

        self.layout.clear_widgets()
        for item in self.items:
            widget_type = item.get("type")
            if widget_type == "text":
                widget = TextPreview(
                    title=item.get("title", ""),
                    body=item.get("body", ""),
                    button_text=item.get("button_text", "Go"),
                    target_screen=item.get("target_screen", "")
                )
            elif widget_type == "image":
                widget = ImagePreview(
                    image_source=item.get("image_source", ""),
                    caption=item.get("caption", ""),
                    target_screen=item.get("target_screen", "")
                )
            else:
                continue
            widget.screen_manager = self.screen_manager
            self.layout.add_widget(widget)
