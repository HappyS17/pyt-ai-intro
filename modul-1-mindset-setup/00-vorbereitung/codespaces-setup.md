# GitHub Codespaces Setup

**Zeitaufwand:** 15 Minuten  
**Ziel:** Cloud-basierte Entwicklungsumgebung ohne lokale Installation

## 🎯 Was ist GitHub Codespaces?

GitHub Codespaces ist eine **vollständig konfigurierte Cloud-IDE** direkt in deinem Browser:

- ✅ Keine lokale Installation nötig
- ✅ Funktioniert auf jedem Gerät (Windows, Mac, Linux, Tablet)
- ✅ Alle Tools bereits installiert
- ✅ Kostenlos für Studierende

---

## 💰 Kostenlos für alle Studierenden

### ✅ Gute Nachricht: Keine .edu Email nötig!

Jeder mit einem **kostenlosen GitHub Account** bekommt automatisch:

| Ressource | Limit |
|-----------|-------|
| **Compute-Stunden/Monat** | 60 Stunden |
| **Storage** | 15 GB |
| **Gleichzeitige Codespaces** | 1 aktiv |
| **Machine Type** | 2-core (Standard) |

**Beispiel:** 60 Stunden = 2 Stunden pro Tag für einen Monat ✅

### Optional: GitHub Student Developer Pack

Falls deine Institution eine **.edu Email-Adresse** anbietet, kannst du zusätzliche Vorteile bekommen:

1. Gehe zu [github.com/education/students](https://github.com/education/students)
2. Klicke "Get benefits"
3. Verifiziere mit deiner **.edu Email-Adresse**
4. Warte auf Bestätigung (meist sofort)

**Aber:** Du brauchst das NICHT für Codespaces - die 60 Stunden/Monat bekommst du auch ohne!

---

## 🚀 Codespace starten

### Option 1: Schnellstart (empfohlen)

1. Gehe zum Repository: [github.com/talent-factory/pyt-ai-intro](https://github.com/talent-factory/pyt-ai-intro)
2. Klicke grüner Button **"Code"**
3. Wähle **"Codespaces"** Tab
4. Klicke **"Create codespace on main"**
5. Warte ~2 Minuten auf Initialisierung

### Option 2: Über GitHub.dev (noch schneller, aber limitiert)

1. Drücke `.` (Punkt) auf der Repository-Seite
2. Öffnet VS Code im Browser
3. ⚠️ Nur für Datei-Bearbeitung, nicht für Ausführung

---

## ✅ Nach dem Start

### Automatisch installiert

- ✅ Python 3.13
- ✅ Git
- ✅ VS Code Extensions (Python, Copilot, etc.)
- ✅ Alle Dependencies aus `requirements-dev.txt`

### Terminal öffnen

```bash
# Terminal öffnen: Ctrl+` (Backtick)
python --version
# Sollte: Python 3.13.x
```

### Erstes Programm testen

```bash
# Erstelle test.py
echo 'print("Hello from Codespaces!")' > test.py

# Führe aus
python test.py
```

---

## 🔄 Codespace verwalten

### Codespace pausieren (spart Stunden!)

1. Gehe zu [github.com/codespaces](https://github.com/codespaces)
2. Klick auf dein Codespace
3. Klick **"..."** → **"Stop codespace"**
4. ⏸️ Pausiert = keine Stunden verbraucht

### Codespace löschen

1. [github.com/codespaces](https://github.com/codespaces)
2. Klick **"..."** → **"Delete"**
3. Speichert Speicherplatz

### Codespace fortsetzen

1. [github.com/codespaces](https://github.com/codespaces)
2. Klick auf dein Codespace
3. Startet automatisch

---

## 💡 Tipps & Tricks

### Keyboard Shortcuts

- `Ctrl+` ` ` - Terminal öffnen
- `Ctrl+Shift+P` - Command Palette
- `Ctrl+/` - Kommentar
- `Ctrl+S` - Speichern (auto-save ist an)

### GitHub Copilot nutzen

- Tippe in `.py` Datei
- Copilot schlägt Code vor
- `Tab` zum Akzeptieren

### Port Forwarding

Wenn du einen Server startest (Flask, FastAPI):

```bash
python -m flask run
# Oder
uvicorn main:app --reload
```

→ Codespaces zeigt automatisch einen Link zum Öffnen

---

## ⚠️ Wichtig: Stunden sparen

### Automatisches Herunterfahren

- Nach **30 Minuten Inaktivität** → Codespace pausiert
- Nach **30 Tagen** → Codespace gelöscht

### Manuelle Verwaltung

- **Immer pausieren** wenn du fertig bist
- Nicht mehrere Codespaces gleichzeitig offen lassen
- Lösche alte Codespaces

---

## 🆘 Probleme?

### Codespace startet nicht

- Warte 2-3 Minuten
- Aktualisiere die Seite
- Versuche einen neuen Codespace

### Zu langsam

- Schliesse andere Browser-Tabs
- Nutze 2-core Machine (Standard)
- Pausiere und starte neu

### Stunden aufgebraucht

- Warte bis zum nächsten Monat
- Oder nutze lokale Installation
- Oder frag deinen Kursleiter

---

## 📚 Weitere Ressourcen

- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [GitHub Student Pack](https://education.github.com/pack)
- [Codespaces Pricing](https://github.com/features/codespaces/pricing)

---

## ✅ Fertig?

Dein Codespace ist bereit! Du kannst jetzt:

- ✅ Python-Code schreiben und ausführen
- ✅ Git-Befehle nutzen
- ✅ GitHub Copilot verwenden
- ✅ Alle Kursmaterialien bearbeiten

**Weiter zu:** [Installationsanleitung (lokal)](./installationsanleitung.md) oder [Erste Schritte](./erste-schritte.md)
