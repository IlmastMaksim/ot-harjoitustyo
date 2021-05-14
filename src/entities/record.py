class Record:
    """Luokka, joka kuvaa yksittäistä käyttäjän liikuntasuoritusta.

    Attributes:
        exercise: Kuvaa suoritetun harjoituksen nimettä
        sets: Kuvaa sarjojen määrää
        reps: Kuvaa toistojen määrää
        username: Kuvaa käyttäjän tunnusta
        created_on: Kuvaa suorituspäivämäärää
    """

    def __init__(self, exercise, sets, reps, username, created_on):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.username = username
        self.created_on = created_on
