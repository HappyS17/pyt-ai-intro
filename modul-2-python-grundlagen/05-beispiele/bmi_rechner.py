"""
BMI-Rechner mit Interpretation
Demonstriert: Variablen, Datentypen, Berechnungen, Bedingungen
"""


def berechne_bmi(gewicht: float, groesse: float) -> float:
    """
    Berechnet den Body Mass Index (BMI).

    Args:
        gewicht: Körpergewicht in Kilogramm
        groesse: Körpergrösse in Metern

    Returns:
        BMI-Wert gerundet auf 2 Dezimalstellen

    Raises:
        ValueError: Wenn Werte ungültig sind
    """
    if gewicht <= 0:
        raise ValueError("Gewicht muss positiv sein")
    if groesse <= 0:
        raise ValueError("Grösse muss positiv sein")

    bmi = gewicht / (groesse ** 2)
    return round(bmi, 2)


def interpretiere_bmi(bmi: float) -> str:
    """
    Interpretiert den BMI-Wert nach WHO-Klassifikation.

    Args:
        bmi: Body Mass Index

    Returns:
        Klassifikation als String
    """
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"


def main() -> None:
    """Hauptfunktion - Interaktiver BMI-Rechner."""
    print("=== BMI-RECHNER ===\n")

    try:
        # Eingabe
        gewicht = float(input("Gewicht (kg): "))
        groesse = float(input("Grösse (m): "))

        # Berechnung
        bmi = berechne_bmi(gewicht, groesse)
        kategorie = interpretiere_bmi(bmi)

        # Ausgabe
        print(f"\n📊 Ihr BMI: {bmi}")
        print(f"📋 Kategorie: {kategorie}")

        # Zusätzliche Informationen
        print("\n💡 WHO-Klassifikation:")
        print("  < 18.5  : Untergewicht")
        print("  18.5-25 : Normalgewicht ✓")
        print("  25-30   : Übergewicht")
        print("  > 30    : Adipositas")

    except ValueError as e:
        print(f"❌ Fehler: {e}")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")


if __name__ == "__main__":
    main()
