"""
current_dictionary.py

Created on: 10.0.2023
Author: Dominik Knoll

Description:
CurrentDictionary is a Singleton what inherits everything form the Dictionary class.
In this class the current dictionary of the program is saved.
"""
from model.dictionary import Dictionary


class CurrentDictionary(Dictionary):
    __instance = None

    def __init__(self, dictionary_file_path: str = None) -> None:
        if CurrentDictionary.__instance != None:
            raise Exception("CurrentDictionary is a singleton.")
        super().__init__(dictionary_file_path)
        CurrentDictionary.__instance = self

    @staticmethod
    def get_instance() -> None:
        if CurrentDictionary.__instance == None:
            return CurrentDictionary()
        return CurrentDictionary.__instance
