from .mixins import Navigation
from tkinter.filedialog import askopenfilename


class Controller(Navigation):

    def __init__(self):
        super().__init__()

    def transcribe_data(self, view):
        filename = askopenfilename()
        # add transcribe logic here
        transcribed_data = filename ## put actual here
        view.setvar('transcript', transcribed_data)
        self.navigate_to_view(view, 'upload-view')
