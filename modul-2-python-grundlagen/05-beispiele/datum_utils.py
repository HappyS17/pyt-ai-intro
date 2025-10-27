"""
Datums-Utilities
Demonstriert: datetime-Modul, Datums-Berechnungen, Formatierung
"""

from datetime import datetime, date, timedelta


def aktuelles_datum() -> date:
    """
    Gibt das aktuelle Datum zurück.

    Returns:
        Heutiges Datum
    """
    return date.today()


def aktuelle_zeit() -> datetime:
    """
    Gibt aktuelle Datum und Zeit zurück.

    Returns:
        Aktueller Zeitpunkt
    """
    return datetime.now()


def formatiere_datum(datum: date, format: str = "%d.%m.%Y") -> str:
    """
    Formatiert ein Datum als String.

    Args:
        datum: Zu formatierendes Datum
        format: Format-String (Standard: DD.MM.YYYY)

    Returns:
        Formatierter Datums-String

    Examples:
        >>> d = date(2025, 1, 15)
        >>> formatiere_datum(d)
        '15.01.2025'
        >>> formatiere_datum(d, "%Y-%m-%d")
        '2025-01-15'
    """
    return datum.strftime(format)


def parse_datum(datum_str: str, format: str = "%Y-%m-%d") -> date:
    """
    Parst Datum-String zu date-Objekt.

    Args:
        datum_str: Datum als String
        format: Format des Strings (Standard: YYYY-MM-DD)

    Returns:
        date-Objekt

    Raises:
        ValueError: Wenn Datum ungültig
    """
    return datetime.strptime(datum_str, format).date()


def tage_bis(ziel_datum: date) -> int:
    """
    Berechnet Tage bis zu einem Ziel-Datum.

    Args:
        ziel_datum: Ziel-Datum

    Returns:
        Anzahl Tage (negativ wenn in der Vergangenheit)
    """
    heute = date.today()
    differenz = ziel_datum - heute
    return differenz.days


def tage_zwischen(datum1: date, datum2: date) -> int:
    """
    Berechnet Tage zwischen zwei Daten.

    Args:
        datum1: Erstes Datum
        datum2: Zweites Datum

    Returns:
        Anzahl Tage (Betrag)
    """
    return abs((datum2 - datum1).days)


def addiere_tage(datum: date, tage: int) -> date:
    """
    Addiert Tage zu einem Datum.

    Args:
        datum: Ausgangsdatum
        tage: Anzahl Tage (kann negativ sein)

    Returns:
        Neues Datum
    """
    return datum + timedelta(days=tage)


def naechster_wochentag(datum: date, wochentag: int) -> date:
    """
    Findet das nächste Auftreten eines Wochentags.

    Args:
        datum: Ausgangsdatum
        wochentag: Wochentag (0=Montag, 6=Sonntag)

    Returns:
        Datum des nächsten Wochentags
    """
    tage_bis_wochentag = (wochentag - datum.weekday()) % 7
    if tage_bis_wochentag == 0:
        tage_bis_wochentag = 7  # Nächste Woche
    return datum + timedelta(days=tage_bis_wochentag)


def ist_wochenende(datum: date) -> bool:
    """
    Prüft ob Datum ein Wochenende ist.

    Args:
        datum: Zu prüfendes Datum

    Returns:
        True wenn Samstag (5) oder Sonntag (6)
    """
    return datum.weekday() >= 5


def ist_schaltjahr(jahr: int) -> bool:
    """
    Prüft ob ein Jahr ein Schaltjahr ist.

    Args:
        jahr: Jahr

    Returns:
        True wenn Schaltjahr
    """
    return (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0)


def alter_berechnen(geburtsdatum: date) -> int:
    """
    Berechnet Alter in Jahren.

    Args:
        geburtsdatum: Geburtsdatum

    Returns:
        Alter in Jahren
    """
    heute = date.today()
    alter = heute.year - geburtsdatum.year

    # Korrektur wenn Geburtstag noch nicht war dieses Jahr
    if (heute.month, heute.day) < (geburtsdatum.month, geburtsdatum.day):
        alter -= 1

    return alter


def arbeitstage_zwischen(start: date, ende: date) -> int:
    """
    Zählt Arbeitstage (Mo-Fr) zwischen zwei Daten.

    Args:
        start: Startdatum
        ende: Enddatum

    Returns:
        Anzahl Arbeitstage
    """
    arbeitstage = 0
    aktuell = start

    while aktuell <= ende:
        if aktuell.weekday() < 5:  # Mo-Fr
            arbeitstage += 1
        aktuell += timedelta(days=1)

    return arbeitstage


def quartal(datum: date) -> int:
    """
    Gibt das Quartal eines Datums zurück.

    Args:
        datum: Datum

    Returns:
        Quartal (1-4)
    """
    return (datum.month - 1) // 3 + 1


def woche_des_jahres(datum: date) -> int:
    """
    Gibt die Kalenderwoche zurück.

    Args:
        datum: Datum

    Returns:
        Kalenderwoche (1-53)
    """
    return datum.isocalendar()[1]


def demo_datums_operationen() -> None:
    """Demonstriert Datums-Operationen."""
    print("=" * 70)
    print("  📅 DATUMS-UTILITIES DEMO")
    print("=" * 70)

    # Aktuelles Datum
    heute = aktuelles_datum()
    jetzt = aktuelle_zeit()

    print(f"\n📆 AKTUELLES DATUM & ZEIT")
    print("─" * 40)
    print(f"Datum:           {formatiere_datum(heute)}")
    print(f"ISO-Format:      {heute}")
    print(f"Zeit:            {jetzt.strftime('%H:%M:%S')}")
    print(f"Vollständig:     {jetzt.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"Wochentag:       {heute.strftime('%A')}")
    print(f"Kalenderwoche:   {woche_des_jahres(heute)}")
    print(f"Quartal:         Q{quartal(heute)}")
    print(f"Ist Wochenende:  {'Ja' if ist_wochenende(heute) else 'Nein'}")

    # Datum-Berechnungen
    print(f"\n📊 BERECHNUNGEN")
    print("─" * 40)

    # Wichtige Daten
    neujahr = date(heute.year, 1, 1)
    tage_seit_neujahr = tage_zwischen(neujahr, heute)
    print(f"Tage seit Neujahr:     {tage_seit_neujahr}")

    silvester = date(heute.year, 12, 31)
    tage_bis_silvester = tage_bis(silvester)
    print(f"Tage bis Silvester:    {tage_bis_silvester}")

    # Wochentage
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    print(f"\nNächste Wochentage:")
    for i, tag in enumerate(wochentage):
        naechster = naechster_wochentag(heute, i)
        print(f"  {tag:12} {formatiere_datum(naechster)}")

    # Datum-Arithmetik
    print(f"\n📈 DATUM-ARITHMETIK")
    print("─" * 40)
    print(f"Heute:             {formatiere_datum(heute)}")
    print(f"Vor 7 Tagen:       {formatiere_datum(addiere_tage(heute, -7))}")
    print(f"In 14 Tagen:       {formatiere_datum(addiere_tage(heute, 14))}")
    print(f"Vor 30 Tagen:      {formatiere_datum(addiere_tage(heute, -30))}")
    print(f"In 90 Tagen:       {formatiere_datum(addiere_tage(heute, 90))}")

    # Arbeitstage
    start_monat = date(heute.year, heute.month, 1)
    ende_monat = addiere_tage(start_monat, 31)
    # Korrigiere auf letzten Tag des Monats
    while ende_monat.month != heute.month:
        ende_monat = addiere_tage(ende_monat, -1)

    arbeitstage = arbeitstage_zwischen(start_monat, ende_monat)
    print(f"\nArbeitstage im {heute.strftime('%B')}: {arbeitstage}")

    # Alter berechnen
    print(f"\n🎂 ALTERSBERECHNUNG")
    print("─" * 40)
    test_geburtstage = [
        date(1990, 5, 15),
        date(2000, 12, 31),
        date(2010, 1, 1),
    ]

    for geburtsdatum in test_geburtstage:
        alter = alter_berechnen(geburtsdatum)
        print(f"{formatiere_datum(geburtsdatum)} → {alter} Jahre")

    # Schaltjahre
    print(f"\n📅 SCHALTJAHRE")
    print("─" * 40)
    for jahr in range(heute.year - 2, heute.year + 3):
        symbol = "✓" if ist_schaltjahr(jahr) else "✗"
        print(f"{jahr}: {symbol}")


def countdown_bis(ziel_datum: date, ereignis: str) -> None:
    """
    Zeigt Countdown bis zu einem Ereignis.

    Args:
        ziel_datum: Datum des Ereignisses
        ereignis: Name des Ereignisses
    """
    tage = tage_bis(ziel_datum)

    print(f"\n⏰ COUNTDOWN: {ereignis.upper()}")
    print("─" * 40)
    print(f"Datum:  {formatiere_datum(ziel_datum)}")

    if tage > 0:
        print(f"In:     {tage} Tage(n)")

        # Wochen und Tage
        wochen = tage // 7
        rest_tage = tage % 7
        print(f"        = {wochen} Woche(n) und {rest_tage} Tag(e)")

    elif tage == 0:
        print("Status: HEUTE! 🎉")
    else:
        print(f"Status: Vor {abs(tage)} Tag(en) (vorbei)")


def interaktive_datums_tools() -> None:
    """Interaktive Datums-Werkzeuge."""
    print("\n" + "=" * 70)
    print("  🛠️  INTERAKTIVE DATUMS-TOOLS")
    print("=" * 70)

    while True:
        print("\n1. Alter berechnen")
        print("2. Tage zwischen zwei Daten")
        print("3. Arbeitstage zählen")
        print("4. Countdown erstellen")
        print("5. Zurück")

        wahl = input("\nWähle (1-5): ")

        if wahl == "1":
            try:
                datum_str = input("Geburtsdatum (JJJJ-MM-TT): ")
                geburtsdatum = parse_datum(datum_str)
                alter = alter_berechnen(geburtsdatum)
                print(f"✓ Alter: {alter} Jahre")

                # Nächster Geburtstag
                naechster_geburtstag = date(date.today().year, geburtsdatum.month, geburtsdatum.day)
                if naechster_geburtstag < date.today():
                    naechster_geburtstag = date(date.today().year + 1, geburtsdatum.month, geburtsdatum.day)

                tage = tage_bis(naechster_geburtstag)
                print(f"🎂 Nächster Geburtstag in {tage} Tage(n)")

            except ValueError as e:
                print(f"❌ Ungültiges Datum: {e}")

        elif wahl == "2":
            try:
                datum1_str = input("Erstes Datum (JJJJ-MM-TT): ")
                datum2_str = input("Zweites Datum (JJJJ-MM-TT): ")

                datum1 = parse_datum(datum1_str)
                datum2 = parse_datum(datum2_str)

                tage = tage_zwischen(datum1, datum2)
                print(f"✓ Differenz: {tage} Tage")

            except ValueError as e:
                print(f"❌ Ungültiges Datum: {e}")

        elif wahl == "3":
            try:
                start_str = input("Startdatum (JJJJ-MM-TT): ")
                ende_str = input("Enddatum (JJJJ-MM-TT): ")

                start = parse_datum(start_str)
                ende = parse_datum(ende_str)

                arbeitstage = arbeitstage_zwischen(start, ende)
                gesamt_tage = tage_zwischen(start, ende)

                print(f"✓ Arbeitstage (Mo-Fr): {arbeitstage}")
                print(f"  Gesamt-Tage:         {gesamt_tage}")

            except ValueError as e:
                print(f"❌ Ungültiges Datum: {e}")

        elif wahl == "4":
            try:
                datum_str = input("Ziel-Datum (JJJJ-MM-TT): ")
                ereignis = input("Ereignis-Name: ")

                ziel = parse_datum(datum_str)
                countdown_bis(ziel, ereignis)

            except ValueError as e:
                print(f"❌ Ungültiges Datum: {e}")

        elif wahl == "5":
            break

        else:
            print("❌ Ungültige Wahl")


def main() -> None:
    """Hauptfunktion."""
    # Demo
    demo_datums_operationen()

    # Interaktiv
    if input("\nInteraktive Tools starten? (j/n): ").lower() == "j":
        interaktive_datums_tools()

    print("\n👋 Programm beendet")


if __name__ == "__main__":
    main()
