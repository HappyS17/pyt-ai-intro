# Übung 1: Chatbot mit API

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Ziel

Einen funktionsfähigen Chatbot mit LLM API erstellen.

## Aufgabe

Erstellen Sie einen Chatbot mit Persönlichkeit und Kontext-Management.

## Prompt-Vorlage

```text
Erstelle einen Python-Chatbot mit OpenAI API:

Features:
1. System-Prompt für Persönlichkeit
2. Kontext-Management (letzte N Nachrichten)
3. Streaming-Responses
4. Token-Counting
5. Kosten-Tracking

Anforderungen:
- Klasse ChatBot
- Methode chat(message: str) -> str
- Methode reset()
- Methode get_cost() -> float
- CLI-Interface

Beispiel:
```python
bot = ChatBot(
    system_prompt="Du bist ein Python-Tutor",
    model="gpt-3.5-turbo",
    max_context=10
)

response = bot.chat("Erkläre List Comprehensions")
print(response)
print(f"Kosten: ${bot.get_cost():.4f}")
```

Mit Type Hints, Docstrings und Error Handling.
```

## Erwartetes Ergebnis

- Funktionierender Chatbot
- Kontext wird beibehalten
- Kosten werden getrackt
- CLI funktioniert

## ✅ Erfolg

- [ ] Chatbot funktioniert
- [ ] Kontext-Management
- [ ] Kosten-Tracking
- [ ] Error Handling
- [ ] Code dokumentiert

---

**Zurück zu:** [Übungen README](./README.md)
