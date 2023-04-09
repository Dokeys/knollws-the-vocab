import tkinter


def get_words_string_with_comma(words: list[str]) -> str:
    searched_words_string = ""
    for word in words:
        searched_words_string += f"{word}, "
    searched_words_string = searched_words_string[:-2]  # remove last ", "
    return searched_words_string


def adjust_font_size_with_window_size(
    master: tkinter.Widget, font_size: int, min_font_size: int, width: int
) -> None:
    while True:
        master.config(font=("Arial", font_size))
        master.update()
        if master.winfo_width() < width - 20 or font_size <= min_font_size:
            return
        font_size -= 1
