# Aufgabe 2: Code-Comprehension und Reverse Engineering

**Zeitaufwand:** 60 Minuten
**Punkte:** 20% der Nachbearbeitung
**Schwierigkeit:** ⭐⭐☆

## 🎯 Lernziele

Nach dieser Aufgabe können Sie:

- Unbekannten Python-Code systematisch analysieren
- Code-Logik nachvollziehen und dokumentieren
- Funktionen und Datenstrukturen identifizieren
- Code-Qualität bewerten
- KI effektiv für Code-Erklärungen nutzen

## 📋 Aufgabenstellung

Analysieren Sie das unten stehende Python-Programm und erstellen Sie eine umfassende Dokumentation. Ziel ist es, den Code vollständig zu verstehen und für andere verständlich zu machen.

## 💻 Zu analysierender Code

```python
def process_data(raw_data):
    result = []
    for item in raw_data:
        if isinstance(item, (int, float)):
            result.append(item ** 2)
        elif isinstance(item, str):
            result.append(len(item))
        elif isinstance(item, list):
            result.append(sum(item))
        else:
            result.append(None)
    return result

def filter_data(data, threshold=10):
    return [x for x in data if x is not None and x > threshold]

def aggregate(data):
    if not data:
        return {"sum": 0, "avg": 0, "max": 0, "min": 0, "count": 0}

    return {
        "sum": sum(data),
        "avg": sum(data) / len(data),
        "max": max(data),
        "min": min(data),
        "count": len(data)
    }

def analyze(input_data, threshold=10):
    processed = process_data(input_data)
    filtered = filter_data(processed, threshold)
    stats = aggregate(filtered)

    return {
        "original": input_data,
        "processed": processed,
        "filtered": filtered,
        "statistics": stats,
        "removed_count": len(processed) - len(filtered)
    }

# Beispielaufruf
test_data = [5, "hello", [1, 2, 3], 3.5, "AI", 10, [5, 5, 5], "code"]
result = analyze(test_data, threshold=20)
print(result)
```

## ✅ Anforderungen

Erstellen Sie ein Markdown-Dokument (`code-comprehension.md`) mit folgenden Abschnitten:

### 1. Übersicht (10 Punkte)

- [ ] **Zweck des Programms:** Beschreiben Sie in 3-5 Sätzen, was das Programm macht
- [ ] **Hauptfunktionen:** Listung aller 4 Funktionen mit Kurzbeschreibung
- [ ] **Datenfluss:** Diagramm oder Beschreibung, wie Daten durch die Funktionen fliessen

### 2. Detaillierte Funktionsanalyse (40 Punkte)

Für **jede der 4 Funktionen** beschreiben Sie:

- [ ] **Zweck:** Was macht diese Funktion?
- [ ] **Parameter:** Welche Eingaben nimmt sie?
- [ ] **Rückgabewert:** Was gibt sie zurück?
- [ ] **Logik:** Wie funktioniert die Implementierung? (Schritt für Schritt)
- [ ] **Beispiel:** Zeigen Sie ein konkretes Beispiel mit Eingabe und Ausgabe

### 3. Code-Qualitätsanalyse (25 Punkte)

- [ ] **Stärken:** 3 positive Aspekte des Codes
- [ ] **Schwächen:** 3 Verbesserungsmöglichkeiten
- [ ] **Best Practices:** Welche Python-Best-Practices werden befolgt/verletzt?
- [ ] **Fehlerbehandlung:** Fehlt Fehlerbehandlung? Wo könnte das problematisch sein?

### 4. Verbesserungsvorschläge (15 Punkte)

- [ ] **Code-Verbesserungen:** Schreiben Sie eine verbesserte Version einer Funktion
- [ ] **Dokumentation:** Fügen Sie Docstrings hinzu
- [ ] **Type Hints:** Ergänzen Sie Type Hints
- [ ] **Begründung:** Erklären Sie, warum Ihre Version besser ist

### 5. Eigene Experimente (10 Punkte)

- [ ] **Testfälle:** Erstellen Sie 3 weitere Testfälle
- [ ] **Erwartete Ergebnisse:** Vorhersage der Ausgabe
- [ ] **Tatsächliche Ergebnisse:** Führen Sie den Code aus und vergleichen Sie
- [ ] **Erkenntnisse:** Was haben Sie durch die Tests gelernt?

## 📊 Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| **Übersicht** | 2 | Klare Zusammenfassung des Programms |
| **Funktionsanalyse** | 8 | Alle 4 Funktionen detailliert erklärt |
| **Qualitätsanalyse** | 5 | Stärken und Schwächen identifiziert |
| **Verbesserungen** | 3 | Sinnvolle Verbesserungen mit Code |
| **Experimente** | 2 | Eigene Testfälle durchgeführt |
| **GESAMT** | **20** | |

## 📝 Template für Ihre Dokumentation

```markdown
# Code-Comprehension: Datenanalyse-Programm

## 1. Übersicht

### Zweck des Programms
[Ihre Beschreibung]

### Hauptfunktionen
1. `process_data()`: [Kurzbeschreibung]
2. `filter_data()`: [Kurzbeschreibung]
3. `aggregate()`: [Kurzbeschreibung]
4. `analyze()`: [Kurzbeschreibung]

### Datenfluss
```
Eingabe → process_data() → filter_data() → aggregate() → Ausgabe
```

## 2. Detaillierte Funktionsanalyse

### Funktion 1: `process_data(raw_data)`

**Zweck:** [Beschreibung]

**Parameter:**
- `raw_data` (list): [Beschreibung]

**Rückgabewert:**
- (list): [Beschreibung]

**Logik:**
1. [Schritt 1]
2. [Schritt 2]
...

**Beispiel:**
```python
# Eingabe
raw_data = [5, "hello", [1, 2, 3]]

# Ausgabe
# [25, 5, 6]

# Erklärung:
# - 5 ist eine Zahl → 5² = 25
# - "hello" ist ein String → len("hello") = 5
# - [1, 2, 3] ist eine Liste → sum([1, 2, 3]) = 6
```

[Wiederholen Sie dies für alle 4 Funktionen]

## 3. Code-Qualitätsanalyse

### Stärken ✅
1. [Stärke 1 mit Erklärung]
2. [Stärke 2]
3. [Stärke 3]

### Schwächen ⚠️
1. [Schwäche 1 mit Erklärung]
2. [Schwäche 2]
3. [Schwäche 3]

### Best Practices
- [Analyse]

### Fehlerbehandlung
- [Analyse]

## 4. Verbesserungsvorschläge

### Verbesserte Version von `process_data()`

```python
def process_data(raw_data: list) -> list:
    """
    Verarbeitet Rohdaten und konvertiert sie zu numerischen Werten.

    Args:
        raw_data: Liste mit gemischten Datentypen

    Returns:
        Liste mit verarbeiteten numerischen Werten
    """
    # [Ihr verbesserter Code]
```

**Verbesserungen:**
- [Erklärung 1]
- [Erklärung 2]

## 5. Eigene Experimente

### Testfall 1
```python
# Eingabe
test_data = [...]

# Erwartete Ausgabe
# [...]

# Tatsächliche Ausgabe
# [...]

# Erkenntnisse
# [...]
```

[Wiederholen für Testfall 2 und 3]

## Zusammenfassung

[Ihre wichtigsten Erkenntnisse]
```

## 💡 Hinweise für die Analyse

### Schritt-für-Schritt-Vorgehen

**1. Erste Durchsicht (10 Min.)**
- Code einmal komplett durchlesen
- Groben Zweck identifizieren
- Unbekannte Konzepte markieren

**2. Funktion für Funktion (30 Min.)**
- Mit der kleinsten Funktion beginnen (`aggregate`)
- Jeden Codeblock einzeln analysieren
- Beispiele mit Stift und Papier durchrechnen

**3. Zusammenhänge verstehen (10 Min.)**
- Wie rufen Funktionen einander auf?
- Welche Daten fliessen zwischen Funktionen?
- Was ist der Gesamtzweck?

**4. Dokumentation schreiben (10 Min.)**
- Template ausfüllen
- Beispiele hinzufügen
- Verbesserungen vorschlagen

### Fragen, die Sie beantworten sollten

**Für `process_data()`:**
- Was passiert mit verschiedenen Datentypen?
- Warum werden Zahlen quadriert?
- Warum wird bei Strings die Länge genommen?
- Was bedeutet `isinstance()`?

**Für `filter_data()`:**
- Was macht die List Comprehension?
- Warum wird auf `None` geprüft?
- Was ist der Standardwert für `threshold`?
- Welche Werte werden entfernt?

**Für `aggregate()`:**
- Was passiert, wenn `data` leer ist?
- Warum wird `sum()` zweimal aufgerufen?
- Welche Statistiken werden berechnet?
- Gibt es effizientere Methoden?

**Für `analyze()`:**
- Welche Rolle spielt diese Funktion?
- Wie werden die anderen Funktionen orchestriert?
- Was wird zurückgegeben?
- Warum wird `removed_count` berechnet?

### KI-Prompts für Hilfe

**Für Konzepterklärungen:**
```
Erkläre den folgenden Python-Code Zeile für Zeile:
```python
result = [x for x in data if x is not None and x > threshold]
```

Was macht diese List Comprehension und wie funktioniert die Bedingung?
```

**Für Code-Qualität:**
```
Analysiere diesen Python-Code und identifiziere:
1. Stärken (Best Practices)
2. Schwächen (Code Smells)
3. Potenzielle Bugs
4. Verbesserungsvorschläge

[Code einfügen]
```

**Für Verbesserungen:**
```
Wie könnte ich folgende Funktion verbessern?
[Code einfügen]

Bitte achte auf:
- Type Hints
- Docstrings
- Fehlerbehandlung
- Lesbarkeit
- Effizienz
```

### Nützliche Python-Konzepte

**List Comprehensions:**
```python
# Longform
result = []
for x in data:
    if x > 10:
        result.append(x)

# List Comprehension (äquivalent)
result = [x for x in data if x > 10]
```

**isinstance():**
```python
# Prüft den Typ eines Objekts
isinstance(5, int)           # True
isinstance("hello", str)     # True
isinstance([1, 2], list)     # True
isinstance(5, (int, float))  # True (einer von mehreren)
```

**Dictionary Comprehensions:**
```python
# Erstellt ein Dictionary mit Berechnungen
stats = {
    "sum": sum(data),
    "avg": sum(data) / len(data)
}
```

## 🔍 Beispiel-Analyse (Teillösung)

### Analyse der Funktion `filter_data()`

**Zweck:** Filtert verarbeitete Daten basierend auf einem Schwellenwert.

**Parameter:**
- `data` (list): Liste mit numerischen Werten (oder None)
- `threshold` (int, optional): Mindestwert, Standardwert ist 10

**Rückgabewert:**
- (list): Liste mit Werten > threshold (None-Werte ausgeschlossen)

**Logik:**
1. Verwendet List Comprehension für kompakte Filterung
2. Prüft zwei Bedingungen mit `and`:
   - `x is not None`: Schliesst None-Werte aus
   - `x > threshold`: Behält nur Werte über Schwellenwert
3. Gibt neue gefilterte Liste zurück (Original unverändert)

**Beispiel:**
```python
# Eingabe
data = [25, 5, 6, None, 15, 30]
threshold = 10

# Prozess
# 25: 25 > 10 → ✓ behalten
# 5:  5 > 10  → ✗ entfernen
# 6:  6 > 10  → ✗ entfernen
# None: ist None → ✗ entfernen
# 15: 15 > 10 → ✓ behalten
# 30: 30 > 10 → ✓ behalten

# Ausgabe
[25, 15, 30]
```

**Stärken:**
- ✅ Kompakt und pythonisch (List Comprehension)
- ✅ Funktionaler Stil (keine Seiteneffekte)
- ✅ Flexibel durch optionalen Parameter

**Schwächen:**
- ⚠️ Keine Type Hints
- ⚠️ Kein Docstring
- ⚠️ Keine Validierung (was wenn `data` kein List ist?)

**Verbesserte Version:**
```python
def filter_data(data: list, threshold: float = 10) -> list:
    """
    Filtert numerische Daten basierend auf einem Schwellenwert.

    Args:
        data: Liste mit numerischen Werten oder None
        threshold: Mindestwert für Filterung (Standard: 10)

    Returns:
        Liste mit Werten > threshold (None-Werte ausgeschlossen)

    Raises:
        TypeError: Wenn data keine Liste ist

    Examples:
        >>> filter_data([25, 5, None, 15], threshold=10)
        [25, 15]
    """
    if not isinstance(data, list):
        raise TypeError("data muss eine Liste sein")

    return [x for x in data if x is not None and x > threshold]
```

## 📚 Zusätzliche Challenges (Optional)

Falls Sie mehr Zeit haben:

1. **Performance-Analyse:**
   - Messen Sie die Ausführungszeit mit `time.time()`
   - Testen Sie mit grossen Datensätzen (10.000+ Elemente)
   - Gibt es Engpässe?

2. **Unit Tests:**
   - Schreiben Sie `pytest` Tests für alle Funktionen
   - Testen Sie Edge Cases (leere Listen, nur None-Werte, etc.)

3. **Alternative Implementierung:**
   - Nutzen Sie `pandas` oder `numpy` für effizientere Verarbeitung
   - Vergleichen Sie Performance und Lesbarkeit

## ✅ Selbsttest vor Abgabe

- [ ] Alle 5 Abschnitte vollständig ausgefüllt
- [ ] Jede Funktion detailliert erklärt
- [ ] Mindestens 3 Stärken und 3 Schwächen identifiziert
- [ ] Mindestens 1 Funktion verbessert mit Code
- [ ] 3 eigene Testfälle durchgeführt
- [ ] Dokumentation ist klar und strukturiert
- [ ] Markdown korrekt formatiert

## 📤 Abgabe

Erstellen Sie eine Datei `code-comprehension.md` und fügen Sie sie Ihrem Git-Repository hinzu.

---

**Viel Erfolg bei der Analyse!** 🔍

**Zurück zur Nachbearbeitung:** [README](./README.md)
