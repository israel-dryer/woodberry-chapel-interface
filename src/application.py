import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from views.upload_view import UploadView
from views.home_view import HomeView
from views.help_view import HelpView


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.style = Style()
        self.style.theme_use('sandstone')
        self.title('Woodberry Chapel Interface')
        self.minsize(height=530, width=1180)
        header = self.create_header()
        header.pack(side=tk.TOP, fill=tk.X)
        self.body = ttk.Frame(self)
        self.body.pack(fill=tk.BOTH, expand=tk.YES)

        # add views
        self.help_view = HelpView(self.body)
        self.upload_view = UploadView(self.body)
        self.home_view = HomeView(self.body)
        self.home_view.pack(pady=10, fill=tk.BOTH, expand=tk.YES)

    def create_header(self):
        frame = ttk.Frame(self, padding=10)
        letter = ttk.Label(
            master=frame,
            text='W',
            font=("French Script MT", 40, "bold"),
            style='warning.TLabel'
        )
        letter.pack(side=tk.LEFT, padx=5)
        header = ttk.Label(
            master=frame,
            text='Woodberry Chapel Interface',
            font=("Helvetica", 30)
        )
        header.pack(side=tk.LEFT)

        # navigate to home when clicking the letter
        letter.bind('<Button-1>', self.navigate_to_home)

        return frame

    def navigate_to_home(self, *_):

        if self.home_view.winfo_ismapped():
            return

        for view in [self.upload_view, self.help_view]:
            if view.winfo_ismapped():
                view.pack_forget()

        self.home_view.pack(pady=10, fill=tk.BOTH, expand=tk.YES)
        self.update_idletasks()


if __name__ == '__main__':

    app = Application()
    app.mainloop()
