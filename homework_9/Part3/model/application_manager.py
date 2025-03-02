from homework_9.Part3.model.pages.left_panel import LeftPanel
from homework_9.Part3.model.pages.text_box_page import TextBoxPage
from homework_9.Part3.model.pages.practice_form_page import PracticeFormPage

class ApplicationManager:
    def __init__(self):
        self.left_panel = LeftPanel()
        self.text_box_page = TextBoxPage()
        self.practice_form_page = PracticeFormPage()