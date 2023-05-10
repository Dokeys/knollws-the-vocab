# Knollws the Vocab - VocableTrainer

## Description

A simple program to practice vocabulary. The vocabularies are read from a simple CSV file.

## Screenshots

![](files/Screenshot-1.png)
![](files/Screenshot-2.png)

## Design

This is a redesign with the MVC-Pattern. This leads to a better decoupling between the modules.

```mermaid
flowchart LR
    View-->|Action|Controller
    Controller-->|Update|View
    Model-->|Notify|Controller
    Controller-->|Update|Model
    
    Model<-->Database[(Database)]
    User<-->View
```

## Model

```mermaid
classDiagram

class Model
class VocablePicker
class CurrentDictionary
class Dictionary
class CurrentVocable
class Vocable


Model --* VocablePicker
CurrentDictionary --|> Dictionary
VocablePicker *-- CurrentDictionary
CurrentVocable --|> Vocable
VocablePicker *-- CurrentVocable


class VocablePicker{
    +set_new_dictionary(path: str)
    +set_new_vocable()
    +get_untranslated_words() List~str~
    +check_vocable(input: str)  bool
}

class CurrentDictionary{
    -__instance: CurrentDictionary
    +get_instance()    
}

class Dictionary{
    +languages: list[str]
    +vocables: list[Vocable]
    +read_dictionary(dictionary_file_path: str)
    #_read_header_from_file(dictionary_file_path: str)
    #_read_vocables_from_file(dictionary_file_path: str)
}

class Vocable{
    +native: list[str]
    +foreign: list[str]
}

class CurrentVocable{
    -__instance: CurrentVocable
    +get_instance()
    +set_vocable
}
```

## View

```mermaid
classDiagram

class View
class VocableTrainerGui
class UI
class InputOutputFrame

View -- UI
UI <|-- VocableTrainerGui
VocableTrainerGui *-- InputOutputFrame

class UI{
    <<AbstractClass>>
    +set_untranslated_words_text(words_string: str)
    +bind_user_input(callback)
    +get_entry_text() str
    +clear_entry()
    +set_response_text(response_string: str)
}

class VocableTrainerGui{
    +bind_user_input(callback)
    +set_untranslated_words_text(untranslated_words: List~str~)
    +get_entry_text() str
    +clear_entry()
    +set_response_text(response_string: str)
}

class InputOutputFrame{
    set_untranslated_words(untranslated_words_string: str)
    get_entry_field_text() str
    clear_entry_field()
    set_response_text(response_string: str)
}
```

## Controller

```mermaid
classDiagram
class Controller


class Controller{
    +view:  
    +model : VocablePicker
    +new_vocable()
}
```
