import pytest

from model.dictionary import *

TEST_DICTIONARY_PATH = "model/tests/test_dictionarys/test.csv"


def test_no_dictionary_file() -> None:
    with pytest.raises(FileNotFoundError):
        Dictionary("model/tests/not_there.dict")


def test_dictionary_language() -> None:
    test_dictionary = Dictionary(TEST_DICTIONARY_PATH)

    assert test_dictionary.languages[0] == "Deutsch", "language[0] isn't Deutsch"
    assert test_dictionary.languages[1] == "Englisch", "language[1] isn't Deutsch"


def test_read_vocables_from_file() -> None:
    test_dictionary = Dictionary(TEST_DICTIONARY_PATH)

    # Test with just one word in the csv file
    assert test_dictionary.vocables[0].native == ["EinWortInDeutsch"]
    assert test_dictionary.vocables[0].foreign == ["OneWordInEnglish"]
    # Test with two words in native language
    assert test_dictionary.vocables[1].native == ["Eins", "Zwei"]
    assert test_dictionary.vocables[1].foreign == ["TwoWordsInGerman"]
    # Test with two words in foreign language
    assert test_dictionary.vocables[2].native == ["ZweiWörterInEnglisch"]
    assert test_dictionary.vocables[2].foreign == ["one", "two"]
    # Test words with spaces
    assert test_dictionary.vocables[3].native == ["Wort mit Leerzeichen"]
    assert test_dictionary.vocables[3].foreign == ["Word with spaces"]
    # Test with space and tab at the start and beginning
    assert test_dictionary.vocables[4].native == [
        "Word mit Leerzeichen am anfang und ende"
    ]
    assert test_dictionary.vocables[4].foreign == ["Word with tab at the start and end"]
