# Prompt-Iteration Beispiel

**Für:** Modul 4 - Agentic Coding  
**Version:** 1.0

---

## 📖 Fallstudie: Email-Validator entwickeln

Dieses Beispiel zeigt, wie man durch Iteration zu besseren Ergebnissen kommt.

---

## 🔴 Iteration 1: Zu vage

### Prompt
```
Schreib einen Email-Validator
```

### Ergebnis (nicht ideal)
```python
def validate_email(email):
    if '@' in email:
        return True
    return False
```

**Probleme:**
- Zu simpel
- Keine echte Validierung
- Keine Fehlerbehandlung
- Keine Tests

---

## 🟡 Iteration 2: Bessere Anforderungen

### Prompt
```
Schreib einen Email-Validator in Python, der:
1. Prüft ob @ vorhanden ist
2. Prüft ob . nach @ vorhanden ist
3. Prüft ob Länge > 5 ist
4. Gibt True/False zurück

Schreib auch einen Test.
```

### Ergebnis (besser)
```python
def validate_email(email):
    """Validiere eine Email-Adresse."""
    if not isinstance(email, str):
        return False
    
    if '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local, domain = parts
    
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    if len(email) < 5:
        return False
    
    return True

# Test
assert validate_email("test@example.com") == True
assert validate_email("invalid") == False
assert validate_email("test@domain") == False
```

**Verbesserungen:**
- Bessere Logik
- Fehlerbehandlung
- Tests vorhanden
- Docstring

**Noch nicht ideal:**
- Keine Regex
- Keine erweiterten Validierungen
- Keine Exception-Handling

---

## 🟢 Iteration 3: Professionelle Lösung

### Prompt
```
Schreib einen produktiven Email-Validator mit:

Anforderungen:
1. Nutze Regex für RFC 5322 Validierung
2. Prüfe auf häufige Fehler (doppelte @, Leerzeichen)
3. Implementiere aussagekräftige Exceptions
4. Schreib umfassende Tests mit pytest
5. Füge Docstring mit Beispielen hinzu
6. Implementiere Logging

Beispiel-Validierungen:
- "test@example.com" → True
- "test.name+tag@example.co.uk" → True
- "test@domain" → False (kein TLD)
- "test @example.com" → False (Leerzeichen)
- "test@@example.com" → False (doppeltes @)

Gib mir auch ein Beispiel wie man es nutzt.
```

### Ergebnis (professionell)
```python
import re
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailValidationError(Exception):
    """Basis-Exception für Email-Validierung"""
    pass

class InvalidEmailFormat(EmailValidationError):
    """Email-Format ist ungültig"""
    pass

def validate_email(email: str) -> Tuple[bool, str]:
    """Validiere eine Email-Adresse nach RFC 5322.
    
    Args:
        email: Email-Adresse zum Validieren
        
    Returns:
        Tuple[bool, str]: (ist_gültig, nachricht)
        
    Raises:
        EmailValidationError: Wenn Input ungültig
        
    Examples:
        >>> validate_email("test@example.com")
        (True, "Email ist gültig")
        
        >>> validate_email("invalid")
        (False, "Kein @ Symbol gefunden")
    """
    if not isinstance(email, str):
        raise EmailValidationError("Email muss ein String sein")
    
    email = email.strip()
    
    # Prüfe auf Leerzeichen
    if ' ' in email:
        logger.warning(f"Email enthält Leerzeichen: {email}")
        return False, "Email darf keine Leerzeichen enthalten"
    
    # Prüfe auf @ Symbol
    if email.count('@') != 1:
        logger.warning(f"Email hat {email.count('@')} @ Symbole")
        return False, "Email muss genau ein @ Symbol haben"
    
    # Regex für RFC 5322 (vereinfacht)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        logger.warning(f"Email passt nicht zu Pattern: {email}")
        return False, "Email-Format ist ungültig"
    
    logger.info(f"Email validiert: {email}")
    return True, "Email ist gültig"

# Verwendungsbeispiel
if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "user.name+tag@example.co.uk",
        "invalid",
        "test @example.com",
        "test@@example.com",
    ]
    
    for email in test_emails:
        is_valid, message = validate_email(email)
        print(f"{email}: {is_valid} - {message}")
```

### Tests
```python
import pytest
from email_validator import validate_email, EmailValidationError

class TestEmailValidator:
    """Tests für Email-Validator"""
    
    def test_valid_emails(self):
        """Teste gültige Emails"""
        valid_emails = [
            "test@example.com",
            "user.name@example.com",
            "user+tag@example.co.uk",
            "123@example.com",
        ]
        for email in valid_emails:
            is_valid, _ = validate_email(email)
            assert is_valid, f"{email} sollte gültig sein"
    
    def test_invalid_emails(self):
        """Teste ungültige Emails"""
        invalid_emails = [
            "invalid",
            "test@domain",
            "test @example.com",
            "test@@example.com",
            "@example.com",
            "test@",
        ]
        for email in invalid_emails:
            is_valid, _ = validate_email(email)
            assert not is_valid, f"{email} sollte ungültig sein"
    
    def test_non_string_input(self):
        """Teste Non-String Input"""
        with pytest.raises(EmailValidationError):
            validate_email(123)
    
    def test_error_messages(self):
        """Teste aussagekräftige Fehlermeldungen"""
        is_valid, message = validate_email("test @example.com")
        assert not is_valid
        assert "Leerzeichen" in message
```

**Verbesserungen:**
- Regex für echte Validierung
- Exception-Handling
- Logging
- Umfassende Tests
- Type Hints
- Docstrings mit Beispielen
- Produktionsreife

---

## 🎯 Lernpunkte

### Was hat sich verbessert?

| Aspekt | Iteration 1 | Iteration 2 | Iteration 3 |
|--------|------------|------------|------------|
| Validierung | Zu simpel | Besser | RFC 5322 |
| Tests | Keine | Basis | Umfassend |
| Fehlerbehandlung | Keine | Minimal | Professionell |
| Logging | Keine | Keine | Vorhanden |
| Dokumentation | Keine | Minimal | Vollständig |
| Produktionsreife | Nein | Teilweise | Ja |

### Iterationsprozess

```
1. Erste Lösung: Funktioniert, aber zu simpel
   ↓
2. Feedback: Bessere Anforderungen definieren
   ↓
3. Zweite Lösung: Besser, aber noch nicht professionell
   ↓
4. Feedback: Produktionsanforderungen hinzufügen
   ↓
5. Finale Lösung: Professionell und wartbar
```

---

## 💡 Tipps für effektive Iteration

1. **Starte simpel:** Erste Version muss nicht perfekt sein
2. **Teste früh:** Finde Probleme schnell
3. **Gib Feedback:** Erkläre was nicht passt
4. **Sei spezifisch:** "Besser" ist zu vage
5. **Iteriere:** Mehrere Runden sind normal

---

## 📚 Ressourcen

- [RFC 5322 Email Format](https://tools.ietf.org/html/rfc5322)
- [Python regex Module](https://docs.python.org/3/library/re.html)
- [pytest Documentation](https://docs.pytest.org/)

---

**Merksatz:** "Perfekt ist der Feind des Guten - aber Iteration macht es besser!"

