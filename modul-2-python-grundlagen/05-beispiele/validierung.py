"""
Validierungsfunktionen-Modul
Demonstriert: Funktionen, Rückgabewerte, Dokumentation, Wiederverwendbarkeit
"""

import re


def validiere_email(email: str) -> bool:
    """
    Validiert eine E-Mail-Adresse.

    Args:
        email: Zu validierende E-Mail-Adresse

    Returns:
        True wenn E-Mail gültig

    Examples:
        >>> validiere_email("test@example.com")
        True
        >>> validiere_email("invalid.email")
        False
    """
    # Einfaches E-Mail-Pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validiere_telefon_ch(telefon: str) -> bool:
    """
    Validiert Schweizer Telefonnummer.

    Akzeptiert Formate:
    - 079 123 45 67
    - 0791234567
    - +41 79 123 45 67
    - +41791234567

    Args:
        telefon: Zu validierende Telefonnummer

    Returns:
        True wenn Telefonnummer gültig
    """
    # Leerzeichen entfernen
    clean = telefon.replace(" ", "").replace("-", "")

    # Schweizer Muster
    patterns = [
        r'^0[1-9]\d{8}$',          # 0791234567
        r'^\+41[1-9]\d{8}$',       # +41791234567
    ]

    return any(re.match(pattern, clean) for pattern in patterns)


def validiere_plz_ch(plz: str) -> bool:
    """
    Validiert Schweizer Postleitzahl (4-stellig).

    Args:
        plz: Zu validierende PLZ

    Returns:
        True wenn PLZ gültig

    Examples:
        >>> validiere_plz_ch("8000")
        True
        >>> validiere_plz_ch("123")
        False
    """
    return len(plz) == 4 and plz.isdigit() and 1000 <= int(plz) <= 9999


def validiere_iban_ch(iban: str) -> bool:
    """
    Validiert Schweizer IBAN (vereinfacht).

    Format: CH## #### #### #### #### #

    Args:
        iban: Zu validierende IBAN

    Returns:
        True wenn IBAN gültig (Format-Check, keine Prüfsumme)
    """
    # Leerzeichen entfernen
    clean = iban.replace(" ", "").upper()

    # Schweizer IBAN: CH + 2 Prüfziffern + 5 Bankcode + 12 Kontonummer
    if not clean.startswith("CH"):
        return False

    if len(clean) != 21:
        return False

    # Prüfe ob nach CH nur Ziffern folgen
    return clean[2:].isdigit()


def validiere_url(url: str) -> bool:
    """
    Validiert URL (vereinfacht).

    Args:
        url: Zu validierende URL

    Returns:
        True wenn URL gültig

    Examples:
        >>> validiere_url("https://www.example.com")
        True
        >>> validiere_url("example.com")
        False
    """
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern, url) is not None


def validiere_passwort_staerke(passwort: str) -> tuple[bool, str]:
    """
    Validiert Passwortstärke.

    Kriterien:
    - Mindestens 8 Zeichen
    - Mindestens 1 Grossbuchstabe
    - Mindestens 1 Kleinbuchstabe
    - Mindestens 1 Ziffer

    Args:
        passwort: Zu validierendes Passwort

    Returns:
        Tuple (ist_gueltig, fehler_nachricht)
    """
    if len(passwort) < 8:
        return False, "Passwort muss mindestens 8 Zeichen lang sein"

    if not any(c.isupper() for c in passwort):
        return False, "Passwort muss mindestens 1 Grossbuchstaben enthalten"

    if not any(c.islower() for c in passwort):
        return False, "Passwort muss mindestens 1 Kleinbuchstaben enthalten"

    if not any(c.isdigit() for c in passwort):
        return False, "Passwort muss mindestens 1 Ziffer enthalten"

    return True, "Passwort ist stark"


def validiere_kreditkarte(nummer: str) -> bool:
    """
    Validiert Kreditkartennummer mit Luhn-Algorithmus.

    Args:
        nummer: Kreditkartennummer (mit oder ohne Leerzeichen)

    Returns:
        True wenn Nummer gültig
    """
    # Leerzeichen und Bindestriche entfernen
    clean = nummer.replace(" ", "").replace("-", "")

    # Nur Ziffern erlaubt
    if not clean.isdigit():
        return False

    # Länge prüfen (13-19 Ziffern für gängige Karten)
    if not 13 <= len(clean) <= 19:
        return False

    # Luhn-Algorithmus
    def luhn_checksum(card_number: str) -> bool:
        def digits_of(n: str) -> list[int]:
            return [int(d) for d in n]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(str(d * 2)))

        return checksum % 10 == 0

    return luhn_checksum(clean)


def validiere_ahv_nummer(ahv: str) -> bool:
    """
    Validiert Schweizer AHV-Nummer (vereinfacht).

    Format: 756.XXXX.XXXX.XX

    Args:
        ahv: AHV-Nummer

    Returns:
        True wenn Format gültig
    """
    # Punkte entfernen
    clean = ahv.replace(".", "")

    # Muss mit 756 beginnen (Schweiz)
    if not clean.startswith("756"):
        return False

    # Muss 13 Ziffern haben
    if len(clean) != 13 or not clean.isdigit():
        return False

    return True


def validiere_datum(datum: str, format: str = "%Y-%m-%d") -> bool:
    """
    Validiert Datum-String.

    Args:
        datum: Datum als String
        format: Erwartetes Format (Standard: YYYY-MM-DD)

    Returns:
        True wenn Datum gültig

    Examples:
        >>> validiere_datum("2025-01-15")
        True
        >>> validiere_datum("2025-13-01")  # Monat 13 existiert nicht
        False
    """
    from datetime import datetime

    try:
        datetime.strptime(datum, format)
        return True
    except ValueError:
        return False


def validiere_alter(alter: int, min_alter: int = 0, max_alter: int = 120) -> bool:
    """
    Validiert Altersangabe.

    Args:
        alter: Alter in Jahren
        min_alter: Mindestalter (Standard: 0)
        max_alter: Maximalalter (Standard: 120)

    Returns:
        True wenn Alter im gültigen Bereich
    """
    return min_alter <= alter <= max_alter


def demo_validierungen() -> None:
    """Demonstriert alle Validierungsfunktionen."""
    print("=" * 70)
    print("  ✅ VALIDIERUNGSFUNKTIONEN-DEMO")
    print("=" * 70)

    # Test-Daten
    tests = [
        ("E-Mail", validiere_email, [
            ("test@example.com", True),
            ("invalid.email", False),
            ("name@domain.co.uk", True),
        ]),
        ("Telefon CH", validiere_telefon_ch, [
            ("079 123 45 67", True),
            ("+41 79 123 45 67", True),
            ("123", False),
        ]),
        ("PLZ CH", validiere_plz_ch, [
            ("8000", True),
            ("1234", True),
            ("123", False),
            ("10000", False),
        ]),
        ("IBAN CH", validiere_iban_ch, [
            ("CH93 0076 2011 6238 5295 7", True),
            ("DE89 3704 0044 0532 0130 00", False),
            ("CH12345", False),
        ]),
        ("URL", validiere_url, [
            ("https://www.example.com", True),
            ("http://example.com/path", True),
            ("example.com", False),
        ]),
        ("Kreditkarte", validiere_kreditkarte, [
            ("4532 1488 0343 6467", True),  # Visa Test
            ("1234 5678 9012 3456", False),  # Ungültig
        ]),
        ("AHV-Nummer", validiere_ahv_nummer, [
            ("756.1234.5678.97", True),
            ("123.4567.8901.23", False),
        ]),
        ("Datum", validiere_datum, [
            ("2025-01-15", True),
            ("2025-13-01", False),
            ("2025-02-30", False),
        ]),
    ]

    for kategorie, funktion, test_faelle in tests:
        print(f"\n{kategorie}")
        print("─" * 40)

        for eingabe, erwartet in test_faelle:
            ergebnis = funktion(eingabe)
            symbol = "✓" if ergebnis == erwartet else "✗"
            status = "PASS" if ergebnis == erwartet else "FAIL"

            print(f"{symbol} {eingabe:30} -> {ergebnis} [{status}]")


def interaktive_validierung() -> None:
    """Interaktive Validierung von Benutzereingaben."""
    print("\n" + "=" * 70)
    print("  🔍 INTERAKTIVE VALIDIERUNG")
    print("=" * 70)

    while True:
        print("\n1. E-Mail validieren")
        print("2. Telefon (CH) validieren")
        print("3. PLZ (CH) validieren")
        print("4. IBAN (CH) validieren")
        print("5. URL validieren")
        print("6. Passwort-Stärke prüfen")
        print("7. Zurück")

        wahl = input("\nWähle (1-7): ")

        if wahl == "1":
            email = input("E-Mail-Adresse: ")
            if validiere_email(email):
                print("✓ E-Mail ist gültig")
            else:
                print("✗ E-Mail ist ungültig")

        elif wahl == "2":
            telefon = input("Telefonnummer: ")
            if validiere_telefon_ch(telefon):
                print("✓ Telefonnummer ist gültig")
            else:
                print("✗ Telefonnummer ist ungültig")

        elif wahl == "3":
            plz = input("PLZ: ")
            if validiere_plz_ch(plz):
                print("✓ PLZ ist gültig")
            else:
                print("✗ PLZ ist ungültig (muss 4-stellig sein, 1000-9999)")

        elif wahl == "4":
            iban = input("IBAN: ")
            if validiere_iban_ch(iban):
                print("✓ IBAN ist gültig")
            else:
                print("✗ IBAN ist ungültig")

        elif wahl == "5":
            url = input("URL: ")
            if validiere_url(url):
                print("✓ URL ist gültig")
            else:
                print("✗ URL ist ungültig (muss mit http:// oder https:// beginnen)")

        elif wahl == "6":
            passwort = input("Passwort: ")
            gueltig, nachricht = validiere_passwort_staerke(passwort)
            if gueltig:
                print(f"✓ {nachricht}")
            else:
                print(f"✗ {nachricht}")

        elif wahl == "7":
            break

        else:
            print("❌ Ungültige Wahl")


def main() -> None:
    """Hauptfunktion."""
    # Demo
    demo_validierungen()

    # Interaktiv
    if input("\nInteraktive Validierung starten? (j/n): ").lower() == "j":
        interaktive_validierung()

    print("\n👋 Programm beendet")


if __name__ == "__main__":
    main()
