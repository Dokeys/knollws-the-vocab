import tkinter
from tkinter import ttk
from typing import Callable

from view.settings.view_settings_frame import ViewSettingsFrame
from view.settings.vocable_picker_settings_frame import VocablePickerSettingsFrame
from view.settings.sound_settings_frame import SoundSettingsFrame
from model.settings import Settings


class SettingsFrame(tkinter.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        # setup style
        style = ttk.Style()
        style.configure("TButton", font=("calibri", 18, "bold"), borderwidth="4")
        style.configure("TLabel", font=("calibri", 20, "bold"), borderwidth="4")
        # Settings label
        self.lbl_settings = ttk.Label(self)
        self.lbl_settings.config(text="Settings")
        self.lbl_settings.pack()
        self.view_settings_frame = ViewSettingsFrame(self)
        self.view_settings_frame.pack(anchor="w")
        # vocable picker settings
        self.vocable_picker_settings_frame = VocablePickerSettingsFrame(self)
        self.vocable_picker_settings_frame.pack(anchor="w")
        # sound settings
        self.sound_settings_frame = SoundSettingsFrame(self)
        self.sound_settings_frame.pack(anchor="w")

        self.btn_back = ttk.Button(self, text="Back")
        self.btn_back.pack(anchor="s")

    def bind_back_button_clicked(
        self, callback: Callable[[tkinter.Event], None]
    ) -> None:
        self.btn_back.config(command=callback)

    def _back_clicked(self) -> None:
        print("back in settings clicked")
