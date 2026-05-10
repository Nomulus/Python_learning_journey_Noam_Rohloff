"""Wir haben eine Liste mit Spannungsmesswerten in Kilovolt (kV) erhalten. Schreibe eine Funktion, die diese Liste bereinigt:

Alle Werte unter 0 sollen ignoriert werden (Messfehler).

Falls ein Wert 100 kV überschreitet, soll eine Warnung ausgegeben werden.

Berechne den Durchschnitt der gültigen Werte. 

measurements = [12.5, -1.0, 95.0, 110.2, 88.7]

Skalierung & Offset
Unsere Sensoren haben einen systematischen Fehler. Wir müssen die Rohwerte korrigieren, bevor wir sie auswerten.

Schreibe eine neue Funktion calibrate_measurements(raw_data), die folgendes tut:

Offset: Ziehe von jedem Wert 0.5 ab.

Skalierung: Multipliziere das Ergebnis mit einem Kalibrierungsfaktor von 1.02.

Filter: Behalte nur die Ergebnisse, die nach der Rechnung über 0 liegen.

Anforderung: Nutze für die gesamte Berechnung und den Filter nur eine einzige List Comprehension.

Beispieldaten:
raw_values = [0.4, 1.2, 5.0, 0.5, 10.0]"""

def main():
    measurements = [12.5, -1.0, 95.0, 110.2, 88.7]

    measurements = calibrate_measurements(measurements)

    clean_data = validate_measurements(measurements)

    print(f"clean data: {clean_data[0]}, average kV: {clean_data[1]}")
    
def calibrate_measurements(measurements):
    """Function to clean up data and compensate for calibration error 
    
    param measurements: list = raw measurements to be analysed
    return clean_data: list = cleaned up data """

    return [data for m in measurements if (data := (m - 0.5) *1.02) > 0]

def validate_measurements(measurements):
    """Function to validate measurements and warn of high voltages and return the average
    
    param measurements: list = List of measurements to be evaluated

    return clean: list = list of all the clean measurements
    return average: float = the average of the clean data
    """

    clean = measurements 

    for measurement in clean:
        if measurement > 100:
            print(f"warning, {measurement} kV.")

    average = sum(clean)/len(clean)

    return clean, average



if __name__ == "__main__":
    main()