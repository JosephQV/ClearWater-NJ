from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import webbrowser


class EducationalResourcesList(BoxLayout):
    def __init__(self, **kwargs):
        super(EducationalResourcesList, self).__init__(**kwargs)
        
    
    def open_resource_link(self, link): 
        print(link)
        # temporary, as an example
        webbrowser.open("https://www-doh.nj.gov/doh-shad/topic/Water.html")
        
        