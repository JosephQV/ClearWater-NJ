from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty


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
        

# These classes represent Screens that would be navigated to from the communication
# screen for different topics of feedback. For now there is just this one as a
# placeholder / example.
class TapWaterFeedbackScreen(Screen):
    pass

    
class EmailScreen(Screen):
    recipient = "default recipient (placeholder)"
    email_body_text = StringProperty("Default email body (placeholder)")
    
    
    def test_submit(self):
        # placeholder function to demonstrate calling a function upon clicking a
        # button in the form
        # print attribute values
        print(self.recipient)
        print(self.email_body_text)
        self.email_body_text = "Submitted"