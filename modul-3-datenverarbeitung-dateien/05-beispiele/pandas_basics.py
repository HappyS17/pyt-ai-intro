"""
pandas Grundlagen
Verwendung: Lektion 2 - Live-Demo
"""
import pandas as pd
from pathlib import Path


def erstelle_beispiel_daten():
    """Erstellt Beispiel-CSV für Demos."""
    daten = {
        'name': ['Anna', 'Bob', 'Clara', 'David', 'Eva'],
        'alter': [25, 30, 28, 35, 22],
        'stadt': ['Zürich', 'Bern', 'Basel', 'Zürich', 'Bern'],
        'gehalt': [75000, 85000, 72000, 95000, 68000]
    }
    
    df = pd.DataFrame(daten)
    df.to_csv('mitarbeiter.csv', index=False)
    print("✓ Beispiel-Datei erstellt: mitarbeiter.csv")
    return df


def demo_lesen():
    """Demo: CSV mit pandas lesen."""
    print("\n=== DEMO: CSV LESEN ===\n")
    
    # CSV einlesen
    df = pd.read_csv('mitarbeiter.csv')
    
    # Erste Zeilen anzeigen
    print("Erste 3 Zeilen:")
    print(df.head(3))
    
    # Info über DataFrame
    print("\nDataFrame Info:")
    print(df.info())
    
    # Statistiken
    print("\nStatistiken:")
    print(df.describe())


def demo_filtern():
    """Demo: Daten filtern."""
    print("\n=== DEMO: FILTERN ===\n")
    
    df = pd.read_csv('mitarbeiter.csv')
    
    # Einfacher Filter
    print("Mitarbeiter über 25:")
    aelter_25 = df[df['alter'] > 25]
    print(aelter_25)
    
    # Mehrere Bedingungen
    print("\nMitarbeiter in Zürich über 25:")
    zuerich_alt = df[(df['stadt'] == 'Zürich') & (df['alter'] > 25)]
    print(zuerich_alt)
    
    # Bestimmte Spalten
    print("\nNur Name und Gehalt:")
    print(df[['name', 'gehalt']])


def demo_aggregieren():
    """Demo: Daten aggregieren."""
    print("\n=== DEMO: AGGREGIEREN ===\n")
    
    df = pd.read_csv('mitarbeiter.csv')
    
    # Durchschnitt
    print(f"Durchschnittsalter: {df['alter'].mean():.1f}")
    print(f"Durchschnittsgehalt: {df['gehalt'].mean():.0f}")
    
    # Gruppieren
    print("\nDurchschnittsgehalt pro Stadt:")
    nach_stadt = df.groupby('stadt')['gehalt'].mean()
    print(nach_stadt)
    
    # Mehrere Aggregationen
    print("\nStatistiken pro Stadt:")
    stats = df.groupby('stadt').agg({
        'alter': ['mean', 'min', 'max'],
        'gehalt': ['mean', 'sum']
    })
    print(stats)


def demo_sortieren():
    """Demo: Daten sortieren."""
    print("\n=== DEMO: SORTIEREN ===\n")
    
    df = pd.read_csv('mitarbeiter.csv')
    
    # Nach Alter sortieren
    print("Nach Alter (aufsteigend):")
    print(df.sort_values('alter'))
    
    # Nach Gehalt (absteigend)
    print("\nNach Gehalt (absteigend):")
    print(df.sort_values('gehalt', ascending=False))
    
    # Mehrere Spalten
    print("\nNach Stadt und Alter:")
    print(df.sort_values(['stadt', 'alter']))


def demo_neue_spalten():
    """Demo: Neue Spalten erstellen."""
    print("\n=== DEMO: NEUE SPALTEN ===\n")
    
    df = pd.read_csv('mitarbeiter.csv')
    
    # Berechnung
    df['gehalt_pro_jahr'] = df['gehalt'] * 12
    df['alter_gruppe'] = df['alter'].apply(
        lambda x: 'Jung' if x < 30 else 'Erfahren'
    )
    
    print("Mit neuen Spalten:")
    print(df)


def demo_speichern():
    """Demo: Daten speichern."""
    print("\n=== DEMO: SPEICHERN ===\n")
    
    df = pd.read_csv('mitarbeiter.csv')
    
    # Als CSV
    df.to_csv('output.csv', index=False)
    print("✓ Gespeichert als CSV: output.csv")
    
    # Als JSON
    df.to_json('output.json', orient='records', indent=2)
    print("✓ Gespeichert als JSON: output.json")
    
    # Als Excel (benötigt openpyxl)
    try:
        df.to_excel('output.xlsx', index=False)
        print("✓ Gespeichert als Excel: output.xlsx")
    except ImportError:
        print("⚠ Excel-Export benötigt: pip install openpyxl")


def main():
    """Hauptfunktion."""
    print("=" * 50)
    print("PANDAS GRUNDLAGEN")
    print("=" * 50)
    
    # Beispieldaten erstellen
    erstelle_beispiel_daten()
    
    # Demos durchführen
    demo_lesen()
    demo_filtern()
    demo_aggregieren()
    demo_sortieren()
    demo_neue_spalten()
    demo_speichern()
    
    print("\n" + "=" * 50)
    print("ALLE DEMOS ABGESCHLOSSEN")
    print("=" * 50)


if __name__ == "__main__":
    main()
