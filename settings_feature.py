from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty


class SettingsScreen(Screen):
    pass


class SettingSelection(BoxLayout):
    setting_name = StringProperty("Setting")
    setting_choices = ListProperty(["Choice 1", "Choice 2"])

