from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty

import webbrowser
from urllib.parse import quote


# This class is the main screen reached when navigating to a "communication" or "feedback"
# menu within the app
class CommunicationScreen(Screen):
    pass


# This class defines a widget we will use on the commmunication screen to contain a
# menu of different choices for topics of feedback.
class FeedbackNavigationMenu(BoxLayout):
    pass
        

class FeedbackMenuItem(Button):
    button_text = StringProperty("")          # text displayed for this option
    screen = StringProperty("")  # screen name to navigate to when clicked
    
class EmailScreen(Screen):
    recipient = StringProperty("default recipient (placeholder)")
    email_subject_text = StringProperty("Default email subject (placeholder)")
    email_body_text = StringProperty("Default email body (placeholder)")
    
    def submit_email(self):
        print(self.recipient)
        print(self.email_subject_text)
        print(self.email_body_text)
        
        self.email_body_text = "Submitted" # Visual confirmation
        
        mailto_link = f"mailto:{self.recipient}?subject={quote(self.email_subject_text)}&body={quote(self.email_body_text)}"
        print(mailto_link)
        webbrowser.open(mailto_link)
        
        
# These classes represent Screens that are navigated to from the communication
# screen for different topics of feedback.
class TapWaterFeedbackScreen(Screen):
    testkitslink = "https://thewatershed.org/tapwatch"
    checkpipeslink = "https://www.nj.gov/dep/watersupply/dwc-lead-consumer.html"
    njdepcomplaintlink = "https://www.nj.gov/dep/watersupply/pwq-complaint.html"
    
    def open_link(self, link):
        webbrowser.open(link)

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
