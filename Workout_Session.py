import datetime
import sys

class Workout_Session:
    def __init__(self, muscle_group, date = datetime.datetime.now()) -> None:
        print("__initiatet__")
        self._muscle_group = muscle_group
        self.date = date
        self.train()
    
    def __str__(self):
        print("__str__")
        return str(self.date)
    
    def train(self):
        while True: 
            user_exercise_list = self.excercise()
            current_exercise = self.try_to_convert(user_exercise_list)

    def excercise(self):
        print("excercise, weight, reps")
        user_exercise_list = input().split(",")
        return user_exercise_list

    def try_to_convert(self, user_exercise_list):
        try:
            user_exercise_dict = {"exercise" : user_exercise_list[0], "weight" : user_exercise_list[1] if float(user_exercise_list[1]) >= 0 else print("not acceped"), "reps" : user_exercise_list[2] if float(user_exercise_list[2]) >= 0 else print("Not accepted")}
            return user_exercise_dict
        except ValueError:
            print("Invalid input, copy my formating:\n")


def main():
    Workout = Workout_Session("Back", datetime.datetime(2026, 5, 5))
    print(Workout)

if __name__ == "__main__":
    main()