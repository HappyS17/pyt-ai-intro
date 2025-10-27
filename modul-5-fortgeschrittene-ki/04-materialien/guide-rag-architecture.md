# RAG Architecture Guide

Umfassender Guide für RAG-Systeme.

## Komponenten

### 1. Document Loader

```python
def load_documents(paths: list[str]) -> list[str]:
    """Lädt Dokumente."""
    documents = []
    for path in paths:
        with open(path, 'r') as f:
            documents.append(f.read())
    return documents
```

### 2. Chunker

```python
def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    """Teilt Text in Chunks."""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    
    return chunks
```

### 3. Embedder

```python
def create_embeddings(texts: list[str]) -> list[list[float]]:
    """Erstellt Embeddings."""
    embeddings = []
    for text in texts:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        embeddings.append(response.data[0].embedding)
    return embeddings
```

### 4. Vector Store

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("docs")

# Hinzufügen
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(chunks))]
)

# Suchen
results = collection.query(
    query_texts=["Frage"],
    n_results=3
)
```

### 5. Retriever

```python
def retrieve(query: str, n: int = 3) -> list[str]:
    """Findet relevante Chunks."""
    results = collection.query(
        query_texts=[query],
        n_results=n
    )
    return results['documents'][0]
```

### 6. Generator

```python
def generate_answer(query: str, context: list[str]) -> str:
    """Generiert Antwort."""
    context_str = "\n\n".join(context)
    
    prompt = f"""Kontext:
{context_str}

Frage: {query}

Beantworte die Frage basierend auf dem Kontext."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
```

## Vollständige Pipeline

```python
def rag_query(question: str) -> str:
    # 1. Retrieve
    relevant_chunks = retrieve(question, n=3)
    
    # 2. Augment + Generate
    answer = generate_answer(question, relevant_chunks)
    
    return answer
```

## Optimierungen

### Chunk-Overlap

```python
def chunk_with_overlap(text: str, size: int, overlap: int):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), size - overlap):
        chunk = ' '.join(words[i:i+size])
        chunks.append(chunk)
    
    return chunks
```

### Reranking

```python
def rerank(query: str, chunks: list[str]) -> list[str]:
    """Rerankt Chunks nach Relevanz."""
    # Nutze Cross-Encoder oder LLM
    pass
```

### Hybrid Search

```python
def hybrid_search(query: str):
    # Semantic Search
    semantic_results = vector_search(query)
    
    # Keyword Search
    keyword_results = bm25_search(query)
    
    # Kombiniere
    return merge_results(semantic_results, keyword_results)
```

---

**Zurück zu:** [Materialien README](./README.md)
