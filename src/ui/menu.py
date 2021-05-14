from dearpygui import core, simple
from services.user import user_services


class Menu:
    def theme_setting(sender, data):
        core.set_theme(data)

    def dump_db():
        user_services.delete_records_by_username()

    with simple.window("Main Window", no_title_bar=True, autosize=True, no_resize=True):
        with simple.menu_bar(name="Main Menu"):
            with simple.menu(name="Settings"):
                with simple.menu("Theme"):
                    core.add_menu_item(
                        "Dark", callback=theme_setting, callback_data="Dark"
                    )
                    core.add_menu_item(
                        "Light", callback=theme_setting, callback_data="Light"
                    )
                    core.add_menu_item(
                        "Classic", callback=theme_setting, callback_data="Classic"
                    )
                    core.add_menu_item(
                        "Dark 2", callback=theme_setting, callback_data="Dark 2"
                    )
                    core.add_menu_item(
                        "Grey", callback=theme_setting, callback_data="Grey"
                    )
                    core.add_menu_item(
                        "Dark Grey", callback=theme_setting, callback_data="Dark Grey"
                    )
                    core.add_menu_item(
                        "Cherry", callback=theme_setting, callback_data="Cherry"
                    )
                    core.add_menu_item(
                        "Purple", callback=theme_setting, callback_data="Purple"
                    )
                    core.add_menu_item(
                        "Gold", callback=theme_setting, callback_data="Gold"
                    )
                    core.add_menu_item(
                        "Red", callback=theme_setting, callback_data="Red"
                    )
                with simple.menu(name="Database"):
                    core.add_menu_item("Dump database", callback=dump_db)
        core.add_spacing(count=10)
    simple.hide_item("Main Menu")
