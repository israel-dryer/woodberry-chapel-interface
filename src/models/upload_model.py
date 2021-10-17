from dataclasses import dataclass


@dataclass
class UploadModel:
    """Class for tracking an upload instance"""

    title: str
    description: str
    transcript: str
    username: str
    password: str
