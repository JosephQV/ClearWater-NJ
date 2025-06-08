import logging

from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase

from app.user_interface.reusable_components.navigation import WindowManager
from app.user_interface.reusable_components.feed_widgets import HorizontalFeed, LargeFeedItem, SmallFeedItem
from app.user_interface.reusable_components.form_widgets import Form, LabeledCheckbox, LabeledDropdown, LabeledNumericInput, LabeledTextInput
from app.user_interface.home import HomeScreen
from app.user_interface.resources import ResourcesScreen
from app.user_interface.settings import SettingsScreen
from app.user_interface.user import UserScreen, UserDataScreen
from app.user_interface.communication import CommunicationScreen
from app.user_interface.water import WaterQualityScreen, WaterContaminantSelectionScreen, TestingKitSelectionScreen, WaterTestInputScreen
from app.user_interface.map import MapScreen

from data.app_config import APP_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH, IMAGES, FONT_FILE, FONT_ITALIC_FILE
from data.text_and_translation import APP_TEXT
from app.themes.colors import COLORS
from app.models.user_data import UserController
from app.models.log_config import setup_logging


LabelBase.register(name="NotoSans", fn_regular=FONT_FILE, fn_italic=FONT_ITALIC_FILE)


# Starting logging
setup_logging()

logger = logging.getLogger(__name__)

# Setting default window size to (width, height) in pixels. This is a 9 x 16 aspect ratio.
Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)


class MainApplication(App):
    title = APP_TITLE
    text = APP_TEXT
    colors = COLORS
    images = IMAGES
    user_controller = UserController()
        
    def build(self):
        self.screen_manager = WindowManager()
        self.screen_manager.add_widget(HomeScreen())
        self.screen_manager.add_widget(MapScreen())
        self.screen_manager.add_widget(ResourcesScreen())
        self.screen_manager.add_widget(WaterQualityScreen())
        self.screen_manager.add_widget(TestingKitSelectionScreen())
        self.screen_manager.add_widget(WaterContaminantSelectionScreen())
        self.screen_manager.add_widget(WaterTestInputScreen())
        self.screen_manager.add_widget(SettingsScreen())
        self.screen_manager.add_widget(UserScreen())
        self.screen_manager.add_widget(UserDataScreen())
        self.screen_manager.add_widget(CommunicationScreen())
        return self.screen_manager
    
    def language(self):
        return self.user_controller.get_language()
    
    def user_data(self):
        return self.user_controller.user_data
