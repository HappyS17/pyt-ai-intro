# Lektion 3: AI Agents & Tool Use

**Dauer:** 50 Minuten  
**Für:** Modul 5 - Fortgeschrittene KI

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:
- ✅ Verstehen was AI Agents sind
- ✅ Tools/Functions für Agents definieren
- ✅ Einfache Agents implementieren
- ✅ Multi-Step Reasoning verstehen
- ✅ Agents debuggen

---

## 📚 Konzepte

### Was ist ein AI Agent?

Ein AI Agent ist ein Programm, das:
1. **Wahrnimmt:** Versteht die aktuelle Situation
2. **Denkt:** Überlegt was zu tun ist
3. **Handelt:** Führt Aktionen durch
4. **Lernt:** Verbessert sich durch Feedback

### Agent vs. Chatbot

| Aspekt | Chatbot | Agent |
|--------|---------|-------|
| Interaktion | Nur Text | Text + Tools |
| Fähigkeiten | Antworten | Aktionen durchführen |
| Komplexität | Einfach | Komplex |
| Beispiel | ChatGPT | GitHub Copilot |

---

## 🔧 Tool Definition

### Struktur

```python
def get_weather(location: str) -> str:
    """Hole Wetterdaten für einen Ort.
    
    Args:
        location: Stadt oder Koordinaten
        
    Returns:
        Wetterbeschreibung
    """
    # Implementierung
    return f"Wetter in {location}: Sonnig, 22°C"

# Tool-Definition für Agent
tools = [
    {
        "name": "get_weather",
        "description": "Hole aktuelle Wetterdaten",
        "function": get_weather,
        "parameters": {
            "location": "str - Stadt oder Koordinaten"
        }
    }
]
```

### Beispiel-Tools

```python
def calculator(expression: str) -> float:
    """Berechne mathematische Ausdrücke"""
    return eval(expression)

def search_web(query: str) -> str:
    """Suche im Web"""
    # Würde echte API nutzen
    return f"Ergebnisse für: {query}"

def send_email(to: str, subject: str, body: str) -> bool:
    """Sende eine Email"""
    # Würde echte Email-API nutzen
    return True

def get_time() -> str:
    """Hole aktuelle Zeit"""
    from datetime import datetime
    return datetime.now().isoformat()
```

---

## 🤖 Einfacher Agent

### Struktur

```python
from anthropic import Anthropic

client = Anthropic()

# Tools definieren
tools = [
    {
        "name": "calculator",
        "description": "Berechne mathematische Ausdrücke",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematischer Ausdruck"
                }
            },
            "required": ["expression"]
        }
    }
]

def calculator(expression: str) -> str:
    """Führe Berechnung durch"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Fehler: {e}"

def run_agent(user_message: str):
    """Führe Agent aus"""
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        # Rufe Claude auf
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # Prüfe ob Tool-Aufruf
        if response.stop_reason == "tool_use":
            # Finde Tool-Aufruf
            tool_use = next(
                (block for block in response.content 
                 if block.type == "tool_use"),
                None
            )
            
            if tool_use:
                # Führe Tool aus
                tool_name = tool_use.name
                tool_input = tool_use.input
                
                if tool_name == "calculator":
                    result = calculator(tool_input["expression"])
                
                # Füge Ergebnis zu Messages hinzu
                messages.append({"role": "assistant", "content": response.content})
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": result
                        }
                    ]
                })
        else:
            # Agent ist fertig
            final_response = next(
                (block.text for block in response.content 
                 if hasattr(block, "text")),
                None
            )
            return final_response

# Nutzen
result = run_agent("Was ist 25 * 4 + 10?")
print(result)
```

---

## 🔄 Multi-Step Reasoning

### Beispiel: Reiseplanung

```
Benutzer: "Plane eine Reise nach Berlin für 3 Tage"

Agent denkt:
1. Ich brauche Flugpreise
2. Ich brauche Hotel-Preise
3. Ich brauche Sehenswürdigkeiten
4. Ich brauche Wetter-Vorhersage

Agent handelt:
1. Ruft search_flights() auf
2. Ruft search_hotels() auf
3. Ruft get_attractions() auf
4. Ruft get_weather() auf

Agent antwortet:
"Hier ist dein Reiseplan..."
```

---

## ⚠️ Häufige Fehler

| Fehler | Lösung |
|--------|--------|
| Tool gibt falsches Format | Validiere Output |
| Agent ruft Tool nicht auf | Prüfe Tool-Definition |
| Endlosschleife | Setze max. Iterationen |
| Zu viele Tools | Reduziere auf nötige |

---

## 🎯 Best Practices

1. **Tools klar definieren:** Beschreibung ist wichtig
2. **Error Handling:** Tools sollten robust sein
3. **Limits setzen:** Max. Iterationen, Timeout
4. **Logging:** Debugge Agent-Entscheidungen
5. **Testen:** Teste mit verschiedenen Inputs

---

## 💡 Praktische Übung

Implementiere einen Agent mit:
- [ ] Mindestens 2 Tools
- [ ] Error Handling
- [ ] Logging
- [ ] Tests

---

## 📚 Ressourcen

- [Anthropic Tool Use Guide](https://docs.anthropic.com/claude/docs/tool-use)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)

---

**Merksatz:** "Agents sind wie Assistenten - gib ihnen die richtigen Tools!" 🤖

