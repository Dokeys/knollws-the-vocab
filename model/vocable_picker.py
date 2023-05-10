"""
vocable_picker.py

Created on: 10.05.2023
Author: Dominik Knoll

Description:
The VocablePicker is the model part of the program. This part of the program is 
responsible for everything to do with vocabluary. Everything what have to do with
loading a dicitionary, checking the user input vocables and choosing the next 
vocable should be placed here.
"""
import random

from model.current_dictionary import CurrentDictionary
from model.current_vocable import CurrentVocable
from model.vocable import Vocable
import model.response as response
import view.text_adjustments as text_adjustments


class VocablePicker:
    CurrentDictionary()  # creates Singleton
    CurrentVocable()  # creates Singleton

    def __init__(self, dictionary_path: str = None) -> None:
        if dictionary_path != None:
            self.set_new_dictionary(dictionary_path)

    @staticmethod
    def set_new_dictionary(path: str) -> None:
        """
        set up a new CurrentDictionary with a file path.
        """
        dictionary = CurrentDictionary.get_instance()
        dictionary.read_dictionary(path)

    def set_new_vocable(self) -> None:
        """
        set a new CurrentVocable from CurrentDictionary.
        """
        dictionary = CurrentDictionary.get_instance()
        current_vocable = CurrentVocable.get_instance()

        if len(dictionary.vocables) == 0:
            raise Exception("no vocables inside dictionary")
        vocable = self.random_vocable_mechanism()
        current_vocable.set_vocable(vocable)

    @staticmethod
    def get_untranslated_words() -> list[str]:
        """
        returns a list of string from CurrentVocable.
        @return string list with untranslated words.
        """
        current_vocable = CurrentVocable.get_instance()
        return current_vocable.native

    @staticmethod
    def vocable_input(input: str) -> response.Response:
        """
        checks if the input sring matches to one word of the trantslated words
        @return bool True when input was right
        """
        res = response.Response()
        current_vocable = CurrentVocable.get_instance()

        if input in current_vocable.foreign:
            res.is_right = True
            res.response = VocablePicker._get_right_input_string(input)
            res.additional_info = VocablePicker._get_additional_info_string(input)
        else:
            res.is_right = False
            res.response = VocablePicker._get_wrong_input_string(input)
            res.additional_info = ""

        return res

    @staticmethod
    def random_vocable_mechanism() -> Vocable:
        """
        picks a random vocable from CurrentDictionary.
        """
        dictionary = CurrentDictionary.get_instance()
        random_index_int = random.randint(0, len(dictionary.vocables) - 1)
        return dictionary.vocables[random_index_int]

    @staticmethod
    def _get_right_input_string(input: str) -> str:
        current_vocable = CurrentVocable.get_instance()
        return f"Richtig: {input} für {text_adjustments.get_words_string_with_comma(current_vocable.native)} war richtig"

    @staticmethod
    def _get_wrong_input_string(input: str) -> str:
        current_vocable = CurrentVocable.get_instance()
        response_string = f"Falsch: {text_adjustments.get_words_string_with_comma(current_vocable.native)}"
        response_string += f" = {text_adjustments.get_words_string_with_comma(current_vocable.foreign)}"
        if input != "":
            response_string += f", nicht {input}."

        return response_string

    @staticmethod
    def _get_additional_info_string(input: str) -> str:
        current_vocable = CurrentVocable.get_instance()

        if len(current_vocable.foreign) == 1:
            return ""
        # if there are more than one correct answer possibility's
        response_string = "Alternative: "
        # filter out word that user has entered
        alternative_words = list(set(current_vocable.foreign).difference(set([input])))
        response_string += text_adjustments.get_words_string_with_comma(
            alternative_words
        )

        return response_string
