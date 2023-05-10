"""
controller.py

Created on: 10.05.2023
Author: Dominik Knoll

Description:
TODO add a description and clarify the main part of this module

"""
from model.vocable_picker import VocablePicker
from view.ui import UI

import view.text_adjustments as text_adjustments
from model.tip import Tip


class Controller:
    def __init__(self, model: VocablePicker, view: UI) -> None:
        self.model = model
        self.view = view
        view.bind_user_input(self.user_input)
        view.bind_tip(self.tip)
        self.model.set_new_dictionary("./dictionarys/Vocablen.csv")
        self._set_untranslated_words()

    def user_input(self, event=None) -> None:
        self.view.set_input_response()
        self.view.clear_entry()
        self.model.set_new_vocable()
        Tip.reset_tip()
        self._set_untranslated_words()

    def tip(self, event=None) -> None:
        tip_string = Tip.get_tip_string()
        self.view.set_tip_text(tip_string)

    def _set_untranslated_words(self) -> None:
        self.model.set_new_vocable()
        untranslated_words = self.model.get_untranslated_words()
        untranslated_words_string = text_adjustments.get_words_string_with_comma(
            untranslated_words
        )
        self.view.set_untranslated_words_text(untranslated_words_string)

    def run(self) -> None:
        self.view.mainloop()
