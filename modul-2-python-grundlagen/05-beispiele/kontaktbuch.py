"""
Kontaktbuch-Verwaltung
Demonstriert: Dictionaries, Listen, CRUD-Operationen, Suche
"""


def kontakt_erstellen(name: str, telefon: str, email: str = "", notizen: str = "") -> dict:
    """
    Erstellt einen neuen Kontakt.

    Args:
        name: Name des Kontakts
        telefon: Telefonnummer
        email: E-Mail-Adresse (optional)
        notizen: Zusätzliche Notizen (optional)

    Returns:
        Kontakt-Dictionary
    """
    return {
        "name": name,
        "telefon": telefon,
        "email": email,
        "notizen": notizen,
    }


def kontakt_hinzufuegen(kontakte: list, kontakt: dict) -> None:
    """
    Fügt einen Kontakt hinzu.

    Args:
        kontakte: Liste der Kontakte
        kontakt: Hinzuzufügender Kontakt
    """
    # Prüfen ob Kontakt bereits existiert
    if any(k["name"].lower() == kontakt["name"].lower() for k in kontakte):
        print(f"⚠️  Kontakt '{kontakt['name']}' existiert bereits!")
        return

    kontakte.append(kontakt)
    print(f"✓ Kontakt '{kontakt['name']}' hinzugefügt")


def kontakte_anzeigen(kontakte: list) -> None:
    """
    Zeigt alle Kontakte an.

    Args:
        kontakte: Liste der Kontakte
    """
    if not kontakte:
        print("📇 Keine Kontakte vorhanden")
        return

    # Sortieren nach Name
    sortiert = sorted(kontakte, key=lambda k: k["name"].lower())

    print(f"\n📇 KONTAKTBUCH ({len(kontakte)} Kontakte)")
    print("=" * 70)

    for kontakt in sortiert:
        print(f"\n👤 {kontakt['name']}")
        print(f"   📞 {kontakt['telefon']}")
        if kontakt["email"]:
            print(f"   📧 {kontakt['email']}")
        if kontakt["notizen"]:
            print(f"   📝 {kontakt['notizen']}")


def kontakt_suchen(kontakte: list, suchbegriff: str) -> list:
    """
    Sucht Kontakte nach Namen, Telefon oder E-Mail.

    Args:
        kontakte: Liste der Kontakte
        suchbegriff: Suchbegriff

    Returns:
        Liste der gefundenen Kontakte
    """
    suchbegriff = suchbegriff.lower()

    ergebnisse = []
    for kontakt in kontakte:
        if (
            suchbegriff in kontakt["name"].lower()
            or suchbegriff in kontakt["telefon"]
            or suchbegriff in kontakt["email"].lower()
        ):
            ergebnisse.append(kontakt)

    return ergebnisse


def kontakt_bearbeiten(kontakte: list, name: str) -> bool:
    """
    Bearbeitet einen Kontakt.

    Args:
        kontakte: Liste der Kontakte
        name: Name des zu bearbeitenden Kontakts

    Returns:
        True wenn erfolgreich
    """
    for kontakt in kontakte:
        if kontakt["name"].lower() == name.lower():
            print(f"\nBearbeite '{kontakt['name']}'")
            print("(Enter drücken um Feld beizubehalten)\n")

            # Neue Werte eingeben
            neuer_name = input(f"Name [{kontakt['name']}]: ") or kontakt["name"]
            neues_telefon = input(f"Telefon [{kontakt['telefon']}]: ") or kontakt["telefon"]
            neue_email = input(f"E-Mail [{kontakt['email']}]: ") or kontakt["email"]
            neue_notizen = input(f"Notizen [{kontakt['notizen']}]: ") or kontakt["notizen"]

            # Aktualisieren
            kontakt["name"] = neuer_name
            kontakt["telefon"] = neues_telefon
            kontakt["email"] = neue_email
            kontakt["notizen"] = neue_notizen

            print(f"✓ Kontakt '{neuer_name}' aktualisiert")
            return True

    print(f"❌ Kontakt '{name}' nicht gefunden")
    return False


def kontakt_loeschen(kontakte: list, name: str) -> bool:
    """
    Löscht einen Kontakt.

    Args:
        kontakte: Liste der Kontakte
        name: Name des zu löschenden Kontakts

    Returns:
        True wenn erfolgreich
    """
    for i, kontakt in enumerate(kontakte):
        if kontakt["name"].lower() == name.lower():
            # Bestätigung
            bestaetigung = input(f"Kontakt '{kontakt['name']}' wirklich löschen? (j/n): ")
            if bestaetigung.lower() == "j":
                kontakte.pop(i)
                print(f"✓ Kontakt '{name}' gelöscht")
                return True
            else:
                print("❌ Löschen abgebrochen")
                return False

    print(f"❌ Kontakt '{name}' nicht gefunden")
    return False


def statistik_anzeigen(kontakte: list) -> None:
    """
    Zeigt Statistiken des Kontaktbuchs.

    Args:
        kontakte: Liste der Kontakte
    """
    if not kontakte:
        print("📊 Keine Kontakte vorhanden")
        return

    # Statistiken berechnen
    gesamt = len(kontakte)
    mit_email = sum(1 for k in kontakte if k["email"])
    mit_notizen = sum(1 for k in kontakte if k["notizen"])

    # Buchstaben-Verteilung
    buchstaben = {}
    for kontakt in kontakte:
        erster_buchstabe = kontakt["name"][0].upper()
        buchstaben[erster_buchstabe] = buchstaben.get(erster_buchstabe, 0) + 1

    print(f"\n📊 STATISTIK")
    print("=" * 30)
    print(f"Gesamt:         {gesamt}")
    print(f"Mit E-Mail:     {mit_email} ({(mit_email/gesamt)*100:.1f}%)")
    print(f"Mit Notizen:    {mit_notizen} ({(mit_notizen/gesamt)*100:.1f}%)")

    print(f"\nAnfangsbuchstaben:")
    for buchstabe in sorted(buchstaben.keys()):
        anzahl = buchstaben[buchstabe]
        balken = "█" * anzahl
        print(f"  {buchstabe}: {balken} ({anzahl})")


def demo_daten_laden(kontakte: list) -> None:
    """
    Lädt Demo-Kontakte.

    Args:
        kontakte: Liste der Kontakte
    """
    demo = [
        ("Anna Müller", "079 123 45 67", "anna@example.com", "Kollegin aus Kurs"),
        ("Beat Meier", "078 987 65 43", "beat.meier@mail.ch", ""),
        ("Claudia Weber", "076 555 11 22", "", "Nachbarin"),
        ("Daniel Fischer", "077 444 33 22", "d.fischer@example.com", "Python-Experte"),
    ]

    for name, telefon, email, notizen in demo:
        kontakt = kontakt_erstellen(name, telefon, email, notizen)
        kontakte.append(kontakt)

    print(f"✓ {len(demo)} Demo-Kontakte geladen")


def main() -> None:
    """Hauptfunktion - Interaktives Kontaktbuch."""
    kontakte = []

    print("=" * 40)
    print("  📇 KONTAKTBUCH")
    print("=" * 40)

    # Demo-Daten laden?
    if input("\nDemo-Kontakte laden? (j/n): ").lower() == "j":
        demo_daten_laden(kontakte)

    while True:
        print("\n1. Kontakt hinzufügen")
        print("2. Alle Kontakte anzeigen")
        print("3. Kontakt suchen")
        print("4. Kontakt bearbeiten")
        print("5. Kontakt löschen")
        print("6. Statistik anzeigen")
        print("7. Beenden")

        wahl = input("\nWähle (1-7): ")

        if wahl == "1":
            print("\n--- Neuer Kontakt ---")
            name = input("Name: ")
            telefon = input("Telefon: ")
            email = input("E-Mail (optional): ")
            notizen = input("Notizen (optional): ")

            if name and telefon:
                kontakt = kontakt_erstellen(name, telefon, email, notizen)
                kontakt_hinzufuegen(kontakte, kontakt)
            else:
                print("❌ Name und Telefon sind erforderlich!")

        elif wahl == "2":
            kontakte_anzeigen(kontakte)

        elif wahl == "3":
            suchbegriff = input("Suchbegriff: ")
            ergebnisse = kontakt_suchen(kontakte, suchbegriff)

            if ergebnisse:
                print(f"\n🔍 {len(ergebnisse)} Ergebnis(se) gefunden:")
                for kontakt in ergebnisse:
                    print(f"\n👤 {kontakt['name']}")
                    print(f"   📞 {kontakt['telefon']}")
                    if kontakt["email"]:
                        print(f"   📧 {kontakt['email']}")
            else:
                print(f"❌ Keine Kontakte mit '{suchbegriff}' gefunden")

        elif wahl == "4":
            name = input("Name des Kontakts: ")
            kontakt_bearbeiten(kontakte, name)

        elif wahl == "5":
            name = input("Name des Kontakts: ")
            kontakt_loeschen(kontakte, name)

        elif wahl == "6":
            statistik_anzeigen(kontakte)

        elif wahl == "7":
            print(f"\n👋 Kontaktbuch wird geschlossen ({len(kontakte)} Kontakte)")
            break

        else:
            print("❌ Ungültige Wahl!")


if __name__ == "__main__":
    main()
