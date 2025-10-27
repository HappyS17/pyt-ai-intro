# Prompt-Experimente

**Zeitaufwand:** 60 Minuten  
**Ziel:** Verschiedene Prompt-Patterns praktisch testen

## 🎯 Aufgabe

Führen Sie Experimente mit verschiedenen Prompt-Patterns durch und dokumentieren Sie die Ergebnisse.

## Experiment 1: Role-Based Prompting (15 Min.)

### Aufgabe

Testen Sie denselben Prompt mit und ohne Rolle.

**Ohne Rolle:**
```text
Schreibe eine Funktion zur Passwort-Validierung.
```

**Mit Rolle:**
```text
Du bist ein Senior Python-Entwickler mit Fokus auf Security.

Schreibe eine Funktion zur Passwort-Validierung mit:
- Mindestens 8 Zeichen
- Gross- und Kleinbuchstaben
- Zahlen und Sonderzeichen
- Type Hints und Docstrings
- Unit Tests
```

### Dokumentation

**Ergebnis ohne Rolle:**
```text
[Was hat die KI generiert?]
```

**Ergebnis mit Rolle:**
```text
[Was hat die KI generiert?]
```

**Unterschiede:**
```text
[Welche Unterschiede haben Sie beobachtet?]
```

## Experiment 2: Context-Rich Prompting (15 Min.)

### Aufgabe

Vergleichen Sie vagen vs. detaillierten Prompt.

**Vage:**
```text
Erstelle eine Funktion für Datenvalidierung.
```

**Detailliert:**
```text
Kontext:
- Ich arbeite an einer Web-App für Benutzerregistrierung
- Technologie: Python 3.11, FastAPI
- Datenbank: PostgreSQL

Aufgabe:
Erstelle eine Funktion validate_user_data() die:
- Email-Format prüft
- Passwort-Stärke validiert
- Alter zwischen 18-120 prüft
- Pydantic Models nutzt

Constraints:
- Type Hints verwenden
- Aussagekräftige Fehlermeldungen
- Keine externen Libraries ausser Pydantic

Rückgabe:
- Tuple (is_valid: bool, errors: list[str])
```

### Dokumentation

**Qualität vager Prompt:**
```text
[Bewertung 1-5]
```

**Qualität detaillierter Prompt:**
```text
[Bewertung 1-5]
```

**Learnings:**
```text
[Was haben Sie gelernt?]
```

## Experiment 3: Chain-of-Thought (15 Min.)

### Aufgabe

Fordern Sie explizit Reasoning an.

**Prompt:**
```text
Ich habe folgenden Code der langsam ist:

```python
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates
```

Erkläre Schritt für Schritt:
1. Was ist das Performance-Problem?
2. Welche Komplexität hat der Code?
3. Wie kann man es optimieren?
4. Implementiere die optimierte Version
```

### Dokumentation

**Erklärung der KI:**
```text
[Kopieren Sie die Erklärung]
```

**Optimierter Code:**
```python
# [Kopieren Sie den Code]
```

**War die Erklärung hilfreich?**
```text
[Ihre Bewertung]
```

## Experiment 4: Few-Shot Learning (15 Min.)

### Aufgabe

Geben Sie Beispiele für gewünschtes Format.

**Prompt:**
```text
Erstelle Docstrings im Google-Style für folgende Funktionen.

Beispiel 1:
```python
def add(a, b):
    return a + b
```

Docstring:
```python
def add(a: int, b: int) -> int:
    """
    Addiert zwei Zahlen.
    
    Args:
        a: Erste Zahl
        b: Zweite Zahl
    
    Returns:
        Summe von a und b
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b
```

Jetzt für diese Funktion:
```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```
```

### Dokumentation

**Generierter Docstring:**
```python
# [Kopieren Sie das Ergebnis]
```

**Entspricht es dem Beispiel?**
```text
[Ja/Nein und warum]
```

## 🎯 Zusammenfassung

### Welches Pattern war am effektivsten?

```text
[Ihre Einschätzung]
```

### Was haben Sie über Prompt Engineering gelernt?

```text
[Ihre Learnings]
```

### Wie werden Sie Prompts in Zukunft formulieren?

```text
[Ihre Strategie]
```

## ✅ Checkliste

- [ ] Alle 4 Experimente durchgeführt
- [ ] Ergebnisse dokumentiert
- [ ] Unterschiede analysiert
- [ ] Learnings notiert

---

**Zurück zu:** [Vorbereitung README](./README.md)
