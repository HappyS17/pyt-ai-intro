# Modul 5: Fortgeschrittene KI-Integration

**Dauer:** 1 Tag (4 Lektionen à 50 Minuten)  
**Voraussetzung:** Module 1-4 abgeschlossen

## 🎯 Lernziele

Nach diesem Modul können Sie:

- LLM APIs (OpenAI, Anthropic) nutzen
- RAG-Systeme (Retrieval-Augmented Generation) bauen
- Prompt-Chaining implementieren
- AI Agents entwickeln
- Embeddings und Vector Databases verwenden
- Ethische Aspekte verstehen
- Kosten optimieren
- Production-Ready AI-Apps erstellen

## 📚 Modulstruktur

### [00-vorbereitung](./00-vorbereitung/)

**Zeitaufwand:** 2-3 Stunden

- Leseauftrag: LLM Basics, RAG, Embeddings
- API-Setup (OpenAI/Anthropic)
- Ethik und Verantwortung
- Kosten-Kalkulation

### [01-praxis](./01-praxis/)

**Zeitaufwand:** 4 × 50 Minuten

1. **LLM APIs & Prompt Engineering** (OpenAI/Anthropic APIs)
2. **RAG-Systeme** (Embeddings, Vector Search, Context)
3. **AI Agents & Tool Use** (Function Calling, Multi-Step)
4. **Production & Ethics** (Error Handling, Monitoring, Ethics)

### [02-uebungen](./02-uebungen/)

**Zeitaufwand:** 4 × 15 Minuten

- Übung 1: Chatbot mit API
- Übung 2: Dokument-Q&A mit RAG
- Übung 3: Agent mit Tools
- Übung 4: Ethik-Analyse

### [03-nachbearbeitung](./03-nachbearbeitung/)

**Zeitaufwand:** 8-10 Stunden

- Aufgabe 1: RAG-System für Dokumentation
- Aufgabe 2: Multi-Agent-System
- Aufgabe 3: Production-Ready AI-App
- Aufgabe 4: Abschlussprojekt
- Persönliche Reflexion

### [04-materialien](./04-materialien/)

- LLM API Cheat Sheet
- RAG Architecture Guide
- Prompt Engineering Advanced
- Ethics Checklist
- Cost Optimization Guide

### [05-beispiele](./05-beispiele/)

- Chatbot-Implementierung
- RAG-System
- AI Agent
- Production-Setup

## ⏱️ Zeitplan

| Zeit | Aktivität |
|------|-----------|
| 08:00 - 08:50 | Lektion 1: LLM APIs & Prompt Engineering |
| 08:50 - 09:00 | Pause |
| 09:00 - 09:50 | Lektion 2: RAG-Systeme |
| 09:50 - 10:00 | Pause |
| 10:00 - 10:50 | Lektion 3: AI Agents & Tool Use |
| 10:50 - 11:00 | Pause |
| 11:00 - 11:50 | Lektion 4: Production & Ethics |

**Gesamtdauer:** 3 Std. 20 Min. + 30 Min. Pausen

## 🎓 Kompetenzen

Nach diesem Modul beherrschen Sie:

### Technisch

- [ ] LLM APIs nutzen (OpenAI, Anthropic)
- [ ] RAG-Systeme implementieren
- [ ] Embeddings erstellen und nutzen
- [ ] Vector Databases verwenden
- [ ] AI Agents bauen
- [ ] Function Calling implementieren
- [ ] Streaming Responses
- [ ] Error Handling für APIs

### Konzeptionell

- [ ] RAG-Architektur verstehen
- [ ] Prompt-Chaining designen
- [ ] Agent-Patterns kennen
- [ ] Kosten optimieren
- [ ] Ethische Implikationen bewerten
- [ ] Production Best Practices

## 🔑 Kernkonzepte

### Large Language Models (LLMs)

**Definition:** Neuronale Netze mit Milliarden Parametern, trainiert auf riesigen Textmengen.

**Wichtige Modelle:**

- GPT-4 (OpenAI)
- Claude 3 (Anthropic)
- Gemini (Google)

### RAG (Retrieval-Augmented Generation)

```text
1. User Query
   ↓
2. Retrieve relevant documents (Vector Search)
   ↓
3. Augment prompt with context
   ↓
4. Generate response with LLM
   ↓
5. Return answer
```

**Vorteile:**

- Aktuelle Informationen
- Reduzierte Halluzinationen
- Nachvollziehbare Quellen

### Embeddings

**Definition:** Vektorrepräsentationen von Text, die semantische Ähnlichkeit erfassen.

```python
text = "Python ist eine Programmiersprache"
embedding = get_embedding(text)  # [0.123, -0.456, ...]
```

### AI Agents

**Definition:** Systeme die autonom Aufgaben lösen durch:

1. Planung
2. Tool-Nutzung
3. Iteration
4. Selbst-Korrektur

## 📋 Voraussetzungen

### Aus Modulen 1-4

- Python-Grundlagen
- API-Calls (requests)
- JSON-Verarbeitung
- Fehlerbehandlung
- Agentic Coding

### Neu in Modul 5

- LLM APIs
- Embeddings
- Vector Databases
- RAG-Architektur
- AI Agents

### Technische Requirements

- Python 3.11+
- API Keys (OpenAI oder Anthropic)
- pip packages:
  - openai / anthropic
  - langchain (optional)
  - chromadb / pinecone
  - tiktoken

## 🔗 Navigation

- **Vorheriges Modul:** [Modul 4 - Agentic Coding](../modul-4-agentic-coding/)
- **Zurück zur Übersicht:** [Hauptverzeichnis](../README.md)

## 💡 Tipps für Studierende

### API-Nutzung

1. **API Keys sicher aufbewahren** - Nie in Git committen!
2. **Kosten im Auge behalten** - Monitoring einrichten
3. **Rate Limits beachten** - Exponential Backoff
4. **Fehlerbehandlung** - APIs können ausfallen
5. **Caching nutzen** - Redundante Calls vermeiden

### RAG Best Practices

1. **Chunk-Grösse optimieren** - Nicht zu gross, nicht zu klein
2. **Overlap verwenden** - Kontext nicht verlieren
3. **Metadata nutzen** - Für besseres Filtering
4. **Hybrid Search** - Keyword + Semantic
5. **Reranking** - Beste Ergebnisse zuerst

### Ethik & Verantwortung

- ⚠️ Bias in Modellen erkennen
- ⚠️ Datenschutz beachten
- ⚠️ Transparenz schaffen
- ⚠️ Missbrauch verhindern
- ⚠️ Umweltauswirkungen bedenken

## 🎯 Projekt-Ideen

### Für Nachbearbeitung

1. **Dokumentations-Assistent**
   - RAG über Projekt-Docs
   - Q&A Interface
   - Code-Beispiele generieren

2. **Code-Review-Agent**
   - Analysiert Pull Requests
   - Gibt Feedback
   - Schlägt Verbesserungen vor

3. **Research-Assistant**
   - Sammelt Informationen
   - Fasst zusammen
   - Erstellt Reports

4. **Personal Knowledge Base**
   - Notizen organisieren
   - Semantische Suche
   - Automatische Zusammenfassungen

## 📎 Ressourcen

### Empfohlene Lektüre

- OpenAI API Documentation
- Anthropic Claude Documentation
- "Building LLM Applications" (O'Reilly)
- RAG Papers (Lewis et al.)

### Tools & Libraries

- **LLM APIs:** openai, anthropic
- **Frameworks:** langchain, llamaindex
- **Vector DBs:** chromadb, pinecone, weaviate
- **Embeddings:** sentence-transformers
- **Monitoring:** langsmith, helicone

### Kosten-Übersicht

| Modell | Input (1M tokens) | Output (1M tokens) |
|--------|-------------------|-------------------|
| GPT-4 Turbo | $10 | $30 |
| GPT-3.5 Turbo | $0.50 | $1.50 |
| Claude 3 Opus | $15 | $75 |
| Claude 3 Sonnet | $3 | $15 |

**Tipp:** Für Entwicklung GPT-3.5 oder Claude Sonnet nutzen!

## 🌟 Besonderheiten dieses Moduls

Modul 5 ist der **Höhepunkt** des Kurses:

- Sie bauen echte AI-Anwendungen
- Sie arbeiten mit State-of-the-Art Technologie
- Sie reflektieren über gesellschaftliche Auswirkungen
- Sie erstellen ein Portfolio-Projekt

## ⚠️ Wichtige Hinweise

### API Keys

```bash
# .env Datei (NICHT committen!)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

### Kosten-Kontrolle

```python
# Maximale Tokens limitieren
max_tokens=500

# Caching nutzen
@cache
def get_embedding(text):
    ...
```

### Rate Limits

```python
# Exponential Backoff
import time
from openai import RateLimitError

for attempt in range(3):
    try:
        response = client.chat.completions.create(...)
        break
    except RateLimitError:
        time.sleep(2 ** attempt)
```

---

**Erstellt:** Oktober 2025  
**Version:** 1.0  
**Letztes Modul des Kurses!** 🎓
