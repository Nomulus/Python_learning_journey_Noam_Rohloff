"""Wir haben eine Liste mit Spannungsmesswerten in Kilovolt (kV) erhalten. Schreibe eine Funktion, die diese Liste bereinigt:

Alle Werte unter 0 sollen ignoriert werden (Messfehler).

Falls ein Wert 100 kV überschreitet, soll eine Warnung ausgegeben werden.

Berechne den Durchschnitt der gültigen Werte. 

measurements = [12.5, -1.0, 95.0, 110.2, 88.7]"""

def main():
    measurements = [12.5, -1.0, 95.0, 110.2, 88.7]

    clean_data = validate_measurements(measurements)
    print(f"clean data: {clean_data[0]}, average kV: {clean_data[1]}")
    

def validate_measurements(measurements):
    """Function to validate measurements and warn of high voltages and return the average
    
    param measurements: list = List of measurements to be evaluated

    return clean: list = list of all the clean measurements
    return average: float = the average of the clean data
    """

    clean = [measurement for measurement in measurements if measurement>= 0]
    
    for measurement in clean:
        if measurement > 100:
            print(f"warning, {measurement} kV.")

    average = sum(clean)/len(clean)

    return clean, average



if __name__ == "__main__":
    main()