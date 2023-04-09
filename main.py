from model.vocable_picker import VocablePicker
from view.vocabel_trainer_gui import VocabelTrainerGui
from controller.controller import Controller


def main() -> None:
    model = VocablePicker()
    view = VocabelTrainerGui(model)
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()
