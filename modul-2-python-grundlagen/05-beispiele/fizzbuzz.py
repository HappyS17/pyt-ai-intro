"""
FizzBuzz: Klassisches Programmier-Problem
Verwendung: Lektion 2 - Live-Demo

Regeln:
- Bei Vielfachen von 3: "Fizz"
- Bei Vielfachen von 5: "Buzz"
- Bei Vielfachen von 3 und 5: "FizzBuzz"
- Sonst: Die Zahl
"""


def fizzbuzz(n: int) -> str:
    """
    Gibt FizzBuzz-Wert für eine Zahl zurück.
    
    Args:
        n: Zu prüfende Zahl
    
    Returns:
        "FizzBuzz", "Fizz", "Buzz" oder die Zahl als String
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    """Hauptfunktion."""
    print("FizzBuzz von 1 bis 30:\n")
    
    for zahl in range(1, 31):
        ergebnis = fizzbuzz(zahl)
        print(f"{zahl:2d}: {ergebnis}")


if __name__ == "__main__":
    main()
