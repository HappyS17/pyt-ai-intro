# Übung 2: Git-Repository erstellen

**Dauer:** 20 Minuten  
**Lektion:** 2  
**Ziel:** Erste praktische Erfahrung mit Git

## 🎯 Lernziel

Ein Git-Repository von Grund auf erstellen und die wichtigsten Git-Befehle anwenden.

## 📝 Aufgabenstellung

Erstellen Sie Ihr erstes Git-Repository mit einem README und einer Python-Datei.

## 🔄 Schritt-für-Schritt-Anleitung

### Schritt 1: Projekt-Ordner erstellen (2 Min.)

```bash
mkdir mein-python-projekt
cd mein-python-projekt
```

### Schritt 2: Git initialisieren (2 Min.)

```bash
git init
git config user.name "Ihr Name"
git config user.email "ihre.email@example.com"
```

**Prüfen:**

```bash
git status
# Sollte zeigen: "On branch main" oder "On branch master"
```

### Schritt 3: README mit KI erstellen (5 Min.)

**Nutzen Sie ChatGPT/Claude mit diesem Prompt:**

```text
Erstelle ein README.md für mein Python-Lernprojekt.

Es soll enthalten:
- Titel: "Mein Python-Lernprojekt"
- Beschreibung: Was ich in diesem Kurs lerne
- Technologien: Python, Git, VS Code
- Autor: [Ihr Name]
- Datum: [Heutiges Datum]

Formatierung in Markdown.
```

**Speichern Sie das Ergebnis** als `README.md` im Projekt-Ordner.

### Schritt 4: .gitignore erstellen (2 Min.)

Erstellen Sie eine Datei `.gitignore` mit folgendem Inhalt:

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
```

### Schritt 5: Ersten Commit erstellen (3 Min.)

```bash
# Status prüfen
git status

# Alle Dateien hinzufügen
git add .

# Commit erstellen
git commit -m "docs: Initiales Projekt-Setup mit README und gitignore"

# Prüfen
git log
```

### Schritt 6: Python-Datei hinzufügen (3 Min.)

Erstellen Sie eine Datei `hello.py`:

```python
# Mein erstes Python-Programm
print("Hello, Git!")
print("Ich lerne Python und Versionskontrolle.")
```

### Schritt 7: Zweiten Commit erstellen (3 Min.)

```bash
# Status prüfen
git status

# Datei hinzufügen
git add hello.py

# Commit erstellen
git commit -m "feat: Hello World Programm hinzugefügt"

# Historie anzeigen
git log --oneline
```

## ✅ Checkliste

- [ ] Ordner erstellt
- [ ] Git initialisiert
- [ ] Git konfiguriert (Name, E-Mail)
- [ ] README.md erstellt (mit KI)
- [ ] .gitignore erstellt
- [ ] Erster Commit erfolgreich
- [ ] hello.py erstellt
- [ ] Zweiter Commit erfolgreich
- [ ] `git log` zeigt beide Commits

## 🆘 Troubleshooting

### Problem: "Author identity unknown"

**Lösung:**

```bash
git config user.name "Ihr Name"
git config user.email "ihre.email@example.com"
```

### Problem: "Nothing to commit"

**Mögliche Ursachen:**

- Haben Sie Dateien erstellt?
- Sind Sie im richtigen Ordner?
- Haben Sie `git add` ausgeführt?

**Prüfen:**

```bash
ls -la  # Dateien anzeigen
git status  # Git-Status prüfen
```

### Problem: Editor öffnet sich bei Commit

**Lösung:**

- Schliessen Sie den Editor (`:wq` in Vim, `Ctrl+X` in Nano)
- Oder nutzen Sie immer `-m "Nachricht"`

### Problem: "fatal: not a git repository"

**Lösung:**

```bash
# Prüfen Sie, ob Sie im richtigen Ordner sind
pwd

# Git initialisieren
git init
```

## 🎓 Reflexion

**Was haben Sie gelernt?**

- [ ] Git-Repository initialisieren
- [ ] Dateien zum Staging hinzufügen
- [ ] Commits erstellen
- [ ] Git-Historie anzeigen
- [ ] .gitignore verwenden

**Wichtige Befehle:**

```bash
git init          # Repository erstellen
git status        # Status prüfen
git add .         # Alle Dateien hinzufügen
git commit -m ""  # Commit erstellen
git log           # Historie anzeigen
```

---

**Zurück zur Übungsübersicht:** [Übungen README](./README.md)
