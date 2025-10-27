# Lektion 2: RAG-Systeme

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

- Embeddings erstellen
- Vector Search implementieren
- RAG Pipeline bauen

## 📚 Theorie (15 Min.)

### Embeddings

```python
from openai import OpenAI

client = OpenAI()

def get_embedding(text: str) -> list[float]:
    """Erstellt Embedding für Text."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding
```

### Vector Database (ChromaDB)

```python
import chromadb

# Client erstellen
client = chromadb.Client()

# Collection erstellen
collection = client.create_collection("docs")

# Dokumente hinzufügen
collection.add(
    documents=["Python ist toll", "JavaScript ist auch gut"],
    ids=["1", "2"]
)

# Suchen
results = collection.query(
    query_texts=["Programmiersprachen"],
    n_results=2
)
```

### RAG Pipeline

```python
def rag_query(question: str) -> str:
    """RAG-Pipeline."""
    # 1. Retrieve
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    context = "\n".join(results['documents'][0])
    
    # 2. Augment
    prompt = f"Kontext:\n{context}\n\nFrage: {question}"
    
    # 3. Generate
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
```

## 💻 Live-Demo (20 Min.)

Dokument-Q&A System mit RAG.

## ✏️ Übung (15 Min.)

RAG für eigene Dokumente.

---

**Weiter zu:** [Lektion 3 - Agents](./lektion-3-agents.md)
