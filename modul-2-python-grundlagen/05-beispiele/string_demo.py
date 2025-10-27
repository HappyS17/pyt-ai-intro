"""
String-Manipulationen Demo
Demonstriert: String-Methoden, Slicing, Formatierung, f-strings
"""


def string_operationen_demo() -> None:
    """Zeigt verschiedene String-Operationen."""
    text = "  Python ist grossartig!  "

    print("=== STRING-OPERATIONEN ===\n")

    # Grundlegende Methoden
    print("Original:", repr(text))
    print("strip():", text.strip())
    print("upper():", text.upper())
    print("lower():", text.lower())
    print("replace():", text.replace("Python", "Programmieren"))

    # String-Informationen
    print(f"\nLänge: {len(text)}")
    print(f"Beginnt mit '  Python': {text.startswith('  Python')}")
    print(f"Endet mit '!  ': {text.endswith('!  ')}")
    print(f"Enthält 'gross': {'gross' in text}")

    # String-Slicing
    wort = "Python"
    print(f"\n=== SLICING mit '{wort}' ===")
    print(f"wort[0]: {wort[0]}")        # Erstes Zeichen
    print(f"wort[-1]: {wort[-1]}")      # Letztes Zeichen
    print(f"wort[0:3]: {wort[0:3]}")    # Erste 3 Zeichen
    print(f"wort[::2]: {wort[::2]}")    # Jedes 2. Zeichen
    print(f"wort[::-1]: {wort[::-1]}")  # Rückwärts


def string_formatierung_demo() -> None:
    """Zeigt verschiedene String-Formatierungsmethoden."""
    name = "Anna"
    alter = 25
    note = 1.75

    print("\n=== STRING-FORMATIERUNG ===\n")

    # f-strings (modern, empfohlen)
    print(f"f-string: {name} ist {alter} Jahre alt.")
    print(f"Mit Berechnung: {name} wird in 10 Jahren {alter + 10} sein.")
    print(f"Zahlenformatierung: Note: {note:.1f}")

    # format() Methode
    print("\nformat(): {} ist {} Jahre alt.".format(name, alter))

    # % Operator (veraltet, aber manchmal gesehen)
    print("\n%%-Operator: %s ist %d Jahre alt." % (name, alter))

    # Erweiterte Formatierung
    preis = 19.99
    print(f"\nPreis: {preis:>10.2f} CHF")  # Rechtsbündig, 10 Zeichen, 2 Dezimalen
    print(f"Prozent: {0.856:.1%}")         # Als Prozent mit 1 Dezimale


def text_analyse(text: str) -> dict:
    """
    Analysiert einen Text.

    Args:
        text: Zu analysierender Text

    Returns:
        Dictionary mit Statistiken
    """
    woerter = text.split()

    return {
        "zeichen": len(text),
        "zeichen_ohne_leerzeichen": len(text.replace(" ", "")),
        "woerter": len(woerter),
        "saetze": text.count(".") + text.count("!") + text.count("?"),
        "grossbuchstaben": sum(1 for c in text if c.isupper()),
        "kleinbuchstaben": sum(1 for c in text if c.islower()),
        "ziffern": sum(1 for c in text if c.isdigit()),
    }


def palindrom_pruefer(text: str) -> bool:
    """
    Prüft, ob ein Text ein Palindrom ist.

    Args:
        text: Zu prüfender Text

    Returns:
        True wenn Palindrom, sonst False
    """
    # Text normalisieren: Kleinbuchstaben, nur Buchstaben
    clean = "".join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]


def main() -> None:
    """Hauptfunktion - Demonstriert alle String-Funktionen."""
    # Operationen
    string_operationen_demo()

    # Formatierung
    string_formatierung_demo()

    # Text-Analyse
    print("\n=== TEXT-ANALYSE ===\n")
    beispiel_text = "Python 3.11 ist toll! Es macht Spass zu lernen."
    stats = text_analyse(beispiel_text)

    print(f"Text: '{beispiel_text}'\n")
    for key, value in stats.items():
        print(f"{key:25}: {value}")

    # Palindrom-Prüfung
    print("\n=== PALINDROM-PRÜFER ===\n")
    test_woerter = ["Anna", "Racecar", "Python", "Otto", "Lagerregal"]
    for wort in test_woerter:
        ist_palindrom = palindrom_pruefer(wort)
        symbol = "✓" if ist_palindrom else "✗"
        print(f"{symbol} {wort:12} -> {ist_palindrom}")


if __name__ == "__main__":
    main()
