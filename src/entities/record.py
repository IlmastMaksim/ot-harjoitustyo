class Record:
    """Luokka, joka kuvaa yksittäistä käyttäjän liikuntasuoritusta.

    Attributes:
        exercise: Kuvaa suoritetun harjoituksen nimettä
        sets: Kuvaa sarjojen määrää
        reps: Kuvaa toistojen määrää
        created_on: Kuvaa suorituspäivämäärää
    """

    def __init__(self, exercise, sets, reps, created_on):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.created_on = created_on
