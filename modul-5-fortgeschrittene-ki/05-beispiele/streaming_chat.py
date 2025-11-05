"""
Chatbot mit Streaming Responses

Demonstriert:
- Streaming von Antworten
- Echtzeit-Ausgabe
- Token-Verbrauch
"""

from anthropic import Anthropic

client = Anthropic()

def stream_chat(user_message: str) -> None:
    """Streame Antwort in Echtzeit"""
    
    print(f"\nDu: {user_message}")
    print("Assistent: ", end="", flush=True)
    
    # Nutze stream context manager
    with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system="Du bist ein hilfreicher Assistent.",
        messages=[
            {"role": "user", "content": user_message}
        ]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    
    print()  # Neue Zeile

def main():
    """Hauptfunktion"""
    print("🤖 Streaming Chatbot (Tippe 'exit' zum Beenden)")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nDu: ").strip()
            
            if user_input.lower() == "exit":
                print("Auf Wiedersehen!")
                break
            
            if not user_input:
                continue
            
            stream_chat(user_input)
            
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen!")
            break
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

