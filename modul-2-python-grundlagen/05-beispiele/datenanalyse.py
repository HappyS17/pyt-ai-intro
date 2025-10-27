"""
Verkaufsdaten-Analyse
Demonstriert: Listen, Dictionaries, Statistik-Berechnungen, Aggregation
"""


# Beispiel-Verkaufsdaten
VERKAUFSDATEN = [
    {"produkt": "Laptop", "kategorie": "Elektronik", "preis": 1200, "menge": 5},
    {"produkt": "Maus", "kategorie": "Elektronik", "preis": 25, "menge": 50},
    {"produkt": "Tastatur", "kategorie": "Elektronik", "preis": 80, "menge": 30},
    {"produkt": "Tisch", "kategorie": "Möbel", "preis": 350, "menge": 10},
    {"produkt": "Stuhl", "kategorie": "Möbel", "preis": 120, "menge": 25},
    {"produkt": "Buch", "kategorie": "Medien", "preis": 15, "menge": 100},
    {"produkt": "DVD", "kategorie": "Medien", "preis": 10, "menge": 80},
]


def berechne_umsatz(verkauf: dict) -> float:
    """
    Berechnet den Umsatz eines Verkaufs.

    Args:
        verkauf: Verkaufs-Dictionary

    Returns:
        Umsatz (Preis × Menge)
    """
    return verkauf["preis"] * verkauf["menge"]


def gesamtumsatz(verkaeufe: list) -> float:
    """
    Berechnet den Gesamtumsatz aller Verkäufe.

    Args:
        verkaeufe: Liste der Verkäufe

    Returns:
        Gesamtumsatz
    """
    return sum(berechne_umsatz(v) for v in verkaeufe)


def umsatz_nach_kategorie(verkaeufe: list) -> dict:
    """
    Gruppiert Umsatz nach Kategorie.

    Args:
        verkaeufe: Liste der Verkäufe

    Returns:
        Dictionary {kategorie: umsatz}
    """
    kategorien = {}

    for verkauf in verkaeufe:
        kategorie = verkauf["kategorie"]
        umsatz = berechne_umsatz(verkauf)
        kategorien[kategorie] = kategorien.get(kategorie, 0) + umsatz

    return kategorien


def top_produkte(verkaeufe: list, anzahl: int = 3) -> list:
    """
    Findet die Top-Produkte nach Umsatz.

    Args:
        verkaeufe: Liste der Verkäufe
        anzahl: Anzahl der Top-Produkte

    Returns:
        Liste der Top-Produkte (sortiert)
    """
    # Umsatz zu jedem Verkauf hinzufügen
    mit_umsatz = []
    for verkauf in verkaeufe:
        kopie = verkauf.copy()
        kopie["umsatz"] = berechne_umsatz(verkauf)
        mit_umsatz.append(kopie)

    # Nach Umsatz sortieren (absteigend)
    sortiert = sorted(mit_umsatz, key=lambda v: v["umsatz"], reverse=True)

    return sortiert[:anzahl]


def durchschnittspreis_nach_kategorie(verkaeufe: list) -> dict:
    """
    Berechnet den Durchschnittspreis pro Kategorie.

    Args:
        verkaeufe: Liste der Verkäufe

    Returns:
        Dictionary {kategorie: durchschnittspreis}
    """
    # Gruppieren nach Kategorie
    kategorien = {}
    for verkauf in verkaeufe:
        kategorie = verkauf["kategorie"]
        if kategorie not in kategorien:
            kategorien[kategorie] = []
        kategorien[kategorie].append(verkauf["preis"])

    # Durchschnitt berechnen
    durchschnitte = {}
    for kategorie, preise in kategorien.items():
        durchschnitte[kategorie] = sum(preise) / len(preise)

    return durchschnitte


def verkaufsstatistik(verkaeufe: list) -> dict:
    """
    Berechnet umfassende Statistiken.

    Args:
        verkaeufe: Liste der Verkäufe

    Returns:
        Dictionary mit Statistiken
    """
    if not verkaeufe:
        return {}

    # Alle Preise und Mengen
    preise = [v["preis"] for v in verkaeufe]
    mengen = [v["menge"] for v in verkaeufe]
    umsaetze = [berechne_umsatz(v) for v in verkaeufe]

    return {
        "anzahl_produkte": len(verkaeufe),
        "gesamtumsatz": sum(umsaetze),
        "durchschnittsumsatz": sum(umsaetze) / len(umsaetze),
        "hoechster_umsatz": max(umsaetze),
        "niedrigster_umsatz": min(umsaetze),
        "durchschnittspreis": sum(preise) / len(preise),
        "durchschnittsmenge": sum(mengen) / len(mengen),
        "gesamtmenge": sum(mengen),
    }


def balkendiagramm(daten: dict, breite: int = 50) -> None:
    """
    Zeigt ASCII-Balkendiagramm.

    Args:
        daten: Dictionary {label: wert}
        breite: Maximale Breite der Balken
    """
    if not daten:
        return

    # Maximaler Wert für Skalierung
    max_wert = max(daten.values())

    print()
    for label, wert in sorted(daten.items(), key=lambda x: x[1], reverse=True):
        # Balken-Länge berechnen
        balken_laenge = int((wert / max_wert) * breite)
        balken = "█" * balken_laenge

        # Formatierung
        print(f"{label:15} {balken} {wert:,.2f} CHF")


def hauptanalyse(verkaeufe: list) -> None:
    """
    Führt Haupt-Datenanalyse durch.

    Args:
        verkaeufe: Liste der Verkäufe
    """
    print("\n" + "=" * 70)
    print("  📊 VERKAUFSDATEN-ANALYSE")
    print("=" * 70)

    # 1. Gesamtstatistik
    stats = verkaufsstatistik(verkaeufe)

    print(f"\n📈 GESAMTSTATISTIK")
    print("─" * 40)
    print(f"Anzahl Produkte:       {stats['anzahl_produkte']}")
    print(f"Gesamtumsatz:          {stats['gesamtumsatz']:>10,.2f} CHF")
    print(f"Durchschnittsumsatz:   {stats['durchschnittsumsatz']:>10,.2f} CHF")
    print(f"Höchster Umsatz:       {stats['hoechster_umsatz']:>10,.2f} CHF")
    print(f"Niedrigster Umsatz:    {stats['niedrigster_umsatz']:>10,.2f} CHF")
    print(f"Durchschnittspreis:    {stats['durchschnittspreis']:>10,.2f} CHF")
    print(f"Gesamtmenge verkauft:  {stats['gesamtmenge']:>10}")

    # 2. Umsatz nach Kategorie
    print(f"\n💰 UMSATZ NACH KATEGORIE")
    print("─" * 40)
    kategorien_umsatz = umsatz_nach_kategorie(verkaeufe)
    balkendiagramm(kategorien_umsatz)

    # Prozentuale Verteilung
    gesamt = sum(kategorien_umsatz.values())
    print(f"\nProzentuale Verteilung:")
    for kategorie, umsatz in sorted(
        kategorien_umsatz.items(), key=lambda x: x[1], reverse=True
    ):
        prozent = (umsatz / gesamt) * 100
        print(f"  {kategorie:15} {prozent:>6.1f}%")

    # 3. Top-Produkte
    print(f"\n🏆 TOP 3 PRODUKTE")
    print("─" * 40)
    top = top_produkte(verkaeufe, 3)

    for i, produkt in enumerate(top, 1):
        medaillen = ["🥇", "🥈", "🥉"]
        medaille = medaillen[i - 1] if i <= 3 else "  "
        print(
            f"{medaille} {i}. {produkt['produkt']:15} "
            f"{produkt['umsatz']:>10,.2f} CHF "
            f"({produkt['menge']} × {produkt['preis']:.2f} CHF)"
        )

    # 4. Durchschnittspreis nach Kategorie
    print(f"\n💵 DURCHSCHNITTSPREIS NACH KATEGORIE")
    print("─" * 40)
    durchschnitte = durchschnittspreis_nach_kategorie(verkaeufe)

    for kategorie, preis in sorted(durchschnitte.items()):
        print(f"{kategorie:15} {preis:>10,.2f} CHF")


def interaktive_abfrage(verkaeufe: list) -> None:
    """
    Interaktive Datenabfrage.

    Args:
        verkaeufe: Liste der Verkäufe
    """
    print("\n" + "=" * 70)
    print("  🔍 INTERAKTIVE ABFRAGE")
    print("=" * 70)

    while True:
        print("\n1. Produkt nach Name suchen")
        print("2. Produkte nach Kategorie filtern")
        print("3. Produkte über bestimmtem Preis")
        print("4. Zurück")

        wahl = input("\nWähle (1-4): ")

        if wahl == "1":
            name = input("Produktname: ").lower()
            ergebnisse = [v for v in verkaeufe if name in v["produkt"].lower()]

            if ergebnisse:
                for v in ergebnisse:
                    umsatz = berechne_umsatz(v)
                    print(
                        f"  {v['produkt']:15} | "
                        f"{v['kategorie']:12} | "
                        f"{v['preis']:>6.2f} CHF | "
                        f"{v['menge']:>3} St. | "
                        f"Umsatz: {umsatz:>8.2f} CHF"
                    )
            else:
                print(f"❌ Keine Produkte mit '{name}' gefunden")

        elif wahl == "2":
            kategorie = input("Kategorie: ")
            ergebnisse = [v for v in verkaeufe if v["kategorie"].lower() == kategorie.lower()]

            if ergebnisse:
                gesamt = sum(berechne_umsatz(v) for v in ergebnisse)
                print(f"\n{len(ergebnisse)} Produkt(e) in '{kategorie}':")
                for v in ergebnisse:
                    print(f"  - {v['produkt']}: {v['preis']:.2f} CHF × {v['menge']}")
                print(f"Kategorie-Umsatz: {gesamt:.2f} CHF")
            else:
                print(f"❌ Keine Produkte in Kategorie '{kategorie}'")

        elif wahl == "3":
            try:
                min_preis = float(input("Mindestpreis (CHF): "))
                ergebnisse = [v for v in verkaeufe if v["preis"] >= min_preis]

                if ergebnisse:
                    print(f"\n{len(ergebnisse)} Produkt(e) über {min_preis:.2f} CHF:")
                    for v in sorted(ergebnisse, key=lambda x: x["preis"], reverse=True):
                        print(f"  {v['produkt']:15} {v['preis']:>8.2f} CHF")
                else:
                    print(f"❌ Keine Produkte über {min_preis:.2f} CHF")
            except ValueError:
                print("❌ Ungültiger Preis")

        elif wahl == "4":
            break

        else:
            print("❌ Ungültige Wahl")


def main() -> None:
    """Hauptfunktion."""
    # Haupt-Analyse
    hauptanalyse(VERKAUFSDATEN)

    # Interaktive Abfrage
    if input("\nInteraktive Abfrage starten? (j/n): ").lower() == "j":
        interaktive_abfrage(VERKAUFSDATEN)

    print("\n👋 Analyse beendet")


if __name__ == "__main__":
    main()
