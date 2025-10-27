# Übung 1: Komplexe Feature-Implementierung

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Mit Advanced Prompt Engineering ein komplexes Feature implementieren.

## Wählen Sie EINE Option

### Option A: Email-Validator mit erweiterten Features

#### Anforderungen

Erstellen Sie einen Email-Validator mit:

- Format-Validierung (Regex)
- Disposable Email Detection
- MX Record Check (optional)
- Typo-Suggestions
- Batch-Validierung

#### Prompt-Vorlage

```text
Du bist ein Senior Python-Entwickler mit Fokus auf Input-Validierung.

Kontext:
- Web-Anwendung für Benutzerregistrierung
- Python 3.11, keine externen Libraries ausser re
- Muss robust und performant sein

Aufgabe:
Erstelle eine EmailValidator-Klasse mit:

1. validate(email: str) -> tuple[bool, list[str]]
   - Prüft Format mit Regex
   - Gibt (is_valid, errors) zurück

2. is_disposable(email: str) -> bool
   - Prüft gegen Liste bekannter Disposable-Domains
   - Liste: ['tempmail.com', 'guerrillamail.com', '10minutemail.com']

3. suggest_correction(email: str) -> str | None
   - Erkennt häufige Typos (gmial.com → gmail.com)
   - Gibt Korrektur-Vorschlag oder None

4. validate_batch(emails: list[str]) -> dict
   - Validiert mehrere Emails
   - Gibt Statistik zurück

Constraints:
- Type Hints für alle Funktionen
- Docstrings im Google-Style
- Unit Tests mit pytest
- Keine externen Libraries

Beispiel:
```python
validator = EmailValidator()
is_valid, errors = validator.validate("test@gmial.com")
# is_valid = True (Format OK)
# errors = []

suggestion = validator.suggest_correction("test@gmial.com")
# suggestion = "test@gmail.com"
```

Format:
1. Klassen-Definition
2. Unit Tests
3. Verwendungsbeispiel
```

#### Erwartetes Ergebnis

- Vollständige EmailValidator-Klasse
- Mindestens 5 Unit Tests
- Dokumentation

### Option B: URL-Parser mit Komponenten-Extraktion

#### Anforderungen

Parser der URLs in Komponenten zerlegt:

- Schema (http/https)
- Domain
- Path
- Query Parameters
- Fragment
- Validierung

#### Prompt-Vorlage

```text
Du bist ein erfahrener Python-Entwickler für Web-Technologien.

Erstelle eine URLParser-Klasse die URLs in Komponenten zerlegt.

Anforderungen:
1. parse(url: str) -> URLComponents
   - Zerlegt URL in Komponenten
   - Gibt Dataclass zurück

2. validate(url: str) -> bool
   - Prüft ob URL gültig

3. get_query_params(url: str) -> dict
   - Extrahiert Query Parameters

4. build_url(components: URLComponents) -> str
   - Baut URL aus Komponenten

Beispiel:
```python
parser = URLParser()
components = parser.parse("https://example.com/path?key=value#section")
# components.schema = "https"
# components.domain = "example.com"
# components.path = "/path"
# components.query = {"key": "value"}
# components.fragment = "section"
```

Mit:
- Type Hints
- Docstrings
- Unit Tests
- Error Handling
```

### Option C: JSON-Schema-Validator

#### Anforderungen

Validator für JSON gegen Schema:

- Schema-Definition
- Type-Checking
- Required Fields
- Custom Validators
- Fehlerberichte

#### Prompt-Vorlage

```text
Erstelle einen JSON-Schema-Validator in Python.

Features:
1. Definiere Schema mit Types
2. Validiere JSON gegen Schema
3. Detaillierte Fehlerberichte
4. Custom Validators

Beispiel-Schema:
```python
schema = {
    "name": {"type": "string", "required": True},
    "age": {"type": "int", "min": 0, "max": 150},
    "email": {"type": "string", "validator": "email"}
}
```

Beispiel-Verwendung:
```python
validator = JSONValidator(schema)
is_valid, errors = validator.validate(data)
```

Mit vollständiger Implementierung und Tests.
```

## 💡 Tipps

- Beginnen Sie mit klarem, strukturiertem Prompt
- Iterieren Sie bei Bedarf
- Testen Sie den generierten Code
- Verstehen Sie jede Zeile

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] Feature vollständig implementiert
- [ ] Tests vorhanden und bestehen
- [ ] Code dokumentiert
- [ ] Sie verstehen den Code
- [ ] Code läuft ohne Fehler

---

**Zurück zu:** [Übungen README](./README.md)
