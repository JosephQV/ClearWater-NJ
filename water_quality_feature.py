from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
import pandas as pd
import os

contaminant_data = fr"{os.curdir}/resources/GSS_Inorganic_Chemicals_Data.xlsx"


def get_mcl(contaminant_name):
    contaminant_df = pd.read_excel(contaminant_data)
    row = contaminant_df[contaminant_df['Contaminant Name'] == contaminant_name]
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
    submit_button = ObjectProperty(None)
    
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

        result_text = '\n'.join([f'{k}: {v}' for k, v in results.items()])
        print(result_text) # placeholder for testing

        df=pd.DataFrame(data_for_excel, columns=['Contaminant', 'Input Value', 'Message'])
        df.to_excel(fr"{os.curdir}/resources/user/test_results.xlsx", index=False)


class WaterTestInputItem(BoxLayout):
    contaminant_name = StringProperty("")


class WaterContaminantSelectionScreen(Screen):
    
    def refresh_screen(self, selection_form):
        form_container_widget = selection_form.ids.selection_form_container
        selection_form.clear_form(form_container_widget)


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
    
        
        