from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.clock import Clock
import logging
import os


logger = logging.getLogger(__name__)

Builder.load_file(os.path.join(os.path.dirname(__file__), "form_widgets.kv"))


class LabeledNumericInput(BoxLayout):
    label_text = StringProperty("Label:")
    input_value = NumericProperty(0)
    value_bounds = ListProperty([float('-inf'), float('inf')])

    def check_for_valid_input(self):
        try:
            value = float(self.ids.input.text)
            if not (self.value_bounds[0] <= value <= self.value_bounds[1]):
                logger.info(f"Input out of bounds: {value}")
                return False
            self.input_value = value
            return True
        except ValueError:
            logger.info("Invalid numeric input")
            return False


class LabeledTextInput(BoxLayout):
    label_text = StringProperty("Label:")
    input_value = StringProperty("")

    def check_for_valid_input(self):
        text = self.ids.input.text.strip()
        if not text:
            logger.info("Empty text input")
            return False
        self.input_value = text
        return True


class LabeledDropdown(BoxLayout):
    label_text = StringProperty("Label:")
    options = ListProperty([])
    input_value = StringProperty("")

    def check_for_valid_input(self):
        selected = self.ids.dropdown.text
        if selected not in self.options:
            logger.info("Invalid dropdown selection")
            return False
        self.input_value = selected
        return True


class LabeledCheckbox(BoxLayout):
    label_text = StringProperty("Check:")
    input_value = BooleanProperty(False)
    required = BooleanProperty(False)

    def check_for_valid_input(self):
        if self.required and not self.input_value:
            return False
        return True


class Form(ScrollView):
    form_items = ListProperty([])
    layout = ObjectProperty(None)
    post_submit_function = ObjectProperty(lambda form_data: None)
    next_screen = StringProperty("")
    instruction_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._initialize_layout)

    def _initialize_layout(self, dt):
        if self.form_items:
            self.fill_form()

    def fill_form(self, *args):
        if not self.layout:
            logger.warning("Form layout container not initialized.")
            return

        self.layout.clear_widgets()
        for widget in self._create_widgets_from_items(self.form_items):
            self.layout.add_widget(widget)

    def _create_widgets_from_items(self, items):
        widget_map = {
            "Text": LabeledTextInput,
            "Numeric": LabeledNumericInput,
            "Dropdown": LabeledDropdown,
            "Checkbox": LabeledCheckbox,
        }

        widgets = []
        for i, item in enumerate(items):
            try:
                widget_type = item.get("type")
                widget_cls = widget_map.get(widget_type)
                if not widget_cls:
                    raise ValueError(f"Unsupported widget type: {widget_type}")
                kwargs = {k: v for k, v in item.items() if k != "type"}
                widget = widget_cls(**kwargs)
                widgets.append(widget)
            except Exception as e:
                logger.error(f"Error initializing form widget #{i}: {e}")
        
        validation_label = self.ids.get("validation_label")
        if validation_label:
            validation_label.text = ""  # reset message
        
        return widgets

    def submit_form(self, screen_manager):
        form_data = {}
        first_invalid = None
        validation_label = self.ids.get("validation_label")

        if validation_label:
            validation_label.text = ""  # reset message

        for widget in reversed(self.layout.children):  # reversed to preserve visual order
            valid = widget.check_for_valid_input() if hasattr(widget, 'check_for_valid_input') else True

            # Reset any previous background color
            if hasattr(widget, 'ids') and 'input' in widget.ids:
                widget.ids.input.background_color = [1, 1, 1, 1]
            elif hasattr(widget, 'ids') and 'dropdown' in widget.ids:
                widget.ids.dropdown.background_color = [1, 1, 1, 1]

            if not valid:
                if hasattr(widget, 'ids'):
                    if 'input' in widget.ids:
                        widget.ids.input.background_color = [1, 0.8, 0.8, 1]  # light red
                        widget.ids.input.focus = True
                    elif 'dropdown' in widget.ids:
                        widget.ids.dropdown.background_color = [1, 0.8, 0.8, 1]
                if not first_invalid:
                    first_invalid = widget
                continue

            form_data[widget.label_text] = widget.input_value

        if first_invalid:
            if validation_label:
                validation_label.text = "Please correct highlighted fields."
            return
        
        self.post_submit_function(form_data)

        # Optional: switch screens
        if self.next_screen:
            screen_manager.switch_screens(self.next_screen)