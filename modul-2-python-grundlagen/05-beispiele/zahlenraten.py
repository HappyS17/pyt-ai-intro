"""
Zahlenratespiel
Demonstriert: Schleifen, Bedingungen, Zufallszahlen, Benutzereingabe
"""

import random


def zahlenraten_spiel(min_zahl: int = 1, max_zahl: int = 100, max_versuche: int = 7) -> None:
    """
    Spielt ein Zahlenratespiel.

    Args:
        min_zahl: Kleinste mögliche Zahl
        max_zahl: Grösste mögliche Zahl
        max_versuche: Maximale Anzahl Versuche
    """
    # Zufallszahl generieren
    geheimzahl = random.randint(min_zahl, max_zahl)
    versuche = 0

    print(f"\n🎲 Ich habe mir eine Zahl zwischen {min_zahl} und {max_zahl} ausgedacht.")
    print(f"Du hast {max_versuche} Versuche!\n")

    while versuche < max_versuche:
        try:
            # Eingabe
            tipp = int(input(f"Versuch {versuche + 1}/{max_versuche}: "))

            # Validierung
            if tipp < min_zahl or tipp > max_zahl:
                print(f"⚠️  Bitte eine Zahl zwischen {min_zahl} und {max_zahl} eingeben!")
                continue

            versuche += 1

            # Prüfung
            if tipp == geheimzahl:
                print(f"\n🎉 GLÜCKWUNSCH! Du hast die Zahl in {versuche} Versuch(en) erraten!")
                return
            elif tipp < geheimzahl:
                print("📈 Zu niedrig!")
            else:
                print("📉 Zu hoch!")

            # Verbleibende Versuche
            verbleibend = max_versuche - versuche
            if verbleibend > 0:
                print(f"   Noch {verbleibend} Versuch(e) übrig.\n")

        except ValueError:
            print("❌ Bitte eine gültige Zahl eingeben!\n")

    # Spiel verloren
    print(f"\n😢 Leider verloren! Die Zahl war {geheimzahl}.")


def berechne_optimale_strategie(min_zahl: int, max_zahl: int) -> int:
    """
    Berechnet die optimale Anzahl Versuche (Binäre Suche).

    Args:
        min_zahl: Kleinste Zahl
        max_zahl: Grösste Zahl

    Returns:
        Minimale Anzahl Versuche im schlechtesten Fall
    """
    import math
    bereich = max_zahl - min_zahl + 1
    return math.ceil(math.log2(bereich))


def schwierigkeitsgrad_waehlen() -> tuple[int, int, int]:
    """
    Lässt Benutzer Schwierigkeitsgrad wählen.

    Returns:
        Tuple (min_zahl, max_zahl, max_versuche)
    """
    print("\n=== SCHWIERIGKEITSGRAD ===")
    print("1. Einfach    (1-50,  8 Versuche)")
    print("2. Normal     (1-100, 7 Versuche)")
    print("3. Schwer     (1-200, 8 Versuche)")
    print("4. Experte    (1-500, 9 Versuche)")

    while True:
        try:
            wahl = input("\nWähle (1-4): ")

            if wahl == "1":
                return 1, 50, 8
            elif wahl == "2":
                return 1, 100, 7
            elif wahl == "3":
                return 1, 200, 8
            elif wahl == "4":
                return 1, 500, 9
            else:
                print("❌ Bitte 1-4 wählen!")

        except:
            print("❌ Ungültige Eingabe!")


def statistik_anzeigen(gespielt: int, gewonnen: int) -> None:
    """
    Zeigt Spiel-Statistik an.

    Args:
        gespielt: Anzahl gespielter Spiele
        gewonnen: Anzahl gewonnener Spiele
    """
    if gespielt == 0:
        return

    gewinnrate = (gewonnen / gespielt) * 100

    print(f"\n📊 STATISTIK")
    print("─" * 30)
    print(f"Gespielt: {gespielt}")
    print(f"Gewonnen: {gewonnen}")
    print(f"Verloren: {gespielt - gewonnen}")
    print(f"Gewinnrate: {gewinnrate:.1f}%")


def main() -> None:
    """Hauptfunktion - Spiel-Loop."""
    print("=" * 40)
    print("  🎯 ZAHLENRATESPIEL")
    print("=" * 40)

    gespielt = 0
    gewonnen = 0

    while True:
        # Schwierigkeit wählen
        min_zahl, max_zahl, max_versuche = schwierigkeitsgrad_waehlen()

        # Tipp zur Strategie
        optimale_versuche = berechne_optimale_strategie(min_zahl, max_zahl)
        print(f"\n💡 Tipp: Mit binärer Suche brauchst du maximal {optimale_versuche} Versuche!")

        # Spiel starten
        zahlenraten_spiel(min_zahl, max_zahl, max_versuche)
        gespielt += 1

        # TODO: Tracken ob gewonnen (erfordert Refactoring von zahlenraten_spiel)
        # Für Demo: Benutzer selbst fragen
        if input("\nHast du gewonnen? (j/n): ").lower() == "j":
            gewonnen += 1

        # Statistik zeigen
        statistik_anzeigen(gespielt, gewonnen)

        # Nochmal spielen?
        nochmal = input("\nNochmal spielen? (j/n): ")
        if nochmal.lower() != "j":
            print("\n👋 Danke fürs Spielen!")
            break


if __name__ == "__main__":
    main()
