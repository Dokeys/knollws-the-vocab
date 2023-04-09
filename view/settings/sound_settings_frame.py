import tkinter
from tkinter import ttk

from model.settings import Settings


class SoundSettingsFrame(tkinter.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.lbl_sound_settings = ttk.Label(self, text="Sound:", font=("calimbri", 14))
        self.lbl_sound_settings.pack(anchor="w")

        self.fail_sound = tkinter.BooleanVar()
        self.fail_sound.set(Settings.get_fail_sound())
        self.chbx_fail_sound = ttk.Checkbutton(
            self,
            text="fail sound",
            variable=self.fail_sound,
            command=self.fail_sound_changed,
        )
        self.chbx_fail_sound.pack(anchor="w")

        self.fail_reader = tkinter.BooleanVar()
        self.fail_reader.set(Settings.get_fail_sound())
        self.chbx_fail_reader = ttk.Checkbutton(
            self,
            text="fail reader",
            variable=self.fail_reader,
            command=self.fail_reader_changed,
        )
        self.chbx_fail_reader.pack(anchor="w")

    def fail_sound_changed(self) -> None:
        Settings.set_fail_sound(self.fail_sound.get())

    def fail_reader_changed(self) -> None:
        Settings.set_fail_reader(self.fail_reader.get())
