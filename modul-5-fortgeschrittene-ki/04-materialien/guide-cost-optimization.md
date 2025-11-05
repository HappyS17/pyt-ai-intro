# Cost Optimization Guide

**Für:** Modul 5 - Fortgeschrittene KI  
**Version:** 1.0

---

## 💰 Warum Kosten-Optimierung wichtig ist

- ✅ Spart Geld
- ✅ Verbessert Skalierbarkeit
- ✅ Reduziert Latenz
- ✅ Verbessert User Experience

---

## 📊 Kostenmodelle

### OpenAI Pricing (Beispiel)

```
GPT-4:
- Input: $0.03 / 1K tokens
- Output: $0.06 / 1K tokens

GPT-3.5-turbo:
- Input: $0.0005 / 1K tokens
- Output: $0.0015 / 1K tokens

Claude 3.5 Sonnet:
- Input: $0.003 / 1K tokens
- Output: $0.015 / 1K tokens
```

### Kostenberechnung

```python
def calculate_cost(input_tokens, output_tokens, model="gpt-3.5-turbo"):
    """Berechne API-Kosten"""
    pricing = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "claude-3.5-sonnet": {"input": 0.003, "output": 0.015}
    }
    
    rates = pricing[model]
    input_cost = (input_tokens / 1000) * rates["input"]
    output_cost = (output_tokens / 1000) * rates["output"]
    
    return input_cost + output_cost
```

---

## 🎯 Optimierungs-Strategien

### 1. Model Selection

```python
# ❌ Teuer: Nutze GPT-4 für alles
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hallo"}]
)

# ✅ Günstig: Nutze günstigeres Modell für einfache Tasks
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hallo"}]
)

# ✅ Smart: Nutze richtiges Modell für Task
if is_complex_task:
    model = "gpt-4"
else:
    model = "gpt-3.5-turbo"
```

### 2. Prompt Optimization

```python
# ❌ Teuer: Lange Prompts
prompt = """
Du bist ein Python-Experte mit 20 Jahren Erfahrung.
Du kennst alle Best Practices...
[100 Zeilen Kontext]
Schreib mir Code für X
"""

# ✅ Günstig: Kurze, prägnante Prompts
prompt = """
Schreib Python-Code für X.
Nutze Best Practices.
"""

# Einsparung: 80% weniger Input-Tokens
```

### 3. Caching

```python
import redis

cache = redis.Redis()

def get_response(prompt):
    # Prüfe Cache
    cached = cache.get(prompt)
    if cached:
        return cached
    
    # Rufe API auf
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Speichere im Cache
    cache.set(prompt, response, ex=3600)  # 1 Stunde
    
    return response
```

### 4. Batch Processing

```python
# ❌ Teuer: Einzelne Requests
for item in items:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": item}]
    )

# ✅ Günstig: Batch-Requests
batch_requests = [
    {"custom_id": f"request-{i}", "params": {"messages": [...]}}
    for i, item in enumerate(items)
]

# Nutze Batch API (günstiger, aber langsamer)
```

### 5. Token Reduction

```python
# ❌ Teuer: Viele Tokens
text = """
Dies ist ein sehr langer Text mit vielen Wörtern
die nicht wirklich notwendig sind um die Bedeutung
zu verstehen. Wir könnten das viel kürzer machen.
"""

# ✅ Günstig: Komprimierter Text
text = "Langer Text mit vielen unnötigen Wörtern"

# Einsparung: 60% weniger Tokens
```

---

## 📈 Monitoring & Tracking

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CostTracker:
    def __init__(self):
        self.total_cost = 0
        self.requests = 0
    
    def track_request(self, input_tokens, output_tokens, model):
        """Verfolge API-Kosten"""
        cost = calculate_cost(input_tokens, output_tokens, model)
        self.total_cost += cost
        self.requests += 1
        
        logger.info(f"Request #{self.requests}: ${cost:.4f}")
        logger.info(f"Total: ${self.total_cost:.2f}")
        
        return cost

# Nutzen
tracker = CostTracker()
tracker.track_request(100, 50, "gpt-3.5-turbo")
```

---

## 🎯 Optimierungs-Checkliste

- [ ] **Model Selection:** Nutze richtiges Modell
- [ ] **Prompt Optimization:** Kurze, prägnante Prompts
- [ ] **Caching:** Cache häufige Anfragen
- [ ] **Batch Processing:** Nutze Batch API wenn möglich
- [ ] **Token Reduction:** Minimiere Token-Nutzung
- [ ] **Monitoring:** Verfolge Kosten
- [ ] **Rate Limiting:** Verhindere Missbrauch

---

## 💡 Praktische Tipps

### 1. Kosten-Budgets setzen
```python
MAX_MONTHLY_COST = 100  # $100/Monat

if total_cost > MAX_MONTHLY_COST:
    logger.warning("Budget überschritten!")
    disable_expensive_features()
```

### 2. Alerts konfigurieren
```python
if daily_cost > 10:  # $10/Tag
    send_alert("Hohe API-Kosten!")
```

### 3. A/B Testing
```python
# Teste verschiedene Modelle
model_a = "gpt-4"  # Teuer, aber besser
model_b = "gpt-3.5-turbo"  # Günstig

# Vergleiche Qualität vs. Kosten
```

---

## 📊 Kostenvergleich

| Szenario | Modell | Kosten/1000 Requests |
|----------|--------|---------------------|
| Einfache Fragen | GPT-3.5 | $0.50 |
| Komplexe Aufgaben | GPT-4 | $3.00 |
| Mit Caching | GPT-3.5 | $0.25 |
| Mit Batch API | GPT-3.5 | $0.10 |

---

## 🚀 Skalierungs-Strategie

```
Phase 1: MVP (Kosten: $10/Monat)
- Nutze günstigstes Modell
- Kein Caching
- Kleine Nutzerbasis

Phase 2: Growth (Kosten: $100/Monat)
- Implementiere Caching
- Nutze Batch API
- Monitoring aktiv

Phase 3: Scale (Kosten: $1000/Monat)
- Fine-tuning für spezifische Tasks
- Eigene Modelle trainieren
- Komplexe Optimierungen
```

---

## 📚 Ressourcen

- [OpenAI Pricing](https://openai.com/pricing)
- [Anthropic Pricing](https://www.anthropic.com/pricing)
- [Cost Optimization Best Practices](https://platform.openai.com/docs/guides/tokens)

---

## ✅ Checkliste für Production

- [ ] Kosten-Tracking implementiert
- [ ] Budgets gesetzt
- [ ] Alerts konfiguriert
- [ ] Caching aktiv
- [ ] Monitoring läuft
- [ ] Dokumentation vorhanden

---

**Merksatz:** "Jeder Token zählt - optimiere weise!" 💰

