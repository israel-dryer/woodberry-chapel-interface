import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from controllers.upload_controller import Controller


class UploadView(ttk.Frame):

    def __init__(self, master, **kwargs):
        kwargs.update(name='upload-view')
        super().__init__(master, **kwargs)
        self.controller = Controller()
        self.create_view()

    def create_view(self):

        self.configure(padding=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create form variables
        self.setvar('title', '')
        self.setvar('description', '')
        self.setvar('transcript', '')
        self.setvar('username', '')
        self.setvar('password', '')

        # title
        title_lbl = ttk.Label(
            master=self,
            text='Title',
            font='-weight bold'
        )
        title_lbl.grid(row=0, column=0, sticky=tk.W)

        title_entry = ttk.Entry(
            master=self,
            textvariable='title'
        )
        title_entry.grid(row=1, column=0, sticky=tk.EW, padx=(0, 5),
                         pady=(0, 15))

        # description
        desc_lbl = ttk.Label(
            master=self,
            text='Description',
            font='-weight bold'
        )
        desc_lbl.grid(row=2, column=0, sticky=tk.W)

        desc_entry = ttk.Entry(
            master=self,
            textvariable='description'
        )
        desc_entry.grid(row=3, column=0, sticky=tk.EW, padx=(0, 5),
                        pady=(0, 15))

        # transcript
        transcript = ttk.Label(
            master=self,
            text='Transcript (Only for Website)',
            font='-weight bold'
        )
        transcript.grid(row=4, column=0, sticky=tk.W)

        transcript_entry = ttk.Entry(
            master=self,
            textvariable='transcript'
        )
        transcript_entry.grid(row=5, column=0, sticky=tk.EW, padx=(0, 5),
                              pady=(0, 15))

        # username
        username_lbl = ttk.Label(
            master=self,
            text='Username',
            font='-weight bold'
        )
        username_lbl.grid(row=6, column=0, sticky=tk.W)

        username_entry = ttk.Entry(
            master=self,
            textvariable='username',
        )
        username_entry.grid(row=7, column=0, sticky=tk.EW, padx=(0, 5),
                            pady=(0, 15))

        # password
        password_lbl = ttk.Label(
            master=self,
            text='Password',
            font='-weight bold'
        )
        password_lbl.grid(row=8, column=0, sticky=tk.W)

        password_entry = ttk.Entry(
            master=self,
            textvariable='password',
            show='*'
        )
        password_entry.grid(row=9, column=0, sticky=tk.EW, padx=(0, 5),
                            pady=(0, 15))

        file_preview = ttk.Button(
            master=self,
            text='File Preview',
            command=lambda: self.controller.preview_file(self)
        )
        file_preview.grid(column=1, row=0, rowspan=5, sticky=tk.NSEW,
                          padx=(5, 0), pady=(0, 15))

        upload_file = ttk.Button(
            master=self,
            text='Upload',
            command=lambda: self.controller.upload_file(self)
        )
        upload_file.grid(column=1, row=5, rowspan=5, sticky=tk.NSEW,
                         padx=(5, 0), pady=(0, 15))
