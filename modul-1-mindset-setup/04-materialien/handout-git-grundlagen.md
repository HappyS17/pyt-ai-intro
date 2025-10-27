# Handout: Git-Grundlagen

Einführung in die Versionskontrolle mit Git.

## 🎯 Was ist Git?

Git ist ein **Versionskontrollsystem**, das Änderungen an Dateien über die Zeit hinweg speichert.

### Warum Git?

- ✅ **Sicherheit:** Keine Angst, Code zu verlieren
- ✅ **Historie:** Alle Änderungen nachvollziehbar
- ✅ **Experimente:** Neue Features risikolos ausprobieren
- ✅ **Zusammenarbeit:** Mit anderen entwickeln
- ✅ **Portfolio:** Code auf GitHub zeigen

### Git vs. GitHub

| Git | GitHub |
|-----|--------|
| Versionskontroll-System | Online-Plattform |
| Lokal auf Ihrem Computer | Im Internet |
| Kostenlos und Open Source | Kostenlos für öffentliche Repos |
| Kommandozeilen-Tool | Web-Interface |

## 📚 Grundlegende Konzepte

### Repository (Repo)

Ein Projekt mit Git-Versionskontrolle.

```text
mein-projekt/
├── .git/              ← Git-Datenbank (versteckt)
├── README.md
├── main.py
└── .gitignore
```

### Commit

Ein Snapshot des Projekts zu einem bestimmten Zeitpunkt.

```text
Commit 1: "Initial commit"
    ↓
Commit 2: "feat: Login hinzugefügt"
    ↓
Commit 3: "fix: Fehler behoben"
```

### Staging Area

Zwischenbereich für Dateien, die committet werden sollen.

```text
Working Directory → Staging Area → Repository
    (Ändern)        (git add)      (git commit)
```

### Branch

Eine parallele Version des Projekts.

```text
main:    A → B → C → D
              ↓
feature:      E → F
```

## 🔄 Der Git-Workflow

### Schritt 1: Repository initialisieren

```bash
# Neues Repository erstellen
git init

# Oder: Bestehendes klonen
git clone <url>
```

### Schritt 2: Änderungen machen

```bash
# Dateien erstellen/ändern
# ... in VS Code arbeiten ...
```

### Schritt 3: Status prüfen

```bash
git status

# Zeigt:
# - Geänderte Dateien
# - Neue Dateien
# - Gelöschte Dateien
```

### Schritt 4: Dateien zum Staging hinzufügen

```bash
# Einzelne Datei
git add dateiname.py

# Alle Dateien
git add .
```

### Schritt 5: Commit erstellen

```bash
git commit -m "Beschreibung der Änderung"
```

### Schritt 6: Historie anzeigen

```bash
git log
# Oder kompakt:
git log --oneline
```

## 📝 Wichtige Befehle

### Repository-Befehle

```bash
# Repository initialisieren
git init

# Status anzeigen
git status

# Konfiguration
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"
```

### Änderungen verwalten

```bash
# Dateien hinzufügen
git add dateiname.py
git add .

# Commit erstellen
git commit -m "Nachricht"

# Änderungen anzeigen
git diff
```

### Historie

```bash
# Commits anzeigen
git log
git log --oneline
git log --graph

# Bestimmten Commit anzeigen
git show <commit-id>
```

### Änderungen rückgängig machen

```bash
# Datei aus Staging entfernen
git reset dateiname.py

# Änderungen an Datei verwerfen
git checkout -- dateiname.py

# Letzten Commit rückgängig
git reset --soft HEAD~1
```

## 🎯 .gitignore

### Was ist .gitignore?

Eine Datei, die Git sagt, welche Dateien ignoriert werden sollen.

### Warum wichtig?

- Temporäre Dateien nicht committen
- Secrets nicht hochladen
- Grosse Dateien ausschliessen
- IDE-Konfigurationen ignorieren

### Beispiel .gitignore für Python

```gitignore
# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
env/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Secrets
.env
*.key
config.ini
```

### .gitignore erstellen

```bash
# Datei erstellen
touch .gitignore

# Inhalt hinzufügen
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# Committen
git add .gitignore
git commit -m "chore: gitignore hinzugefügt"
```

## 💡 Best Practices

### Commit-Messages

#### Gute Messages

```bash
git commit -m "feat: Benutzer-Login implementiert"
git commit -m "fix: Fehler bei Passwort-Validierung behoben"
git commit -m "docs: README aktualisiert"
git commit -m "refactor: Code-Struktur verbessert"
```

#### Schlechte Messages

```bash
git commit -m "Änderungen"          # ❌ Zu vage
git commit -m "asdf"                # ❌ Nicht aussagekräftig
git commit -m "WIP"                 # ❌ Work in Progress
git commit -m "Fix"                 # ❌ Was wurde gefixt?
```

#### Message-Format

```text
<typ>: <kurze Beschreibung>

<optionale Details>
```

**Typen:**

- `feat:` - Neue Features
- `fix:` - Bugfixes
- `docs:` - Dokumentation
- `style:` - Formatierung
- `refactor:` - Code-Umstrukturierung
- `test:` - Tests
- `chore:` - Wartungsarbeiten

### Wann committen?

#### Gute Zeitpunkte

- ✅ Nach jeder logischen Änderung
- ✅ Wenn ein Feature funktioniert
- ✅ Vor grösseren Änderungen
- ✅ Am Ende des Arbeitstages

#### Schlechte Zeitpunkte

- ❌ Bei kaputtem Code
- ❌ Zu grosse Commits (viele Änderungen)
- ❌ Zu kleine Commits (jede Zeile einzeln)

### Commit-Grösse

```text
❌ Zu gross:
"feat: Komplette Anwendung mit Login, Dashboard, 
Datenbank, API und Frontend"

✅ Richtig:
"feat: Login-Formular hinzugefügt"
"feat: Login-Validierung implementiert"
"feat: Login-API-Endpoint erstellt"
```

## 🆘 Häufige Probleme

### Problem 1: "Author identity unknown"

**Ursache:** Git kennt Ihren Namen nicht.

**Lösung:**

```bash
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"
```

### Problem 2: "fatal: not a git repository"

**Ursache:** Kein Git-Repository im aktuellen Ordner.

**Lösung:**

```bash
# Prüfen Sie den Ordner
pwd

# Git initialisieren
git init
```

### Problem 3: Falscher Commit

**Ursache:** Commit mit Fehler oder falscher Message.

**Lösung:**

```bash
# Letzten Commit rückgängig (Änderungen behalten)
git reset --soft HEAD~1

# Änderungen korrigieren
# ...

# Neu committen
git commit -m "Korrigierte Nachricht"
```

### Problem 4: Datei versehentlich hinzugefügt

**Ursache:** Falsche Datei mit `git add` hinzugefügt.

**Lösung:**

```bash
# Aus Staging entfernen
git reset dateiname.py

# Oder alle Dateien
git reset
```

## 🎓 Übungen

### Übung 1: Erstes Repository

```bash
# 1. Ordner erstellen
mkdir git-uebung
cd git-uebung

# 2. Git initialisieren
git init

# 3. Datei erstellen
echo "# Mein erstes Repo" > README.md

# 4. Status prüfen
git status

# 5. Datei hinzufügen
git add README.md

# 6. Commit erstellen
git commit -m "docs: Initial README"

# 7. Historie anzeigen
git log
```

### Übung 2: Mehrere Commits

```bash
# 1. Neue Datei erstellen
echo "print('Hello')" > hello.py

# 2. Committen
git add hello.py
git commit -m "feat: Hello-Programm"

# 3. Datei ändern
echo "print('World')" >> hello.py

# 4. Committen
git add hello.py
git commit -m "feat: World hinzugefügt"

# 5. Historie anzeigen
git log --oneline
```

### Übung 3: .gitignore

```bash
# 1. .gitignore erstellen
echo "__pycache__/" > .gitignore

# 2. Committen
git add .gitignore
git commit -m "chore: gitignore hinzugefügt"

# 3. Prüfen
git status
```

## ✅ Checkliste: Git-Grundlagen

- [ ] Ich verstehe, was Git ist
- [ ] Ich kann ein Repository initialisieren
- [ ] Ich kann Dateien zum Staging hinzufügen
- [ ] Ich kann Commits erstellen
- [ ] Ich kann die Historie anzeigen
- [ ] Ich kann .gitignore verwenden
- [ ] Ich schreibe gute Commit-Messages
- [ ] Ich committe zur richtigen Zeit
- [ ] Ich kann häufige Probleme lösen

## 📚 Weiterführende Themen

### Für später

- **Branches:** Parallele Entwicklung
- **Merging:** Branches zusammenführen
- **Remote Repositories:** Mit GitHub arbeiten
- **Pull Requests:** Code-Review
- **Konflikte lösen:** Merge-Konflikte
- **Git-Workflows:** Feature-Branch, Gitflow

---

**Zurück zu Materialien:** [Materialien README](./README.md)
