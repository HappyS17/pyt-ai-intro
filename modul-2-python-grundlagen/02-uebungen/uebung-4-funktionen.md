# Übung 4: Funktionen & Module

**Dauer:** 15 Minuten | **Lektion:** 4 | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Wiederverwendbare Funktionen in einem Modul erstellen.

## Aufgabenstellung

Erstellen Sie ein Modul `utils.py` mit 3-4 Utility-Funktionen.

## Anforderungen

### String-Utilities (wählen Sie 1-2)

```python
def ist_palindrom(text: str) -> bool:
    """Prüft ob Text ein Palindrom ist."""
    pass

def zaehle_woerter(text: str) -> int:
    """Zählt Wörter in Text."""
    pass
```

### Mathe-Utilities (wählen Sie 1-2)

```python
def ist_gerade(zahl: int) -> bool:
    """Prüft ob Zahl gerade ist."""
    pass

def durchschnitt(zahlen: list[float]) -> float:
    """Berechnet Durchschnitt."""
    pass
```

### Listen-Utilities (wählen Sie 1)

```python
def entferne_duplikate(liste: list) -> list:
    """Entfernt Duplikate aus Liste."""
    pass
```

## Vorgaben

- Jede Funktion mit Docstring
- Type Hints verwenden
- Tests im `if __name__ == "__main__"` Block

## Beispiel-Struktur

```python
"""
Mein Utility-Modul
"""

def ist_palindrom(text: str) -> bool:
    """Prüft ob Text ein Palindrom ist."""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    # Tests
    print(ist_palindrom("anna"))  # True
    print(ist_palindrom("test"))  # False
```

## Prompt-Vorlage

```text
Erstelle ein Python-Modul mit Utility-Funktionen:

1. ist_palindrom(text) - Prüft Palindrom
2. ist_gerade(zahl) - Prüft gerade Zahl
3. durchschnitt(zahlen) - Berechnet Durchschnitt

Anforderungen:
- Jede Funktion mit Docstring
- Type Hints verwenden
- Tests im if __name__ == "__main__" Block
- Kommentare auf Deutsch
```

---

**Zurück zu:** [Übungen README](./README.md)
