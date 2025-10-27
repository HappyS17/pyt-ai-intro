"""
Zahlenraten-Spiel
Verwendung: Lektion 3 - Prompt-Iteration Beispiel
Zeigt, wie ein Prompt iterativ verbessert wird
"""

import random


def spiel_starten():
    """
    Startet ein neues Zahlenraten-Spiel.
    """
    # Computer wählt zufällige Zahl zwischen 1 und 100
    ziel_zahl = random.randint(1, 100)
    versuche = 0
    
    print("\n" + "=" * 50)
    print("ZAHLENRATEN-SPIEL")
    print("=" * 50)
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt.")
    print("Versuche sie zu erraten!")
    print("(Gib 'quit' ein, um aufzugeben)")
    print("=" * 50)
    
    # Spiel-Schleife
    while True:
        # Eingabe vom Benutzer
        eingabe = input("\nDein Tipp: ")
        
        # Beenden prüfen
        if eingabe.lower() == 'quit':
            print(f"\nDie richtige Zahl war: {ziel_zahl}")
            print("Schade, dass du aufgibst!")
            break
        
        # Eingabe validieren
        try:
            tipp = int(eingabe)
        except ValueError:
            print("Fehler: Bitte gib eine gültige Zahl ein!")
            continue
        
        # Bereich prüfen
        if tipp < 1 or tipp > 100:
            print("Fehler: Die Zahl muss zwischen 1 und 100 liegen!")
            continue
        
        # Versuch zählen
        versuche += 1
        
        # Tipp prüfen
        if tipp < ziel_zahl:
            print("Zu niedrig! Versuche es nochmal.")
        elif tipp > ziel_zahl:
            print("Zu hoch! Versuche es nochmal.")
        else:
            # Gewonnen!
            print("\n" + "=" * 50)
            print("🎉 GLÜCKWUNSCH! 🎉")
            print(f"Du hast die Zahl {ziel_zahl} erraten!")
            print(f"Du hast {versuche} Versuche gebraucht.")
            print("=" * 50)
            break


def main():
    """
    Hauptfunktion mit Spiel-Schleife.
    """
    while True:
        # Spiel starten
        spiel_starten()
        
        # Nochmal spielen?
        nochmal = input("\nNochmal spielen? (ja/nein): ")
        if nochmal.lower() not in ['ja', 'j', 'yes', 'y']:
            print("\nDanke fürs Spielen! Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()
