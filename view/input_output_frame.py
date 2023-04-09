import tkinter
from tkinter import ttk
from typing import Protocol

import view.text_adjustments as text_adjustments

SEARCHED_WORD_UNTRANSLATED_DEFAULT_FONT_SIZE = 25
RESPONSE_TO_LAST_INPUT_DEFAULT_FONT_SIZE = 16


class ResponseInfo(Protocol):
    is_right: bool
    response: str


class InputOutputFrame(tkinter.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        # Label for searched untranslated words
        self.lbl_untranslated_words = ttk.Label(self)
        self.lbl_untranslated_words.config(
            font=("calibri", SEARCHED_WORD_UNTRANSLATED_DEFAULT_FONT_SIZE),
        )
        self.lbl_untranslated_words.pack(padx=10, pady=10)
        # Entry field for user input
        self.entry_field = tkinter.StringVar()
        self.txt_entry_field = ttk.Entry(
            self, textvariable=self.entry_field, font=("calibri", 16), justify="center"
        )
        self.txt_entry_field.pack()
        # Label contains the answer to last input
        self.lbl_response = ttk.Label(
            self,
            text="Enter correct translation",
            font=("calibri", RESPONSE_TO_LAST_INPUT_DEFAULT_FONT_SIZE),
            foreground="gray51",
        )
        self.lbl_response.pack(padx=0, pady=0)
        # Label for special infos, like other right answers or a tipp for the searched word
        self.lbl_info_field = ttk.Label(self, font=("calibri", 14), foreground="blue")
        self.lbl_info_field.pack(padx=0, pady=0)

    def set_untranslated_words(self, untranslated_words_string: str) -> None:
        self.update()
        self.lbl_untranslated_words.config(text=untranslated_words_string)
        text_adjustments.adjust_font_size_with_window_size(
            self.lbl_untranslated_words,
            SEARCHED_WORD_UNTRANSLATED_DEFAULT_FONT_SIZE,
            10,
            self.winfo_width(),
        )

    def get_entry_field_text(self) -> str:
        entry = self.entry_field.get()
        entry = entry.strip()
        return entry

    def clear_entry_field(self) -> None:
        self.entry_field.set("")

    def set_response_text(self, response: ResponseInfo) -> None:
        self.lbl_response.config(text=response.response)

        if response.is_right:
            self.lbl_response.config(foreground="green")
        else:
            self.lbl_response.config(foreground="red")

        self.update()
        text_adjustments.adjust_font_size_with_window_size(
            self.lbl_response,
            RESPONSE_TO_LAST_INPUT_DEFAULT_FONT_SIZE,
            10,
            self.winfo_width(),
        )

    def set_info_text(self, info_text: str) -> None:
        self.lbl_info_field.config(text=info_text)
