from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
import pandas as pd
from kivy.lang import Builder

file_path= r"C:\Users\sghal\New folder\TestGSS\GSS Inorganic Chemicals Data.xlsx"
df = pd.read_excel(file_path)

print(df.dtypes)
print(df.head())

def get_mcl(contaminant_name):
    row = df[df['Contaminant Name'] == contaminant_name]
    if not row.empty:
        mcl = row['Maximum Contaminant Level (MCL)'].values[0]
        try:
            return float(mcl)
        except ValueError:
            return 'Not found'
    else:
        return 'Not found'
    
    
    
class WaterQualityScreen(Screen):
    nav_bar_id = ObjectProperty(None)

class WaterTestInputScreen(Screen):
    pass

class WaterTestInputForm(BoxLayout):
    kv_contaminant_value_1 = ObjectProperty(None)
    kv_contaminant_value_2 = ObjectProperty(None)
    kv_contaminant_value_3 = ObjectProperty(None)
    kv_contaminant_value_4 = ObjectProperty(None)
    kv_contaminant_value_5 = ObjectProperty(None)
    result_label = ObjectProperty(None)
    submit_button = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(WaterTestInputForm, self).__init__(**kwargs)
    
    def submit_button_action(self):
        contaminants = [
            ("Antimony", self.kv_contaminant_value_1.text),
            ("Arsenic", self.kv_contaminant_value_2.text),
            ("Asbestos", self.kv_contaminant_value_3.text),
            ("Barium", self.kv_contaminant_value_4.text),
            ("Beryllium", self.kv_contaminant_value_5.text),
        ]
        
        results = {}
        data_for_excel= []
        
        for contaminant, input_value in contaminants:
            mcl = get_mcl(contaminant)
            print(f"Processing {contaminant}: input_value={input_value}, mcl={mcl}")
            if mcl != 'Not found':
                try:
                    input_value = float(input_value)
                    mcl = float(mcl)
                    print(f"Converted values: input_value={input_value}, mcl={mcl}")
                    if input_value > mcl:
                        message = f"Exceeded"
                    else:
                        message = f"In range"
                except ValueError:
                    message = "Invalid"
            else:
                message = "Not found"
            results[contaminant] = message
            data_for_excel.append([contaminant, input_value, message])

        result_text = '/n'.join([f'{k}: {v}' for k, v in results.items()])
        self.result_label.text = result_text

        df=pd.DataFrame(data_for_excel, columns=['Contaminant', 'Input Value', 'Message'])
        df.to_excel('user_input_results.xlsx', index=False)
        print("Data exported to user_input_results.xlsx")

class WaterQualityApp(App):
    def build(self):
        return WaterTestInputForm()
    
if __name__ == '__main__':
    Builder.load_file(r"C:/Users/sghal/New folder/TestGSS/NewGSSTeam12Project/kivy_design_files/waterqualityscreen.kv")
    

#WaterQualityApp().run()
#if __name__== '__main__':
#    WaterQualityApp().run()
        
        # Load data into pandas dataframe like
        # Contaminant Name  Level
        # ...               ...
        # ...               ...
        # etc.              etc.



class WaterContaminantSelectionForm(BoxLayout):
    def process_contaminant_selections(self, form_container_widget):
        selected = dict()
        child_widgets = form_container_widget.children
        for child in child_widgets:
            if type(child) is ContaminantSelectableItem:
                selected.update({child.contaminant_text : child.is_selected})
        print(selected)
        return selected
    
    def clear_form(self, form_container_widget):
        child_widgets = form_container_widget.children
        for child in child_widgets:
            if type(child) is ContaminantSelectableItem:
                child.ids.check_box.active = False
                child.is_selected = False


class ContaminantSelectableItem(BoxLayout):
    contaminant_text = StringProperty("Default Contaminant")
    is_selected = BooleanProperty(False)
    
        
        