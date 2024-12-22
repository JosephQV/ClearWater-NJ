from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import webbrowser
import pandas as pd


class ResourcesScreen(Screen):
    pass


class EducationalResourcesList(BoxLayout):
    def __init__(self, **kwargs):
        super(EducationalResourcesList, self).__init__(**kwargs)
        
    def get_link(self, display_name):

        df = pd.read_excel("DataSheets.xlsx", index_col=0)
        df.head()
        result = df[df["Display Name"].str.casefold() == display_name]
        if not result.empty:
            return result.iloc[0]["Name"]
        else:
            return "Display name not found in the resource list"

    def open_resource_link(self, link): 
        link = self.get_link(display_name)
        print(link)
        # temporary, as an example
        webbrowser.open("https://www-doh.nj.gov/doh-shad/topic/Water.html")
        
        