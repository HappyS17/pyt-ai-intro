# Installationsanleitung

**Zeitaufwand:** ca. 90 Minuten  
**Ziel:** Eine vollständig funktionierende Entwicklungsumgebung

## 🎯 Was Sie installieren werden

1. **Python** - Die Programmiersprache
2. **Git** - Versionskontrolle
3. **VS Code** - Code-Editor
4. **uv** - Modernes Python-Paketverwaltungstool
5. **KI-Assistent** - GitHub Copilot oder Alternative

---

## 1️⃣ Python installieren

### Windows

1. Besuchen Sie [python.org/downloads](https://www.python.org/downloads/)
2. Laden Sie die neueste Version herunter (Python 3.11 oder höher)
3. **WICHTIG:** Aktivieren Sie "Add Python to PATH" während der Installation
4. Installieren Sie Python

**Testen:**
```bash
python --version
# Sollte ausgeben: Python 3.11.x oder höher
```

### macOS

**Option A: Mit Homebrew (empfohlen)**
```bash
# Homebrew installieren (falls noch nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python installieren
brew install python@3.11
```

**Option B: Von python.org**
1. Besuchen Sie [python.org/downloads](https://www.python.org/downloads/)
2. Laden Sie den macOS Installer herunter
3. Führen Sie die Installation durch

**Testen:**
```bash
python3 --version
# Sollte ausgeben: Python 3.11.x oder höher
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

**Testen:**
```bash
python3 --version
```

---

## 2️⃣ Git installieren

### Windows

1. Besuchen Sie [git-scm.com/download/win](https://git-scm.com/download/win)
2. Laden Sie den Installer herunter
3. Installieren Sie mit Standardeinstellungen

### macOS

```bash
# Mit Homebrew
brew install git

# ODER: Xcode Command Line Tools
xcode-select --install
```

### Linux

```bash
sudo apt install git
```

### Git konfigurieren (alle Systeme)

```bash
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"
```

**Testen:**
```bash
git --version
# Sollte ausgeben: git version 2.x.x
```

---

## 3️⃣ VS Code installieren

1. Besuchen Sie [code.visualstudio.com](https://code.visualstudio.com/)
2. Laden Sie die Version für Ihr Betriebssystem herunter
3. Installieren Sie VS Code

### Empfohlene Extensions installieren

Öffnen Sie VS Code und installieren Sie folgende Extensions:

1. **Python** (Microsoft)
   - Extension ID: `ms-python.python`
   - Suchen Sie in der Extension-Ansicht (Ctrl/Cmd+Shift+X)

2. **GitHub Copilot** (falls verfügbar)
   - Extension ID: `GitHub.copilot`
   - Benötigt GitHub-Account mit Copilot-Zugang

3. **GitLens** (optional, aber empfohlen)
   - Extension ID: `eamodio.gitlens`
   - Bessere Git-Integration

4. **Python Indent** (optional)
   - Extension ID: `KevinRose.vsc-python-indent`
   - Hilft bei der Einrückung

**Testen:**
- Öffnen Sie VS Code
- Drücken Sie `Ctrl/Cmd+Shift+P`
- Tippen Sie "Python: Select Interpreter"
- Sie sollten Ihre Python-Installation sehen

---

## 4️⃣ uv installieren

**uv** ist ein modernes, schnelles Tool für Python-Paketverwaltung.

### Windows (PowerShell)

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Nach der Installation

Starten Sie Ihr Terminal neu und testen Sie:

```bash
uv --version
# Sollte ausgeben: uv x.x.x
```

---

## 5️⃣ KI-Assistent einrichten

### Option A: GitHub Copilot (empfohlen, falls verfügbar)

1. **GitHub-Account erstellen** (falls noch nicht vorhanden)
   - Besuchen Sie [github.com](https://github.com)
   - Registrieren Sie sich

2. **Copilot aktivieren**
   - Studenten: [Kostenloser Zugang](https://education.github.com/pack)
   - Andere: [Copilot-Abo](https://github.com/features/copilot)

3. **In VS Code anmelden**
   - Öffnen Sie VS Code
   - Klicken Sie auf das GitHub-Symbol unten links
   - Melden Sie sich an

### Option B: Alternative KI-Tools

Falls GitHub Copilot nicht verfügbar ist:

1. **ChatGPT**
   - Kostenloser Account: [chat.openai.com](https://chat.openai.com)
   - Nutzen Sie es im Browser parallel zu VS Code

2. **Claude**
   - Kostenloser Account: [claude.ai](https://claude.ai)
   - Nutzen Sie es im Browser

---

## ✅ Abschluss-Check

Führen Sie folgende Tests durch:

### Test 1: Python

```bash
python --version
# oder
python3 --version
```

### Test 2: Git

```bash
git --version
git config --global user.name
```

### Test 3: VS Code + Python

1. Öffnen Sie VS Code
2. Erstellen Sie eine neue Datei `test.py`
3. Schreiben Sie:
   ```python
   print("Hello, World!")
   ```
4. Führen Sie die Datei aus (Play-Button oben rechts)
5. Sie sollten "Hello, World!" in der Ausgabe sehen

### Test 4: uv

```bash
uv --version
```

### Test 5: KI-Assistent

- **GitHub Copilot:** Öffnen Sie eine `.py` Datei und beginnen Sie zu tippen - Sie sollten Vorschläge sehen
- **ChatGPT/Claude:** Öffnen Sie die Website und stellen Sie eine Testfrage

---

## 📸 Dokumentation

Erstellen Sie Screenshots von:

1. ✅ Python-Version im Terminal
2. ✅ Git-Version und Konfiguration
3. ✅ VS Code mit Python-Extension
4. ✅ Erfolgreiche Ausführung von "Hello, World!"
5. ✅ uv-Version

**Speichern Sie diese in einem Ordner** - Sie werden sie für die Nachbearbeitung benötigen.

---

## 🆘 Häufige Probleme

### Python nicht im PATH (Windows)

**Problem:** `python` Befehl wird nicht erkannt

**Lösung:**
1. Python erneut installieren
2. "Add Python to PATH" aktivieren
3. ODER: Manuell zum PATH hinzufügen

### Git Credential Helper

Falls Git ständig nach Passwort fragt:

```bash
# Windows
git config --global credential.helper wincred

# macOS
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper store
```

### VS Code findet Python nicht

1. Drücken Sie `Ctrl/Cmd+Shift+P`
2. Tippen Sie "Python: Select Interpreter"
3. Wählen Sie Ihre Python-Installation manuell aus

---

## 🎉 Geschafft!

Wenn alle Tests erfolgreich waren, sind Sie bereit für die nächsten Schritte!

**Weiter zu:** [Erste Schritte mit KI](./erste-schritte.md)
