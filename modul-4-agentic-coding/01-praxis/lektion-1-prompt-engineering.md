# Lektion 1: Advanced Prompt Engineering

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

- Effektive Prompts strukturieren
- Kontext optimal nutzen
- Iterativ verfeinern
- Constraints definieren

## 📚 Theorie (15 Min.)

### Prompt-Anatomie

```text
[ROLLE]
Du bist ein erfahrener Python-Entwickler mit Fokus auf Clean Code.

[KONTEXT]
Ich arbeite an einem CLI-Tool für Dateiverarbeitung.
Technologie: Python 3.11, pytest, click

[AUFGABE]
Erstelle eine Funktion, die CSV-Dateien validiert.

[CONSTRAINTS]
- Type Hints verwenden
- Docstrings im Google-Style
- Exception Handling
- Maximale Komplexität: O(n)

[BEISPIEL]
Input: "data.csv" mit Spalten [name, age, city]
Output: True/False + Liste von Fehlern

[FORMAT]
Gib mir:
1. Die Funktion
2. Unit Tests
3. Verwendungsbeispiel
```

### Prompt-Patterns

#### 1. Role-Based

```text
Du bist ein Senior Python-Entwickler mit 10 Jahren Erfahrung
in Datenverarbeitung und Test-Driven Development.
```

#### 2. Chain-of-Thought

```text
Erkläre Schritt für Schritt:
1. Was ist das Problem?
2. Welche Lösungsansätze gibt es?
3. Welcher ist am besten?
4. Implementiere die Lösung
```

#### 3. Few-Shot Learning

```text
Beispiel 1:
Input: [1, 2, 3]
Output: 6

Beispiel 2:
Input: [10, 20, 30]
Output: 60

Jetzt für: [5, 15, 25]
```

## 💻 Live-Demo (20 Min.)

### Demo: Feature-Implementierung

**Schlechter Prompt:**
```text
Schreibe eine Funktion für Passwort-Validierung
```

**Guter Prompt:**
```text
Erstelle eine Python-Funktion zur Passwort-Validierung.

Anforderungen:
- Mindestens 8 Zeichen
- Mindestens 1 Grossbuchstabe
- Mindestens 1 Kleinbuchstabe
- Mindestens 1 Zahl
- Mindestens 1 Sonderzeichen

Rückgabe:
- Tuple (is_valid: bool, errors: list[str])

Zusätzlich:
- Type Hints
- Docstring
- Unit Tests mit pytest
- Edge Cases berücksichtigen
```

### Iteration

```text
Iteration 1: Basis-Implementierung
Iteration 2: "Füge Passwort-Stärke-Score hinzu (0-5)"
Iteration 3: "Optimiere für Performance"
Iteration 4: "Füge Custom Rules hinzu"
```

## ✏️ Übung (15 Min.)

Implementieren Sie mit KI:

**Option A: Email-Validator**
- Validiert Email-Format
- Prüft Disposable-Domains
- Mit Tests

**Option B: URL-Parser**
- Extrahiert Komponenten
- Validiert Format
- Mit Tests

---

**Weiter zu:** [Lektion 2 - TDD](./lektion-2-tdd.md)
