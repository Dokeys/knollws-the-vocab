import dataclasses
import csv
import os

from model.vocable import Vocable


class DictionaryEmptyError(Exception):
    pass


# ToDo DictionaryReader Klasse für mehr Aufteilung?


class Dictionary:
    def __init__(self, dictionary_file_path: str = None) -> None:
        self.languages: list[str] = []
        self.vocables: list[Vocable] = []
        if dictionary_file_path != None:
            self.read_dictionary(dictionary_file_path)

    def read_dictionary(self, dictionary_file_path: str) -> None:
        self._read_header_from_file(dictionary_file_path)
        self._read_vocables_from_file(dictionary_file_path)

    def _read_header_from_file(self, dictionary_file_path: str) -> None:
        """
        Reads the header from a dictionary file and sets the languages in the dictionary object.
        """
        if not isinstance(dictionary_file_path, str):
            raise TypeError("dictionary_file_path must be a string.")
        if not os.path.isfile(dictionary_file_path):
            raise FileNotFoundError(
                f"dictionary file not found: {dictionary_file_path}"
            )
        with open(dictionary_file_path, "r") as dictionary_file:
            header = dictionary_file.readline()

        try:
            with open(dictionary_file_path, "r") as dictionary_file:
                csv_reader = csv.reader(dictionary_file, delimiter=";")
                header = next(csv_reader)
        except IOError as e:
            raise IOError(f"An error occurred while reading the dictionary file: {e}")

        if len(header) < 2:
            raise ValueError(f"Invalid header format: {header}")

        self.languages = header[:2]

    def _read_vocables_from_file(self, dictionary_file_path: str) -> None:
        if not isinstance(dictionary_file_path, str):
            raise TypeError("dictionary_file_path must be a string.")
        if not os.path.isfile(dictionary_file_path):
            raise FileNotFoundError(
                f"dictionary file not found: {dictionary_file_path}"
            )

        try:
            with open(dictionary_file_path, "r", encoding="utf-8") as dictionary_file:
                csv_reader = csv.reader(dictionary_file, delimiter=";")
                next(csv_reader)  # ignore first line
                self.vocables.clear()
                for words in csv_reader:
                    native_words = words[0].strip().split(",")
                    foreign_words = words[1].strip().split(",")

                    self.vocables.append(
                        Vocable(native=native_words, foreign=foreign_words)
                    )
        except IOError as e:
            raise IOError(f"An error occurred while reading the dictionary file: {e}")
        except csv.Error as e:
            raise csv.InvalidFileFormatError(
                f"An error occurred while parsing the dictionary file: {e}"
            )
