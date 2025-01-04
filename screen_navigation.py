from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, FadeTransition, NoTransition, SlideTransition
from kivy.clock import Clock
from shared_config import *
import os


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
    
    mywater_img = ObjectProperty(None)
    map_img = ObjectProperty(None)
    home_img = ObjectProperty(None)
    resources_img = ObjectProperty(None)
    communication_img = ObjectProperty(None)
    
    mywater_icon_path = "resources/icons/mywater_icon.png"
    map_icon_path = "resources/icons/map_icon.png"
    home_icon_path = "resources/icons/home_icon.png"
    resources_icon_path = "resources/icons/resources_icon.png"
    communication_icon_path = "resources/icons/communication_icon.png"
    
    mywater_icon_selected_path = "resources/icons/mywater_icon_selected.png"
    map_icon_selected_path = "resources/icons/map_icon_selected.png"
    home_icon_selected_path = "resources/icons/home_icon_selected.png"
    resources_icon_selected_path = "resources/icons/resources_icon_selected.png"
    communication_icon_selected_path = "resources/icons/communication_icon_selected.png"
    
    default_icon_paths = [mywater_icon_path, map_icon_path, home_icon_path, resources_icon_path, communication_icon_path]
    selected_icon_paths = [mywater_icon_selected_path, map_icon_selected_path, home_icon_selected_path, resources_icon_selected_path, communication_icon_selected_path]
    
                
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
        
        
            

        

# This class represents a menu bar to access the user's own water quality information if applicable.
# It will be at the top of every screen.
class UserMenuNavigation(BoxLayout):
    app_icon_path = fr"{os.curdir}\resources\icons\app_icon.png"
    settings_icon_path = fr"{os.curdir}\resources\icons\menu_icon.webp"
    user_icon_path = fr"{os.curdir}\resources\icons\user_icon.png"
    
    def navigate_to_settings(self, screen_manager):
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = "left"
        screen_manager.current = "settings_screen"
        screen_manager.transition = NoTransition()


class StartScreen(Screen):
    app_icon_path = fr"{os.curdir}\resources\icons\app_icon.png"

    def on_enter(self):
        Clock.schedule_once(self.fade_to_home, 2)
        
    
    def fade_to_home(self, time):
        self.manager.transition = FadeTransition()
        self.manager.current = "home_screen"
        self.manager.transition = NoTransition()
        

class BackMenuBar(BoxLayout):
    title_text = StringProperty("")
    prev_screen = StringProperty("")
    back_icon_path = fr"{os.curdir}\resources\icons\back_icon.webp"
    
    def back_to_prev_screen(self, screen_manager):
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = "right"
        screen_manager.current = self.prev_screen
        screen_manager.transition = NoTransition()