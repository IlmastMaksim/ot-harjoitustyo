from dearpygui import core, simple
from services.user import user_services
from ui.menu import Menu
from ui.tab import Tab


class Login:
    def __init__(self):
        with simple.window(
            "Login Window", no_title_bar=True, autosize=True, no_resize=True
        ):
            core.add_group(name="signup_els")
            core.add_group(name="login_els")
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
            core.add_text(
                "Incorrect Password.", color=[255, 0, 0], parent="Login Window"
            )
            simple.hide_item("Incorrect Password.")

    def log_in(self, sender, data):
        username = core.get_value("Username##login")
        password = core.get_value("Password##login")
        result = user_services.login_user(username, password)
        if result:
            Menu()
            core.delete_item("Login Window")
            core.add_tab_bar(name="tab_bar", parent="Main Window")
            Tab("Workout", "tab_bar").generate()
            Tab("Records", "tab_bar").generate()
            simple.show_item("Main Menu")
        else:
            simple.show_item("Incorrect Password.")

    def sign_up(self):
        username = core.get_value("Username##signup")
        email = core.get_value("Email##signup")
        password = core.get_value("Password##signup")
        if not username or not email or not password:
            simple.show_item("Please, fill all the inputs")
        try:
            user_services.signup_user(username, email, password)
            self.cancel_signup()
        except:
            simple.show_item("Something went wrong")


    def show_signup_els(self):
        simple.hide_item("login_els")
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
