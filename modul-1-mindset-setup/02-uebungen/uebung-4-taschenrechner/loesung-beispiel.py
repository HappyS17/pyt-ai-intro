"""
Einfacher Taschenrechner
Musterlösung für Übung 4
"""

def calculate(num1, num2, operation):
    """
    Führt eine Rechenoperation mit zwei Zahlen durch.
    
    Args:
        num1 (float): Erste Zahl
        num2 (float): Zweite Zahl
        operation (str): Operation (+, -, *, /)
    
    Returns:
        float oder str: Ergebnis oder Fehlermeldung
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Fehler: Division durch Null ist nicht möglich!"
        return num1 / num2
    else:
        return "Fehler: Ungültige Operation!"


def get_number(prompt):
    """
    Liest eine Zahl vom Benutzer ein mit Fehlerbehandlung.
    
    Args:
        prompt (str): Eingabeaufforderung
    
    Returns:
        float oder None: Eingegebene Zahl oder None bei Fehler
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige Zahl ein!")
        return None


def main():
    """
    Hauptfunktion des Taschenrechners.
    """
    print("=" * 40)
    print("    EINFACHER TASCHENRECHNER")
    print("=" * 40)
    print("Operationen: +, -, *, /")
    print("Beenden mit 'quit' oder 'q'")
    print("=" * 40)
    
    while True:
        # Erste Zahl einlesen
        print()
        first_input = input("Erste Zahl (oder 'quit'): ")
        
        # Beenden prüfen
        if first_input.lower() in ['quit', 'q']:
            print("Auf Wiedersehen!")
            break
        
        # Erste Zahl konvertieren
        try:
            num1 = float(first_input)
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein!")
            continue
        
        # Operation einlesen
        operation = input("Operation (+, -, *, /): ")
        
        # Gültige Operation prüfen
        if operation not in ['+', '-', '*', '/']:
            print("Fehler: Ungültige Operation!")
            continue
        
        # Zweite Zahl einlesen
        num2 = get_number("Zweite Zahl: ")
        if num2 is None:
            continue
        
        # Berechnung durchführen
        result = calculate(num1, num2, operation)
        
        # Ergebnis ausgeben
        print("-" * 40)
        if isinstance(result, str):  # Fehlermeldung
            print(result)
        else:
            print(f"Ergebnis: {num1} {operation} {num2} = {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()
