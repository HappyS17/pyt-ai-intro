# Aufgabe 2: Multi-Agent System

**Schwierigkeit:** ⭐⭐⭐⭐  
**Zeitaufwand:** 150 Minuten  
**Deadline:** Vor Abschluss

## 🎯 Ziel

Ein Multi-Agent-System entwickeln, bei dem mehrere Agents zusammenarbeiten.

## 📋 Aufgabenstellung

Entwickle ein System mit mindestens 2 Agents, die zusammenarbeiten um ein Problem zu lösen.

### Beispiel-Szenarien

#### Szenario 1: Reiseplanung
```
Agent 1 (Planner): Erstellt Reiseplan
Agent 2 (Researcher): Sucht Informationen
Agent 3 (Optimizer): Optimiert Kosten

Workflow:
1. Benutzer: "Plane Reise nach Berlin"
2. Planner: "Ich brauche Flüge, Hotels, Aktivitäten"
3. Researcher: "Suche Flüge, Hotels, Sehenswürdigkeiten"
4. Optimizer: "Hier ist der beste Plan für dein Budget"
```

#### Szenario 2: Code Review
```
Agent 1 (Developer): Schreibt Code
Agent 2 (Reviewer): Überprüft Code
Agent 3 (Tester): Testet Code

Workflow:
1. Developer: "Schreib eine Funktion für X"
2. Reviewer: "Überprüfe auf Best Practices"
3. Tester: "Teste mit verschiedenen Inputs"
4. Feedback Loop: Verbessern bis perfekt
```

#### Szenario 3: Datenanalyse
```
Agent 1 (DataLoader): Lädt Daten
Agent 2 (Analyzer): Analysiert Daten
Agent 3 (Visualizer): Erstellt Visualisierungen

Workflow:
1. DataLoader: "Lade Verkaufsdaten"
2. Analyzer: "Berechne Statistiken"
3. Visualizer: "Erstelle Diagramme"
4. Reporter: "Schreib Bericht"
```

## 🔧 Technische Anforderungen

### Agent-Struktur
```python
class Agent:
    def __init__(self, name: str, role: str, tools: list):
        self.name = name
        self.role = role
        self.tools = tools
    
    def think(self, context: str) -> str:
        """Denke über Problem nach"""
        pass
    
    def act(self, action: str) -> str:
        """Führe Aktion durch"""
        pass
    
    def communicate(self, message: str, recipient: 'Agent') -> None:
        """Kommuniziere mit anderem Agent"""
        pass
```

### Koordination
```python
class AgentCoordinator:
    def __init__(self, agents: list[Agent]):
        self.agents = agents
        self.message_queue = []
    
    def run(self, task: str) -> str:
        """Koordiniere Agents"""
        # 1. Verteile Task
        # 2. Agents arbeiten
        # 3. Sammle Ergebnisse
        # 4. Gib Ergebnis zurück
        pass
```

## 📊 Anforderungen

### Funktionalität
- [ ] Mindestens 2 Agents
- [ ] Agents können kommunizieren
- [ ] Agents haben unterschiedliche Rollen
- [ ] Koordination funktioniert
- [ ] Ergebnis ist sinnvoll

### Code-Qualität
- [ ] Saubere Architektur
- [ ] Gute Fehlerbehandlung
- [ ] Aussagekräftige Logs
- [ ] Tests vorhanden

### Dokumentation
- [ ] README mit Erklärung
- [ ] Architektur-Diagramm
- [ ] Beispiel-Workflow
- [ ] API-Dokumentation

## 🎓 Lernziele

Nach dieser Aufgabe kannst du:
- ✅ Multi-Agent-Systeme verstehen
- ✅ Agent-Kommunikation implementieren
- ✅ Koordination zwischen Agents
- ✅ Komplexe Workflows automatisieren

## 📁 Deliverables

1. **agents/** - Agent-Implementierungen
2. **coordinator.py** - Koordinations-Logik
3. **tests/** - Unit Tests
4. **README.md** - Dokumentation
5. **example.py** - Verwendungsbeispiel

## 💡 Implementierungs-Tipps

### 1. Message Queue
```python
from queue import Queue

class AgentSystem:
    def __init__(self):
        self.message_queue = Queue()
    
    def send_message(self, from_agent, to_agent, message):
        self.message_queue.put({
            'from': from_agent,
            'to': to_agent,
            'message': message
        })
```

### 2. State Management
```python
class AgentState:
    def __init__(self):
        self.shared_state = {}
    
    def update(self, key, value):
        self.shared_state[key] = value
    
    def get(self, key):
        return self.shared_state.get(key)
```

### 3. Logging
```python
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)

# In Agents
logger.info(f"Agent {self.name}: {action}")
```

## 🔄 Workflow-Beispiel

```
Task: "Analysiere Verkaufsdaten und erstelle Bericht"

1. Coordinator empfängt Task
2. DataLoader Agent:
   - Lädt CSV-Datei
   - Validiert Daten
   - Speichert in shared_state
3. Analyzer Agent:
   - Liest Daten aus shared_state
   - Berechnet Statistiken
   - Speichert Ergebnisse
4. Reporter Agent:
   - Liest Ergebnisse
   - Erstellt Bericht
   - Gibt Ergebnis zurück
5. Coordinator gibt Ergebnis an Benutzer
```

## ✅ Checkliste

- [ ] Mindestens 2 Agents implementiert
- [ ] Agents können kommunizieren
- [ ] Koordination funktioniert
- [ ] Tests vorhanden (70%+ Coverage)
- [ ] Dokumentation vollständig
- [ ] Beispiel funktioniert
- [ ] Code-Qualität gut
- [ ] Git-History sauber

## 📚 Ressourcen

- [LangChain Multi-Agent](https://python.langchain.com/docs/modules/agents/)
- [AutoGen Framework](https://microsoft.github.io/autogen/)
- [CrewAI](https://docs.crewai.com/)

---

**Merksatz:** "Zusammenarbeit macht Agents stärker!" 🤝

