from dearpygui import core
from dearpygui import simple
from ui.gui_builder import GuiBuilder


if __name__ == "__main__":
    template = GuiBuilder(500, 500, theme="Dark")
    template.make_gui()
    template.run_gui()
