# Aufgabe 3: KI-Anwendung in Production

**Schwierigkeit:** ⭐⭐⭐⭐⭐  
**Zeitaufwand:** 200 Minuten  
**Deadline:** Vor Abschluss

## 🎯 Ziel

Eine produktionsreife KI-Anwendung entwickeln und deployen.

## 📋 Anforderungen

### Funktionalität
- [ ] Vollständige KI-Integration
- [ ] Benutzer-Interface (Web oder CLI)
- [ ] Datenbank-Integration
- [ ] API-Endpoints
- [ ] Error Handling

### Production-Readiness
- [ ] Monitoring & Logging
- [ ] Rate Limiting
- [ ] Authentication
- [ ] Caching
- [ ] Performance-Optimierung

### Deployment
- [ ] Docker-Container
- [ ] CI/CD Pipeline
- [ ] Deployment-Dokumentation
- [ ] Skalierbarkeit

### Sicherheit & Ethik
- [ ] Input Validation
- [ ] Data Privacy
- [ ] Bias-Checking
- [ ] Audit Trail

## 🏗️ Architektur

```
┌─────────────────────────────────────────┐
│         Frontend (Web/CLI)              │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│         API Gateway                     │
│    (Authentication, Rate Limiting)      │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Business Logic Layer               │
│  (Agents, Processing, Validation)       │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
┌───▼──┐  ┌─────▼──┐  ┌──────▼──┐
│ LLM  │  │Database│  │ Cache   │
│ API  │  │        │  │ (Redis) │
└──────┘  └────────┘  └─────────┘
```

## 🔧 Technologie-Stack

### Backend
```python
# FastAPI für API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Anthropic für LLM
from anthropic import Anthropic

# SQLAlchemy für Datenbank
from sqlalchemy import create_engine

# Redis für Caching
import redis

# Pydantic für Validierung
from pydantic import BaseModel
```

### Frontend
```html
<!-- HTML/JavaScript oder React -->
<form id="chat-form">
    <input type="text" id="message" placeholder="Nachricht...">
    <button type="submit">Senden</button>
</form>

<script>
    document.getElementById('chat-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = document.getElementById('message').value;
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message})
        });
        const data = await response.json();
        console.log(data.response);
    });
</script>
```

### Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install uv && uv sync

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📊 Implementierungs-Schritte

### Phase 1: Backend (60 Min.)
- [ ] FastAPI Setup
- [ ] LLM Integration
- [ ] Datenbank-Schema
- [ ] API-Endpoints

### Phase 2: Frontend (40 Min.)
- [ ] HTML/CSS
- [ ] JavaScript für API-Calls
- [ ] Error Handling
- [ ] Responsive Design

### Phase 3: Production (60 Min.)
- [ ] Monitoring Setup
- [ ] Logging
- [ ] Error Handling
- [ ] Performance-Optimierung

### Phase 4: Deployment (40 Min.)
- [ ] Docker-Image
- [ ] CI/CD Pipeline
- [ ] Deployment-Test
- [ ] Dokumentation

## 💻 Beispiel-Implementierung

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from anthropic import Anthropic
import logging

app = FastAPI()
client = Anthropic()
logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat-Endpoint"""
    try:
        # Validierung
        if not request.message or len(request.message) > 1000:
            raise HTTPException(status_code=400, detail="Invalid input")
        
        # LLM-Aufruf
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": request.message}
            ]
        )
        
        response_text = message.content[0].text
        
        logger.info(f"Chat: {request.message[:50]}... -> {response_text[:50]}...")
        
        return ChatResponse(response=response_text)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal error")
```

## 📋 Deployment-Checkliste

- [ ] **Code:**
  - [ ] Alle Tests bestehen
  - [ ] Code-Review durchgeführt
  - [ ] Secrets nicht in Git

- [ ] **Infrastruktur:**
  - [ ] Docker-Image gebaut
  - [ ] Environment-Variablen gesetzt
  - [ ] Datenbank migriert

- [ ] **Monitoring:**
  - [ ] Logging konfiguriert
  - [ ] Metriken eingerichtet
  - [ ] Alerts konfiguriert

- [ ] **Sicherheit:**
  - [ ] SSL/TLS aktiviert
  - [ ] Authentication funktioniert
  - [ ] Rate Limiting aktiv

- [ ] **Performance:**
  - [ ] Caching funktioniert
  - [ ] API-Latenz < 500ms
  - [ ] Kann 100 Requests/s verarbeiten

## 📚 Ressourcen

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [GitHub Actions CI/CD](https://docs.github.com/en/actions)
- [Render Deployment](https://render.com/)

## ✅ Finale Checkliste

- [ ] Anwendung funktioniert lokal
- [ ] Anwendung deployed
- [ ] Monitoring aktiv
- [ ] Dokumentation vollständig
- [ ] Tests vorhanden
- [ ] Performance akzeptabel
- [ ] Sicherheit gewährleistet
- [ ] Bereit für Produktion

---

**Merksatz:** "Production ist nicht das Ende, sondern der Anfang!" 🚀

