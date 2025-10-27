"""
Taschenrechner mit Grundrechenarten
Verwendung: Lektion 4 - Musterlösung für Übung 4
Zeigt Best Practices: Funktionen, Fehlerbehandlung, Dokumentation
"""

def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b


def subtrahiere(a, b):
    """Subtrahiert zwei Zahlen."""
    return a - b


def multipliziere(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b


def dividiere(a, b):
    """
    Dividiert zwei Zahlen.
    
    Args:
        a (float): Dividend
        b (float): Divisor
    
    Returns:
        float oder str: Ergebnis oder Fehlermeldung
    """
    if b == 0:
        return "Fehler: Division durch Null ist nicht möglich!"
    return a / b


def hole_zahl(prompt):
    """
    Liest eine Zahl vom Benutzer ein mit Fehlerbehandlung.
    
    Args:
        prompt (str): Eingabeaufforderung
    
    Returns:
        float oder None: Eingegebene Zahl oder None bei Fehler
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein!")
            return None


def zeige_menu():
    """Zeigt das Operationsmenü an."""
    print("\n" + "=" * 50)
    print("TASCHENRECHNER")
    print("=" * 50)
    print("Operationen:")
    print("  + : Addition")
    print("  - : Subtraktion")
    print("  * : Multiplikation")
    print("  / : Division")
    print("  q : Beenden")
    print("=" * 50)


def berechne(zahl1, zahl2, operation):
    """
    Führt die gewählte Operation aus.
    
    Args:
        zahl1 (float): Erste Zahl
        zahl2 (float): Zweite Zahl
        operation (str): Operation (+, -, *, /)
    
    Returns:
        float oder str: Ergebnis oder Fehlermeldung
    """
    if operation == '+':
        return addiere(zahl1, zahl2)
    elif operation == '-':
        return subtrahiere(zahl1, zahl2)
    elif operation == '*':
        return multipliziere(zahl1, zahl2)
    elif operation == '/':
        return dividiere(zahl1, zahl2)
    else:
        return "Fehler: Ungültige Operation!"


def main():
    """
    Hauptfunktion des Taschenrechners.
    """
    print("Willkommen beim Taschenrechner!")
    
    while True:
        zeige_menu()
        
        # Operation wählen
        operation = input("\nWähle eine Operation (+, -, *, /, q): ").strip()
        
        # Beenden prüfen
        if operation.lower() == 'q':
            print("\nAuf Wiedersehen!")
            break
        
        # Operation validieren
        if operation not in ['+', '-', '*', '/']:
            print("Fehler: Ungültige Operation! Bitte wähle +, -, *, / oder q.")
            continue
        
        # Erste Zahl einlesen
        zahl1 = hole_zahl("Erste Zahl: ")
        if zahl1 is None:
            continue
        
        # Zweite Zahl einlesen
        zahl2 = hole_zahl("Zweite Zahl: ")
        if zahl2 is None:
            continue
        
        # Berechnung durchführen
        ergebnis = berechne(zahl1, zahl2, operation)
        
        # Ergebnis ausgeben
        print("\n" + "-" * 50)
        if isinstance(ergebnis, str):  # Fehlermeldung
            print(ergebnis)
        else:
            print(f"Ergebnis: {zahl1} {operation} {zahl2} = {ergebnis}")
        print("-" * 50)


if __name__ == "__main__":
    main()
