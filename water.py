from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
import datetime, time
import os
import json
import pathlib

from contaminant_databases import get_contaminant_dataframe, get_weighted_contaminant_score
from shared_config import USER_DATA_FILE
from user import get_user_data


class WaterQualityScreen(Screen):
    nav_bar_id = ObjectProperty(None)


class WaterTestInputScreen(Screen):
    water_test_form = ObjectProperty(None)
    
    def create_water_test_form(self, selected_contaminants):
        self.water_test_form.fill_form(selected_contaminants)
        
    def on_leave(self):
        self.water_test_form.clear_form()


class WaterTestInputForm(BoxLayout):
    contaminant_entries = {}
    form_container = ObjectProperty(None)
        
    
    def fill_form(self, selected_contaminants):
        contaminant_df = get_contaminant_dataframe()
        for contaminant, selected in selected_contaminants.items():
            if selected is True:
                print(contaminant)
                row = contaminant_df.loc[contaminant]
                if row is not None:
                    input_item = WaterTestInputItem(
                        contaminant_name=contaminant,
                        measuring_unit=str(row["Unit"])
                    )
                    self.form_container.add_widget(input_item)
                    self.contaminant_entries.update({contaminant: input_item})

        
    def clear_form(self):
        for input_item in self.contaminant_entries.values():
            self.form_container.remove_widget(input_item)
            print("removing: ", input_item)
            
        self.contaminant_entries.clear()
    
    
    def submit_water_test(self):
        user_results_df = get_contaminant_dataframe()
        user_results_df["Exceeds"] = -1
        
        for contaminant, input_item in self.contaminant_entries.items():
            row = user_results_df.loc[contaminant]
            try:
                user_level = float(input_item.level_input_text)
            except ValueError as e:
                print("Error reading input: ", e)
                continue
                           
            if row is not None:
                mcl = float(row["Maximum Contaminant Level (MCL)"])
                mclg = float(row["Maximum Contaminant Level Goal (MCLG)"])
                try:
                    if user_level > mcl:
                        message = f"Exceeded"
                        user_results_df.loc[contaminant, "Exceeds"] = 2
                    elif user_level > mclg:
                        user_results_df.loc[contaminant, "Exceeds"] = 1
                    else:
                        user_results_df.loc[contaminant, "Exceeds"] = 0
                    message = "Entered " + contaminant
                except ValueError as e:
                    message = "Invalid: " + str(e)
            else:
                message = "Not found"
            print(message)

        user_results_df.to_excel(fr"{os.curdir}/resources/user/test_results_{datetime.date.today()}_{time.time()}.xlsx")
        user_scores = get_weighted_contaminant_score(user_results_df)
        
        user_data = get_user_data()
        with open(USER_DATA_FILE, "w") as file:
            user_data["water_tests"] = user_data["water_tests"] + {"date": datetime.date.today(), "scores": user_scores}
            json.dump(user_data, file)


class WaterTestInputItem(BoxLayout):
    contaminant_name = StringProperty("")
    measuring_unit = StringProperty("")
    level_input_text = StringProperty("0")
    
    def __init__(self, contaminant_name, measuring_unit, **kwargs):
        super(WaterTestInputItem, self).__init__(**kwargs)
        self.contaminant_name = contaminant_name
        self.measuring_unit = measuring_unit


class WaterContaminantSelectionScreen(Screen):
    selection_form = ObjectProperty(None)
    
    def on_pre_enter(self):
        if self.selection_form.form_created is False:
            self.selection_form.create_form()
        self.selection_form.clear_form()
    
    def process_contaminant_selections(self, selection_form):
        selected = dict()
        for contaminant, selection_item in selection_form.contaminant_selections.items():
            selected.update({contaminant : selection_item.is_selected})
        
        self.manager.get_screen("watertestinput_screen").create_water_test_form(selected)


class WaterContaminantSelectionForm(BoxLayout):
    contaminant_selections = {}
    form_container = ObjectProperty(None)
    form_created = False
        
    def __init__(self, **kwargs):
        super(WaterContaminantSelectionForm, self).__init__(**kwargs)
        
    def create_form(self):
        contaminant_df = get_contaminant_dataframe()
        for contaminant in contaminant_df.index:
            select_item = ContaminantSelectableItem(str(contaminant))
            self.form_container.add_widget(select_item)
            self.contaminant_selections.update({str(contaminant): select_item})
        self.form_created = True
    
    def clear_form(self):
        for selection_item in self.contaminant_selections.values():
            selection_item.check_box.active = False
            selection_item.is_selected = False


class ContaminantSelectableItem(BoxLayout):
    contaminant_text = StringProperty("Default Contaminant")
    is_selected = BooleanProperty(False)
    check_box = ObjectProperty(None)
    
    def __init__(self, contaminant, **kwargs):
        super(ContaminantSelectableItem, self).__init__(**kwargs)
        self.contaminant_text = contaminant
    

class WaterTestResultsScreen(Screen):
    pass


class WaterTestResultsWidget(BoxLayout):
    pass
        
        