from abc import ABC, abstractmethod
import tkinter
from typing import Callable


class UI(ABC):
    @abstractmethod
    def set_untranslated_words_text(self, words_string: str) -> None:
        pass

    @abstractmethod
    def bind_user_input(self, callback: Callable[[tkinter.Event], None]) -> None:
        pass

    @abstractmethod
    def bind_tip(self, callback: Callable[[tkinter.Event], None]) -> None:
        pass

    @abstractmethod
    def get_entry_text(self) -> str:
        pass

    @abstractmethod
    def clear_entry(self) -> None:
        pass

    @abstractmethod
    def set_input_response(self) -> None:
        pass

    @abstractmethod
    def set_tip_text(self, tip_string: str) -> None:
        pass
