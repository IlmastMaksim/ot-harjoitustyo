from dearpygui import core, simple
from services.user import user_services
from ui.menu import Menu
from ui.tab import Tab


class Login:
    def __init__(self):
        with simple.window("Login Window", no_title_bar=True, autosize=True, no_resize=True):
            core.add_group(name="signup_els")
            core.add_group(name="login_els")
            core.add_input_text(
                "Username##login", on_enter=True, parent="login_els"
            )
            core.add_input_text(
                "Password##login",
                password=True,
                on_enter=True,
                parent="login_els",
            )
            core.add_button("Log in", callback=self.log_in, parent="login_els")
            core.add_button(
                "Create an account", callback=self.show_signup_btns, parent="login_els"
            )
            core.add_text("Incorrect Password.", color=[255, 0, 0], parent="Login Window")
            simple.hide_item("Incorrect Password.")


    def log_in(self, sender, data):
        if core.get_value("Password##login") == "password":
            result = user_services.log_in()
            Menu()
            core.delete_item("Login Window")
            core.add_tab_bar(name="tab_bar", parent="Main Window")
            Tab("Workout", "tab_bar").generate()
            Tab("Records", "tab_bar").generate()
            simple.show_item("Main Menu")
        else:
            simple.show_item("Incorrect Password.")

    def sign_up(self):
        pass

    def show_signup_btns(self):
        simple.hide_item("login_els")
        core.add_input_text(
            "Username##signup", on_enter=True, parent="signup_els"
        )
        core.add_input_text(
            "Email##signup", on_enter=True, parent="signup_els"
        )
        core.add_input_text(
            "Password##signup",
            password=True,
            on_enter=True,
            parent="signup_els",
        )
        core.add_button("Cancel", callback=self.cancel_signup, parent="signup_els")
        core.add_button("Sign up", callback=self.sign_up, parent="signup_els")

    def cancel_signup(self):
        core.delete_item("Username##signup")
        core.delete_item("Email##signup")
        core.delete_item("Password##signup")
        core.delete_item("Cancel")
        core.delete_item("Sign up")
        simple.show_item("login_els")