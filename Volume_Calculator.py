"""Kontext:Wir brauchen ein Modul, das bestehende Trainingsdaten auswertet, anstatt sie nur abzufragen.Deine Aufgabe:
Klassen-Struktur: Erstelle eine Klasse Exercise (Name, Gewicht, Wiederholungen) und eine Klasse Workout (Name, Liste von Exercises).
Kein User-Input: Die Klassen dürfen keine input() Befehle enthalten. Alle Daten müssen beim Erstellen der Objekte über Parameter übergeben werden.
Die Logik: Schreibe eine Funktion calculate_total_volume(workout), die das Gesamtgewicht eines Workouts berechnet (Summe von $Gewicht \times Wiederholungen$ aller Übungen).
Der Test-Lauf: Erstelle im if __name__ == "__main__": Block manuell zwei Workouts:"Push Day" mit 2 Übungen."Pull Day" mit 2 Übungen.
Die Ausgabe: Das Programm soll beide Workouts und deren jeweiliges Gesamtvolumen sauber in der Konsole ausgeben.Zeitlimit: 30 Minuten.
habe doch 1 std gebraucht 

Die Aufgabe: Workout-Analyse Pro
Szenario:
Ein reiner Volumen-Zähler reicht uns nicht. Wir wollen wissen, was die schwerste Übung war und welche Übungen nur zum Aufwärmen dienten.

Deine Anforderungen:

Erweiterung der Klasse Workout:

Füge eine Methode get_heaviest_exercise() hinzu. Sie soll das Excercise Objekt zurückgeben, bei dem das Gewicht am höchsten war.

Die "Warm-up" Logik:

Schreibe eine Funktion print_workout_report(workout, threshold).

Diese Funktion soll alle Übungen des Workouts auflisten.

Der Clou: Wenn das Gewicht einer Übung unter dem threshold (Grenzwert) liegt, soll hinter der Übung der Hinweis (Warm-up) erscheinen.

Die History-Challenge:

Erstelle eine Liste namens history, die deine zwei Workouts von vorhin (push_day und pull_day) enthält.

Schreibe eine Schleife, die über diese history geht und für jedes Workout den Report ausgibt und anzeigt, welche Übung jeweils die schwerste war.

Zeitlimit: 30 Minuten.
Regel: Keine neuen Bibliotheken, nur saubere Logik mit Listen und Objekten."""
import re

class Excercise():
    def __init__(self, name, weight, reps) -> None:
        self._name = name
        self._weight = weight
        self._reps = reps
    
    def Volume(self) -> float:
        weight = self._weight
        weight = self.weight_to_int(weight)
        volume = weight * self._reps
        self.volume = volume
        return volume
    
    def weight_to_int(self, weight) -> float:
        weight = re.sub(r"[a-zA-Z]", "", str(weight))
        return float(weight)



class Workout():
    def __init__(self, name, *excercises)-> None:
        self.name = name
        self.excercises = excercises
    
    def calculate_total_Volume(self) -> float:
        Volume = 0
        for excercise in self.excercises:
            Volume += excercise.Volume()
        return Volume
    

def main() -> None:
    pull_down = Excercise("pull_down", 60, 10)
    overhead_tryceps_extencion = Excercise("overhead_tryceps_extencion", 32, 10)

    pull_day= Workout("pull_day", pull_down, overhead_tryceps_extencion)

    bench_press = Excercise("bench_press", 70, 10)
    incline_bench_press = Excercise("incline_bench_press", 50, 10)

    push_day = Workout("push_day", bench_press, incline_bench_press)

    print(f"Your Workout Volume for pull day comes out to {pull_day.calculate_total_Volume()} kg, well done.")
    for excercise in pull_day.excercises:
        print(f"You moved {excercise.volume} kg with {excercise._name}")

    print(f"Your Workout Volume for push day comes out to {push_day.calculate_total_Volume()} kg, well done.")



if __name__ == "__main__":
    main()