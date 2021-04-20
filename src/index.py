from dearpygui import core
from dearpygui import simple
from initialize_database import initialize_database
from ui.gui_builder import GuiBuilder


if __name__ == "__main__":
    initialize_database()
    template = GuiBuilder(500, 500, theme="Dark")
    template.make_gui()
    template.run_gui()
