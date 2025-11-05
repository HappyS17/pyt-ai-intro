"""
Einfaches RAG (Retrieval-Augmented Generation) System

Demonstriert:
- Dokument-Speicherung
- Ähnlichkeits-Suche
- Kontext-Augmentation
"""

from anthropic import Anthropic

client = Anthropic()

# Beispiel-Dokumente
documents = [
    {
        "id": 1,
        "title": "Python Basics",
        "content": "Python ist eine Programmiersprache. Variablen speichern Werte. Listen sind geordnete Sammlungen."
    },
    {
        "id": 2,
        "title": "Web Development",
        "content": "Flask ist ein Web-Framework. Django ist ein vollständiges Framework. APIs ermöglichen Kommunikation."
    },
    {
        "id": 3,
        "title": "Data Science",
        "content": "Pandas ist für Datenanalyse. NumPy für numerische Berechnungen. Matplotlib für Visualisierung."
    }
]

def simple_search(query: str, top_k: int = 2) -> list:
    """Einfache Ähnlichkeits-Suche (Wort-Matching)"""
    query_words = set(query.lower().split())
    
    results = []
    for doc in documents:
        doc_words = set(doc["content"].lower().split())
        # Berechne Ähnlichkeit
        similarity = len(query_words & doc_words) / len(query_words | doc_words)
        results.append((doc, similarity))
    
    # Sortiere nach Ähnlichkeit
    results.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in results[:top_k]]

def rag_query(user_query: str) -> str:
    """Beantworte Frage mit RAG"""
    
    # Suche relevante Dokumente
    relevant_docs = simple_search(user_query)
    
    # Erstelle Kontext
    context = "\n\n".join([
        f"Dokument: {doc['title']}\n{doc['content']}"
        for doc in relevant_docs
    ])
    
    # Erstelle Prompt mit Kontext
    system_prompt = f"""Du bist ein hilfreicher Assistent.
Nutze die folgenden Dokumente um die Frage zu beantworten:

{context}

Wenn die Antwort nicht in den Dokumenten steht, sag das."""
    
    # Rufe Claude auf
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
    print("📚 RAG System (Tippe 'exit' zum Beenden)")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nFrage: ").strip()
            
            if user_input.lower() == "exit":
                print("Auf Wiedersehen!")
                break
            
            if not user_input:
                continue
            
            response = rag_query(user_input)
            print(f"\nAntwort: {response}")
            
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen!")
            break
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

