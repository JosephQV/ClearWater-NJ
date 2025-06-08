import webbrowser
from urllib.parse import quote


class CommunicationController:
    pass


class EmailController:
    recipient = ""
    email_subject_text = ""
    email_body_text = ""

    def submit_email(self):   
        self.email_body_text = "Submitted" # Visual confirmatiom
        mailto_link = f"mailto:{self.recipient}?subject={quote(self.email_subject_text)}&body={quote(self.email_body_text)}"
        print(mailto_link)
        webbrowser.open(mailto_link)
        
        
class TapWaterFeedbackController:
    def open_link(self, link):
        webbrowser.open(link)