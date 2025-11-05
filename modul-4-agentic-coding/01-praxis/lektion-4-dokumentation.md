# Lektion 4: Dokumentation & Best Practices

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Lernziele

- Docstrings schreiben
- README erstellen
- Code kommentieren
- API-Dokumentation

## 📚 Theorie (15 Min.)

### Docstring-Styles

#### Google Style

```python
def function(arg1: int, arg2: str) -> bool:
    """Kurze Beschreibung.
    
    Längere Beschreibung falls nötig.
    
    Args:
        arg1: Beschreibung von arg1
        arg2: Beschreibung von arg2
    
    Returns:
        Beschreibung des Rückgabewerts
    
    Raises:
        ValueError: Wenn arg1 negativ
    
    Example:
        >>> function(5, "test")
        True
    """
    pass
```

### README-Struktur

```markdown
# Projekt-Name

Kurze Beschreibung

## Features

- Feature 1
- Feature 2

## Installation

```bash
uv sync
```

## Usage

```python
from myproject import MyClass
```

## Testing

```bash
pytest
```

## License

MIT
```

## 💻 Live-Demo (20 Min.)

### Demo: Projekt dokumentieren

Prompt für KI:
```text
Erstelle vollständige Dokumentation für folgendes Projekt:

[CODE/PROJEKT-BESCHREIBUNG]

Benötigt:
1. README.md mit allen Sections
2. Docstrings für alle Funktionen
3. Inline-Comments wo nötig
4. CHANGELOG.md
5. CONTRIBUTING.md
```

## ✏️ Übung (15 Min.)

Dokumentiere eigenes Projekt mit KI.

---

**Zurück zu:** [Praxis README](./README.md)
