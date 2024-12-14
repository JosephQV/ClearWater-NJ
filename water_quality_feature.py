from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
import pandas as pd


class WaterQualityScreen(Screen):
    pass


class WaterTestInputForm(BoxLayout):
    contaminant_1_label = ObjectProperty(None)
    contaminant_2_label = ObjectProperty(None)
    contaminant_3_label = ObjectProperty(None)
    contaminant_4_label = ObjectProperty(None)
    contaminant_5_label = ObjectProperty(None)
    contaminant_1 = ObjectProperty(None)
    contaminant_2 = ObjectProperty(None)
    contaminant_3 = ObjectProperty(None)
    contaminant_4 = ObjectProperty(None)
    contaminant_5 = ObjectProperty(None)
    response_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(WaterTestInputForm, self).__init__(**kwargs)
        self.load_data_from_excel(r'C:\Users\sghal\Downloads\GSS_Inorganic_Chemicals_Data.xlsx')

    def load_data_from_excel(self, file_path):
        df = pd.read_excel(file_path)
        contaminant_names = df['Contaminant Name'].tolist()
        self.contaminant_1_label.text = f"{contaminant_names[0]} (mg/L)"
        self.contaminant_2_label.text = f"{contaminant_names[1]} (mg/L)"
        self.contaminant_3_label.text = f"{contaminant_names[2]} (mg/L)"
        self.contaminant_4_label.text = f"{contaminant_names[3]} (mg/L)"
        self.contaminant_5_label.text = f"{contaminant_names[4]} (mg/L)"
        

    def submit_button_action(self):
        response_text = (
            f"Recieved inputs:\n"
            f"Contaminant 1: {self.contaminant_1.text}\n"
            f"Contaminant 2: {self.contaminant_2.text}\n"
            f"Contaminant 3: {self.contaminant_3.text}\n"
            f"Contaminant 4: {self.contaminant_4.text}\n"
            f"Contaminant 5: {self.contaminant_5.text}\n"
        )
        self.response_label.text = response_text

class WaterQualityApp(App):
    def build(self):
        return WaterTestInputForm()
if __name__== '__main__':
    WaterQualityApp().run()
        
        # Load data into pandas dataframe like
        # Contaminant Name  Level
        # ...               ...
        # ...               ...
        # etc.              etc.

