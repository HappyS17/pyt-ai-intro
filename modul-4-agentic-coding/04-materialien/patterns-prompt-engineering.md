# Prompt Engineering Patterns

Bewährte Patterns für effektives Prompt Engineering.

## 1. Role-Based Prompting

### Pattern

```text
Du bist ein [ROLLE] mit [EXPERTISE].

[AUFGABE]
```

### Beispiel

```text
Du bist ein Senior Python-Entwickler mit 10 Jahren Erfahrung in Web-Entwicklung und Security.

Erstelle eine sichere Login-Funktion mit:
- Password Hashing (bcrypt)
- Rate Limiting
- Session Management
```

### Wann nutzen?

- Für spezifische Expertise
- Wenn Kontext wichtig ist
- Für professionelle Code-Qualität

## 2. Context-Rich Prompting

### Pattern

```text
Kontext:
- [PROJEKT-INFO]
- [TECHNOLOGIE]
- [CONSTRAINTS]

Aufgabe:
[SPEZIFIKATION]

Constraints:
- [EINSCHRÄNKUNGEN]
```

### Beispiel

```text
Kontext:
- E-Commerce-Plattform
- Python 3.11, FastAPI, PostgreSQL
- 10.000+ Nutzer täglich

Aufgabe:
Implementiere Warenkorb-Funktionalität

Constraints:
- Muss skalierbar sein
- Redis für Caching
- Maximale Response-Zeit: 100ms
```

## 3. Chain-of-Thought

### Pattern

```text
Erkläre Schritt für Schritt:
1. [SCHRITT 1]
2. [SCHRITT 2]
...

Dann implementiere die Lösung.
```

### Beispiel

```text
Erkläre Schritt für Schritt wie man einen LRU Cache implementiert:
1. Welche Datenstruktur?
2. Welche Operationen?
3. Wie O(1) erreichen?

Dann implementiere in Python.
```

## 4. Few-Shot Learning

### Pattern

```text
Hier sind Beispiele:

Beispiel 1:
[INPUT] → [OUTPUT]

Beispiel 2:
[INPUT] → [OUTPUT]

Jetzt für:
[NEUE AUFGABE]
```

## 5. Iterative Refinement

### Pattern

```text
Iteration 1: Basis-Implementierung
Iteration 2: Feature X hinzufügen
Iteration 3: Optimieren
Iteration 4: Edge Cases
```

---

**Zurück zu:** [Materialien README](./README.md)
