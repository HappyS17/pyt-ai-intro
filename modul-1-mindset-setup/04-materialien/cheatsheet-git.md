# Git Cheatsheet

Schnellreferenz für die wichtigsten Git-Befehle.

## 🚀 Repository erstellen

```bash
# Neues Repository initialisieren
git init

# Repository klonen
git clone <url>
```

## ⚙️ Konfiguration

```bash
# Name setzen
git config --global user.name "Ihr Name"

# E-Mail setzen
git config --global user.email "ihre.email@example.com"

# Konfiguration anzeigen
git config --list
```

## 📊 Status & Info

```bash
# Status anzeigen
git status

# Änderungen anzeigen
git diff

# Commit-Historie anzeigen
git log

# Kompakte Historie
git log --oneline

# Grafische Historie
git log --graph --oneline --all
```

## ➕ Änderungen hinzufügen

```bash
# Einzelne Datei hinzufügen
git add dateiname.py

# Alle Dateien hinzufügen
git add .

# Interaktiv hinzufügen
git add -i
```

## 💾 Commit erstellen

```bash
# Commit mit Nachricht
git commit -m "Beschreibung der Änderung"

# Alle geänderten Dateien committen
git commit -am "Nachricht"

# Letzten Commit ändern
git commit --amend
```

## 🔄 Änderungen rückgängig machen

```bash
# Datei aus Staging entfernen
git reset dateiname.py

# Alle Dateien aus Staging entfernen
git reset

# Änderungen an Datei verwerfen
git checkout -- dateiname.py

# Letzten Commit rückgängig (Änderungen behalten)
git reset --soft HEAD~1

# Letzten Commit rückgängig (Änderungen verwerfen)
git reset --hard HEAD~1
```

## 🌿 Branches

```bash
# Branches anzeigen
git branch

# Neuen Branch erstellen
git branch branch-name

# Zu Branch wechseln
git checkout branch-name

# Branch erstellen und wechseln
git checkout -b branch-name

# Branch löschen
git branch -d branch-name

# Branch umbenennen
git branch -m alter-name neuer-name
```

## 🔗 Remote Repositories

```bash
# Remote-Repository hinzufügen
git remote add origin <url>

# Remote-Repositories anzeigen
git remote -v

# Änderungen hochladen
git push origin main

# Änderungen herunterladen
git pull origin main

# Remote-Repository entfernen
git remote remove origin
```

## 📝 .gitignore

Erstellen Sie eine `.gitignore` Datei im Projekt-Root:

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
```

## 🔍 Häufige Workflows

### Workflow 1: Neue Änderungen committen

```bash
git status                    # Änderungen prüfen
git add .                     # Alle Änderungen hinzufügen
git commit -m "Nachricht"     # Commit erstellen
git log --oneline             # Prüfen
```

### Workflow 2: Mit GitHub arbeiten

```bash
git clone <url>               # Repository klonen
# ... Änderungen machen ...
git add .                     # Änderungen hinzufügen
git commit -m "Nachricht"     # Commit erstellen
git push origin main          # Hochladen
```

### Workflow 3: Projekt starten

```bash
mkdir mein-projekt            # Ordner erstellen
cd mein-projekt               # In Ordner wechseln
git init                      # Git initialisieren
# ... Dateien erstellen ...
git add .                     # Dateien hinzufügen
git commit -m "Initial commit"  # Erster Commit
```

## 🆘 Troubleshooting

### Problem: "Author identity unknown"

```bash
git config user.name "Ihr Name"
git config user.email "ihre.email@example.com"
```

### Problem: "fatal: not a git repository"

```bash
# Prüfen Sie, ob Sie im richtigen Ordner sind
pwd

# Git initialisieren
git init
```

### Problem: Merge-Konflikt

```bash
# Konflikt-Dateien anzeigen
git status

# Dateien manuell bearbeiten
# Konflikt-Marker entfernen: <<<<<<<, =======, >>>>>>>

# Gelöste Dateien hinzufügen
git add konflikt-datei.py

# Merge abschliessen
git commit
```

### Problem: Falscher Commit

```bash
# Letzten Commit rückgängig (Änderungen behalten)
git reset --soft HEAD~1

# Änderungen korrigieren
# ...

# Neu committen
git commit -m "Korrigierte Nachricht"
```

## 💡 Best Practices

### Commit-Messages

**Gute Commit-Messages:**

```bash
git commit -m "feat: Benutzer-Login implementiert"
git commit -m "fix: Fehler bei Passwort-Validierung behoben"
git commit -m "docs: README aktualisiert"
git commit -m "refactor: Code-Struktur verbessert"
```

**Schlechte Commit-Messages:**

```bash
git commit -m "Änderungen"          # ❌ Zu vage
git commit -m "asdf"                # ❌ Nicht aussagekräftig
git commit -m "WIP"                 # ❌ Work in Progress
```

### Commit-Präfixe

- `feat:` - Neue Features
- `fix:` - Bugfixes
- `docs:` - Dokumentation
- `style:` - Formatierung
- `refactor:` - Code-Umstrukturierung
- `test:` - Tests
- `chore:` - Wartungsarbeiten

### Wann committen?

- ✅ Nach jeder logischen Änderung
- ✅ Wenn ein Feature funktioniert
- ✅ Vor grösseren Änderungen
- ✅ Am Ende des Arbeitstages
- ❌ Nicht bei kaputtem Code
- ❌ Nicht zu grosse Commits

## 📚 Weiterführende Links

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

---

**Zurück zu Materialien:** [Materialien README](./README.md)
