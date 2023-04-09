from typing import Callable


class SoundSettings:
    _fail_sound = True
    _fail_reader = True

    @classmethod
    def set_fail_sound(cls, state: bool) -> None:
        cls._fail_sound = state

    @classmethod
    def get_fail_sound(cls) -> bool:
        return cls._fail_sound

    @classmethod
    def set_fail_reader(cls, state: bool) -> None:
        cls._fail_reader = state

    @classmethod
    def get_fail_reader(cls) -> bool:
        return cls._fail_reader


class ViewSettings:
    _transparent_background = False
    _transparent_background_subscribers = []
    _backgroud_color = "#7094db"

    @classmethod
    def set_transparent_background(cls, state: bool) -> None:
        cls._transparent_background = state
        for callback in cls._transparent_background_subscribers:
            callback(cls._transparent_background)

    @classmethod
    def bind_transparent_background_changed(cls, fn: Callable[[bool], None]) -> None:
        cls._transparent_background_subscribers.append(fn)

    @classmethod
    def get_background_color(cls) -> str:
        return cls._backgroud_color


class Settings(SoundSettings, ViewSettings):
    pass
