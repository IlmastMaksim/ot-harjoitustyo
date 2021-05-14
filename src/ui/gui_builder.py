from dearpygui import core
from ui.preliminary import Preliminary


class GuiBuilder:
    def __init__(self, width, height, theme="Dark"):
        self.theme = theme
        self.width = width
        self.height = height

    def make_gui(self):
        Preliminary()

    @staticmethod
    def run_gui():
        core.start_dearpygui(primary_window="Main Window")


gui_builder = GuiBuilder(500, 500, theme="Dark")
