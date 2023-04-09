import tkinter
from tkinter import ttk

from model.settings import Settings


class ViewSettingsFrame(tkinter.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        # view labels
        self.lbl_view = ttk.Label(self, text="View:", font=("calimbri", 14))
        self.lbl_view.pack(anchor="w")
        # checkbutton for transparent background
        self.transparent_background = tkinter.BooleanVar()
        self.chbx_transparent_background = ttk.Checkbutton(
            self,
            text="transparent background",
            variable=self.transparent_background,
            command=self.transparent_background_changed,
        )
        self.chbx_transparent_background.pack(anchor="w")

    def transparent_background_changed(self) -> None:
        Settings.set_transparent_background(self.transparent_background.get())
