# Lektion 2: Setup-Vertiefung & Git Basics

**Dauer:** 50 Minuten  
**Ziel:** VS Code beherrschen und Git-Grundlagen verstehen

## 📋 Ablauf

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-5 Min. | Setup-Probleme klären | Q&A |
| 5-20 Min. | VS Code Workspace & Extensions | Live-Demo |
| 20-35 Min. | Git-Grundlagen | Vortrag + Live-Demo |
| 35-50 Min. | Übung: Git-Repository erstellen | Hands-on |

---

## 🎯 Lernziele

Nach dieser Lektion können die Studierenden:
- VS Code effektiv für Python-Entwicklung nutzen
- Ein Git-Repository erstellen und verwalten
- Die grundlegenden Git-Befehle anwenden
- Mit KI-Unterstützung ein README erstellen

---

## 🔧 Teil 1: Setup-Probleme klären (5 Min.)

### Quick Check

**Fragen an die Studierenden:**
- ✅ Wer hat Python erfolgreich installiert?
- ✅ Wer hat Git installiert?
- ✅ Wer hat VS Code eingerichtet?
- ✅ Wer hat einen KI-Assistenten am Laufen?

### Häufige Probleme lösen

**Problem 1: Python nicht im PATH**
```bash
# Windows: Python neu installieren mit "Add to PATH"
# macOS/Linux: Shell-Profil aktualisieren
```

**Problem 2: Git Credential Helper**
```bash
git config --global credential.helper store
```

**Problem 3: VS Code findet Python nicht**
- `Ctrl/Cmd+Shift+P` → "Python: Select Interpreter"

**Zeitmanagement:** Nicht zu lange bei individuellen Problemen aufhalten - nach der Lektion individuell helfen.

---

## 💻 Teil 2: VS Code Workspace & Extensions (15 Min.)

### VS Code Grundlagen

#### Benutzeroberfläche

**Die wichtigsten Bereiche:**
1. **Explorer** (links): Dateien und Ordner
2. **Editor** (Mitte): Code schreiben
3. **Terminal** (unten): Befehle ausführen
4. **Extensions** (links): Erweiterungen installieren

**Live-Demo:** Kurze Tour durch die Oberfläche

#### Wichtige Shortcuts

| Aktion | Windows/Linux | macOS |
|--------|---------------|-------|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Terminal öffnen | `Ctrl+ö` | `Ctrl+ö` |
| Datei suchen | `Ctrl+P` | `Cmd+P` |
| Speichern | `Ctrl+S` | `Cmd+S` |
| Code ausführen | `F5` oder Play-Button | `F5` oder Play-Button |

### Python in VS Code

#### Python-Extension Features

**1. IntelliSense**
- Autovervollständigung
- Funktionssignaturen
- Dokumentation beim Hovern

**Live-Demo:**
```python
# Tippen Sie "pri" und sehen Sie die Vorschläge
print("Hello, World!")
```

**2. Linting**
- Automatische Code-Analyse
- Fehler und Warnungen anzeigen
- Best Practices vorschlagen

**3. Debugging**
- Breakpoints setzen
- Schritt für Schritt durchgehen
- Variablen inspizieren

**Live-Demo:** Einfaches Debugging-Beispiel

**4. Code ausführen**
- Play-Button oben rechts
- Oder: Rechtsklick → "Run Python File in Terminal"

### Workspace einrichten

#### Projekt-Ordner erstellen

**Live-Demo:**
```bash
# Terminal in VS Code öffnen
mkdir mein-erstes-projekt
cd mein-erstes-projekt
code .  # VS Code im aktuellen Ordner öffnen
```

#### Empfohlene Struktur

```
mein-erstes-projekt/
├── README.md          # Projektbeschreibung
├── requirements.txt   # Python-Abhängigkeiten
├── .gitignore        # Dateien, die Git ignorieren soll
└── src/              # Quellcode
    └── main.py
```

---

## 📚 Teil 3: Git-Grundlagen (15 Min.)

### Was ist Git?

**Versionskontrolle:**
- Speichert Änderungen an Dateien über Zeit
- Ermöglicht Zusammenarbeit
- Macht Änderungen rückgängig
- Zeigt, wer was wann geändert hat

**Warum Git?**
- ✅ Sicherheit: Keine Angst, Code zu verlieren
- ✅ Experimente: Neue Features ausprobieren
- ✅ Zusammenarbeit: Mit anderen entwickeln
- ✅ Portfolio: Code auf GitHub zeigen

### Git-Konzepte

#### Repository (Repo)
- Ein Projekt mit Git-Versionskontrolle
- Enthält alle Dateien und deren Historie

#### Commit
- Ein Snapshot des Projekts zu einem Zeitpunkt
- Mit Nachricht, was geändert wurde

#### Branch
- Eine parallele Version des Projekts
- Standardbranch: `main` oder `master`

### Grundlegende Git-Befehle

#### 1. Repository initialisieren

```bash
git init
# Erstellt ein neues Git-Repository im aktuellen Ordner
```

#### 2. Status prüfen

```bash
git status
# Zeigt, welche Dateien geändert wurden
```

#### 3. Dateien hinzufügen (Staging)

```bash
git add dateiname.py
# Fügt eine Datei zum Staging-Bereich hinzu

git add .
# Fügt alle geänderten Dateien hinzu
```

#### 4. Commit erstellen

```bash
git commit -m "Beschreibung der Änderung"
# Erstellt einen Commit mit Nachricht
```

#### 5. Historie anzeigen

```bash
git log
# Zeigt alle Commits

git log --oneline
# Kompakte Ansicht
```

### Git-Workflow

**Der typische Workflow:**

```bash
# 1. Dateien ändern
# 2. Status prüfen
git status

# 3. Dateien zum Staging hinzufügen
git add .

# 4. Commit erstellen
git commit -m "feat: Neue Funktion hinzugefügt"

# 5. Wiederholen
```

### .gitignore

**Was ist das?**
- Datei, die Git sagt, welche Dateien ignoriert werden sollen
- Wichtig für: temporäre Dateien, Secrets, grosse Dateien

**Beispiel `.gitignore` für Python:**

```gitignore
# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Secrets
.env
*.key
```

### Live-Demo: Erstes Repository

**Schritt für Schritt:**

```bash
# 1. Ordner erstellen
mkdir git-demo
cd git-demo

# 2. Git initialisieren
git init

# 3. Datei erstellen
echo "# Mein erstes Git-Projekt" > README.md

# 4. Status prüfen
git status

# 5. Datei hinzufügen
git add README.md

# 6. Commit erstellen
git commit -m "docs: Initiales README"

# 7. Historie anzeigen
git log
```

---

## 👥 Teil 4: Übung - Git-Repository erstellen (15 Min.)

### Aufgabe

Erstellen Sie Ihr erstes Git-Repository mit einem README.

### Schritt-für-Schritt-Anleitung

#### Schritt 1: Projekt-Ordner erstellen (2 Min.)

```bash
mkdir mein-python-projekt
cd mein-python-projekt
```

#### Schritt 2: Git initialisieren (1 Min.)

```bash
git init
git config user.name "Ihr Name"
git config user.email "ihre.email@example.com"
```

#### Schritt 3: README mit KI erstellen (5 Min.)

**Nutzen Sie ChatGPT/Claude:**

**Prompt:**
```text
Erstelle ein README.md für mein Python-Lernprojekt. 
Es soll enthalten:
- Titel: "Mein Python-Lernprojekt"
- Beschreibung: Was ich in diesem Kurs lerne
- Technologien: Python, Git, VS Code
- Autor: [Ihr Name]
```

**Speichern Sie das Ergebnis** als `README.md`

#### Schritt 4: .gitignore erstellen (2 Min.)

**Prompt für KI:**
```text
Erstelle eine .gitignore Datei für ein Python-Projekt.
```

**Oder kopieren Sie** das Beispiel von oben.

#### Schritt 5: Ersten Commit erstellen (3 Min.)

```bash
# Status prüfen
git status

# Alle Dateien hinzufügen
git add .

# Commit erstellen
git commit -m "docs: Initiales Projekt-Setup"

# Prüfen
git log
```

#### Schritt 6: Python-Datei hinzufügen (2 Min.)

**Erstellen Sie `hello.py`:**
```python
print("Hello, Git!")
```

**Commit:**
```bash
git add hello.py
git commit -m "feat: Hello World Programm hinzugefügt"
```

### Checkliste

- [ ] Ordner erstellt
- [ ] Git initialisiert
- [ ] README.md erstellt (mit KI)
- [ ] .gitignore erstellt
- [ ] Erster Commit
- [ ] hello.py erstellt
- [ ] Zweiter Commit
- [ ] `git log` zeigt beide Commits

### Troubleshooting

**Problem: "Author identity unknown"**
```bash
git config user.name "Ihr Name"
git config user.email "ihre.email@example.com"
```

**Problem: "Nothing to commit"**
- Haben Sie Dateien erstellt?
- Haben Sie `git add` ausgeführt?

**Problem: Editor öffnet sich bei Commit**
- Schliessen Sie den Editor (`:wq` in Vim)
- Oder nutzen Sie immer `-m "Nachricht"`

---

## 🎯 Zusammenfassung (5 Min.)

### Key Takeaways

**VS Code:**
- ✅ Mächtiger Editor für Python
- ✅ Integriertes Terminal
- ✅ Extensions für mehr Funktionalität
- ✅ IntelliSense und Debugging

**Git:**
- ✅ Versionskontrolle für Code
- ✅ Grundbefehle: init, add, commit, status, log
- ✅ .gitignore für unwichtige Dateien
- ✅ Commit-Messages sollten aussagekräftig sein

**Workflow:**
```
Ändern → Status prüfen → Add → Commit → Wiederholen
```

### Best Practices

**Commit-Messages:**
- ✅ Klar und beschreibend
- ✅ Präsens verwenden: "Fügt hinzu" statt "Hinzugefügt"
- ✅ Präfix nutzen: `feat:`, `fix:`, `docs:`

**Beispiele:**
```
✅ feat: Benutzer-Login implementiert
✅ fix: Fehler bei Passwort-Validierung behoben
✅ docs: README aktualisiert
❌ "Änderungen"
❌ "asdf"
❌ "WIP"
```

### Nächste Schritte

- **Lektion 3:** Effektives Prompting lernen
- **Übung:** Weiter mit Git experimentieren
- **Hausaufgabe:** Projekt-Repository aufbauen

### Fragen?

---

## 📎 Anhang für Dozenten

### Timing-Tipps

- **Setup-Probleme:** Maximal 5 Min., Rest nach der Lektion
- **VS Code:** Nicht zu tief einsteigen, Basics reichen
- **Git:** Fokus auf praktische Anwendung, nicht Theorie
- **Übung:** Herumgehen und helfen

### Häufige Fragen

**"Warum nicht GitHub Desktop?"**
- CLI ist universeller und mächtiger
- Besseres Verständnis der Konzepte
- GUI-Tools können später ergänzend genutzt werden

**"Muss ich alle Git-Befehle auswendig können?"**
- Nein, die wichtigsten werden Sie durch Nutzung lernen
- Cheatsheets sind erlaubt
- KI kann bei Git-Befehlen helfen

**"Was ist der Unterschied zwischen Git und GitHub?"**
- Git: Versionskontroll-System (lokal)
- GitHub: Online-Plattform für Git-Repositories
- GitHub kommt in späteren Modulen

### Materialien vorbereiten

- [ ] VS Code auf Beamer vorbereiten
- [ ] Git-Demo-Repository vorbereitet
- [ ] Cheatsheet ausdrucken (optional)
- [ ] Beispiel-README bereithalten

### Backup-Plan

Falls Git-Probleme:
- Fokus auf VS Code verlängern
- Git-Übung als Hausaufgabe
- Individuelle Hilfe nach der Lektion

---

**Nächste Lektion:** [Lektion 3: Effektives Prompting](./lektion-3-prompting.md)
