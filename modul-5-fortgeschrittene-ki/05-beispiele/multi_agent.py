"""
Multi-Agent System

Demonstriert:
- Mehrere Agents
- Agent-Kommunikation
- Koordination
"""

from anthropic import Anthropic
from typing import List

client = Anthropic()

class Agent:
    """Basis-Agent Klasse"""
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.messages = []
    
    def think(self, context: str) -> str:
        """Denke über Kontext nach"""
        
        prompt = f"""Du bist {self.name}, ein {self.role}.
Kontext: {context}

Was ist deine Analyse oder Empfehlung?"""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=256,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.content[0].text

class MultiAgentSystem:
    """Koordiniert mehrere Agents"""
    
    def __init__(self):
        self.agents: List[Agent] = []
        self.shared_context = ""
    
    def add_agent(self, agent: Agent) -> None:
        """Füge Agent hinzu"""
        self.agents.append(agent)
    
    def run(self, task: str) -> None:
        """Führe Task mit allen Agents aus"""
        
        print(f"\n📋 Task: {task}")
        print("=" * 50)
        
        self.shared_context = task
        
        # Jeder Agent denkt über Task nach
        for agent in self.agents:
            print(f"\n🤖 {agent.name} ({agent.role}):")
            print("-" * 40)
            
            thought = agent.think(self.shared_context)
            print(thought)
            
            # Aktualisiere gemeinsamen Kontext
            self.shared_context += f"\n\n{agent.name}: {thought}"
        
        # Finale Zusammenfassung
        print("\n" + "=" * 50)
        print("✅ Multi-Agent Analyse abgeschlossen")

def main():
    """Hauptfunktion"""
    
    # Erstelle System
    system = MultiAgentSystem()
    
    # Füge Agents hinzu
    system.add_agent(Agent("Alice", "Analyst"))
    system.add_agent(Agent("Bob", "Techniker"))
    system.add_agent(Agent("Charlie", "Manager"))
    
    # Beispiel-Tasks
    tasks = [
        "Wie können wir unsere Website schneller machen?",
        "Was sind die Vorteile von Python?",
        "Wie sollten wir ein neues Projekt starten?"
    ]
    
    for task in tasks:
        system.run(task)
        print("\n")

if __name__ == "__main__":
    main()

