from dearpygui import core, simple


class Menu:
    def theme_setting(sender, data):
        core.set_theme(data)

    with simple.window("Main Window"):
        with simple.menu_bar(name="Main Menu"):
            with simple.menu(name="Notifications"):
                with simple.menu("Set notifications"):
                    core.add_menu_item("Every 30 minutes")
                    core.add_menu_item("Every 1 hour")
                    core.add_menu_item("Every 2 hours")
                    core.add_menu_item("Disable")
            with simple.menu(name="Settings"):
                with simple.menu("Theme"):
                    core.add_menu_item(
                        "Dark##Theme 1", callback=theme_setting, callback_data="Dark"
                    )
                    core.add_menu_item(
                        "Light##Theme 2", callback=theme_setting, callback_data="Light"
                    )
        core.add_spacing(count=10)
