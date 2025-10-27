# Übung 2: Dokument-Q&A mit RAG

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

RAG-System für Dokument-Q&A implementieren.

## Aufgabe

Erstellen Sie ein System das Fragen zu Dokumenten beantwortet.

## Prompt-Vorlage

```text
Erstelle ein RAG-System für Dokument-Q&A:

Komponenten:
1. DocumentLoader - Lädt Text-Dateien
2. Chunker - Teilt in Chunks (500 Tokens)
3. Embedder - Erstellt Embeddings
4. VectorStore - Speichert in ChromaDB
5. Retriever - Findet relevante Chunks
6. Generator - Beantwortet mit LLM

Workflow:
1. Dokumente laden und chunken
2. Embeddings erstellen
3. In Vector DB speichern
4. Bei Frage: Relevante Chunks finden
5. Prompt mit Kontext erstellen
6. LLM generiert Antwort

Anforderungen:
- ChromaDB für Vector Storage
- OpenAI für Embeddings und Generation
- Type Hints und Docstrings
- Error Handling

Beispiel:
```python
rag = DocumentQA()
rag.add_documents(["doc1.txt", "doc2.txt"])

answer = rag.ask("Was ist Python?")
print(answer)
```
```

## Erwartetes Ergebnis

- Dokumente werden geladen
- Embeddings erstellt
- Semantic Search funktioniert
- Antworten sind relevant

## ✅ Erfolg

- [ ] RAG-Pipeline funktioniert
- [ ] Relevante Chunks gefunden
- [ ] Antworten korrekt
- [ ] Code dokumentiert

---

**Zurück zu:** [Übungen README](./README.md)
