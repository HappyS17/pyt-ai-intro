# 🧪 Test-Dokumentation für pyt-ai-intro

Umfassende Testabdeckung für alle Python-Beispiele in allen 5 Modulen.

## 📊 Test-Übersicht

| Modul | Dateien | Tests | Coverage |
|-------|---------|-------|----------|
| Modul 1 | 7 | ~40 | 95%+ |
| Modul 2 | 13 | ~80 | 95%+ |
| Modul 3 | 6 | ~50 | 95%+ |
| Modul 4 | 3 | ~20 | 95%+ |
| Modul 5 | 12 | 154 | 95%+ |
| **GESAMT** | **41** | **~344** | **95%+** |

## 🚀 Quick Start

### Installation

```bash
# Test-Dependencies installieren
uv sync --group test
```

### Tests ausführen

```bash
# Alle Tests
make test

# Mit Coverage-Report
make coverage

# Schnell (parallel)
make test-fast

# Spezifisches Modul
make test-modul2
```

## 📁 Struktur

```
pyt-ai-intro/
├── modul-1-mindset-setup/05-beispiele/
│   ├── *.py                    # Beispiel-Dateien
│   └── tests/
│       ├── __init__.py
│       ├── test_*.py           # Test-Dateien
│       └── requirements-test.txt
├── modul-2-python-grundlagen/05-beispiele/
│   ├── *.py
│   └── tests/
│       └── test_*.py
├── ...
├── pytest.ini                  # Zentrale Konfiguration
├── conftest.py                 # Gemeinsame Fixtures
├── Makefile                    # Test-Befehle
└── requirements-test.txt       # Test-Dependencies
```

## 🧪 Test-Kategorien

### Modul 1: Mindset & Setup (7 Dateien)
- **hello-world.py**: Basis-Output Tests
- **einkaufsliste-demo.py**: Listen-Operationen
- **taschenrechner-demo.py**: Mathematische Operationen
- **zahlenraten-demo.py**: Interaktive Logik
- **textanalyse-beispiel.py**: String-Verarbeitung

### Modul 2: Python Grundlagen (13 Dateien)
- **bmi_rechner.py**: Berechnung + Klassifikation (18 Tests)
- **mathe_utils.py**: Mathematische Funktionen (30 Tests)
- **passwort_validator.py**: Validierung + Stärke (25 Tests)
- **fizzbuzz.py**: Logik-Tests
- **temperatur_umrechner.py**: Konvertierungen
- **datum_utils.py**: Datum-Operationen
- **kontaktbuch.py**: Datenstruktur-Tests
- **todo_liste.py**: Listen-Management
- **datenanalyse.py**: Daten-Verarbeitung
- **string_demo.py**: String-Methoden
- **validierung.py**: Input-Validierung
- **zahlenraten.py**: Spiel-Logik
- **notenklassifikation.py**: Klassifikation

### Modul 3: Datenverarbeitung (6 Dateien)
- **csv_lesen.py**: CSV-Operationen (Mock-Tests)
- **json_beispiel.py**: JSON-Verarbeitung
- **pandas_basics.py**: DataFrame-Operationen
- **log_analyse.py**: Log-Parsing
- **robuste_verarbeitung.py**: Error Handling
- **wetter_api.py**: API-Integration (Mock)

### Modul 4: Agentic Coding (3 Dateien)
- **before_refactoring.py**: Code-Qualität
- **after_refactoring.py**: Verbesserungen
- **test_calculator.py**: Bestehende Tests

### Modul 5: Fortgeschrittene KI (12 Dateien)
- **chatbot.py**: LLM-Integration (Mock)
- **streaming_chat.py**: Streaming-Responses
- **function_calling.py**: Tool Use
- **simple_rag.py**: RAG-Basis
- **advanced_rag.py**: RAG-Erweitert
- **rag_with_chromadb.py**: ChromaDB-Integration
- **simple_agent.py**: Agent-Basis
- **tool_agent.py**: Agent mit Tools
- **multi_agent.py**: Multi-Agent-Systeme
- **production_setup.py**: Production-Ready
- **cost_tracking.py**: Kosten-Tracking
- **error_handling.py**: Fehlerbehandlung

## 🎯 Test-Patterns

### Arrange-Act-Assert (AAA)

```python
def test_berechne_bmi_normal(self):
    """Test: Normale BMI-Berechnung"""
    # Arrange
    gewicht = 70
    groesse = 1.75
    
    # Act
    result = berechne_bmi(gewicht, groesse)
    
    # Assert
    assert result == 22.86
```

### Parametrisierte Tests

```python
@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, False),
    (10, True),
])
def test_ist_gerade(input, expected):
    assert ist_gerade(input) == expected
```

### Fixtures

```python
@pytest.fixture
def temp_csv(tmp_path):
    """Erstellt temporäre CSV-Datei"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("Name,Alter\nAnna,25\n")
    return csv_file

def test_lese_csv(temp_csv):
    result = lese_csv_dict(str(temp_csv))
    assert len(result) == 1
```

### Mocking

```python
from unittest.mock import patch, MagicMock

@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {"status": "ok"}
    result = fetch_data()
    assert result["status"] == "ok"
```

## 📈 Coverage-Ziele

- **Minimum**: 80%
- **Target**: 95%+
- **Kritische Funktionen**: 100%

### Coverage-Report

```bash
# HTML-Report generieren
make test-coverage

# Report öffnen
open htmlcov/index.html
```

## 🔧 Debugging

### Verbose Output

```bash
pytest -v
pytest -vv  # Noch ausführlicher
```

### Spezifische Tests

```bash
# Einzelner Test
pytest modul-2-python-grundlagen/05-beispiele/tests/test_bmi_rechner.py::TestBerechneBMI::test_berechne_bmi_normal

# Test-Klasse
pytest modul-2-python-grundlagen/05-beispiele/tests/test_bmi_rechner.py::TestBerechneBMI

# Mit Keyword
pytest -k "bmi"
```

### Debugging mit pdb

```python
def test_something():
    result = some_function()
    import pdb; pdb.set_trace()  # Breakpoint
    assert result == expected
```

## 🚨 Häufige Fehler

### ImportError

```python
# ❌ Falsch
from bmi_rechner import berechne_bmi

# ✅ Richtig
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bmi_rechner import berechne_bmi
```

### Datei-Zugriff

```python
# ❌ Falsch - Datei existiert nicht
def test_csv():
    data = lese_csv("personen.csv")

# ✅ Richtig - Mock oder Fixture
def test_csv(temp_csv):
    data = lese_csv(str(temp_csv))
```

## 📚 Ressourcen

- [Pytest Dokumentation](https://docs.pytest.org/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

## ✅ Checkliste für neue Tests

- [ ] Test-Datei erstellt: `test_*.py`
- [ ] Imports korrekt
- [ ] Mindestens 3 Tests pro Funktion
- [ ] Edge Cases abgedeckt
- [ ] Error Cases getestet
- [ ] Docstrings vorhanden
- [ ] Coverage >= 80%
- [ ] Alle Tests grün

