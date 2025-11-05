# Testing Guide - Modul 5 Beispiele

Umfassende Testabdeckung für alle Python-Beispiele mit **95%+ Coverage**.

## 📊 Test-Übersicht

| Datei | Tests | Coverage | Status |
|-------|-------|----------|--------|
| chatbot.py | 12 | 95%+ | ✅ |
| streaming_chat.py | 6 | 95%+ | ✅ |
| function_calling.py | 13 | 95%+ | ✅ |
| simple_rag.py | 11 | 95%+ | ✅ |
| advanced_rag.py | 13 | 95%+ | ✅ |
| cost_tracking.py | 15 | 95%+ | ✅ |
| production_setup.py | 10 | 95%+ | ✅ |
| error_handling.py | 10 | 95%+ | ✅ |
| simple_agent.py | 8 | 95%+ | ✅ |
| tool_agent.py | 8 | 95%+ | ✅ |
| multi_agent.py | 13 | 95%+ | ✅ |
| rag_with_chromadb.py | 9 | 95%+ | ✅ |
| **GESAMT** | **128 Tests** | **95%+** | **✅** |

## 🚀 Quick Start

### Installation
```bash
cd modul-5-fortgeschrittene-ki/05-beispiele
uv sync --group test
```

### Tests ausführen
```bash
# Alle Tests
pytest

# Mit Coverage
pytest --cov=. --cov-report=html

# Spezifische Datei
pytest tests/test_chatbot.py -v
```

### Mit Makefile
```bash
make install      # Dependencies installieren
make test         # Alle Tests
make test-coverage # Mit Coverage Report
make lint         # Code Quality
```

## 📁 Test-Struktur

```
tests/
├── __init__.py                 # Package Init
├── conftest.py                 # Fixtures & Konfiguration
├── requirements-test.txt       # Dependencies
├── README.md                   # Test-Dokumentation
│
├── test_chatbot.py             # 12 Tests
├── test_streaming_chat.py      # 6 Tests
├── test_function_calling.py    # 13 Tests
├── test_simple_rag.py          # 11 Tests
├── test_advanced_rag.py        # 13 Tests
├── test_cost_tracking.py       # 15 Tests
├── test_production_setup.py    # 10 Tests
├── test_error_handling.py      # 10 Tests
├── test_simple_agent.py        # 8 Tests
├── test_tool_agent.py          # 8 Tests
├── test_multi_agent.py         # 13 Tests
└── test_rag_with_chromadb.py   # 9 Tests
```

## 🧪 Test-Kategorien

### 1. **Chatbot Tests** (test_chatbot.py)
- ✅ Benutzer-Nachricht wird hinzugefügt
- ✅ Assistent-Antwort wird gespeichert
- ✅ Konversations-Speicher wird beibehalten
- ✅ API wird mit korrektem Modell aufgerufen
- ✅ Lange Nachrichten werden verarbeitet

### 2. **Streaming Chat Tests** (test_streaming_chat.py)
- ✅ Stream Context Manager wird genutzt
- ✅ Mehrere Text-Chunks werden verarbeitet
- ✅ Korrektes Modell wird verwendet
- ✅ System Prompt wird gesetzt
- ✅ Max Tokens wird gesetzt

### 3. **Function Calling Tests** (test_function_calling.py)
- ✅ Calculator Tool wird ausgeführt
- ✅ Weather Tool wird ausgeführt
- ✅ Tool-Definitionen sind korrekt
- ✅ Chat mit Tool-Aufruf funktioniert
- ✅ Unbekannte Tools werden behandelt

### 4. **RAG Tests** (test_simple_rag.py, test_advanced_rag.py)
- ✅ Dokumente werden gesucht
- ✅ Relevante Dokumente werden gefunden
- ✅ Top-K wird respektiert
- ✅ BM25 Scoring funktioniert
- ✅ Reranking funktioniert

### 5. **Cost Tracking Tests** (test_cost_tracking.py)
- ✅ CostTracker wird initialisiert
- ✅ Kosten werden berechnet
- ✅ Budget wird überprüft
- ✅ Requests werden verfolgt
- ✅ Stats werden generiert

### 6. **Production Setup Tests** (test_production_setup.py)
- ✅ Rate Limiter funktioniert
- ✅ Request-Zähler wird erhöht
- ✅ Fehler werden behandelt
- ✅ Validierung funktioniert

### 7. **Error Handling Tests** (test_error_handling.py)
- ✅ Retry-Logik funktioniert
- ✅ Fallback-Mechanismen funktionieren
- ✅ Verschiedene Fehlertypen werden behandelt
- ✅ Exponential Backoff funktioniert

### 8. **Agent Tests** (test_simple_agent.py, test_tool_agent.py, test_multi_agent.py)
- ✅ Agents werden initialisiert
- ✅ Think-Act Zyklus funktioniert
- ✅ Tools werden ausgeführt
- ✅ Multi-Agent Koordination funktioniert
- ✅ Memory wird verwaltet

### 9. **ChromaDB RAG Tests** (test_rag_with_chromadb.py)
- ✅ Collection wird initialisiert
- ✅ Dokumente werden hinzugefügt
- ✅ Suche funktioniert
- ✅ ChromaDB Query funktioniert

## 🎯 Coverage-Ziele

- **Minimum**: 85%
- **Target**: 95%+
- **Alle Dateien**: 95%+

## 📈 Coverage Report

```bash
# HTML Report generieren
pytest --cov=. --cov-report=html

# Öffne htmlcov/index.html im Browser
```

## 🔧 Mocking-Strategie

Alle Tests verwenden Mocks für:

```python
# Anthropic API
@patch('module.client')
def test_example(mock_client):
    mock_response = Mock()
    mock_response.content = [Mock(text="Antwort")]
    mock_client.messages.create.return_value = mock_response

# ChromaDB
@patch('module.collection')
def test_example(mock_collection):
    mock_collection.query.return_value = {...}
```

## 🚦 CI/CD Integration

GitHub Actions Workflow in `.github/workflows/tests.yml`:

```yaml
- Python 3.10, 3.11, 3.12, 3.13
- Lint mit flake8
- Tests mit pytest
- Coverage Upload zu Codecov
- Minimum Coverage: 85%
```

## 📝 Test-Beispiel

```python
class TestChatbot:
    """Tests für Chatbot"""
    
    @patch('chatbot.client')
    def test_chat_adds_user_message(self, mock_client):
        """Test: Benutzer-Nachricht wird hinzugefügt"""
        # Arrange
        mock_response = Mock()
        mock_response.content = [Mock(text="Hallo!")]
        mock_client.messages.create.return_value = mock_response
        
        # Act
        result = chat("Hallo")
        
        # Assert
        assert len(conversation_history) == 2
        assert conversation_history[0]["role"] == "user"
```

## 🐛 Debugging

### Verbose Output
```bash
pytest -v -s
```

### Spezifischen Test debuggen
```bash
pytest tests/test_chatbot.py::TestChatFunction::test_chat_adds_user_message -vv
```

### Mit Breakpoint
```python
def test_example():
    breakpoint()  # Debugger stoppt hier
    result = function()
```

## 📚 Weitere Ressourcen

- [Pytest Dokumentation](https://docs.pytest.org/)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [Coverage.py](https://coverage.readthedocs.io/)
- [tests/README.md](tests/README.md) - Detaillierte Test-Dokumentation

## ✅ Checkliste

- [x] 128 Tests geschrieben
- [x] 95%+ Coverage für alle Dateien
- [x] Mocking für externe APIs
- [x] pytest.ini Konfiguration
- [x] Makefile für einfache Befehle
- [x] GitHub Actions Workflow
- [x] requirements-test.txt
- [x] Detaillierte Dokumentation
- [x] Fixtures in conftest.py
- [x] CI/CD Integration

## 🎓 Für Studierende

Diese Tests zeigen:
- ✅ Wie man Unit Tests schreibt
- ✅ Wie man Mocks verwendet
- ✅ Wie man Coverage misst
- ✅ Wie man CI/CD aufbaut
- ✅ Best Practices für Testing

Nutze diese Tests als Vorlage für deine eigenen Projekte!

