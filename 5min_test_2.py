"""Wir haben eine Liste mit Spannungsmesswerten in Kilovolt (kV) erhalten. Schreibe eine Funktion, die diese Liste bereinigt:

Alle Werte unter 0 sollen ignoriert werden (Messfehler).

Falls ein Wert 100 kV überschreitet, soll eine Warnung ausgegeben werden.

Berechne den Durchschnitt der gültigen Werte. 

messwerte = [12.5, -1.0, 95.0, 110.2, 88.7]"""

def main():
    messwerte = [12.5, -1.0, 95.0, 110.2, 88.7]

    print(validate_measurements(messwerte))
    

def validate_measurements(messwerte):
    """Function to validate measurements and warn of high voltages
    
    param messwerte: list = List of measurements to be evaluated
    return clean: list = list of all the clean measurements
    """

    clean = []
    for measurement in messwerte:
        if measurement <0:
            pass
        else:
            clean.append(measurement)
        
        if measurement > 100:
            print(f"warning, {measurement} kV.")
    
    return clean



if __name__ == "__main__":
    main()