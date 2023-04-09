from dataclasses import dataclass


class Response:
    def __init__(self) -> None:
        self.is_right: bool
        self.response: str
        self.additional_info: str

    def __str__(self) -> str:
        return self.response
