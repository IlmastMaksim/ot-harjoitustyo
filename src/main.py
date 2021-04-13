from dearpygui.core import *
from dearpygui.simple import *


with window("Main Window"):
    with menu_bar("MenuBar"):
        with menu("Exercises"):
            add_text('Exercises tab')
        with menu("Calendar"):
            add_text('Calendar tab')
        with menu("Settings"):
            add_text('Settings tab')

start_dearpygui(primary_window="Main Window")