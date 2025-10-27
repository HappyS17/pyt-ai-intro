"""
Mathematik-Utility-Funktionen
Verwendung: Lektion 4 - Live-Demo
"""


def ist_gerade(zahl: int) -> bool:
    """
    Prüft ob Zahl gerade ist.
    
    Args:
        zahl: Zu prüfende Zahl
    
    Returns:
        True wenn gerade, sonst False
    """
    return zahl % 2 == 0


def ist_primzahl(zahl: int) -> bool:
    """
    Prüft ob Zahl eine Primzahl ist.
    
    Args:
        zahl: Zu prüfende Zahl
    
    Returns:
        True wenn Primzahl, sonst False
    """
    if zahl < 2:
        return False
    
    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return False
    
    return True


def fakultaet(n: int) -> int:
    """
    Berechnet die Fakultät von n.
    
    Args:
        n: Positive ganze Zahl
    
    Returns:
        n! (Fakultät)
    
    Example:
        >>> fakultaet(5)
        120
    """
    if n == 0 or n == 1:
        return 1
    return n * fakultaet(n - 1)


def fibonacci(n: int) -> list[int]:
    """
    Gibt die ersten n Fibonacci-Zahlen zurück.
    
    Args:
        n: Anzahl Fibonacci-Zahlen
    
    Returns:
        Liste mit Fibonacci-Zahlen
    
    Example:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib


def durchschnitt(zahlen: list[float]) -> float:
    """
    Berechnet den Durchschnitt einer Zahlenliste.
    
    Args:
        zahlen: Liste von Zahlen
    
    Returns:
        Durchschnitt
    
    Raises:
        ValueError: Wenn Liste leer ist
    """
    if not zahlen:
        raise ValueError("Liste darf nicht leer sein")
    
    return sum(zahlen) / len(zahlen)


# Tests
if __name__ == "__main__":
    print("=== MATHE-UTILS TESTS ===\n")
    
    # ist_gerade
    print(f"10 ist gerade: {ist_gerade(10)}")
    print(f"7 ist gerade: {ist_gerade(7)}")
    
    # ist_primzahl
    print(f"\n17 ist Primzahl: {ist_primzahl(17)}")
    print(f"20 ist Primzahl: {ist_primzahl(20)}")
    
    # fakultaet
    print(f"\n5! = {fakultaet(5)}")
    
    # fibonacci
    print(f"\nFibonacci(10): {fibonacci(10)}")
    
    # durchschnitt
    zahlen = [5, 4, 6, 5]
    print(f"\nDurchschnitt von {zahlen}: {durchschnitt(zahlen)}")
