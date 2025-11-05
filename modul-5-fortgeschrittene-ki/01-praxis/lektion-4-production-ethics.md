# Lektion 4: Production & Ethics

**Dauer:** 50 Minuten  
**Für:** Modul 5 - Fortgeschrittene KI

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:
- ✅ KI-Systeme produktionsreif machen
- ✅ Ethische Implikationen verstehen
- ✅ Bias und Fairness adressieren
- ✅ Sicherheit und Privacy gewährleisten
- ✅ Verantwortungsvoll mit KI umgehen

---

## 🚀 Production Readiness

### Checkliste

- [ ] **Performance:** API-Latenz < 500ms
- [ ] **Skalierbarkeit:** Kann 1000 Requests/min verarbeiten
- [ ] **Monitoring:** Metriken und Logs vorhanden
- [ ] **Error Handling:** Robuste Fehlerbehandlung
- [ ] **Caching:** Häufige Anfragen gecacht
- [ ] **Rate Limiting:** Schutz vor Missbrauch
- [ ] **Authentication:** Nur autorisierte Nutzer
- [ ] **Encryption:** Daten verschlüsselt

### Deployment-Strategie

```python
# Beispiel: FastAPI mit Production-Features

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
import logging

app = FastAPI()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/api/chat")
@limiter.limit("10/minute")
async def chat(message: str):
    """Chat-Endpoint mit Rate Limiting"""
    try:
        logger.info(f"Chat request: {message[:50]}...")
        
        # Validierung
        if not message or len(message) > 1000:
            raise HTTPException(status_code=400, detail="Invalid input")
        
        # Verarbeitung
        response = process_message(message)
        
        logger.info(f"Chat response: {response[:50]}...")
        return {"response": response}
        
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal error")
```

---

## ⚖️ Ethische Überlegungen

### 1. Bias & Fairness

**Problem:** KI-Modelle können Bias aus Trainingsdaten erben

**Lösungen:**
```python
def check_bias(predictions, protected_attributes):
    """Prüfe auf Bias in Vorhersagen"""
    for attr in protected_attributes:
        group_a = predictions[attr == 'A']
        group_b = predictions[attr == 'B']
        
        # Prüfe auf signifikante Unterschiede
        if abs(group_a.mean() - group_b.mean()) > 0.1:
            logger.warning(f"Potential bias detected for {attr}")
            return False
    return True
```

### 2. Transparency & Explainability

**Problem:** "Black Box" KI-Entscheidungen

**Lösungen:**
```python
def explain_decision(input_data, prediction):
    """Erkläre KI-Entscheidung"""
    return {
        "prediction": prediction,
        "confidence": 0.95,
        "reasoning": "Based on features X, Y, Z",
        "similar_examples": [...]
    }
```

### 3. Privacy & Data Protection

**Problem:** Sensible Daten könnten missbraucht werden

**Lösungen:**
```python
# Anonymisierung
def anonymize_data(data):
    """Entferne persönliche Informationen"""
    data['email'] = hash(data['email'])
    data['phone'] = None
    return data

# Differential Privacy
from diffprivlib.models import LogisticRegression
model = LogisticRegression(epsilon=1.0)
```

### 4. Accountability & Responsibility

**Problem:** Wer trägt Verantwortung für KI-Fehler?

**Lösungen:**
```python
# Audit Trail
def log_decision(user_id, input_data, output, model_version):
    """Protokolliere alle KI-Entscheidungen"""
    audit_log.append({
        "timestamp": datetime.now(),
        "user_id": user_id,
        "input": input_data,
        "output": output,
        "model_version": model_version
    })
```

---

## 🔒 Sicherheit

### Input Validation

```python
def validate_input(user_input: str) -> bool:
    """Validiere Benutzer-Input"""
    # Länge prüfen
    if len(user_input) > 10000:
        return False
    
    # Injection-Angriffe prüfen
    dangerous_patterns = ['<script>', 'DROP TABLE', '${']
    for pattern in dangerous_patterns:
        if pattern in user_input:
            return False
    
    return True
```

### API Security

```python
from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def verify_token(credentials = Security(security)):
    """Verifiziere API-Token"""
    token = credentials.credentials
    if not is_valid_token(token):
        raise HTTPException(status_code=401)
    return token
```

---

## 📊 Monitoring & Metrics

```python
from prometheus_client import Counter, Histogram

# Metriken
request_count = Counter('requests_total', 'Total requests')
request_duration = Histogram('request_duration_seconds', 'Request duration')
error_count = Counter('errors_total', 'Total errors')

@app.post("/api/chat")
async def chat(message: str):
    request_count.inc()
    
    with request_duration.time():
        try:
            response = process_message(message)
            return {"response": response}
        except Exception as e:
            error_count.inc()
            raise
```

---

## 🎓 Ethik-Checkliste

- [ ] **Bias:** Wurde auf Bias geprüft?
- [ ] **Transparency:** Können Entscheidungen erklärt werden?
- [ ] **Privacy:** Sind Daten geschützt?
- [ ] **Accountability:** Gibt es Audit Trail?
- [ ] **Fairness:** Werden alle Gruppen fair behandelt?
- [ ] **Safety:** Gibt es Safeguards?
- [ ] **Consent:** Haben Nutzer zugestimmt?

---

## 📚 Ressourcen

- [AI Ethics Guidelines](https://www.oecd.org/ai/principles/)
- [Fairness in ML](https://fairmlbook.org/)
- [Privacy-Preserving ML](https://www.openmined.org/)
- [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)

---

## 💡 Praktische Übung

Implementiere:
- [ ] Input Validation
- [ ] Error Handling
- [ ] Logging
- [ ] Rate Limiting
- [ ] Bias-Check

---

**Merksatz:** "Mit grosser KI-Kraft kommt grosse Verantwortung!" 🦸

