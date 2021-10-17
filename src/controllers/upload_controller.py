from .mixins import Navigation
from tkinter.ttk import Widget
from models.upload_model import UploadModel


class Controller(Navigation):

    def __init__(self):
        super().__init__()

    def preview_file(self, view: Widget):
        model = self.extract_form_data(view)
        print(model)

    def upload_file(self, view: Widget):
        print("uploading file...")

    def extract_form_data(self, view: Widget) -> UploadModel:
        """Extracts form data and returns an instance of the 
        `UploadModel` data class"""
        title = view.getvar('title')
        description = view.getvar('description')
        transcript = view.getvar('transcript')
        username = view.getvar('username')
        password = view.getvar('password')

        model = UploadModel(
            title=title,
            description=description,
            transcript=transcript,
            username=username,
            password=password
        )
        return model
