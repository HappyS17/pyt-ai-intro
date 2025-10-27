# Lektion 1: LLM APIs & Prompt Engineering

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

- OpenAI/Anthropic APIs nutzen
- Chat Completions verstehen
- Streaming implementieren
- Function Calling nutzen

## 📚 Theorie (15 Min.)

### OpenAI API Setup

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Erkläre Python in 3 Sätzen."}
    ],
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].message.content)
```

### Streaming

```python
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Erzähle eine Geschichte"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Function Calling

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Holt Wetter für eine Stadt",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Wie ist das Wetter in Zürich?"}],
    tools=tools
)
```

## 💻 Live-Demo (20 Min.)

### Demo: Chatbot

```python
"""Einfacher Chatbot mit OpenAI"""
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(messages: list) -> str:
    """Sendet Nachricht an API."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )
    return response.choices[0].message.content

# Chat-Loop
messages = [
    {"role": "system", "content": "Du bist ein Python-Tutor."}
]

while True:
    user_input = input("Du: ")
    if user_input.lower() == "quit":
        break
    
    messages.append({"role": "user", "content": user_input})
    response = chat(messages)
    messages.append({"role": "assistant", "content": response})
    
    print(f"Bot: {response}\n")
```

## ✏️ Übung (15 Min.)

Erstelle einen Chatbot mit Persönlichkeit.

---

**Weiter zu:** [Lektion 2 - RAG](./lektion-2-rag.md)
