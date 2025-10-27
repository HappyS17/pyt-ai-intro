"""
Vollständiger Chatbot mit OpenAI API
Verwendung: Lektion 1 - Live-Demo
"""
from openai import OpenAI
import os
from typing import List, Dict


class Chatbot:
    """Einfacher Chatbot mit Kontext-Management."""
    
    def __init__(self, system_prompt: str = "Du bist ein hilfreicher Assistent."):
        """
        Initialisiert Chatbot.
        
        Args:
            system_prompt: System-Prompt für das Modell
        """
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]
        self.model = "gpt-3.5-turbo"
    
    def chat(self, user_message: str) -> str:
        """
        Sendet Nachricht und erhält Antwort.
        
        Args:
            user_message: Nachricht des Benutzers
        
        Returns:
            Antwort des Chatbots
        """
        # User-Nachricht hinzufügen
        self.messages.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # API-Call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                max_tokens=500,
                temperature=0.7
            )
            
            # Antwort extrahieren
            assistant_message = response.choices[0].message.content
            
            # Antwort zum Kontext hinzufügen
            self.messages.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except Exception as e:
            return f"Fehler: {e}"
    
    def reset(self):
        """Setzt Konversation zurück."""
        system_prompt = self.messages[0]["content"]
        self.messages = [{"role": "system", "content": system_prompt}]
    
    def get_context_length(self) -> int:
        """Gibt Anzahl Nachrichten zurück."""
        return len(self.messages) - 1  # Ohne System-Prompt


def main():
    """Hauptfunktion mit Chat-Loop."""
    print("=" * 50)
    print("CHATBOT MIT OPENAI")
    print("=" * 50)
    print("Befehle:")
    print("  'quit' - Beenden")
    print("  'reset' - Konversation zurücksetzen")
    print("  'context' - Kontext-Länge anzeigen")
    print("=" * 50)
    
    # System-Prompt wählen
    print("\nWähle Persönlichkeit:")
    print("1. Hilfreicher Assistent")
    print("2. Python-Tutor")
    print("3. Kreativer Schreiber")
    
    choice = input("\nWahl (1-3): ")
    
    system_prompts = {
        "1": "Du bist ein hilfreicher Assistent.",
        "2": "Du bist ein geduldiger Python-Tutor. Erkläre Konzepte einfach und mit Beispielen.",
        "3": "Du bist ein kreativer Schreiber. Antworte poetisch und inspirierend."
    }
    
    system_prompt = system_prompts.get(choice, system_prompts["1"])
    
    # Chatbot erstellen
    bot = Chatbot(system_prompt)
    
    print("\nChatbot bereit! Starte Konversation:\n")
    
    # Chat-Loop
    while True:
        user_input = input("Du: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == "quit":
            print("\nAuf Wiedersehen!")
            break
        
        if user_input.lower() == "reset":
            bot.reset()
            print("\n[Konversation zurückgesetzt]\n")
            continue
        
        if user_input.lower() == "context":
            print(f"\n[Kontext-Länge: {bot.get_context_length()} Nachrichten]\n")
            continue
        
        # Antwort holen
        response = bot.chat(user_input)
        print(f"\nBot: {response}\n")


if __name__ == "__main__":
    # Prüfe API Key
    if not os.getenv("OPENAI_API_KEY"):
        print("Fehler: OPENAI_API_KEY nicht gesetzt!")
        print("Setze Umgebungsvariable oder erstelle .env Datei")
        exit(1)
    
    main()
