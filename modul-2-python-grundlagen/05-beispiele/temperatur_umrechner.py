"""
Temperaturumrechner: Celsius ↔ Fahrenheit
Verwendung: Lektion 1 - Live-Demo
"""


def celsius_zu_fahrenheit(celsius: float) -> float:
    """
    Wandelt Celsius in Fahrenheit um.
    
    Args:
        celsius: Temperatur in Celsius
    
    Returns:
        Temperatur in Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_zu_celsius(fahrenheit: float) -> float:
    """
    Wandelt Fahrenheit in Celsius um.
    
    Args:
        fahrenheit: Temperatur in Fahrenheit
    
    Returns:
        Temperatur in Celsius
    """
    return (fahrenheit - 32) * 5/9


def main():
    """Hauptfunktion mit Benutzerinteraktion."""
    print("=" * 50)
    print("TEMPERATURUMRECHNER")
    print("=" * 50)
    
    while True:
        print("\n1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Beenden")
        
        wahl = input("\nWahl (1-3): ")
        
        if wahl == "1":
            try:
                celsius = float(input("Temperatur in °C: "))
                fahrenheit = celsius_zu_fahrenheit(celsius)
                print(f"{celsius}°C = {fahrenheit:.1f}°F")
            except ValueError:
                print("Fehler: Bitte gültige Zahl eingeben!")
        
        elif wahl == "2":
            try:
                fahrenheit = float(input("Temperatur in °F: "))
                celsius = fahrenheit_zu_celsius(fahrenheit)
                print(f"{fahrenheit}°F = {celsius:.1f}°C")
            except ValueError:
                print("Fehler: Bitte gültige Zahl eingeben!")
        
        elif wahl == "3":
            print("Auf Wiedersehen!")
            break
        
        else:
            print("Ungültige Wahl!")


if __name__ == "__main__":
    main()
