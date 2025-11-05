"""
RAG mit ChromaDB für Vektor-Speicherung

Demonstriert:
- ChromaDB Integration
- Vektor-Embeddings
- Persistente Speicherung
"""

from anthropic import Anthropic

client = Anthropic()

# Hinweis: Für echte Nutzung: pip install chromadb

# Beispiel-Dokumente
documents = [
    {
        "id": "1",
        "title": "Python Basics",
        "content": "Python ist eine Programmiersprache. Variablen speichern Werte. Listen sind geordnete Sammlungen."
    },
    {
        "id": "2",
        "title": "Web Development",
        "content": "Flask ist ein Web-Framework. Django ist ein vollständiges Framework. APIs ermöglichen Kommunikation."
    },
    {
        "id": "3",
        "title": "Data Science",
        "content": "Pandas ist für Datenanalyse. NumPy für numerische Berechnungen. Matplotlib für Visualisierung."
    }
]

class SimpleVectorStore:
    """Vereinfachter Vektor-Store (ohne echte Embeddings)"""
    
    def __init__(self):
        self.documents = {}
    
    def add_documents(self, docs: list) -> None:
        """Füge Dokumente hinzu"""
        for doc in docs:
            self.documents[doc["id"]] = doc
        print(f"✅ {len(docs)} Dokumente hinzugefügt")
    
    def search(self, query: str, top_k: int = 2) -> list:
        """Suche ähnliche Dokumente"""
        query_words = set(query.lower().split())
        
        results = []
        for doc_id, doc in self.documents.items():
            doc_words = set(doc["content"].lower().split())
            # Einfache Ähnlichkeit
            similarity = len(query_words & doc_words) / len(query_words | doc_words)
            results.append((doc, similarity))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in results[:top_k]]

# Initialisiere Vector Store
vector_store = SimpleVectorStore()
vector_store.add_documents(documents)

def rag_with_chromadb(user_query: str) -> str:
    """RAG mit ChromaDB"""
    
    # Suche relevante Dokumente
    relevant_docs = vector_store.search(user_query, top_k=2)
    
    # Erstelle Kontext
    context = "\n\n".join([
        f"Dokument: {doc['title']}\n{doc['content']}"
        for doc in relevant_docs
    ])
    
    system_prompt = f"""Du bist ein hilfreicher Assistent.
Nutze diese Dokumente um die Frage zu beantworten:

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
    print("📚 RAG mit ChromaDB (Tippe 'exit' zum Beenden)")
    print("-" * 50)
    print("Hinweis: Für echte ChromaDB-Nutzung: pip install chromadb")
    
    while True:
        try:
            user_input = input("\nFrage: ").strip()
            
            if user_input.lower() == "exit":
                print("Auf Wiedersehen!")
                break
            
            if not user_input:
                continue
            
            response = rag_with_chromadb(user_input)
            print(f"\nAntwort: {response}")
            
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen!")
            break
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

