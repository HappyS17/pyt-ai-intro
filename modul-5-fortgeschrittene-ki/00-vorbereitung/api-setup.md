# API-Setup

**Zeitaufwand:** 45 Minuten  
**Ziel:** LLM API einrichten und testen

## 🎯 Aufgabe

Richten Sie einen API-Zugang ein und führen Sie erste Tests durch.

## Option A: OpenAI (empfohlen)

### Schritt 1: Account erstellen (10 Min.)

1. Gehe zu [platform.openai.com](https://platform.openai.com)
2. Registriere dich (Email oder Google)
3. Verifiziere Email
4. Füge Zahlungsmethode hinzu

**Kosten:**
- Erste $5 gratis (für neue Accounts)
- GPT-3.5-Turbo: ~$0.001 pro 1000 Tokens
- GPT-4: ~$0.03 pro 1000 Tokens

### Schritt 2: API Key erstellen (5 Min.)

1. Gehe zu "API Keys"
2. Klicke "Create new secret key"
3. Kopiere Key (wird nur einmal angezeigt!)
4. Speichere sicher (z.B. in Password Manager)

### Schritt 3: Setup in Python (10 Min.)

```bash
# Installation mit uv
uv sync
```

Erstelle `.env` Datei:

```bash
OPENAI_API_KEY=sk-...
```

**Wichtig:** Füge `.env` zu `.gitignore` hinzu!

```bash
echo ".env" >> .gitignore
```

### Schritt 4: Erster Test (10 Min.)

```python
# test_openai.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Einfacher Test
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Sage Hallo auf Deutsch"}
    ],
    max_tokens=50
)

print(response.choices[0].message.content)
print(f"\nTokens verwendet: {response.usage.total_tokens}")
print(f"Kosten: ~${response.usage.total_tokens * 0.000001:.6f}")
```

### Schritt 5: Spending Limit setzen (10 Min.)

1. Gehe zu "Settings" → "Limits"
2. Setze "Monthly budget" (z.B. $10)
3. Aktiviere Email-Benachrichtigungen

## Option B: Anthropic (Claude)

### Schritt 1: Account erstellen

1. Gehe zu [console.anthropic.com](https://console.anthropic.com)
2. Registriere dich
3. Füge Zahlungsmethode hinzu

**Kosten:**
- Claude 3 Sonnet: ~$0.003 pro 1000 Tokens
- Claude 3 Opus: ~$0.015 pro 1000 Tokens

### Schritt 2: API Key

1. Gehe zu "API Keys"
2. Erstelle neuen Key
3. Speichere sicher

### Schritt 3: Setup

```bash
uv sync
```

`.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-...
```

### Schritt 4: Test

```python
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=50,
    messages=[
        {"role": "user", "content": "Sage Hallo auf Deutsch"}
    ]
)

print(response.content[0].text)
```

## Dokumentation

### Welche API haben Sie gewählt?

```text
[ ] OpenAI
[ ] Anthropic
[ ] Andere: _______
```

### Erster Test erfolgreich?

```text
[ ] Ja
[ ] Nein, Fehler: _______
```

### Spending Limit gesetzt?

```text
[ ] Ja, Limit: $_______
[ ] Nein
```

### Geschätzte Kosten für Kurs?

```text
Basierend auf Tests: $_______
```

## ⚠️ Sicherheit

- ❌ **NIEMALS** API Keys in Git committen
- ✅ Immer `.env` Dateien nutzen
- ✅ `.env` in `.gitignore`
- ✅ Spending Limits setzen
- ✅ Keys regelmässig rotieren

## 💡 Tipps

- Für Entwicklung: GPT-3.5-Turbo oder Claude Sonnet (günstiger)
- Für Production: GPT-4 oder Claude Opus (besser)
- Monitoring: Nutze OpenAI Dashboard für Usage-Tracking
- Caching: Speichere häufige Anfragen

## ✅ Checkliste

- [ ] Account erstellt
- [ ] API Key generiert
- [ ] `.env` Datei erstellt
- [ ] `.gitignore` aktualisiert
- [ ] Erster Test erfolgreich
- [ ] Spending Limit gesetzt
- [ ] Kosten verstanden

---

**Zurück zu:** [Vorbereitung README](./README.md)
