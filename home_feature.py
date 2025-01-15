from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    pass
class RegionInput(BoxLayout):
    region = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        
        self.text_input = TextInput(hint_text="Enter town/municipality", multiline=False)
        self.add_widget(self.text_input)

        
        self.submit_button = Button(text="Submit")
        self.submit_button.on_release = self.store_region  
        self.add_widget(self.submit_button)

    def store_region(self):
        """Read input and store it in the class attribute."""
        RegionInput.region = self.text_input.text
        print(f"Region stored: {RegionInput.region}")  # For debugging

class MyApp(App):
    def build(self):
        
        return RegionInput()

if __name__ == "__main__":
    MyApp().run()