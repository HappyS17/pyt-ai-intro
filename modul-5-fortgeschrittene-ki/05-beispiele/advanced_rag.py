"""
Fortgeschrittenes RAG mit Reranking

Demonstriert:
- Mehrere Retrieval-Strategien
- Reranking von Ergebnissen
- Bessere Relevanz
"""

from anthropic import Anthropic
import math

client = Anthropic()

# Beispiel-Dokumente mit Metadaten
documents = [
    {
        "id": 1,
        "title": "Python Basics",
        "content": "Python ist eine Programmiersprache. Variablen speichern Werte. Listen sind geordnete Sammlungen.",
        "category": "programming"
    },
    {
        "id": 2,
        "title": "Web Development",
        "content": "Flask ist ein Web-Framework. Django ist ein vollständiges Framework. APIs ermöglichen Kommunikation.",
        "category": "web"
    },
    {
        "id": 3,
        "title": "Data Science",
        "content": "Pandas ist für Datenanalyse. NumPy für numerische Berechnungen. Matplotlib für Visualisierung.",
        "category": "data"
    }
]

def bm25_score(query: str, doc_content: str) -> float:
    """BM25-ähnliche Bewertung"""
    query_words = query.lower().split()
    doc_words = doc_content.lower().split()
    
    score = 0
    for word in query_words:
        if word in doc_words:
            # Häufigkeit
            freq = doc_words.count(word)
            # Inverse Dokument-Häufigkeit
            idf = math.log(len(documents) / (1 + sum(1 for d in documents if word in d["content"].lower())))
            score += freq * idf
    
    return score

def retrieve_candidates(query: str, top_k: int = 5) -> list:
    """Rufe Kandidaten ab"""
    results = []
    
    for doc in documents:
        score = bm25_score(query, doc["content"])
        results.append((doc, score))
    
    results.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in results[:top_k]]

def rerank(query: str, candidates: list, top_k: int = 2) -> list:
    """Reranke Kandidaten basierend auf Relevanz"""
    # Hier könnte man ein ML-Modell nutzen
    # Für dieses Beispiel nutzen wir einfache Heuristiken
    
    reranked = []
    for doc in candidates:
        # Bonus für exakte Wort-Matches
        bonus = sum(1 for word in query.lower().split() 
                   if word in doc["content"].lower())
        
        # Bonus für Kategorie-Matches
        if any(cat in query.lower() for cat in ["web", "data", "programming"]):
            if doc["category"] in query.lower():
                bonus += 2
        
        reranked.append((doc, bonus))
    
    reranked.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in reranked[:top_k]]

def advanced_rag_query(user_query: str) -> str:
    """Beantworte Frage mit Advanced RAG"""
    
    # Schritt 1: Retrieve
    candidates = retrieve_candidates(user_query, top_k=5)
    
    # Schritt 2: Rerank
    relevant_docs = rerank(user_query, candidates, top_k=2)
    
    # Schritt 3: Augment
    context = "\n\n".join([
        f"[{doc['category'].upper()}] {doc['title']}\n{doc['content']}"
        for doc in relevant_docs
    ])
    
    system_prompt = f"""Du bist ein Experte.
Nutze diese Informationen um die Frage zu beantworten:

{context}

Sei präzise und nutze die Informationen."""
    
    # Schritt 4: Generate
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=512,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    
    return response.content[0].text

def main():
    """Hauptfunktion"""
    print("📚 Advanced RAG mit Reranking (Tippe 'exit' zum Beenden)")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nFrage: ").strip()
            
            if user_input.lower() == "exit":
                print("Auf Wiedersehen!")
                break
            
            if not user_input:
                continue
            
            response = advanced_rag_query(user_input)
            print(f"\nAntwort: {response}")
            
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen!")
            break
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

