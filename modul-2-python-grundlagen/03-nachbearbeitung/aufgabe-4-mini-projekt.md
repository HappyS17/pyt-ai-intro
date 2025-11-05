# Aufgabe 4: Real-World Mini-Projekt

**Zeitaufwand:** 90 Minuten
**Punkte:** 15% der Nachbearbeitung
**Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

Nach dieser Aufgabe können Sie:

- Ein vollständiges Python-Projekt von Grund auf entwickeln
- Mehrere Konzepte (Funktionen, Datenstrukturen, File I/O) kombinieren
- Benutzerfreundliche Kommandozeilen-Anwendungen erstellen
- Projektdokumentation professionell aufbauen
- Gelerntes in einem realen Kontext anwenden

## 📋 Aufgabenstellung

Wählen Sie **1 von 3** Projekten und entwickeln Sie eine funktionierende Anwendung. Das Projekt sollte alle Python-Grundlagen demonstrieren, die Sie in Modul 2 gelernt haben.

## 🎮 Projekt-Optionen

### Option A: Password Manager (Sicherheit) ⭐⭐⭐

**Beschreibung:** Sichere Verwaltung von Passwörtern mit Verschlüsselung.

**Kernfunktionen:**
- Master-Passwort zum Schutz
- Passwörter hinzufügen (Website, Benutzername, Passwort)
- Passwörter anzeigen (nach Master-Passwort)
- Passwort-Generator (sichere, zufällige Passwörter)
- Speicherung in verschlüsselter JSON-Datei

**Technische Anforderungen:**
- Verschlüsselung mit `cryptography` Bibliothek
- Passwort-Hashing mit `hashlib`
- Sichere Eingabe (Passwort nicht sichtbar)
- Datenpersistenz in JSON

**Bewertungsschwerpunkte:**
- ✅ Sicherheit (Verschlüsselung, Hashing)
- ✅ Fehlerbehandlung (falsche Master-Passwörter)
- ✅ Benutzerfreundlichkeit

---

### Option B: Quiz Game (Gamification) ⭐⭐

**Beschreibung:** Interaktives Multiple-Choice-Quiz mit Highscore.

**Kernfunktionen:**
- Fragen aus JSON-Datei laden
- Multiple-Choice-Fragen stellen
- Antworten überprüfen und Punkte zählen
- Highscore-Tabelle speichern
- Verschiedene Kategorien (z.B. Python, Allgemeinwissen)

**Technische Anforderungen:**
- Fragen in JSON-Datei (`questions.json`)
- Zufällige Reihenfolge der Fragen
- Timer für jede Frage (optional)
- Highscore-Persistenz

**Bewertungsschwerpunkte:**
- ✅ Datenstruktur-Design (verschachtelte Dictionaries)
- ✅ Randomisierung
- ✅ User Experience (klares Feedback)

---

### Option C: Workout Tracker (Health & Fitness) ⭐⭐

**Beschreibung:** Verfolgen Sie Trainingseinheiten und Fortschritte.

**Kernfunktionen:**
- Workout hinzufügen (Typ, Dauer, Kalorien, Notizen)
- Workout-Historie anzeigen
- Statistiken (Gesamtkalorien, häufigste Übung, etc.)
- Wöchentliche Zusammenfassung
- Trainingsziele setzen und überprüfen

**Technische Anforderungen:**
- Datenspeicherung in JSON
- Datum/Zeit-Handling mit `datetime`
- Statistik-Berechnungen
- Datenvisualisierung (ASCII-Grafiken)

**Bewertungsschwerpunkte:**
- ✅ Datums-/Zeitverarbeitung
- ✅ Statistik-Berechnungen
- ✅ Datenvisualisierung

## ✅ Anforderungen (alle Projekte)

### Funktionale Anforderungen (8 Punkte)

- [ ] **Alle Kernfunktionen implementiert** (aus der Projektbeschreibung)
- [ ] **Menüsystem:** Klares, interaktives Menü
- [ ] **Datenpersistenz:** Daten werden in Datei gespeichert
- [ ] **Fehlerbehandlung:** Robuste Eingabevalidierung

### Code-Qualität (4 Punkte)

- [ ] **Struktur:** Mindestens 6 gut benannte Funktionen
- [ ] **Dokumentation:** Docstrings für alle Funktionen
- [ ] **Type Hints:** Vollständige Type Annotations
- [ ] **PEP 8:** Code-Style-konform

### Dokumentation (3 Punkte)

- [ ] **README.md:** Installation, Verwendung, Features
- [ ] **Benutzeranleitung:** Wie wird die App benutzt?
- [ ] **Screenshots/Beispiele:** Terminal-Ausgaben zeigen

## 📊 Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| **Funktionalität** | 8 | Alle Kernfunktionen funktionieren |
| **Code-Qualität** | 4 | Struktur, Dokumentation, Style |
| **Dokumentation** | 3 | README vollständig und klar |
| **GESAMT** | **15** | |

## 💻 Option A: Password Manager - Details

### Projektstruktur

```
aufgabe-4-password-manager/
├── password_manager.py    # Hauptprogramm
├── passwords.json.enc     # Verschlüsselte Passwörter (automatisch erstellt)
├── requirements.txt       # cryptography
├── README.md              # Dokumentation
└── .gitignore            # passwords.json.enc nicht committen!
```

### Technische Spezifikation

**requirements.txt:**
```
cryptography==41.0.7
```

**Installation:**
```bash
uv sync
```

**Funktionen:**

1. **Master-Passwort setzen/überprüfen**
   ```python
   def verify_master_password() -> bool:
       """Fragt Master-Passwort ab und verifiziert es."""
   ```

2. **Passwort hinzufügen**
   ```python
   def add_password(website: str, username: str, password: str) -> None:
       """Fügt neues Passwort hinzu."""
   ```

3. **Passwort anzeigen**
   ```python
   def get_password(website: str) -> dict:
       """Gibt Passwort für Website zurück."""
   ```

4. **Passwort generieren**
   ```python
   def generate_password(length: int = 16) -> str:
       """Generiert sicheres, zufälliges Passwort."""
   ```

5. **Daten verschlüsseln/entschlüsseln**
   ```python
   def encrypt_data(data: str, key: bytes) -> bytes:
       """Verschlüsselt Daten mit Fernet."""

   def decrypt_data(encrypted: bytes, key: bytes) -> str:
       """Entschlüsselt Daten."""
   ```

### Code-Beispiel (Starter)

```python
import json
import hashlib
import getpass
from cryptography.fernet import Fernet

def generate_key_from_password(password: str) -> bytes:
    """Generiert Verschlüsselungs-Key aus Master-Passwort."""
    # Hash das Passwort zu einem 32-Byte-Key
    key = hashlib.sha256(password.encode()).digest()
    # Konvertiere zu base64 für Fernet
    import base64
    return base64.urlsafe_b64encode(key)

def verify_master_password() -> tuple[bool, bytes]:
    """
    Fragt Master-Passwort ab und gibt Verschlüsselungs-Key zurück.

    Returns:
        (erfolg, key): Tuple mit Erfolg und Key
    """
    password = getpass.getpass("Master-Passwort: ")
    key = generate_key_from_password(password)

    # Versuche Datei zu entschlüsseln (Test ob Passwort korrekt)
    try:
        # [Hier Ihre Logik zum Testen]
        return True, key
    except:
        return False, None

# Weitere Funktionen implementieren...
```

### Sicherheitshinweise

⚠️ **WICHTIG für echte Passwort-Manager:**
- Dieses Projekt ist ein LERNPROJEKT, nicht für echte Passwörter geeignet
- Für echte Passwörter: Nutzen Sie professionelle Tools (1Password, Bitwarden, etc.)
- Verschlüsselung schützt nur, wenn Master-Passwort sicher ist
- Master-Passwort NIEMALS im Code speichern

### Beispiel-Interaktion

```text
=== PASSWORD MANAGER ===

1. Passwort hinzufügen
2. Passwort anzeigen
3. Alle Passwörter auflisten
4. Passwort generieren
5. Beenden

Wählen Sie (1-5): 1

--- Neues Passwort ---
Website: github.com
Benutzername: user@example.com
Passwort generieren? (j/n): j

Generiertes Passwort: xK9!mP#2qL@7nR$4
Passwort gespeichert ✓

[Zurück zum Menü]
```

---

## 💻 Option B: Quiz Game - Details

### Projektstruktur

```
aufgabe-4-quiz-game/
├── quiz_game.py           # Hauptprogramm
├── questions.json         # Fragen-Datenbank
├── highscores.json        # Highscore-Tabelle
├── README.md              # Dokumentation
└── categories/            # Optional: Mehrere Kategorie-Dateien
    ├── python.json
    └── general.json
```

### Datenstruktur (questions.json)

```json
{
  "questions": [
    {
      "id": 1,
      "category": "Python",
      "question": "Was ist der Ausgabe von: print(type([]))?",
      "options": [
        "<class 'list'>",
        "<class 'array'>",
        "<class 'tuple'>",
        "<class 'dict'>"
      ],
      "correct": 0,
      "difficulty": "easy"
    },
    {
      "id": 2,
      "category": "Python",
      "question": "Welche Methode fügt ein Element am Ende einer Liste hinzu?",
      "options": [
        "add()",
        "append()",
        "insert()",
        "push()"
      ],
      "correct": 1,
      "difficulty": "easy"
    }
  ]
}
```

### Funktionen

```python
def load_questions(filename: str = "questions.json") -> list:
    """Lädt Fragen aus JSON-Datei."""

def ask_question(question: dict) -> bool:
    """
    Stellt eine Frage und gibt zurück, ob Antwort korrekt war.

    Args:
        question: Dictionary mit Frage und Optionen

    Returns:
        True wenn richtig beantwortet
    """

def play_quiz(questions: list) -> int:
    """
    Spielt Quiz und gibt Punktzahl zurück.

    Args:
        questions: Liste von Frage-Dicts

    Returns:
        Erreichte Punktzahl
    """

def save_highscore(name: str, score: int) -> None:
    """Speichert Highscore."""

def show_highscores() -> None:
    """Zeigt Highscore-Tabelle."""
```

### Beispiel-Interaktion

```text
=== PYTHON QUIZ ===

Wählen Sie Kategorie:
1. Python Basics
2. Datenstrukturen
3. Alle Kategorien

Ihre Wahl: 1

--- Frage 1/10 ---
Was ist der Ausgabe von: print(type([]))?

A) <class 'list'>
B) <class 'array'>
C) <class 'tuple'>
D) <class 'dict'>

Ihre Antwort (A-D): A
✓ RICHTIG! (+10 Punkte)

--- Frage 2/10 ---
[...]

=== QUIZ BEENDET ===

Ihre Punktzahl: 80/100
Rang: 3. Platz

Highscores:
1. Anna      - 95 Punkte
2. Bob       - 90 Punkte
3. Sie       - 80 Punkte
4. Charlie   - 75 Punkte
```

---

## 💻 Option C: Workout Tracker - Details

### Projektstruktur

```
aufgabe-4-workout-tracker/
├── workout_tracker.py     # Hauptprogramm
├── workouts.json          # Trainings-Historie
├── README.md              # Dokumentation
└── goals.json             # Trainingsziele (optional)
```

### Datenstruktur (workouts.json)

```json
{
  "workouts": [
    {
      "id": 1,
      "datum": "2025-01-15",
      "uhrzeit": "18:30",
      "typ": "Laufen",
      "dauer_minuten": 30,
      "kalorien": 300,
      "notizen": "5km im Park"
    },
    {
      "id": 2,
      "datum": "2025-01-16",
      "uhrzeit": "07:00",
      "typ": "Krafttraining",
      "dauer_minuten": 45,
      "kalorien": 250,
      "notizen": "Oberkörper"
    }
  ]
}
```

### Funktionen

```python
from datetime import date, datetime

def add_workout(typ: str, dauer: int, kalorien: int, notizen: str = "") -> None:
    """Fügt neues Workout hinzu."""

def show_workouts(filter_days: int = None) -> None:
    """
    Zeigt Workout-Historie.

    Args:
        filter_days: Nur Workouts der letzten N Tage (None = alle)
    """

def calculate_statistics(workouts: list) -> dict:
    """
    Berechnet Statistiken.

    Returns:
        Dictionary mit Stats (total_workouts, total_kalorien, etc.)
    """

def weekly_summary() -> None:
    """Zeigt Zusammenfassung der aktuellen Woche."""

def workout_chart(workouts: list) -> None:
    """Zeigt ASCII-Balkendiagramm der Workouts."""
```

### Beispiel-Interaktion

```text
=== WORKOUT TRACKER ===

1. Workout hinzufügen
2. Workout-Historie
3. Wöchentliche Statistik
4. Monats-Übersicht
5. Beenden

Wählen Sie (1-5): 1

--- Neues Workout ---
Typ (Laufen/Radfahren/Krafttraining/Yoga): Laufen
Dauer (Minuten): 30
Kalorien: 300
Notizen: 5km im Park

Workout gespeichert ✓

[Zurück zum Menü]

Wählen Sie (1-5): 3

=== WÖCHENTLICHE STATISTIK ===
Woche: 15.01. - 21.01.2025

Workouts diese Woche: 5
Gesamtdauer: 180 Min.
Gesamtkalorien: 1450 kcal

Workout-Verteilung:
████████████████ Laufen (3x)
████████ Krafttraining (2x)

Ziel: 5 Workouts/Woche ✓ ERREICHT!
```

### Statistik-Funktionen

```python
def calculate_statistics(workouts: list) -> dict:
    """Berechnet umfassende Statistiken."""
    total_workouts = len(workouts)
    total_kalorien = sum(w["kalorien"] for w in workouts)
    total_dauer = sum(w["dauer_minuten"] for w in workouts)

    # Durchschnitte
    avg_kalorien = total_kalorien / total_workouts if total_workouts > 0 else 0
    avg_dauer = total_dauer / total_workouts if total_workouts > 0 else 0

    # Häufigster Workout-Typ
    from collections import Counter
    typen = [w["typ"] for w in workouts]
    haeufigster = Counter(typen).most_common(1)[0] if typen else ("Keine", 0)

    return {
        "total_workouts": total_workouts,
        "total_kalorien": total_kalorien,
        "total_dauer": total_dauer,
        "avg_kalorien": avg_kalorien,
        "avg_dauer": avg_dauer,
        "haeufigster_typ": haeufigster[0],
        "haeufigster_count": haeufigster[1]
    }
```

---

## 💡 Allgemeine Hinweise

### Entwicklungs-Workflow

1. **Planung (15 Min.)**
   - Skizzieren Sie Hauptfunktionen
   - Definieren Sie Datenstrukturen
   - Erstellen Sie Funktions-Liste

2. **Basis-Implementierung (40 Min.)**
   - Menüsystem zuerst
   - Dann Kernfunktionen eine nach der anderen
   - Testen Sie nach jeder Funktion

3. **Datenpersistenz (15 Min.)**
   - JSON-Speichern/Laden implementieren
   - Fehlerbehandlung bei fehlenden Dateien

4. **Polishing (15 Min.)**
   - Fehlerbehandlung vervollständigen
   - Docstrings und Type Hints hinzufügen
   - README schreiben

5. **Testing (5 Min.)**
   - Alle Menüoptionen durchgehen
   - Edge Cases testen
   - README-Anleitung folgen

### KI-Prompts

**Für Projektstart:**
```
Ich entwickle einen [Projektname] in Python.

Features:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Hilf mir bei:
1. Datenstruktur-Design (welche Dicts/Listen brauche ich?)
2. Funktions-Architektur (welche Funktionen und Parameter?)
3. Projektstruktur (welche Dateien?)

Gib mir einen Überblick, NICHT den kompletten Code.
```

**Für spezifische Probleme:**
```
Ich möchte [Feature] implementieren.
Aktueller Code: [Code einfügen]

Wie kann ich das elegant lösen? Zeige mir:
1. Die Python-Konzepte die ich brauche
2. Ein Code-Beispiel
3. Mögliche Edge Cases
```

### README-Template

```markdown
# [Projekt-Name]

## Beschreibung
[2-3 Sätze über das Projekt]

## Features
- ✅ [Feature 1]
- ✅ [Feature 2]
- ✅ [Feature 3]

## Installation

### Voraussetzungen
- Python 3.11+
- [Weitere Dependencies]

### Setup
```bash
# Repository klonen
git clone [url]

# Dependencies installieren
uv sync

# Programm starten
python [hauptdatei].py
```

## Verwendung

### Erste Schritte
[Schritt-für-Schritt-Anleitung]

### Beispiel-Session
```text
[Beispiel-Ausgabe des Programms]
```

## Projektstruktur
```
projekt/
├── [datei].py
├── [datei].json
└── README.md
```

## Technische Details

### Datenstruktur
[Beschreibung der JSON-Struktur]

### Hauptfunktionen
- `funktion1()`: [Beschreibung]
- `funktion2()`: [Beschreibung]

## Gelerntes
[Was haben Sie durch dieses Projekt gelernt?]

## Mögliche Erweiterungen
- [ ] [Idee 1]
- [ ] [Idee 2]

## Autor
[Ihr Name]

## Lizenz
Lernprojekt für [Kurs-Name]
```

## ✅ Selbsttest vor Abgabe

- [ ] Alle Kernfunktionen implementiert und getestet
- [ ] Menüsystem funktioniert fehlerfrei
- [ ] Daten werden korrekt gespeichert und geladen
- [ ] Fehlerhafte Eingaben werden abgefangen
- [ ] Mindestens 6 Funktionen mit Docstrings
- [ ] Type Hints vollständig
- [ ] README.md vollständig und klar
- [ ] Code auf GitHub gepusht
- [ ] `.gitignore` verhindert sensible Daten im Repo

## 📤 Abgabe

```bash
git add aufgabe-4-[projektname]/
git commit -m "Aufgabe 4: [Projektname] fertiggestellt"
git push
```

---

**Viel Erfolg bei Ihrem Projekt!** 🎯

**Zurück zur Nachbearbeitung:** [README](./README.md)
