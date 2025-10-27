# Lektion 2: Test-Driven Development mit KI

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

- TDD-Prinzipien verstehen
- Tests vor Code schreiben
- Red-Green-Refactor Cycle
- pytest nutzen

## 📚 Theorie (15 Min.)

### TDD-Cycle

```text
1. RED: Test schreiben (schlägt fehl)
2. GREEN: Minimale Implementierung (Test besteht)
3. REFACTOR: Code verbessern (Tests bleiben grün)
```

### Mit KI

```text
Prompt 1: "Schreibe Tests für Calculator-Klasse"
→ Tests generiert

Prompt 2: "Implementiere Calculator basierend auf Tests"
→ Code generiert

Prompt 3: "Refactore für bessere Lesbarkeit"
→ Verbesserter Code
```

### pytest Basics

```python
import pytest

def test_addition():
    assert 2 + 2 == 4

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0)
])
def test_add_parametrized(a, b, expected):
    assert a + b == expected
```

## 💻 Live-Demo (20 Min.)

### Demo: Calculator mit TDD

**Schritt 1: Tests schreiben**

```python
"""Tests für Calculator"""
import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
```

**Schritt 2: Implementierung**

```python
"""Calculator-Klasse"""

class Calculator:
    """Einfacher Taschenrechner."""
    
    def add(self, a: float, b: float) -> float:
        """Addiert zwei Zahlen."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtrahiert b von a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multipliziert zwei Zahlen."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Dividiert a durch b."""
        if b == 0:
            raise ValueError("Division durch Null nicht erlaubt")
        return a / b
```

## ✏️ Übung (15 Min.)

TDD für String-Utilities:

1. Tests schreiben für:
   - `reverse_string()`
   - `is_palindrome()`
   - `count_vowels()`

2. Implementierung mit KI

3. Tests ausführen

---

**Weiter zu:** [Lektion 3 - Review & Refactoring](./lektion-3-review-refactoring.md)
