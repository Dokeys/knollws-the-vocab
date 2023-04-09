import random
from model.current_vocable import CurrentVocable


class Tip:
    _show_tipp_index = 0
    _word_for_tip = ""

    @staticmethod
    def reset_tip() -> None:
        Tip._show_tipp_index = 0

    @staticmethod
    def get_tip_string() -> str:
        current_vocable = CurrentVocable.get_instance()

        if Tip._show_tipp_index == 0:
            random_word_number = random.randrange(0, len(current_vocable.foreign))
            Tip._word_for_tip = current_vocable.foreign[random_word_number]
        Tip._show_tipp_index += 1

        return Tip._word_for_tip[: Tip._show_tipp_index]

    @classmethod
    def was_tip_requested(cls) -> bool:
        if cls._show_tipp_index > 0:
            return True
        else:
            return False
