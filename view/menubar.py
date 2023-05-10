"""
menubar.py

Created on: 10.05.2023
Author: Dominik Knoll

Description:
This contains everything for the menubar on the top of the vocabel_trainer_gui. 
With the menubar it is possible to load another dictionary, change the searched language, 
open the settings or exit the program.
"""
from tkinter import filedialog
import tkinter
from typing import Callable


class MenuBar(tkinter.Menu):
    def __init__(self, master) -> None:
        super().__init__(master)
        # Options Menuebar
        self.options_bar = tkinter.Menu(self, tearoff=False, font=("Arial", 14))
        # -> Open dictionary
        self.options_bar.add_command(
            label="Open dictionary", command=self._open_dictionary_clicked
        )
        # -> Searched language
        self.selected_language = tkinter.IntVar()
        self.selected_language.set(1)  # TODO Not so nice
        self.searched_language_bar = tkinter.Menu(
            self, tearoff=False, font=("Arial", 14)
        )
        # ->-> German radiobutton
        self.searched_language_bar.add_radiobutton(
            label="-",
            command=self._switch_language,
            variable=self.selected_language,
            value=0,
        )
        # ->-> English radiobutton
        self.searched_language_bar.add_radiobutton(
            label="-",
            command=self._switch_language,
            variable=self.selected_language,
            value=1,
        )
        self.options_bar.add_cascade(
            label="Searched language", menu=self.searched_language_bar
        )
        # -> Settings
        self.options_bar.add_command(label="Settings")
        # -> Info
        self.options_bar.add_command(label="Info", command=self._info_clicked)

        # -> Exit
        self.options_bar.add_separator()
        self.options_bar.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="Options", menu=self.options_bar)

    def bind_settings_clicked(self, callback: Callable[[tkinter.Event], None]) -> None:
        self.options_bar.entryconfig("Settings", command=callback)

    @staticmethod
    def _open_dictionary_clicked() -> None:
        filename = filedialog.askopenfilename(
            initialdir="./data/", title="Select a dictionary CSV file"
        )
        print(filename)
        if filename != "":
            print(f"new_dictionary {filename}")
        # TODO implement the load dictionary feature

    def set_up_dictionary_language_information(self, native: str, foreign: str) -> None:
        # change select language radiobuttons
        self.searched_language_bar.entryconfig(0, label=native)
        self.searched_language_bar.entryconfig(1, label=foreign)

    #
    def _switch_language(self) -> None:
        """This method is called when the searched language radiobuttons are pushed."""
        print(f"change_searched_language {self.selected_language.get()}")

    def _settings_clicked(event=None) -> None:
        print("settings clicked")

    @staticmethod
    def _info_clicked() -> None:
        print("show_info_window")
