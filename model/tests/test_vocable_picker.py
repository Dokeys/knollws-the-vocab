import pytest

from model.vocable_picker import *

TEST_DICTIONARY_PATH = "model/tests/test_dictionarys/test.csv"
TEST_DICTIONARY_EMPTY_PATH = "model/tests/test_dictionarys/test_empty_dictionary.csv"
TEST_DICTIONARY_SMALL = "model/tests/test_dictionarys/small_test_dictionary.csv"

vocablepicker = VocablePicker(TEST_DICTIONARY_EMPTY_PATH)


def test_get_new_vocable_empty_dictionary() -> None:
    vocablepicker.set_new_dictionary(TEST_DICTIONARY_EMPTY_PATH)
    # test when dictionary is empty
    with pytest.raises(Exception):
        # when no dictionary is open
        vocablepicker.get_new_vocable()
    # when the csv file has no vocables
    vocablepicker.set_new_dictionary(TEST_DICTIONARY_EMPTY_PATH)
    with pytest.raises(Exception):
        vocablepicker.get_new_vocable()


def test_is_vocable_input_right() -> None:
    vocablepicker.set_new_dictionary(TEST_DICTIONARY_SMALL)
    vocablepicker.set_new_vocable()

    untransladed_word = vocablepicker.get_untranslated_words()

    if "ein Wort" in untransladed_word:
        assert vocablepicker.vocable_input("a word")
    if "zwei" in untransladed_word:
        assert vocablepicker.vocable_input("two")
