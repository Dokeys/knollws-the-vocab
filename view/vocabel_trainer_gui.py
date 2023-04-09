import os
import threading
import tkinter
from tkinter import ttk
from typing import Callable

import simpleaudio
import pyttsx3

from view.input_output_frame import InputOutputFrame
from view.settings.settings_frame import SettingsFrame
from view.menubar import MenuBar
from model.vocable_picker import VocablePicker
from view.ui import UI
import version
from model.settings import Settings
from model.tip import Tip


class VocabelTrainerGui(tkinter.Tk, UI):
    def __init__(self, model: VocablePicker) -> None:
        super().__init__()
        self.model = model
        self.title(f"Knollws the Vocab {version.Version.get_version_string()}")
        self.geometry("600x180")
        self.iconbitmap("./files/logo.ico")
        Settings.bind_transparent_background_changed(self.set_transparent_background)

        self.fail_sound = simpleaudio.WaveObject.from_wave_file(
            "./files/sounds/fail.wav"
        )
        self.speech_engine = pyttsx3.init()

        self.menubar = MenuBar(self)
        self.menubar.bind_settings_clicked(self.show_settings_frame)
        self.config(menu=self.menubar)
        self.input_output_frame = InputOutputFrame(self)
        self.settings_frame = SettingsFrame(self)
        self.settings_frame.bind_back_button_clicked(self.show_input_output_frame)
        self.show_input_output_frame()

    def show_input_output_frame(self, event=None) -> None:
        self.settings_frame.pack_forget()
        self.input_output_frame.pack(fill=tkinter.BOTH, expand=True)
        self.input_output_frame.update()

    def show_settings_frame(self) -> None:
        self.input_output_frame.pack_forget()
        self.settings_frame.pack(fill="both", expand=True, padx=100)
        self.update()
        # ToDo
        print(f"{self.winfo_width()}x{self.settings_frame.winfo_height()}")
        self.geometry(f"{self.winfo_width()}x{self.settings_frame.winfo_height()}")

    # ToDo
    def bind_user_input(self, callback: Callable[[tkinter.Event], None]) -> None:
        self.input_output_frame.txt_entry_field.bind("<Return>", callback)

    # ToDo
    def bind_tip(self, callback: Callable[[tkinter.Event], None]) -> None:
        self.input_output_frame.txt_entry_field.bind("<Control_L>", callback)

    def set_transparent_background(self, state: bool) -> None:
        if state:
            self.attributes("-alpha", 0.8)
            self.attributes("-transparentcolor", "red")
            self.config(background="red")
            self.input_output_frame.config(background="red")
        else:
            self.attributes("-alpha", 1)
            self.config(background=Settings.get_background_color())
            self.input_output_frame.config(background=Settings.get_background_color())

    def set_untranslated_words_text(self, untranslated_words_string: str) -> None:
        self.input_output_frame.set_untranslated_words(untranslated_words_string)

    def get_entry_text(self) -> str:
        return self.input_output_frame.get_entry_field_text()

    def clear_entry(self) -> None:
        self.input_output_frame.clear_entry_field()

    def set_input_response(self) -> None:
        user_input = self.get_entry_text()
        response = self.model.vocable_input(user_input)

        self.input_output_frame.set_response_text(response)
        self.input_output_frame.set_info_text(response.additional_info)
        if not response.is_right and Settings.get_fail_sound():
            self.fail_sound.play()
        if (
            not response.is_right
            or Tip.was_tip_requested()
            and Settings.get_fail_reader()
        ):
            self.speech_engine.say(response.response)
            try:
                thread = threading.Thread(target=self.speech_engine.runAndWait)
                thread.start()
            except:
                print("run loop already started")

    def set_tip_text(self, tip_string: str) -> None:
        self.input_output_frame.set_info_text(tip_string)
