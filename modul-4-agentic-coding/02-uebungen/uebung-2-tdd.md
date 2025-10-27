# Übung 2: TDD String-Utilities

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Test-Driven Development mit KI praktizieren.

## Aufgabe

Implementieren Sie String-Utilities mit TDD-Ansatz.

## Schritt 1: Tests schreiben (5 Min.)

### Prompt für Tests

```text
Schreibe Unit Tests für folgende String-Utility-Funktionen:

1. reverse_string(text: str) -> str
   - Kehrt String um
   - Behandelt leere Strings
   - Behandelt Unicode

2. is_palindrome(text: str) -> bool
   - Prüft ob Palindrom
   - Ignoriert Gross-/Kleinschreibung
   - Ignoriert Leerzeichen

3. count_vowels(text: str) -> int
   - Zählt Vokale (a,e,i,o,u)
   - Gross-/Kleinschreibung egal
   - Umlaute (ä,ö,ü) zählen

4. truncate(text: str, length: int, suffix: str = "...") -> str
   - Kürzt Text auf Länge
   - Fügt Suffix hinzu
   - Schneidet bei Wortgrenze

Verwende pytest und parametrize für mehrere Test-Cases.
```

### Erwartetes Ergebnis

```python
import pytest

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

@pytest.mark.parametrize("text,expected", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected

# ... weitere Tests
```

## Schritt 2: Implementierung (5 Min.)

### Prompt für Implementierung

```text
Implementiere die String-Utility-Funktionen basierend auf diesen Tests:

[KOPIERE DIE TESTS HIER EIN]

Anforderungen:
- Alle Tests müssen bestehen
- Type Hints verwenden
- Docstrings im Google-Style
- Effiziente Implementierung
```

### Erwartetes Ergebnis

```python
def reverse_string(text: str) -> str:
    """
    Kehrt einen String um.
    
    Args:
        text: Zu invertierender String
    
    Returns:
        Umgekehrter String
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]

# ... weitere Funktionen
```

## Schritt 3: Tests ausführen (2 Min.)

```bash
pytest test_string_utils.py -v
```

### Erwartete Ausgabe

```text
test_reverse_string PASSED
test_is_palindrome[racecar-True] PASSED
test_is_palindrome[hello-False] PASSED
test_count_vowels PASSED
test_truncate PASSED

5 passed in 0.03s
```

## Schritt 4: Refactoring (3 Min.)

### Prompt für Refactoring

```text
Refactore die String-Utilities:

1. Verbessere Lesbarkeit
2. Optimiere Performance
3. Füge Edge-Case-Handling hinzu
4. Behalte alle Tests grün

Aktueller Code:
[KOPIERE CODE HIER EIN]
```

## Alternative: Eigene Funktionen

Wählen Sie eigene Funktionen:

1. **Schritt 1:** Definieren Sie 3-4 Funktionen
2. **Schritt 2:** Lassen Sie KI Tests schreiben
3. **Schritt 3:** Lassen Sie KI implementieren
4. **Schritt 4:** Führen Sie Tests aus
5. **Schritt 5:** Refactoring

## 💡 TDD-Prinzipien

- ✅ **Red:** Test schreiben (schlägt fehl)
- ✅ **Green:** Minimale Implementierung
- ✅ **Refactor:** Code verbessern

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] Tests zuerst geschrieben
- [ ] Implementierung folgt Tests
- [ ] Alle Tests bestehen
- [ ] Code refactored
- [ ] Sie verstehen TDD-Cycle

---

**Zurück zu:** [Übungen README](./README.md)
