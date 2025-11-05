# Aufgabe 2: Persönliches Projekt-Setup

**Zeitaufwand:** 90 Minuten  
**Abgabe:** Vor Modul 2  
**Punkte:** 35% der Nachbearbeitung

## 🎯 Ziel

Erstellen Sie ein vollständiges Git-Repository mit mindestens 3 funktionierenden Python-Programmen.

## 📋 Aufgabenstellung

### Was zu tun ist

1. **Git-Repository erstellen** mit sinnvoller Struktur
2. **3+ Python-Programme** schreiben (mit KI-Unterstützung)
3. **README.md** erstellen mit Projektbeschreibung
4. **requirements.txt** erstellen (falls Bibliotheken genutzt werden)
5. **.gitignore** erstellen
6. **Sinnvolle Commits** mit guten Messages
7. **Code dokumentieren** mit Kommentaren

### Anforderungen

#### Minimum-Anforderungen

- ✅ Git-Repository initialisiert
- ✅ Mindestens 3 verschiedene Python-Programme
- ✅ Jedes Programm funktioniert fehlerfrei
- ✅ README.md vorhanden und aussagekräftig
- ✅ .gitignore vorhanden
- ✅ Mindestens 5 sinnvolle Commits
- ✅ Code ist kommentiert

#### Bonus-Punkte

- 🌟 Mehr als 3 Programme
- 🌟 requirements.txt vorhanden
- 🌟 Tests für Programme
- 🌟 Ausführliche Dokumentation
- 🌟 Kreative/nützliche Programme

## 📂 Projekt-Struktur

### Empfohlene Struktur

```text
mein-python-projekt/
├── README.md                    # Projektbeschreibung
├── .gitignore                   # Git-Ignore-Datei
├── requirements.txt             # Python-Abhängigkeiten (optional)
├── programm1_taschenrechner.py  # Programm 1
├── programm2_textanalyse.py     # Programm 2
├── programm3_zahlenraten.py     # Programm 3
└── tests/                       # Tests (optional)
    ├── test_programm1.py
    └── test_programm2.py
```

## 📝 README.md Template

```markdown
# Mein Python-Projekt

**Autor:** [Ihr Name]  
**Datum:** [Datum]  
**Kurs:** Python & KI-gestütztes Programmieren - Modul 1

## 📖 Beschreibung

Dieses Repository enthält meine ersten Python-Programme, die ich im Rahmen 
von Modul 1 mit KI-Unterstützung erstellt habe.

## 🚀 Programme

### 1. Taschenrechner (`programm1_taschenrechner.py`)

**Beschreibung:** Ein einfacher Taschenrechner mit Grundrechenarten.

**Features:**
- Addition, Subtraktion, Multiplikation, Division
- Fehlerbehandlung (Division durch Null)
- Benutzerfreundliche Oberfläche

**Ausführen:**
```bash
python programm1_taschenrechner.py
```

### 2. Textanalyse (`programm2_textanalyse.py`)

**Beschreibung:** Analysiert einen Text und gibt Statistiken aus.

**Features:**
- Wörter zählen
- Zeichen zählen
- Längstes Wort finden
- Durchschnittliche Wortlänge

**Ausführen:**
```bash
python programm2_textanalyse.py
```

### 3. Zahlenraten (`programm3_zahlenraten.py`)

**Beschreibung:** Ein Spiel, bei dem der Computer eine Zahl wählt und 
der Benutzer raten muss.

**Features:**
- Zufällige Zahl zwischen 1-100
- Hinweise (zu hoch/niedrig)
- Versuche zählen
- Schwierigkeitsgrade

**Ausführen:**
```bash
python programm3_zahlenraten.py
```

## 🛠️ Installation

### Voraussetzungen

- Python 3.8 oder höher
- (Optional) Weitere Bibliotheken aus `requirements.txt`

### Setup

```bash
# Repository klonen
git clone <repository-url>
cd mein-python-projekt

# Abhängigkeiten installieren mit uv
uv sync
```

## 📚 Verwendete Technologien

- Python 3.11
- Git für Versionskontrolle
- KI-Tools: ChatGPT/Claude für Code-Generierung

## 🎓 Lernziele

In diesem Projekt habe ich gelernt:

- Git-Grundlagen (init, add, commit, log)
- Python-Grundlagen (Variablen, Funktionen, Schleifen)
- Effektives Prompting für KI-Tools
- Code-Dokumentation
- Fehlerbehandlung

## 📝 Entwicklungsprozess

Für jedes Programm:

1. Problem analysiert und zerlegt
2. Prompt für KI formuliert
3. Code generiert und verstanden
4. Code getestet und angepasst
5. Dokumentiert und committet

## 🐛 Bekannte Probleme

- [Falls vorhanden, hier auflisten]

## 🔮 Zukünftige Verbesserungen

- [ ] GUI hinzufügen
- [ ] Mehr Fehlerbehandlung
- [ ] Unit-Tests schreiben
- [ ] Code refactoring

## 📄 Lizenz

Dieses Projekt wurde für Bildungszwecke erstellt.

## 🙏 Danksagungen

- Dozent: [Name]
- KI-Tools: ChatGPT, Claude
- Kurs-Community

---

**Kontakt:** [Ihre E-Mail]
```

## 💻 Programm-Ideen

### Einfach (Minimum)

1. **Taschenrechner** - Grundrechenarten
2. **Zahlenraten** - Ratespiel
3. **Textanalyse** - Wörter/Zeichen zählen

### Mittel

4. **Einkaufsliste** - Liste verwalten
5. **Notizen-App** - Notizen speichern/laden
6. **Passwort-Generator** - Sichere Passwörter

### Fortgeschritten (Bonus)

7. **Quiz-Programm** - Fragen und Antworten
8. **Kontaktliste** - Kontakte verwalten
9. **Datei-Organizer** - Dateien sortieren
10. **Wetter-Abfrage** - API-Integration

## 🔄 Git-Workflow

### Schritt-für-Schritt

```bash
# 1. Repository erstellen
mkdir mein-python-projekt
cd mein-python-projekt
git init

# 2. Git konfigurieren
git config user.name "Ihr Name"
git config user.email "ihre.email@example.com"

# 3. .gitignore erstellen
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo "venv/" >> .gitignore

# 4. Initial commit
git add .gitignore
git commit -m "chore: Initial commit mit gitignore"

# 5. README erstellen
# ... README.md erstellen ...
git add README.md
git commit -m "docs: README hinzugefügt"

# 6. Erstes Programm
# ... programm1.py erstellen ...
git add programm1_taschenrechner.py
git commit -m "feat: Taschenrechner implementiert"

# 7. Zweites Programm
# ... programm2.py erstellen ...
git add programm2_textanalyse.py
git commit -m "feat: Textanalyse implementiert"

# 8. Drittes Programm
# ... programm3.py erstellen ...
git add programm3_zahlenraten.py
git commit -m "feat: Zahlenraten-Spiel implementiert"

# 9. Dokumentation aktualisieren
# ... README.md aktualisieren ...
git add README.md
git commit -m "docs: README mit Programmbeschreibungen aktualisiert"

# 10. Historie prüfen
git log --oneline
```

## ✅ Checkliste

### Repository-Setup

- [ ] Git initialisiert
- [ ] .gitignore erstellt
- [ ] README.md erstellt
- [ ] Sinnvolle Ordnerstruktur

### Programme

- [ ] Programm 1 funktioniert
- [ ] Programm 2 funktioniert
- [ ] Programm 3 funktioniert
- [ ] Alle Programme getestet
- [ ] Code ist kommentiert

### Git-Commits

- [ ] Mindestens 5 Commits
- [ ] Commit-Messages sind aussagekräftig
- [ ] Commits folgen Konvention (feat:, fix:, docs:)
- [ ] Logische Commit-Reihenfolge

### Dokumentation

- [ ] README.md vollständig
- [ ] Jedes Programm beschrieben
- [ ] Installation erklärt
- [ ] Ausführung erklärt

## 📤 Abgabe

### Option 1: GitHub/GitLab

1. Repository auf GitHub/GitLab hochladen
2. Repository-Link einreichen
3. Sicherstellen, dass Repository öffentlich oder für Dozent zugänglich ist

### Option 2: ZIP-Datei

1. Repository als ZIP exportieren
2. Sicherstellen, dass `.git` Ordner enthalten ist
3. ZIP-Datei hochladen

### Was einreichen?

- Repository-Link ODER ZIP-Datei
- Kurze Beschreibung (2-3 Sätze) über Ihr Projekt

## 🎓 Bewertungskriterien

### Git-Nutzung (30%)

- [ ] Repository korrekt initialisiert
- [ ] Sinnvolle Commits
- [ ] Gute Commit-Messages
- [ ] .gitignore vorhanden

### Code-Qualität (40%)

- [ ] Programme funktionieren
- [ ] Code ist lesbar
- [ ] Code ist kommentiert
- [ ] Fehlerbehandlung vorhanden

### Dokumentation (20%)

- [ ] README vollständig
- [ ] Klare Beschreibungen
- [ ] Ausführungsanleitung
- [ ] Lernziele dokumentiert

### Kreativität (10%)

- [ ] Interessante Programm-Ideen
- [ ] Eigene Features hinzugefügt
- [ ] Über Minimum hinaus

## 💡 Tipps

### Tipp 1: Klein anfangen

Beginnen Sie mit einfachen Programmen und erweitern Sie sie schrittweise.

### Tipp 2: Regelmässig committen

Committen Sie nach jeder logischen Änderung, nicht alles auf einmal.

### Tipp 3: Code testen

Testen Sie jedes Programm gründlich, bevor Sie es committen.

### Tipp 4: Dokumentieren

Schreiben Sie Kommentare während des Codens, nicht nachträglich.

---

**Zurück zur Nachbearbeitung:** [Nachbearbeitung README](./README.md)
