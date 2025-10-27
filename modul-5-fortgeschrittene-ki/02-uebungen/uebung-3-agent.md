# Übung 3: Agent mit Tools

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

AI Agent mit Tool-Nutzung implementieren.

## Aufgabe

Erstellen Sie einen Agent der Tools nutzen kann.

## Prompt-Vorlage

```text
Erstelle einen AI Agent mit Function Calling:

Tools:
1. calculator(expression: str) -> float
   - Berechnet mathematische Ausdrücke
   
2. search_web(query: str) -> str
   - Simuliert Web-Suche (Mock)
   
3. get_weather(city: str) -> dict
   - Holt Wetter-Daten (Mock)

Agent-Logik:
1. User-Anfrage analysieren
2. Passende Tools auswählen
3. Tools ausführen
4. Ergebnis in Antwort integrieren

Verwende OpenAI Function Calling:
- Tools als JSON Schema definieren
- LLM entscheidet welches Tool
- Tool ausführen
- Ergebnis zurück an LLM

Beispiel:
```python
agent = Agent()

# Agent nutzt Calculator-Tool
response = agent.run("Was ist 15 * 23?")
print(response)  # "15 * 23 = 345"

# Agent nutzt Weather-Tool
response = agent.run("Wie ist das Wetter in Zürich?")
print(response)
```

Mit vollständiger Implementierung.
```

## Erwartetes Ergebnis

- Agent wählt richtige Tools
- Tools werden ausgeführt
- Antworten integrieren Tool-Ergebnisse

## ✅ Erfolg

- [ ] Function Calling funktioniert
- [ ] Tools werden genutzt
- [ ] Antworten korrekt
- [ ] Code dokumentiert

---

**Zurück zu:** [Übungen README](./README.md)
