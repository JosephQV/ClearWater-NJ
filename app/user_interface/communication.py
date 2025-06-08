from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.app import App

from app.interface_controllers.communication_controller import CommunicationController, EmailController, TapWaterFeedbackController
from data.text_and_translation import APP_TEXT
from data.app_config import IMAGES

import os


Builder.load_file(f"{os.path.dirname(os.path.abspath(__file__))}/communication.kv")


# This class is the main screen reached when navigating to a "communication" or "feedback"
# menu within the app
class CommunicationScreen(Screen):
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = CommunicationController()
        
    def get_feedback_navigation_items(self):
        app = App.get_running_app()
        lang = app.user_controller.get_language() if app is not None else "en"
        items = [
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["tapwaterfeedback"][lang],
                "target_screen": "tapwaterfeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["waterbillfeedback"][lang],
                "target_screen": "waterbillfeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["homepipesfeedback"][lang],
                "target_screen": "homepipesfeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["stateinfrastructurefeedback"][lang],
                "target_screen": "stateinfrastructurefeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["surfacewaterfeedback"][lang],
                "target_screen": "surfacewaterfeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["pollutionfeedback"][lang],
                "target_screen": "pollutionfeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["floodingfeedback"][lang],
                "target_screen": "floodingfeedback_screen"
            },
            {
                "type": "image",
                "image_source": IMAGES["app"],
                "caption": APP_TEXT["communication_screen"]["watershedfeedback"][lang],
                "target_screen": "watershedfeedback_screen"
            },
        ]
        return items


class EmailScreen(Screen):
    controller = ObjectProperty(None)
    recipient = StringProperty("default recipient (placeholder)")
    email_subject_text = StringProperty("Default email subject (placeholder)")
    email_body_text = StringProperty("Default email body (placeholder)")
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = EmailController()
        
    def get_email_form_items(self):
        pass
    
        
# These classes represent Screens that are navigated to from the communication
# screen for different topics of feedback.
class TapWaterFeedbackScreen(Screen):
    testkitslink = "https://thewatershed.org/tapwatch"
    checkpipeslink = "https://www.nj.gov/dep/watersupply/dwc-lead-consumer.html"
    njdepcomplaintlink = "https://www.nj.gov/dep/watersupply/pwq-complaint.html"
    controller = ObjectProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = TapWaterFeedbackController()
        

class WaterBillFeedbackScreen(Screen):
    pass


class HomePipesFeedbackScreen(Screen):
    pass


class StateInfrastructureFeedbackScreen(Screen):
    pass


class SurfaceWaterFeedbackScreen(Screen):
    pass


class PollutionFeedbackScreen(Screen):
    pass


class FloodingFeedbackScreen(Screen):
    pass


class WatershedFeedbackScreen(Screen):
    pass
