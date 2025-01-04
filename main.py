from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.lang import Builder
from kivy.core.window import Window
import os

# Importing our own code from the other files
from water_quality_feature import *     # "*" imports everything from that file
from educational_resources_feature import *
from communication_feature import *
from settings_feature import *
from home_feature import *
from screen_navigation import *
from shared_config import *


# Setting default window size to (width, height) in pixels. This is a 9 x 16 aspect ratio.
Window.size = (350, 622)

# Creating a class that sub-classes the kivy ScreenManager class for maintaing behavior
# between multiple screens. It doesn't do anything unique yet but having this dedicated class
# may be useful later. I set the transitions between screens to none (instant transition).
class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.transition = NoTransition()

# These lines use the kivy Builder variable to load any kivy design files we created that are needed
# for the app. The 'os.curdir' uses the standard Python package os (operating system) to get the
# current directory. This directory path is inserted at the beginning of the file paths to each kivy
# file so they can be found on any computer while we develop this.
# Note: the order matters, the main file should be loaded last like it is done here.
kivy_design_file_dir = f"{os.curdir}/kivy_design_files/"
for file in os.listdir(kivy_design_file_dir):
    Builder.load_file(os.path.join(kivy_design_file_dir, file))
    
main_kv_design_file = Builder.load_file(os.path.join(kivy_design_file_dir, "main_design.kv"))

# This is the main class that sub-classes the kivy App class.  We override the default build method of the App
# class to do what we need when starting the app, which for now is just returning the file path
# of the main kivy design file, which creates a screen manager and each of the screens.
class MainApplication(App):
    primary_theme_color = PRIMARY_THEME_COLOR
    secondary_theme_color = SECONDARY_THEME_COLOR
        
    def build(self):
        # this design file returns a screen manager, it is set to an attribute of the app class here.
        self.screen_manager = main_kv_design_file
        return main_kv_design_file


# This if-statement just checks if the current running Python file's file name is "__main__". The name of the
# current Python file is stored implicitly (by default) by Python in the __name__ variable. For the Python file
# that is directly executed however, this __name__ variable holds "__main__", regardless of what the file is called.
# This if-statement is commonly included in Python programs because it allows us to check if this file was executed
# directly (e.g. 'python main.py' in the terminal) or if it is being imported (when importing packages/modules, 
# the code inside them is read and executed by the Python interpreter). Without this if-statement, if this file was
# imported by other Python code files, the following lines would be executed and the app would be built and ran
# when we don't want it to be. Even if we never import this file anywhere else, it is good practice to have this
# conditional statement.
if __name__ == "__main__":
    app = MainApplication()
    app.run()