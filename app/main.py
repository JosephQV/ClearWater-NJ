import logging

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

from app.user_interface.reusable_components.navigation import WindowManager
from app.user_interface.reusable_components.feed_widgets import HorizontalFeed, LargeFeedItem, SmallFeedItem
from app.user_interface.reusable_components.form_widgets import Form, LabeledCheckbox, LabeledDropdown, LabeledNumericInput, LabeledTextInput
from app.user_interface.home import HomeScreen
from app.user_interface.resources import ResourcesScreen
from app.user_interface.settings import SettingsScreen
from app.user_interface.user import UserScreen, UserDataScreen
from app.user_interface.communication import CommunicationScreen
from app.user_interface.water import WaterQualityScreen, WaterContaminantSelectionScreen
from app.user_interface.map import MapScreen

from data.app_config import APP_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH, IMAGES
from data.text_and_translation import APP_TEXT
from app.themes.colors import COLORS
from app.models.user_data import get_language, create_user_data_file, get_user_data
from app.models.log_config import setup_logging


# Starting logging
setup_logging()

create_user_data_file()

logger = logging.getLogger(__name__)

# Setting default window size to (width, height) in pixels. This is a 9 x 16 aspect ratio.
Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)


class MainApplication(App):
    title = APP_TITLE
    text = APP_TEXT
    colors = COLORS
    images = IMAGES
        
    def build(self):
        self.screen_manager = WindowManager()
        self.screen_manager.add_widget(HomeScreen())
        self.screen_manager.add_widget(MapScreen())
        self.screen_manager.add_widget(ResourcesScreen())
        self.screen_manager.add_widget(WaterQualityScreen())
        self.screen_manager.add_widget(WaterContaminantSelectionScreen())
        self.screen_manager.add_widget(SettingsScreen())
        self.screen_manager.add_widget(UserScreen())
        self.screen_manager.add_widget(UserDataScreen())
        self.screen_manager.add_widget(CommunicationScreen())
        return self.screen_manager
    
    def language(self):
        return get_language()
    
    def user_data(self):
        return get_user_data()
