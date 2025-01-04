from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty


class WaterQualityScreen(Screen):
    nav_bar_id = ObjectProperty(None)

class WaterTestInputScreen(Screen):
    pass

class WaterContaminantSelectionScreen(Screen):
    def refresh_screen(self, selection_form):
        form_container_widget = selection_form.ids.selection_form_container
        selection_form.clear_form(form_container_widget)


class WaterTestInputForm(BoxLayout):
    def __init__(self, **kwargs):
        super(WaterTestInputForm, self).__init__(**kwargs)
        
        self.contaminant_1 = ObjectProperty(None)
        self.contaminant_2 = ObjectProperty(None)
        self.contaminant_3 = ObjectProperty(None)
        self.contaminant_4 = ObjectProperty(None)
        self.contaminant_5 = ObjectProperty(None)
        
    
    def submit_button_action(self):
        print(self.contaminant_1.text)
        print(self.contaminant_2.text)
        print(self.contaminant_3.text)
        print(self.contaminant_4.text)
        print(self.contaminant_5.text)
        
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
    
        
        