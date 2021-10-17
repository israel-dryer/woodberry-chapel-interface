import tkinter as tk
from tkinter import ttk
from controllers.home_controller import Controller


class HomeView(ttk.Frame):

    def __init__(self, master, **kwargs):
        kwargs.update(name='home-view')
        super().__init__(master, **kwargs)
        self.urls = {
            'youtube': 'https://www.youtube.com',
            'google sheets': 'https://www.google.com',
            'github': 'https://www.github.com',
        }
        self.controller = Controller()
        self.create_view()

    def create_view(self):
        self.configure(padding=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # youtube link
        yt_button = ttk.Button(
            master=self,
            text='YouTube',
            command=lambda: self.controller.navigate_to_url(
                self.urls['youtube']),
        )
        yt_button.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)

        # google sheets link
        gs_button = ttk.Button(
            master=self,
            text='Google Sheets',
            command=lambda: self.controller.navigate_to_url(
                self.urls['google sheets']),
        )
        gs_button.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        # github link
        gh_button = ttk.Button(
            master=self,
            text='Github',
            command=lambda: self.controller.navigate_to_url(
                self.urls['github']),
        )
        gh_button.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)

        # help view link
        hv_button = ttk.Button(
            master=self,
            text='Help',
            command=lambda: self.controller.navigate_to_view(
                self, 'help-view')
        )
        hv_button.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)

        # begin upload process
        upload_btn = ttk.Button(
            master=self,
            text='BEGIN\nUPLOADING\nPROCESS',
            command=lambda: self.controller.navigate_to_view(
                self, 'upload-view')
        )
        upload_btn.grid(row=0, column=2, rowspan=2,
                        sticky=tk.NSEW, padx=5, pady=5)
