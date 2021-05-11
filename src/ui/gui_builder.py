from dearpygui import core, simple
from ui.login import Login
from services.user import user_services


class GuiBuilder:
    def __init__(self, width, height, theme="Dark"):
        self.theme = theme
        self.width = width
        self.height = height

    def make_gui(self):
        Login()

    @staticmethod
    def run_gui():
        core.start_dearpygui(primary_window="Main Window")


gui_builder = GuiBuilder(500, 500, theme="Dark")
