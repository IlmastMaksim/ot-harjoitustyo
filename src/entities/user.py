class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: Kuvaa käyttäjän käyttäjätunnusta.
        password: Kuvaa käyttäjän salasanaa.
    """

    def __init__(self, username, email, password, created_on):
        self.username = username
        self.email = email
        self.password = password
        self.created_on = created_on
