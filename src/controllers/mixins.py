import webbrowser
import tkinter as tk
from tkinter.ttk import Widget


class Navigation:
    """A mix-in class to enable control view and web navigation"""

    @staticmethod
    def navigate_to_url(url: str):
        """Open url in a new browser tab"""
        webbrowser.open(url, new=2)

    @staticmethod
    def navigate_to_view(current_view: Widget, target_view: str):
        current_view.pack_forget()
        target = current_view.master.nametowidget(target_view)
        target.pack(pady=10, fill=tk.BOTH, expand=tk.YES)
