"""
Einfacher AI Agent

Demonstriert:
- Agent-Struktur
- Denken-Handeln-Zyklus
- Einfache Entscheidungsfindung
"""

from anthropic import Anthropic

client = Anthropic()

class SimpleAgent:
    """Einfacher Agent mit Denken-Handeln-Zyklus"""
    
    def __init__(self, name: str):
        self.name = name
        self.memory = []
    
    def think(self, situation: str) -> str:
        """Denke über Situation nach"""
        
        prompt = f"""Du bist ein Agent namens {self.name}.
Analysiere diese Situation und entscheide was zu tun ist:

Situation: {situation}

Antworte mit:
1. Analyse der Situation
2. Deine Entscheidung
3. Begründung"""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        thought = response.content[0].text
        self.memory.append({"type": "thought", "content": thought})
        return thought
    
    def act(self, action: str) -> str:
        """Führe Aktion durch"""
        result = f"Agent {self.name} führt aus: {action}"
        self.memory.append({"type": "action", "content": result})
        return result
    
    def run(self, task: str) -> None:
        """Führe Task aus"""
        print(f"\n🤖 Agent '{self.name}' startet Task: {task}")
        print("-" * 50)
        
        # Denke
        print("\n💭 Denken...")
        thought = self.think(task)
        print(thought)
        
        # Handeln
        print("\n⚡ Handeln...")
        action = self.act(task)
        print(action)
        
        print("\n✅ Task abgeschlossen")

def main():
    """Hauptfunktion"""
    
    # Erstelle Agent
    agent = SimpleAgent("Assistant")
    
    # Beispiel-Tasks
    tasks = [
        "Ich muss einen Bericht schreiben. Was sollte ich beachten?",
        "Wie kann ich meine Produktivität verbessern?",
        "Erkläre mir Machine Learning"
    ]
    
    for task in tasks:
        agent.run(task)
        print("\n" + "=" * 50)

if __name__ == "__main__":
    main()

