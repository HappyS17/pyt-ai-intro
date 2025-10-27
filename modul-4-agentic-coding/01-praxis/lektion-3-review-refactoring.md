# Lektion 3: Code Review & Refactoring

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

- Code systematisch reviewen
- Code Smells erkennen
- Refactoring durchführen
- SOLID Principles anwenden

## 📚 Theorie (15 Min.)

### Code Review mit KI

```text
Prompt:
"Reviewe folgenden Code und gib Feedback zu:
1. Code-Qualität
2. Potenzielle Bugs
3. Performance
4. Lesbarkeit
5. Best Practices

[CODE HIER]"
```

### Code Smells

```python
# Smell: Lange Funktion
def process_data(data):
    # 100 Zeilen Code...
    pass

# Besser: Aufteilen
def validate_data(data): pass
def transform_data(data): pass
def save_data(data): pass
```

### SOLID Principles

```text
S - Single Responsibility
O - Open/Closed
L - Liskov Substitution
I - Interface Segregation
D - Dependency Inversion
```

## 💻 Live-Demo (20 Min.)

### Demo: Legacy Code Refactoring

**Vorher:**

```python
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return 'Error'
        return a / b
```

**Nachher:**

```python
from typing import Callable

class Calculator:
    """Verbesserte Calculator-Klasse."""
    
    def __init__(self):
        self.operations: dict[str, Callable] = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
    
    def calculate(self, a: float, b: float, operator: str) -> float:
        """Führt Berechnung durch."""
        if operator not in self.operations:
            raise ValueError(f"Unbekannter Operator: {operator}")
        return self.operations[operator](a, b)
    
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division durch Null")
        return a / b
```

## ✏️ Übung (15 Min.)

Refactore Legacy Code mit KI.

---

**Weiter zu:** [Lektion 4 - Dokumentation](./lektion-4-dokumentation.md)
