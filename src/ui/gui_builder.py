from dearpygui.core import *
from dearpygui.simple import *
from ui.menu import Menu
from ui.tab import Tab

class GuiBuilder:
    def __init__(self, width, height, theme='Dark'):
        self.theme = theme
        self.width = width
        self.height = height

    def make_gui(self):
        add_tab_bar(name='tab_bar', parent="Main Window")
        Tab('Exercises', 'tab_bar').generate()
        Tab('Activity', 'tab_bar').generate()

    @staticmethod
    def run_gui():
        start_dearpygui(primary_window="Main Window")