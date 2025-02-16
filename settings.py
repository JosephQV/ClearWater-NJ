from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty


# Empty template for the settings screen, which is where the user will
# be able to adjust things like the language of information presented in the app.
class SettingsScreen(Screen):
    pass


# This simple widget is defined to make it easier to add options to
# the settings screen by just providing a name and list of choices.
class SettingSelection(BoxLayout):
    setting_name = StringProperty("Setting")
    setting_choices = ListProperty(["Choice 1", "Choice 2"])
    selection_spinner = ObjectProperty(None)

