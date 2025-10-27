"""
Notenklassifikation
Demonstriert: if-elif-else, Bedingungen, Input-Validierung
"""


def punkte_zu_note(punkte: int, max_punkte: int = 100) -> float:
    """
    Konvertiert Punkte in Schweizer Notenskala (1-6).

    Args:
        punkte: Erreichte Punktzahl
        max_punkte: Maximale Punktzahl (Standard: 100)

    Returns:
        Note zwischen 1.0 und 6.0 (auf 0.5 gerundet)

    Raises:
        ValueError: Wenn Punkte ungültig sind
    """
    if punkte < 0 or punkte > max_punkte:
        raise ValueError(f"Punkte müssen zwischen 0 und {max_punkte} liegen")

    # Prozentsatz berechnen
    prozent = (punkte / max_punkte) * 100

    # Schweizer Notenskala (vereinfacht)
    # 90-100%: 6.0 (sehr gut)
    # 80-89%:  5.5
    # 70-79%:  5.0 (gut)
    # 60-69%:  4.5
    # 50-59%:  4.0 (genügend)
    # 40-49%:  3.5
    # <40%:    1.0-3.0 (ungenügend)

    if prozent >= 90:
        note = 6.0
    elif prozent >= 80:
        note = 5.5
    elif prozent >= 70:
        note = 5.0
    elif prozent >= 60:
        note = 4.5
    elif prozent >= 50:
        note = 4.0
    elif prozent >= 40:
        note = 3.5
    elif prozent >= 30:
        note = 3.0
    elif prozent >= 20:
        note = 2.5
    elif prozent >= 10:
        note = 2.0
    else:
        note = 1.0

    return note


def note_zu_praedikat(note: float) -> str:
    """
    Konvertiert Note in Prädikat.

    Args:
        note: Note zwischen 1.0 und 6.0

    Returns:
        Prädikat als String
    """
    if note >= 5.5:
        return "sehr gut"
    elif note >= 5.0:
        return "gut"
    elif note >= 4.0:
        return "genügend"
    else:
        return "ungenügend"


def ist_bestanden(note: float) -> bool:
    """
    Prüft, ob Note zum Bestehen ausreicht.

    Args:
        note: Note zwischen 1.0 und 6.0

    Returns:
        True wenn bestanden (>= 4.0)
    """
    return note >= 4.0


def main() -> None:
    """Hauptfunktion - Interaktive Notenberechnung."""
    print("=== NOTENKLASSIFIKATION ===\n")

    try:
        # Eingabe
        punkte = int(input("Erreichte Punkte: "))
        max_punkte = int(input("Maximale Punkte (Enter für 100): ") or "100")

        # Berechnung
        note = punkte_zu_note(punkte, max_punkte)
        praedikat = note_zu_praedikat(note)
        bestanden = ist_bestanden(note)

        # Ausgabe
        prozent = (punkte / max_punkte) * 100

        print(f"\n📊 ERGEBNIS")
        print(f"{'─' * 30}")
        print(f"Punkte:    {punkte}/{max_punkte} ({prozent:.1f}%)")
        print(f"Note:      {note:.1f}")
        print(f"Prädikat:  {praedikat}")
        print(f"Status:    {'✓ Bestanden' if bestanden else '✗ Nicht bestanden'}")

        # Notenskala anzeigen
        print(f"\n💡 NOTENSKALA")
        print(f"{'─' * 30}")
        print("6.0 : 90-100% (sehr gut)")
        print("5.5 : 80-89%")
        print("5.0 : 70-79%  (gut)")
        print("4.5 : 60-69%")
        print("4.0 : 50-59%  (genügend) ✓")
        print("3.5 : 40-49%")
        print("3.0 : 30-39%  (ungenügend)")
        print("< 3.0: <30%")

    except ValueError as e:
        print(f"❌ Fehler: {e}")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")


# Demo: Batch-Konvertierung
def demo_batch_konvertierung() -> None:
    """Zeigt Batch-Konvertierung mehrerer Punktzahlen."""
    print("\n=== BATCH-KONVERTIERUNG ===\n")

    test_punkte = [95, 85, 75, 65, 55, 45, 35, 25]

    print(f"{'Punkte':<10} {'Prozent':<10} {'Note':<8} {'Prädikat':<15} {'Status'}")
    print("─" * 60)

    for punkte in test_punkte:
        note = punkte_zu_note(punkte)
        praedikat = note_zu_praedikat(note)
        status = "✓" if ist_bestanden(note) else "✗"

        print(f"{punkte:<10} {punkte}%{'':<7} {note:<8.1f} {praedikat:<15} {status}")


if __name__ == "__main__":
    main()

    # Optional: Batch-Demo
    antwort = input("\nBatch-Konvertierung zeigen? (j/n): ")
    if antwort.lower() == "j":
        demo_batch_konvertierung()
