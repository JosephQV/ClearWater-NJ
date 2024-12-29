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

        file = fr"{os.curdir}\resources\DataSheets.xlsx"
        df = pd.read_excel(file)
        df.head()
        result = df[df["Display Name"].str.casefold() == display_name]
        if not result.empty:
            return result.iloc[0]["Name"]
        else:
            return "Display name not found in the resource list"

    def open_resource_link(self, link): 
        link = self.get_link(link)
        print(link)
        # temporary, as an example
        webbrowser.open(link)        
        