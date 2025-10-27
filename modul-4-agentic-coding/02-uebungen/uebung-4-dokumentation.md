# Übung 4: Vollständige Projekt-Dokumentation

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Ziel

Mit KI vollständige Projekt-Dokumentation erstellen.

## Ausgangspunkt

Sie haben ein kleines Projekt ohne Dokumentation:

```python
# calculator.py
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

# main.py
from calculator import Calculator

def main():
    calc = Calculator()
    
    while True:
        print("\n1. Addition")
        print("2. Subtraktion")
        print("3. Historie")
        print("4. Beenden")
        
        choice = input("Wahl: ")
        
        if choice == "1":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print(f"Ergebnis: {calc.add(a, b)}")
        elif choice == "2":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print(f"Ergebnis: {calc.subtract(a, b)}")
        elif choice == "3":
            for entry in calc.get_history():
                print(entry)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
```

## Aufgabe

Erstellen Sie vollständige Dokumentation mit KI.

## Schritt 1: Docstrings (5 Min.)

### Prompt

```text
Füge vollständige Docstrings im Google-Style zu diesem Code hinzu:

[KOPIERE CODE HIER EIN]

Für jede Klasse und Methode:
- Kurze Beschreibung
- Args mit Types
- Returns mit Type
- Beispiele wo sinnvoll
```

### Erwartetes Ergebnis

```python
class Calculator:
    """
    Einfacher Taschenrechner mit Historie-Funktion.
    
    Die Calculator-Klasse bietet grundlegende arithmetische
    Operationen und speichert eine Historie aller Berechnungen.
    
    Attributes:
        history: Liste aller durchgeführten Berechnungen
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.get_history()
        ['2 + 3 = 5']
    """
    
    def __init__(self):
        """Initialisiert Calculator mit leerer Historie."""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """
        Addiert zwei Zahlen.
        
        Args:
            a: Erste Zahl
            b: Zweite Zahl
        
        Returns:
            Summe von a und b
        
        Example:
            >>> calc.add(2, 3)
            5
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    # ... weitere Docstrings
```

## Schritt 2: README.md (5 Min.)

### Prompt

```text
Erstelle ein vollständiges README.md für dieses Projekt:

[KOPIERE CODE HIER EIN]

Sections:
- Titel und Beschreibung
- Features
- Installation
- Usage mit Beispielen
- API-Dokumentation
- Testing
- Contributing (optional)
- License
```

### Erwartetes Ergebnis

```markdown
# Calculator CLI

Ein einfacher Kommandozeilen-Taschenrechner mit Historie-Funktion.

## Features

- ✅ Addition und Subtraktion
- ✅ Berechnungs-Historie
- ✅ Interaktives CLI
- ✅ Fehlerbehandlung

## Installation

```bash
# Klone Repository
git clone https://github.com/user/calculator.git
cd calculator

# Keine Dependencies nötig (Standard-Library)
```

## Usage

### Als CLI

```bash
python main.py
```

### Als Library

```python
from calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # 8

history = calc.get_history()
print(history)  # ['5 + 3 = 8']
```

## API-Dokumentation

### Calculator

#### `__init__()`
Initialisiert Calculator mit leerer Historie.

#### `add(a: float, b: float) -> float`
Addiert zwei Zahlen und speichert in Historie.

...

## Testing

```bash
pytest test_calculator.py
```

## License

MIT
```

## Schritt 3: Inline-Comments (3 Min.)

### Prompt

```text
Füge hilfreiche Inline-Comments zu komplexen Stellen hinzu:

[KOPIERE CODE HIER EIN]

Nur wo wirklich nötig!
Erkläre das "Warum", nicht das "Was".
```

## Schritt 4: CHANGELOG.md (2 Min.)

### Prompt

```text
Erstelle ein CHANGELOG.md für dieses Projekt:

Version 1.0.0 (Initial Release)
```

### Erwartetes Ergebnis

```markdown
# Changelog

Alle wichtigen Änderungen an diesem Projekt werden hier dokumentiert.

## [1.0.0] - 2025-10-27

### Added
- Grundlegende Calculator-Klasse
- Addition und Subtraktion
- Historie-Funktion
- Interaktives CLI
- Vollständige Dokumentation
```

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] Alle Docstrings hinzugefügt
- [ ] README.md vollständig
- [ ] Inline-Comments wo nötig
- [ ] CHANGELOG.md erstellt
- [ ] Dokumentation klar und hilfreich

---

**Zurück zu:** [Übungen README](./README.md)
