from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


# This class is the main screen reached when navigating to a "communication" or "feedback"
# menu within the app
class CommunicationScreen(Screen):
    pass


# This class defines a widget we will use on the commmunication screen to contain a
# menu of different choices for topics of feedback.
class FeedbackNavigationMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(FeedbackNavigationMenu, self).__init__(**kwargs)
        

# These classes represent Screens that would be navigated to from the communication
# screen for different topics of feedback. For now there is just this one as a
# placeholder / example.
class TapWaterFeedbackScreen(Screen):
    pass

    
    