from dearpygui import core, simple
from services.user import user_services
from ui.menu import Menu
from ui.tab import Tab


class Preliminary:
    def __init__(self):
        with simple.window(
            "Login Window", no_title_bar=True, autosize=True, no_resize=True
        ):
            core.add_group(name="signup_els")
            core.add_group(name="login_els")
            self.add_login_els()

    def add_login_els(self):
        core.add_input_text("Username##login", on_enter=True, parent="login_els")
        core.add_input_text(
            "Password##login",
            password=True,
            on_enter=True,
            parent="login_els",
        )
        core.add_button("Log in", callback=self.log_in, parent="login_els")
        core.add_button(
            "Create an account", callback=self.show_signup_els, parent="login_els"
        )
        core.add_text("Incorrect Password", color=[255, 0, 0])
        core.add_text("Please, fill all the inputs", color=[255, 0, 0])
        simple.hide_item("Incorrect Password")
        simple.hide_item("Please, fill all the inputs")

    def logged_in_mode(self):
        Menu()
        core.delete_item("Login Window")
        core.add_tab_bar(name="tab_bar", parent="Main Window")
        Tab("Workout", "tab_bar").generate_tab()
        Tab("Records", "tab_bar").generate_tab()
        simple.show_item("Main Menu")

    def log_in(self):
        username = core.get_value("Username##login")
        password = core.get_value("Password##login")
        if not username or not password:
            simple.show_item("Please, fill all the inputs")
            return
        result = user_services.login_user(username, password)
        if result:
            self.logged_in_mode()
        else:
            simple.show_item("Incorrect Password")

    def sign_up(self):
        username = core.get_value("Username##signup")
        email = core.get_value("Email##signup")
        password = core.get_value("Password##signup")
        if not username or not email or not password:
            simple.show_item("Please, fill all the inputs")
            return
        result = user_services.signup_user(username, email, password)
        if result:
            self.cancel_signup()
        else:
            simple.show_item("Something went wrong")

    def show_signup_els(self):
        self.cancel_login()
        core.add_input_text("Username##signup", on_enter=True, parent="signup_els")
        core.add_input_text("Email##signup", on_enter=True, parent="signup_els")
        core.add_input_text(
            "Password##signup",
            password=True,
            on_enter=True,
            parent="signup_els",
        )
        core.add_button("Cancel", callback=self.cancel_signup, parent="signup_els")
        core.add_button("Sign up", callback=self.sign_up, parent="signup_els")
        core.add_text("Please, fill all the inputs", color=[255, 0, 0])
        core.add_text("Something went wrong", color=[255, 0, 0])
        simple.hide_item("Please, fill all the inputs")
        simple.hide_item("Something went wrong")

    def cancel_signup(self):
        if core.get_value("Please, fill all the inputs"):
            core.delete_item("Please, fill all the inputs")
        if core.get_value("Something went wrong"):
            core.delete_item("Something went wrong")
        core.delete_item("Username##signup")
        core.delete_item("Email##signup")
        core.delete_item("Password##signup")
        core.delete_item("Cancel")
        core.delete_item("Sign up")
        simple.show_item("login_els")
        self.add_login_els()

    def cancel_login(self):
        if core.get_value("Please, fill all the inputs"):
            core.delete_item("Please, fill all the inputs")
        if core.get_value("Incorrect Password"):
            core.delete_item("Incorrect Password")
        core.delete_item("Username##login")
        core.delete_item("Password##login")
        core.delete_item("Log in")
        core.delete_item("Create an account")
