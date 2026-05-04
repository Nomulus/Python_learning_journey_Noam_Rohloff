import datetime

class Workout_Session:
    def __init__(self, muscle_group, date = datetime.datetime.now()) -> None:
        self._muscle_group = muscle_group
        self.date = date
        