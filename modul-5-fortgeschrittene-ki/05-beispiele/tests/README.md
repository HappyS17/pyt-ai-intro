# Tests für Modul 5 Beispiele

Umfassende Testabdeckung für alle Python-Beispiele mit hohem Coverage (95%+).

## Struktur

```
tests/
├── __init__.py                 # Test Package
├── conftest.py                 # Pytest Konfiguration & Fixtures
├── test_chatbot.py             # Tests für chatbot.py
├── test_streaming_chat.py      # Tests für streaming_chat.py
├── test_function_calling.py    # Tests für function_calling.py
├── test_simple_rag.py          # Tests für simple_rag.py
├── test_advanced_rag.py        # Tests für advanced_rag.py
├── test_cost_tracking.py       # Tests für cost_tracking.py
├── test_production_setup.py    # Tests für production_setup.py
├── test_error_handling.py      # Tests für error_handling.py
├── test_simple_agent.py        # Tests für simple_agent.py
├── test_tool_agent.py          # Tests für tool_agent.py
├── test_multi_agent.py         # Tests für multi_agent.py
├── test_rag_with_chromadb.py   # Tests für rag_with_chromadb.py
└── README.md                   # Diese Datei
```

## Installation

```bash
# Installiere Test-Dependencies mit uv
uv sync --group test

# Oder mit Makefile
make install
```

## Tests ausführen

### Alle Tests
```bash
pytest
```

### Mit Coverage Report
```bash
pytest --cov=. --cov-report=html
```

### Spezifische Test-Datei
```bash
pytest tests/test_chatbot.py
```

### Spezifische Test-Klasse
```bash
pytest tests/test_chatbot.py::TestChatFunction
```

### Spezifischer Test
```bash
pytest tests/test_chatbot.py::TestChatFunction::test_chat_adds_user_message
```

### Mit Verbose Output
```bash
pytest -v
```

### Mit Markers
```bash
pytest -m unit
pytest -m integration
```

## Coverage

Alle Tests haben eine Mindestabdeckung von **95%**.

### Coverage Report generieren
```bash
pytest --cov=. --cov-report=html
# Öffne htmlcov/index.html im Browser
```

## Test-Kategorien

### Unit Tests
- Testen einzelne Funktionen/Methoden
- Verwenden Mocks für externe Dependencies
- Schnell und zuverlässig

### Integration Tests
- Testen Zusammenspiel mehrerer Komponenten
- Können echte APIs aufrufen (mit Mocks)
- Langsamer aber realistischer

## Mocking

Alle Tests verwenden Mocks für:
- Anthropic API Client
- ChromaDB Client
- Externe Services

Dies ermöglicht:
- Schnelle Tests ohne API-Aufrufe
- Keine Kosten für API-Calls
- Deterministische Ergebnisse
- Offline-Testing

## Fixtures

Gemeinsame Fixtures in `conftest.py`:

```python
@pytest.fixture
def mock_anthropic_client():
    """Mock Anthropic Client"""
    
@pytest.fixture
def mock_response():
    """Mock API Response"""
    
@pytest.fixture
def sample_documents():
    """Beispiel-Dokumente"""
    
@pytest.fixture
def sample_query():
    """Beispiel-Abfrage"""
```

## Best Practices

1. **Arrange-Act-Assert Pattern**
   ```python
   def test_example():
       # Arrange: Setup
       obj = MyClass()
       
       # Act: Ausführung
       result = obj.method()
       
       # Assert: Überprüfung
       assert result == expected
   ```

2. **Aussagekräftige Test-Namen**
   - `test_chat_adds_user_message` ✅
   - `test_1` ❌

3. **Ein Assertion pro Test** (wenn möglich)
   - Macht Tests fokussiert
   - Einfacher zu debuggen

4. **Mocks für externe Dependencies**
   - Keine echten API-Aufrufe
   - Schneller und zuverlässiger

## Fehlerbehandlung

Tests überprüfen auch:
- Fehlerhafte Eingaben
- Edge Cases
- Exception Handling
- Fallback-Mechanismen

## Continuous Integration

Diese Tests können in CI/CD Pipelines verwendet werden:

```yaml
# GitHub Actions Beispiel
- name: Run Tests
  run: pytest --cov=. --cov-report=xml

- name: Upload Coverage
  uses: codecov/codecov-action@v3
```

## Troubleshooting

### Import Errors
```bash
# Stelle sicher, dass Parent-Verzeichnis im Path ist
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Mock Errors
```bash
# Überprüfe Mock-Setup in conftest.py
pytest -v --tb=long
```

### Timeout Errors
```bash
# Erhöhe Timeout in pytest.ini
timeout = 60
```

## Weitere Ressourcen

- [Pytest Dokumentation](https://docs.pytest.org/)
- [unittest.mock Dokumentation](https://docs.python.org/3/library/unittest.mock.html)
- [Coverage.py](https://coverage.readthedocs.io/)

