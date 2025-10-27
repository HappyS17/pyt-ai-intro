# Aufgabe 1: RAG-System für Dokumentation

**Zeitaufwand:** 180 Minuten | **Punkte:** 30% | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Vollständiges RAG-System für technische Dokumentation.

## Anforderungen

### Funktional

- Dokumente laden (TXT, MD, PDF)
- Intelligent chunken
- Embeddings erstellen
- Vector Database (ChromaDB)
- Semantic Search
- LLM-Integration
- Web-Interface (Streamlit)

### Technisch

- Python 3.11+
- OpenAI API
- ChromaDB
- Streamlit
- Type Hints
- Tests

## Architektur

```python
rag_system/
  __init__.py
  loader.py       # Dokument-Loader
  chunker.py      # Text-Chunking
  embedder.py     # Embedding-Erstellung
  store.py        # Vector Store
  retriever.py    # Retrieval-Logik
  generator.py    # LLM-Integration
  app.py          # Streamlit UI
tests/
  test_chunker.py
  test_retriever.py
docs/
  sample1.md
  sample2.md
```

## Features

1. **Upload-Interface**
   - Drag & Drop für Dokumente
   - Batch-Processing
   - Progress-Anzeige

2. **Q&A-Interface**
   - Frage eingeben
   - Relevante Chunks anzeigen
   - Antwort mit Quellen

3. **Admin-Panel**
   - Dokumente verwalten
   - Statistiken
   - Kosten-Tracking

## Bewertung

| Kriterium | Punkte |
|-----------|--------|
| Funktionalität | 10 |
| Code-Qualität | 8 |
| UI/UX | 5 |
| Tests | 4 |
| Dokumentation | 3 |

**Gesamt:** 30 Punkte

---

**Zurück zu:** [Nachbearbeitung README](./README.md)
