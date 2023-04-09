import dataclasses


@dataclasses.dataclass
class Vocable:
    native: list[str]
    foreign: list[str]
