import dataclasses

from model.vocable import Vocable


@dataclasses.dataclass
class CurrentVocable(Vocable):
    """
    This is a Singleton what inherits everything form the Vocable dataclass.
    In this class the currend searched vocable of the program is saved.
    """

    __instance = None

    def __init__(self) -> None:
        if CurrentVocable.__instance != None:
            raise Exception("CurrentDictionary is a singleton.")
        CurrentVocable.__instance = self

    @staticmethod
    def get_instance() -> None:
        if CurrentVocable.__instance == None:
            return CurrentVocable()
        return CurrentVocable.__instance

    def set_vocable(self, vocable: Vocable) -> None:
        self.native = vocable.native
        self.foreign = vocable.foreign
