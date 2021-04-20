from dearpygui import core, simple
from ui.menu import Menu
from ui.tab import Tab


class GuiBuilder:
    def __init__(self, width, height, theme="Dark"):
        self.theme = theme
        self.width = width
        self.height = height

    def make_gui(self):
        Menu()
        core.add_tab_bar(name="tab_bar", parent="Main Window")
        Tab("Exercises", "tab_bar").generate()
        Tab("Activity", "tab_bar").generate()

    @staticmethod
    def run_gui():
        core.start_dearpygui(primary_window="Main Window")
