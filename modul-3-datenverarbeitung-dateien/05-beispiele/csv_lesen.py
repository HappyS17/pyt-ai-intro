"""
CSV-Daten lesen und verarbeiten
Verwendung: Lektion 2 - Live-Demo
"""
import csv
from pathlib import Path


def lese_csv_basic(dateiname: str) -> list:
    """
    Liest CSV mit csv.reader.
    
    Args:
        dateiname: Pfad zur CSV-Datei
    
    Returns:
        Liste von Listen (Zeilen)
    """
    daten = []
    
    with open(dateiname, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # Erste Zeile überspringen
        
        for row in reader:
            daten.append(row)
    
    return daten


def lese_csv_dict(dateiname: str) -> list:
    """
    Liest CSV mit DictReader.
    
    Args:
        dateiname: Pfad zur CSV-Datei
    
    Returns:
        Liste von Dictionaries
    """
    daten = []
    
    with open(dateiname, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            daten.append(dict(row))
    
    return daten


def schreibe_csv(dateiname: str, daten: list, header: list) -> None:
    """
    Schreibt Daten in CSV-Datei.
    
    Args:
        dateiname: Pfad zur CSV-Datei
        daten: Liste von Listen oder Dictionaries
        header: Liste mit Spaltennamen
    """
    with open(dateiname, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(daten)


def main():
    """Hauptfunktion."""
    # Beispiel-CSV erstellen
    beispiel_daten = [
        ["Anna", "25", "Zürich"],
        ["Bob", "30", "Bern"],
        ["Clara", "28", "Basel"]
    ]
    
    header = ["Name", "Alter", "Stadt"]
    
    # Schreiben
    schreibe_csv("personen.csv", beispiel_daten, header)
    print("CSV erstellt: personen.csv")
    
    # Lesen mit DictReader
    daten = lese_csv_dict("personen.csv")
    
    print("\nGelesene Daten:")
    for person in daten:
        print(f"{person['Name']}, {person['Alter']} Jahre, {person['Stadt']}")


if __name__ == "__main__":
    main()
