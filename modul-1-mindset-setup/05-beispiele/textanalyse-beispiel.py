"""
Textanalyse mit Wortfrequenz
Verwendung: Lektion 1 - Live-Demo
Zeigt Problemdekomposition und algorithmisches Denken
"""

def analysiere_text(text):
    """
    Analysiert einen Text und gibt Statistiken zurück.
    
    Args:
        text (str): Der zu analysierende Text
    
    Returns:
        dict: Dictionary mit Statistiken
    """
    # Wörter zählen
    woerter = text.split()
    anzahl_woerter = len(woerter)
    
    # Zeichen zählen (mit und ohne Leerzeichen)
    anzahl_zeichen_mit = len(text)
    anzahl_zeichen_ohne = len(text.replace(" ", ""))
    
    # Längstes Wort finden
    laengstes_wort = max(woerter, key=len) if woerter else ""
    
    # Wortfrequenz berechnen
    frequenz = {}
    for wort in woerter:
        wort_lower = wort.lower()
        frequenz[wort_lower] = frequenz.get(wort_lower, 0) + 1
    
    # Ergebnisse zurückgeben
    return {
        "anzahl_woerter": anzahl_woerter,
        "anzahl_zeichen_mit": anzahl_zeichen_mit,
        "anzahl_zeichen_ohne": anzahl_zeichen_ohne,
        "laengstes_wort": laengstes_wort,
        "frequenz": frequenz
    }


def zeige_ergebnisse(ergebnisse):
    """
    Zeigt die Analyse-Ergebnisse formatiert an.
    
    Args:
        ergebnisse (dict): Dictionary mit Statistiken
    """
    print("\n" + "=" * 50)
    print("TEXTANALYSE-ERGEBNISSE")
    print("=" * 50)
    print(f"Anzahl Wörter: {ergebnisse['anzahl_woerter']}")
    print(f"Anzahl Zeichen (mit Leerzeichen): {ergebnisse['anzahl_zeichen_mit']}")
    print(f"Anzahl Zeichen (ohne Leerzeichen): {ergebnisse['anzahl_zeichen_ohne']}")
    print(f"Längstes Wort: '{ergebnisse['laengstes_wort']}' ({len(ergebnisse['laengstes_wort'])} Zeichen)")
    
    print("\nWortfrequenz (Top 5):")
    # Sortiere nach Häufigkeit und zeige Top 5
    top_woerter = sorted(ergebnisse['frequenz'].items(), 
                        key=lambda x: x[1], 
                        reverse=True)[:5]
    
    for wort, anzahl in top_woerter:
        print(f"  '{wort}': {anzahl}x")
    print("=" * 50)


def main():
    """
    Hauptfunktion des Programms.
    """
    print("TEXTANALYSE-PROGRAMM")
    print("=" * 50)
    
    # Text vom Benutzer einlesen
    print("\nGeben Sie einen Text ein (oder 'quit' zum Beenden):")
    text = input("> ")
    
    # Beenden, wenn gewünscht
    if text.lower() == 'quit':
        print("Auf Wiedersehen!")
        return
    
    # Text analysieren
    ergebnisse = analysiere_text(text)
    
    # Ergebnisse anzeigen
    zeige_ergebnisse(ergebnisse)


if __name__ == "__main__":
    main()
