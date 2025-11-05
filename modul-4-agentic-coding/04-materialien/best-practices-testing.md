# Best Practices für Testing

**Für:** Modul 4 - Agentic Coding  
**Version:** 1.0

---

## 🎯 Warum Tests wichtig sind

- ✅ Vertrauen in Code
- ✅ Frühe Fehler-Erkennung
- ✅ Refactoring ohne Angst
- ✅ Dokumentation durch Tests
- ✅ Besseres Design

---

## 📋 Test-Struktur

### Arrange-Act-Assert (AAA)

```python
def test_calculator_add():
    # Arrange: Vorbereitung
    calc = Calculator()
    
    # Act: Aktion
    result = calc.add(2, 3)
    
    # Assert: Überprüfung
    assert result == 5
```

### Given-When-Then (BDD)

```python
def test_user_login_with_valid_credentials():
    # Given: Ausgangszustand
    user = User(email="test@example.com", password="secret123")
    
    # When: Aktion
    login_result = user.login("test@example.com", "secret123")
    
    # Then: Ergebnis
    assert login_result.is_authenticated == True
```

---

## 🏷️ Naming Conventions

### Test-Funktionen
```python
# ✅ Gut: Beschreibt was getestet wird
def test_add_two_positive_numbers():
    pass

def test_add_negative_and_positive_number():
    pass

def test_divide_by_zero_raises_error():
    pass

# ❌ Schlecht: Zu vage
def test_add():
    pass

def test_math():
    pass
```

### Test-Dateien
```
# Struktur
src/
  calculator.py
tests/
  test_calculator.py
  test_utils.py
```

---

## ✅ Assertions

### Basis-Assertions
```python
assert result == 5              # Gleichheit
assert result != 0              # Ungleichheit
assert result > 0               # Vergleiche
assert 'error' in message       # Membership
assert isinstance(obj, MyClass) # Typ-Prüfung
```

### pytest Assertions (besser)
```python
from pytest import raises

# Einfache Assertions
assert result == 5

# Mit Nachricht
assert result == 5, f"Expected 5, got {result}"

# Exception-Handling
with raises(ValueError):
    divide(10, 0)

# Mehrere Assertions
assert len(data) > 0
assert data[0]['id'] == 1
assert data[0]['name'] == 'Alice'
```

---

## 🔄 Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

## 🎭 Mocking & Fixtures

### Fixtures (Setup & Teardown)
```python
import pytest

@pytest.fixture
def sample_user():
    """Erstelle einen Test-User"""
    return User(name="Alice", email="alice@example.com")

def test_user_email(sample_user):
    assert sample_user.email == "alice@example.com"
```

### Mocking (externe Dependencies)
```python
from unittest.mock import Mock, patch

def test_api_call():
    # Mock die externe API
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'status': 'ok'}
        
        result = fetch_data()
        
        assert result['status'] == 'ok'
        mock_get.assert_called_once()
```

---

## 📊 Test Coverage

```bash
# Coverage installieren mit uv
uv sync --group test

# Coverage messen
pytest --cov=src tests/

# HTML Report
pytest --cov=src --cov-report=html tests/
```

### Coverage-Ziele
- **Anfänger:** 50-70%
- **Professionell:** 80-90%
- **Kritisch:** 95%+

---

## 🏗️ Test-Pyramide

```
        /\
       /  \  E2E Tests (10%)
      /____\
     /      \
    /  API   \ Integration Tests (30%)
   /  Tests  \
  /___________\
 /             \
/ Unit Tests    \ Unit Tests (60%)
/_______________\
```

### Unit Tests
- Testen einzelne Funktionen
- Schnell & isoliert
- Keine externe Dependencies

### Integration Tests
- Testen Zusammenspiel mehrerer Komponenten
- Mit echten Datenbanken/APIs
- Langsamer als Unit Tests

### E2E Tests
- Testen komplette Workflows
- Aus Benutzer-Perspektive
- Sehr langsam

---

## 🚀 Test-Driven Development (TDD)

### Red-Green-Refactor Zyklus

```
1. RED: Schreibe Test (wird fehlschlagen)
   def test_add():
       assert add(2, 3) == 5

2. GREEN: Schreibe minimalen Code (Test besteht)
   def add(a, b):
       return 5  # Funktioniert für diesen Test!

3. REFACTOR: Verbessere Code
   def add(a, b):
       return a + b
```

---

## 📋 Checkliste für gute Tests

- [ ] **Isoliert:** Tests beeinflussen sich nicht gegenseitig
- [ ] **Deterministisch:** Gleicher Input = gleicher Output
- [ ] **Schnell:** Laufen in Millisekunden
- [ ] **Aussagekräftig:** Klare Fehlermeldungen
- [ ] **Wartbar:** Einfach zu verstehen und ändern
- [ ] **Unabhängig:** Keine Abhängigkeiten zwischen Tests

---

## ⚠️ Häufige Fehler

| Fehler | Lösung |
|--------|--------|
| Tests sind zu langsam | Mocking verwenden, Datenbank-Tests separieren |
| Tests sind flaky | Keine Abhängigkeiten von Zeit/Zufall |
| Zu viele Assertions | Ein Test = ein Konzept |
| Keine Fixtures | DRY-Prinzip auch bei Tests |
| Tests testen Implementation | Tests sollten Verhalten testen |

---

## 🛠️ Tools & Frameworks

| Tool | Zweck |
|------|-------|
| pytest | Test-Framework |
| unittest | Standard Library |
| mock | Mocking |
| pytest-cov | Coverage |
| hypothesis | Property-based Testing |
| faker | Test-Daten generieren |

---

## 📚 Ressourcen

- [pytest Dokumentation](https://docs.pytest.org/)
- [unittest Dokumentation](https://docs.python.org/3/library/unittest.html)
- [Real Python Testing](https://realpython.com/python-testing/)

---

**Merksatz:** "Code ohne Tests ist Legacy Code!" - Michael Feathers

