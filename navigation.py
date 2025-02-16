from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, FadeTransition, NoTransition, SlideTransition
from kivy.clock import Clock
from kivy.uix.button import Button

from shared_config import IMAGES, PRIMARY_THEME_COLOR


# Creating a class that sub-classes the kivy ScreenManager class for maintaing behavior
# between multiple screens.
class WindowManager(ScreenManager):        
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.transition = NoTransition()
        
    def switch_screens(self, next_screen, transition):
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
        

# This class represents a menu bar to access the user's own water quality information if applicable.
# It will be at the top of every screen.
class UserMenuNavigation(BoxLayout):
    pass


class StartScreen(Screen):
    pass
        

class BackMenuBar(BoxLayout):
    title_text = StringProperty("")