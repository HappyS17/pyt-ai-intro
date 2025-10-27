# LLM API Cheat Sheet

Schnellreferenz für OpenAI und Anthropic APIs.

## OpenAI API

### Setup

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### Chat Completion

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Du bist ein Assistent"},
        {"role": "user", "content": "Hallo!"}
    ],
    max_tokens=100,
    temperature=0.7
)

print(response.choices[0].message.content)
```

### Streaming

```python
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Erzähle Geschichte"}],
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
        "description": "Holt Wetter",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            }
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Wetter in Zürich?"}],
    tools=tools
)
```

### Embeddings

```python
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Text für Embedding"
)

embedding = response.data[0].embedding  # Liste von Floats
```

## Anthropic API

### Setup

```python
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
```

### Messages

```python
response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hallo!"}
    ]
)

print(response.content[0].text)
```

## Best Practices

- ✅ API Keys in `.env`
- ✅ Spending Limits setzen
- ✅ Error Handling
- ✅ Retry mit Exponential Backoff
- ✅ Token-Counting
- ✅ Caching für häufige Anfragen

---

**Zurück zu:** [Materialien README](./README.md)
