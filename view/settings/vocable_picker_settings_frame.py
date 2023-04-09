import tkinter
from tkinter import ttk


class VocablePickerSettingsFrame(tkinter.Frame):
    options = [("random", 1), ("intelligent", 2)]

    def __init__(self, master=None) -> None:
        super().__init__(master)

        self.lbl_vocable_picker_settings = ttk.Label(
            self, text="Vocable Picker:", font=("calimbri", 14)
        )
        self.lbl_vocable_picker_settings.pack(anchor="w")

        self.v = tkinter.IntVar()
        self.v.set(1)  # initializing the choice, i.e. Python
        for txt, val in self.options:
            ttk.Radiobutton(
                self,
                text=txt,
                variable=self.v,
                command=self.radiobutton_action,
                value=val,
            ).pack(anchor="w")

    def radiobutton_action(self) -> None:
        print(self.v.get())
