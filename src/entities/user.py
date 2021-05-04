class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: Kuvaa käyttäjän käyttäjätunnusta.
        password: Kuvaa käyttäjän salasanaa.
    """

    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
