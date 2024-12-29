from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
import webbrowser


class ResourcesScreen(Screen):
    pass


class EducationalResourcesList(BoxLayout):
    def __init__(self, **kwargs):
        super(EducationalResourcesList, self).__init__(**kwargs)


class ResourceItem(BoxLayout):
    resource_display_name = StringProperty(None)
    
    def open_resource_link(self):
        # Based on this ResourceItem's resource_display_name property,
        # use the get_link function created previously to find the url link
        # corresponding to this resource name.
        # Note: 'self' represents the instance of the ResourceItem which this
        # function was called on. You can access the resource display name using
        # self.resource_display_name.
        
        # Use the built-in python webbrowser package to open the link that is
        # found using the open() function.
        # As an example:
        webbrowser.open("https://www-doh.nj.gov/doh-shad/topic/Water.html")
        