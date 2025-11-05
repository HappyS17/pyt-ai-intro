# GitHub Codespaces Setup Guide für Dozenten

Dieses Dokument erklärt die Codespaces-Konfiguration und wie Studierende diese nutzen können.

## 📋 Übersicht

Das Projekt ist jetzt vollständig für GitHub Codespaces konfiguriert:

- ✅ `.devcontainer/devcontainer.json` - Automatische Umgebungskonfiguration
- ✅ `requirements-dev.txt` - Alle Dependencies für den Kurs
- ✅ `.gitignore` - Sicherheit für API Keys und Secrets
- ✅ `modul-1-mindset-setup/00-vorbereitung/codespaces-setup.md` - Anleitung für Studierende

---

## 🎯 Was ist Codespaces?

GitHub Codespaces ist eine **vollständig konfigurierte Cloud-IDE**:

- Läuft im Browser (VS Code Web)
- Keine lokale Installation nötig
- Alle Tools automatisch installiert
- **Kostenlos für alle** mit GitHub Free Account (60 Stunden/Monat)
- Keine .edu Email-Adresse erforderlich!

---

## 💰 Kostenmodell für Studierende

### Option 1: Kostenlos mit GitHub Free Account (EMPFOHLEN)

**Voraussetzung:** Kostenloser GitHub Account (keine .edu Email nötig!)

**Kostenlose Limits:**

- **60 Compute-Stunden/Monat** (für jeden!)
- 15 GB Storage
- 1 aktiver Codespace gleichzeitig
- 2-core Machine (Standard)

**Beispiel-Rechnung:**

- 60 Stunden/Monat = 2 Stunden/Tag
- Ausreichend für Kursmaterialien + Übungen
- Pausieren spart Stunden (nach 30 Min. Inaktivität automatisch)

**Wichtig:** Studierende brauchen KEINE .edu Email-Adresse! Jeder mit einem kostenlosen GitHub Account bekommt 60 Stunden/Monat.

### Option 2: GitHub Student Developer Pack (optional)

**Voraussetzung:** .edu Email-Adresse (falls verfügbar)

**Zusätzliche Vorteile:**

- Gleiche 60 Stunden/Monat wie Free Account
- Zusätzliche Tools und Services
- GitHub Pro kostenlos

### Option 3: Für Kurse (GitHub Classroom)

Wenn du **GitHub Classroom** nutzt:

- Kostenlose Codespaces für alle Studierenden (unabhängig von Email)
- Ausreichend für ~50 Studierende mit 5 Assignments/Monat
- Keine Limits für Classroom-Assignments

---

## 🚀 Wie Studierende Codespaces nutzen

### 1. GitHub Student Pack aktivieren

```text
1. Gehe zu github.com/education/students
2. Klick "Get benefits"
3. Verifiziere mit .edu Email
4. Warte auf Bestätigung (meist sofort)
```

### 2. Codespace starten

```text
1. Gehe zum Repository
2. Klick grüner "Code" Button
3. Wähle "Codespaces" Tab
4. Klick "Create codespace on main"
5. Warte ~2 Minuten
```

### 3. Automatisch installiert

Die `.devcontainer.json` installiert automatisch:

- Python 3.13
- Git & GitHub CLI
- VS Code Extensions (Python, Copilot, Ruff, Black)
- Alle Dependencies aus `requirements-dev.txt`

---

## 📦 Was ist in `requirements-dev.txt`?

```text
# Core tools
uv, black, ruff, pytest

# Modul 2: Python Grundlagen
cryptography

# Modul 3: Datenverarbeitung
pandas, beautifulsoup4, requests

# Modul 4: Web Frameworks
flask, fastapi, uvicorn

# Modul 5: Advanced AI
openai, anthropic, langchain, chromadb, tiktoken

# Utilities
ipython, jupyter
```

Alle Packages werden automatisch installiert wenn Codespace startet.

---

## ⚙️ Devcontainer konfigurieren

### `.devcontainer/devcontainer.json` erklärt

```json
{
  "name": "Python & KI-gestütztes Programmieren",
  "image": "mcr.microsoft.com/devcontainers/python:3.13",
  // Base Image: Python 3.13 mit allen Tools
  
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  // Zusätzliche Features: Git & GitHub CLI
  
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "GitHub.Copilot",
        // ... weitere Extensions
      ]
    }
  },
  // VS Code Extensions automatisch installieren
  
  "postCreateCommand": "uv sync --group dev",
  // Nach Erstellung: Dependencies mit uv installieren
  
  "forwardPorts": [5000, 8000, 8080],
  // Ports für Flask, FastAPI, Web Apps
}
```

---

## 🔒 Sicherheit

### `.gitignore` schützt:

- ✅ `.env` Dateien (API Keys)
- ✅ `*.key`, `*.pem` (Zertifikate)
- ✅ `secrets.json` (Geheimnisse)
- ✅ `__pycache__/` (Python Cache)
- ✅ `.venv/` (Virtual Environments)

**Wichtig:** Studierende sollten niemals API Keys committen!

---

## 💡 Best Practices für Dozenten

### 1. Studierende informieren

Teile den Link zur Anleitung:

```text
modul-1-mindset-setup/00-vorbereitung/codespaces-setup.md
```

### 2. Hybrid-Ansatz empfehlen

```text
- Codespaces: Kursmaterialien, Übungen, Demos
- Lokal: Grössere Projekte, unbegrenzte Ressourcen
```

### 3. Stunden sparen

Erinnere Studierende:

- Codespace pausieren wenn fertig (spart Stunden!)
- Alte Codespaces löschen
- Nicht mehrere gleichzeitig offen lassen

### 4. GitHub Classroom nutzen

Wenn du Assignments verteilst:

```text
1. Erstelle GitHub Classroom
2. Studierende akzeptieren Assignment
3. Codespaces automatisch kostenlos
4. Keine Limits für Classroom-Work
```

---

## 🆘 Troubleshooting

### Codespace startet nicht

- Warte 2-3 Minuten
- Aktualisiere die Seite
- Versuche einen neuen Codespace

### Zu langsam

- Schliesse andere Browser-Tabs
- Nutze 2-core Machine (Standard)
- Pausiere und starte neu

### Stunden aufgebraucht

- Warte bis zum nächsten Monat (60 Stunden werden monatlich zurückgesetzt)
- Oder nutze lokale Installation mit `uv sync --group dev`
- Oder nutze Dev Container lokal in VS Code
- Oder frag deinen Kursleiter

### Dependencies nicht installiert

- Terminal öffnen: `Ctrl+` ` `
- Manuell installieren: `uv sync --group dev`

---

## 📚 Weitere Ressourcen

- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [GitHub Student Pack](https://education.github.com/pack)
- [Devcontainer Spec](https://containers.dev/)
- [GitHub Classroom](https://classroom.github.com/)

---

## ✅ Checkliste für Dozenten

- [ ] Studierende über Codespaces informiert
- [ ] Link zur Anleitung geteilt
- [ ] GitHub Student Pack erklärt
- [ ] Hybrid-Ansatz empfohlen
- [ ] GitHub Classroom Setup (optional)
- [ ] Support-Kanal eingerichtet

---

**Fragen?** Kontaktiere den Kurs-Support oder schau in die GitHub Docs.
