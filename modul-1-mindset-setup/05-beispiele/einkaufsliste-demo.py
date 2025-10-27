"""
Einkaufslisten-Verwaltung
Verwendung: Lektion 4 - Live-Demo
Zeigt vollständigen Entwicklungsworkflow
"""

def zeige_menu():
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 50)
    print("EINKAUFSLISTE")
    print("=" * 50)
    print("1. Artikel hinzufügen")
    print("2. Artikel entfernen")
    print("3. Alle Artikel anzeigen")
    print("4. Artikel suchen")
    print("5. Beenden")
    print("=" * 50)


def artikel_hinzufuegen(liste):
    """
    Fügt einen Artikel zur Liste hinzu.
    
    Args:
        liste (list): Die Einkaufsliste
    """
    artikel = input("Artikel-Name: ").strip()
    
    if not artikel:
        print("Fehler: Artikel-Name darf nicht leer sein!")
        return
    
    # Prüfen, ob Artikel schon existiert
    if artikel.lower() in [a.lower() for a in liste]:
        print(f"'{artikel}' ist bereits auf der Liste!")
    else:
        liste.append(artikel)
        print(f"✓ '{artikel}' wurde hinzugefügt.")


def artikel_entfernen(liste):
    """
    Entfernt einen Artikel aus der Liste.
    
    Args:
        liste (list): Die Einkaufsliste
    """
    if not liste:
        print("Die Liste ist leer!")
        return
    
    artikel = input("Artikel-Name: ").strip()
    
    # Suche Artikel (case-insensitive)
    gefunden = False
    for i, item in enumerate(liste):
        if item.lower() == artikel.lower():
            entfernt = liste.pop(i)
            print(f"✓ '{entfernt}' wurde entfernt.")
            gefunden = True
            break
    
    if not gefunden:
        print(f"'{artikel}' ist nicht auf der Liste!")


def artikel_anzeigen(liste):
    """
    Zeigt alle Artikel an.
    
    Args:
        liste (list): Die Einkaufsliste
    """
    if not liste:
        print("\nDie Liste ist leer!")
        return
    
    print("\n" + "-" * 50)
    print(f"EINKAUFSLISTE ({len(liste)} Artikel)")
    print("-" * 50)
    for i, artikel in enumerate(liste, 1):
        print(f"{i}. {artikel}")
    print("-" * 50)


def artikel_suchen(liste):
    """
    Sucht nach einem Artikel.
    
    Args:
        liste (list): Die Einkaufsliste
    """
    if not liste:
        print("Die Liste ist leer!")
        return
    
    suchbegriff = input("Suchbegriff: ").strip().lower()
    
    gefunden = [a for a in liste if suchbegriff in a.lower()]
    
    if gefunden:
        print(f"\nGefundene Artikel ({len(gefunden)}):")
        for artikel in gefunden:
            print(f"  - {artikel}")
    else:
        print(f"Keine Artikel mit '{suchbegriff}' gefunden.")


def main():
    """
    Hauptfunktion des Programms.
    """
    einkaufsliste = []
    
    print("Willkommen zur Einkaufslisten-Verwaltung!")
    
    while True:
        zeige_menu()
        wahl = input("\nWähle eine Option (1-5): ").strip()
        
        if wahl == "1":
            artikel_hinzufuegen(einkaufsliste)
        elif wahl == "2":
            artikel_entfernen(einkaufsliste)
        elif wahl == "3":
            artikel_anzeigen(einkaufsliste)
        elif wahl == "4":
            artikel_suchen(einkaufsliste)
        elif wahl == "5":
            print("\nAuf Wiedersehen!")
            break
        else:
            print("Fehler: Ungültige Eingabe! Bitte wähle 1-5.")


if __name__ == "__main__":
    main()
