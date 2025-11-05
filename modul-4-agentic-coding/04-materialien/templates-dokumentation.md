# Dokumentations-Templates

**Für:** Modul 4 - Agentic Coding  
**Version:** 1.0

---

## 📄 README.md Template

```markdown
# Projektname

Kurze Beschreibung (1-2 Sätze).

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

### Voraussetzungen
- Python 3.11+
- uv

### Schritt-für-Schritt

1. Repository klonen
   \`\`\`bash
   git clone https://github.com/user/project.git
   cd project
   \`\`\`

2. Abhängigkeiten installieren
   \`\`\`bash
   uv sync
   \`\`\`

3. Konfigurieren
   \`\`\`bash
   cp .env.example .env
   # Bearbeite .env mit deinen Einstellungen
   \`\`\`

## Verwendung

### Basis-Beispiel
\`\`\`python
from mymodule import MyClass

obj = MyClass()
result = obj.do_something()
print(result)
\`\`\`

### Erweiterte Beispiele
Siehe [examples/](./examples/) Verzeichnis.

## API-Dokumentation

### MyClass

\`\`\`python
class MyClass:
    def __init__(self, param1: str):
        """Initialisiere MyClass.
        
        Args:
            param1: Beschreibung
        """
        pass
    
    def do_something(self) -> str:
        """Führe etwas aus.
        
        Returns:
            Ergebnis als String
        """
        pass
\`\`\`

## Tests

\`\`\`bash
pytest tests/
pytest --cov=src tests/  # Mit Coverage
\`\`\`

## Beitragen

1. Fork das Projekt
2. Feature-Branch erstellen (\`git checkout -b feature/AmazingFeature\`)
3. Änderungen committen (\`git commit -m 'Add AmazingFeature'\`)
4. Branch pushen (\`git push origin feature/AmazingFeature\`)
5. Pull Request öffnen

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei.

## Kontakt

Fragen? Schreib ein Issue oder kontaktiere den Maintainer.
```

---

## 🔧 Docstring Template (Google Style)

```python
def calculate_average(numbers: list[float]) -> float:
    """Berechne den Durchschnitt einer Liste von Zahlen.
    
    Diese Funktion nimmt eine Liste von Zahlen und berechnet
    ihren arithmetischen Durchschnitt.
    
    Args:
        numbers: Liste von Zahlen (int oder float)
        
    Returns:
        Der Durchschnitt als float
        
    Raises:
        ValueError: Wenn die Liste leer ist
        TypeError: Wenn die Liste nicht-numerische Werte enthält
        
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        
        >>> calculate_average([10.5, 20.5])
        15.5
    """
    if not numbers:
        raise ValueError("Liste darf nicht leer sein")
    
    return sum(numbers) / len(numbers)
```

---

## 📝 CHANGELOG.md Template

```markdown
# Changelog

Alle wichtigen Änderungen an diesem Projekt werden dokumentiert.

## [1.0.0] - 2025-11-05

### Added
- Neue Feature X
- Neue Feature Y
- API-Endpunkt für Z

### Changed
- Verbesserte Performance von Funktion A
- Aktualisierte Abhängigkeiten

### Fixed
- Bug in Modul B behoben
- Fehler bei Fehlerbehandlung korrigiert

### Deprecated
- Alte API wird in v2.0 entfernt

### Removed
- Legacy-Code entfernt

## [0.9.0] - 2025-10-15

### Added
- Beta-Version veröffentlicht

---

Format basiert auf [Keep a Changelog](https://keepachangelog.com/)
```

---

## 🤝 CONTRIBUTING.md Template

```markdown
# Beitragen

Danke, dass du zu diesem Projekt beitragen möchtest!

## Code of Conduct

Bitte sei respektvoll und konstruktiv.

## Wie kann ich beitragen?

### Bugs melden
1. Prüfe, ob der Bug bereits gemeldet wurde
2. Öffne ein Issue mit:
   - Beschreibung des Bugs
   - Schritte zum Reproduzieren
   - Erwartetes vs. aktuelles Verhalten
   - Python-Version und Betriebssystem

### Features vorschlagen
1. Öffne ein Issue mit Label "enhancement"
2. Beschreibe den Use Case
3. Erkläre warum das Feature nützlich ist

### Code beitragen

1. Fork das Projekt
2. Feature-Branch erstellen
   \`\`\`bash
   git checkout -b feature/my-feature
   \`\`\`
3. Code schreiben mit Tests
4. Tests ausführen
   \`\`\`bash
   pytest tests/
   \`\`\`
5. Code formatieren
   \`\`\`bash
   black src/
   ruff check src/
   \`\`\`
6. Commit mit aussagekräftiger Nachricht
7. Push und Pull Request öffnen

## Coding Standards

- Python 3.11+
- PEP 8 Style Guide
- Type Hints verwenden
- Docstrings für alle Funktionen
- Tests für neuen Code

## Pull Request Prozess

1. Update README.md wenn nötig
2. Update CHANGELOG.md
3. Stelle sicher, dass alle Tests bestehen
4. Warte auf Review

---

Danke für deine Unterstützung! 🎉
```

---

## 📋 API-Dokumentation Template

```markdown
# API-Dokumentation

## Authentifizierung

\`\`\`bash
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/v1/...
\`\`\`

## Endpoints

### GET /users

Hole alle Benutzer.

**Query Parameter:**
- `limit` (int): Max. Anzahl (default: 10)
- `offset` (int): Offset (default: 0)

**Response:**
\`\`\`json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com"
    }
  ],
  "total": 100
}
\`\`\`

### POST /users

Erstelle einen neuen Benutzer.

**Request Body:**
\`\`\`json
{
  "name": "Bob",
  "email": "bob@example.com"
}
\`\`\`

**Response:** 201 Created
\`\`\`json
{
  "id": 2,
  "name": "Bob",
  "email": "bob@example.com"
}
\`\`\`

**Fehler:** 400 Bad Request
\`\`\`json
{
  "error": "Email bereits vorhanden"
}
\`\`\`

---

## Error Codes

| Code | Bedeutung |
|------|-----------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |
```

---

## 🎯 Inline-Kommentare Template

```python
# ✅ Gut: Erklärt WARUM, nicht WAS

# Wir sortieren absteigend, weil die neuesten Einträge
# zuerst angezeigt werden sollen
sorted_items = sorted(items, key=lambda x: x.date, reverse=True)

# ❌ Schlecht: Erklärt nur WAS

# Sortiere die Items
sorted_items = sorted(items, key=lambda x: x.date, reverse=True)
```

---

## 📚 Ressourcen

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Merksatz:** "Code ist für Menschen, nicht für Computer!" - Guido van Rossum

