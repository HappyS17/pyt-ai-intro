"""
Passwort-Validator
Demonstriert: Bedingungen, String-Methoden, Boolean-Logik
"""


def validiere_passwort(passwort: str) -> tuple[bool, list[str]]:
    """
    Validiert ein Passwort anhand mehrerer Kriterien.

    Kriterien:
    - Mindestens 8 Zeichen lang
    - Mindestens 1 Grossbuchstabe
    - Mindestens 1 Kleinbuchstabe
    - Mindestens 1 Ziffer
    - Mindestens 1 Sonderzeichen

    Args:
        passwort: Zu validierendes Passwort

    Returns:
        Tuple (ist_gueltig, fehler_liste)
    """
    fehler = []

    # Länge prüfen
    if len(passwort) < 8:
        fehler.append("❌ Mindestens 8 Zeichen erforderlich")

    # Grossbuchstaben prüfen
    if not any(c.isupper() for c in passwort):
        fehler.append("❌ Mindestens 1 Grossbuchstabe erforderlich")

    # Kleinbuchstaben prüfen
    if not any(c.islower() for c in passwort):
        fehler.append("❌ Mindestens 1 Kleinbuchstabe erforderlich")

    # Ziffern prüfen
    if not any(c.isdigit() for c in passwort):
        fehler.append("❌ Mindestens 1 Ziffer erforderlich")

    # Sonderzeichen prüfen
    sonderzeichen = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in sonderzeichen for c in passwort):
        fehler.append("❌ Mindestens 1 Sonderzeichen erforderlich")

    ist_gueltig = len(fehler) == 0

    return ist_gueltig, fehler


def berechne_passwort_staerke(passwort: str) -> str:
    """
    Berechnet die Stärke eines Passworts.

    Args:
        passwort: Zu bewertendes Passwort

    Returns:
        Stärke als String ("schwach", "mittel", "stark", "sehr stark")
    """
    punkte = 0

    # Länge
    if len(passwort) >= 8:
        punkte += 1
    if len(passwort) >= 12:
        punkte += 1
    if len(passwort) >= 16:
        punkte += 1

    # Zeichenvielfalt
    if any(c.isupper() for c in passwort):
        punkte += 1
    if any(c.islower() for c in passwort):
        punkte += 1
    if any(c.isdigit() for c in passwort):
        punkte += 1
    if any(not c.isalnum() for c in passwort):
        punkte += 1

    # Klassifizierung
    if punkte <= 2:
        return "schwach"
    elif punkte <= 4:
        return "mittel"
    elif punkte <= 6:
        return "stark"
    else:
        return "sehr stark"


def zeige_passwort_staerke_visuell(staerke: str) -> str:
    """
    Erstellt visuelle Darstellung der Passwortstärke.

    Args:
        staerke: Stärke als String

    Returns:
        Visueller Balken
    """
    staerke_map = {
        "schwach": ("🔴", "████░░░░░░"),
        "mittel": ("🟡", "██████░░░░"),
        "stark": ("🟢", "████████░░"),
        "sehr stark": ("🟢", "██████████"),
    }

    emoji, balken = staerke_map.get(staerke, ("⚪", "░░░░░░░░░░"))
    return f"{emoji} {balken}"


def main() -> None:
    """Hauptfunktion - Interaktiver Passwort-Validator."""
    print("=== PASSWORT-VALIDATOR ===\n")

    # Eingabe (in Produktion: getpass verwenden!)
    passwort = input("Passwort eingeben: ")

    # Validierung
    ist_gueltig, fehler = validiere_passwort(passwort)
    staerke = berechne_passwort_staerke(passwort)
    visuell = zeige_passwort_staerke_visuell(staerke)

    # Ausgabe
    print(f"\n📊 ANALYSE")
    print("─" * 40)
    print(f"Länge: {len(passwort)} Zeichen")
    print(f"Stärke: {staerke.upper()} {visuell}")

    if ist_gueltig:
        print("\n✓ Passwort erfüllt alle Kriterien!")
    else:
        print("\n✗ Passwort erfüllt nicht alle Kriterien:")
        for fehler_msg in fehler:
            print(f"  {fehler_msg}")

    # Kriterien anzeigen
    print(f"\n💡 KRITERIEN")
    print("─" * 40)
    kriterien = [
        ("Mindestens 8 Zeichen", len(passwort) >= 8),
        ("Grossbuchstabe", any(c.isupper() for c in passwort)),
        ("Kleinbuchstabe", any(c.islower() for c in passwort)),
        ("Ziffer", any(c.isdigit() for c in passwort)),
        ("Sonderzeichen", any(not c.isalnum() for c in passwort)),
    ]

    for kriterium, erfuellt in kriterien:
        symbol = "✓" if erfuellt else "✗"
        print(f"{symbol} {kriterium}")


def demo_passwort_tests() -> None:
    """Demonstriert Validator mit verschiedenen Passwörtern."""
    print("\n=== TEST-PASSWÖRTER ===\n")

    test_passwoerter = [
        "pass",
        "password",
        "Password1",
        "P@ssw0rd",
        "MySecure123!",
        "Sup3r$ecur3P@ssw0rd!",
    ]

    print(f"{'Passwort':<20} {'Gültig':<8} {'Stärke':<12} {'Visualisierung'}")
    print("─" * 70)

    for pw in test_passwoerter:
        gueltig, _ = validiere_passwort(pw)
        staerke = berechne_passwort_staerke(pw)
        visuell = zeige_passwort_staerke_visuell(staerke)

        gueltig_symbol = "✓" if gueltig else "✗"
        print(f"{pw:<20} {gueltig_symbol:<8} {staerke:<12} {visuell}")


if __name__ == "__main__":
    main()

    # Optional: Weitere Tests zeigen
    antwort = input("\nTest-Passwörter zeigen? (j/n): ")
    if antwort.lower() == "j":
        demo_passwort_tests()
