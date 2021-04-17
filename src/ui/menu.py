from dearpygui.core import *
from dearpygui.simple import *

class Menu:
    def theme_setting(sender, data):
        set_theme(data)

    with window("Main Window"):
        with menu_bar(name='Main Menu'):
            with menu(name='Notifications'):
                with menu('Set notifications'):
                    add_menu_item('Every 30 minutes')
                    add_menu_item('Every 1 hour')
                    add_menu_item('Every 2 hours')
                    add_menu_item('Disable')
            with menu(name='Settings'):
                with menu('Theme'):
                    add_menu_item('Dark##Theme 1', callback=theme_setting, callback_data='Dark')
                    add_menu_item('Light##Theme 2', callback=theme_setting, callback_data='Light')
        add_spacing(count=10)
