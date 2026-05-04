import datetime
import sys

class Workout_Session:
    def __init__(self, muscle_group, date = datetime.datetime.now()) -> None:
        self._muscle_group = muscle_group
        self.date = date
        self.train()
    
    def __str__(self):
        return str(self.date)
    
    def train(self):
        while True:
            try:
                self.excercise()
            except SystemExit:
                sys.exit #add by by
    
    def excercise(self):
        print("excercise, weight, reps")
        usr_input = input().split(",")
        print(usr_input)

def main():
    Workout = Workout_Session
    print(Workout)

if __name__ == "__main__":
    main()