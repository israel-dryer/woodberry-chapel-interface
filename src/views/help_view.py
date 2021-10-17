import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from controllers.help_controller import Controller


class HelpView(ttk.Frame):

    def __init__(self, master, **kwargs):
        kwargs.update(name='help-view')
        ttk.Frame.__init__(self, master, **kwargs)
        self.controller = Controller()
        self.create_view()

    def create_view(self):

        self.configure(padding=10)

        Font(
            name='header-font',
            family='Helvetica',
            size=14,
            weight='bold'
        )

        header_left = ttk.Label(
            master=self,
            text='Contact Info of Creators',
            font='header-font'
        )
        header_left.grid(row=0, column=0, sticky=tk.W)

        text_left = tk.Text(master=self)
        text_left.grid(row=1, column=0, sticky=tk.NSEW)

        header_right = ttk.Label(
            master=self,
            text='Alternatives to UI',
            font='header-font'
        )
        header_right.grid(row=0, column=1, sticky=tk.W, padx=5)

        text_right = tk.Text(master=self)
        text_right.grid(row=1, column=1, sticky=tk.NSEW, padx=5)
