# Advanced Prompt Engineering

**Für:** Modul 5 - Fortgeschrittene KI  
**Version:** 1.0

---

## 🎯 Überblick

Advanced Prompt Engineering geht über Basis-Prompts hinaus und nutzt fortgeschrittene Techniken für bessere Ergebnisse.

---

## 🔗 Chain-of-Thought (CoT)

### Basis-Prompt (schlecht)
```
Löse: 2 + 3 * 4 = ?
```

### CoT-Prompt (besser)
```
Löse diese Aufgabe Schritt für Schritt:
2 + 3 * 4

Denk daran:
1. Punkt vor Strich
2. Zeige jeden Schritt
3. Erkläre dein Denken

Lösung:
```

### Ergebnis
```
Schritt 1: Multiplikation zuerst (Punkt vor Strich)
3 * 4 = 12

Schritt 2: Addition
2 + 12 = 14

Antwort: 14
```

---

## 🎭 Few-Shot Learning

### Zero-Shot (keine Beispiele)
```
Klassifiziere diese Sentiment: "Das Produkt ist grossartig!"
```

### Few-Shot (mit Beispielen)
```
Klassifiziere Sentiment als positiv, neutral oder negativ.

Beispiele:
- "Das Produkt ist grossartig!" → positiv
- "Das Produkt ist ok" → neutral
- "Das Produkt ist schrecklich" → negativ

Klassifiziere: "Das Produkt ist grossartig!"
```

### Ergebnis
```
Sentiment: positiv
Grund: Wort "grossartig" ist positiv
```

---

## 🎯 System Prompts

### Struktur
```
Du bist ein [ROLLE] mit [EIGENSCHAFTEN].

Deine Aufgaben:
1. [AUFGABE 1]
2. [AUFGABE 2]
3. [AUFGABE 3]

Wichtige Regeln:
- [REGEL 1]
- [REGEL 2]
- [REGEL 3]

Antworte immer in [FORMAT].
```

### Beispiel: Python-Tutor
```
Du bist ein erfahrener Python-Tutor mit 10 Jahren Erfahrung.

Deine Aufgaben:
1. Erkläre Python-Konzepte einfach
2. Gib praktische Beispiele
3. Zeige häufige Fehler

Wichtige Regeln:
- Nutze einfache Sprache
- Gib immer Code-Beispiele
- Erkläre das WARUM, nicht nur das WAS
- Sei geduldig und ermutigend

Antworte immer mit:
1. Erklärung
2. Code-Beispiel
3. Häufiger Fehler
4. Übungs-Aufgabe
```

---

## 🔄 Iterative Refinement

### Iteration 1: Basis-Prompt
```
Schreib einen Blog-Post über Python
```

### Iteration 2: Mit Anforderungen
```
Schreib einen Blog-Post über Python für Anfänger.
Länge: 500 Wörter
Struktur: Einleitung, 3 Hauptpunkte, Fazit
```

### Iteration 3: Mit Stil
```
Schreib einen Blog-Post über Python für Anfänger.
Länge: 500 Wörter
Struktur: Einleitung, 3 Hauptpunkte, Fazit
Stil: Freundlich, ermutigend, mit Humor
Zielgruppe: Anfänger ohne Programmier-Erfahrung
```

### Iteration 4: Mit Beispielen
```
Schreib einen Blog-Post über Python für Anfänger.
Länge: 500 Wörter
Struktur: Einleitung, 3 Hauptpunkte, Fazit
Stil: Freundlich, ermutigend, mit Humor
Zielgruppe: Anfänger ohne Programmier-Erfahrung

Hauptpunkte:
1. Warum Python lernen?
2. Erste Schritte
3. Häufige Anfängerfehler

Gib Code-Beispiele für jeden Punkt.
```

---

## 🎨 Prompt-Templates

### Template 1: Erklärung
```
Erkläre [KONZEPT] für [ZIELGRUPPE]:

1. Einfache Erklärung (1-2 Sätze)
2. Detaillierte Erklärung (3-5 Sätze)
3. Praktisches Beispiel
4. Häufige Fehler
5. Weiterführende Ressourcen
```

### Template 2: Code-Generierung
```
Schreib Python-Code für [AUFGABE]:

Anforderungen:
- [ANFORDERUNG 1]
- [ANFORDERUNG 2]
- [ANFORDERUNG 3]

Constraints:
- Nutze [LIBRARY]
- Beachte [BEST PRACTICE]
- Implementiere [FEATURE]

Gib auch Tests und Dokumentation.
```

### Template 3: Problem-Lösung
```
Ich habe ein Problem:
[PROBLEM BESCHREIBUNG]

Kontext:
- [KONTEXT 1]
- [KONTEXT 2]

Fehler:
[FEHLER MESSAGE]

Gib mir:
1. Ursache des Problems
2. Schritt-für-Schritt Lösung
3. Code-Beispiel
4. Wie man es in Zukunft vermeidet
```

---

## 🎯 Prompt-Optimierung

### Checkliste

- [ ] **Klarheit:** Ist die Anfrage verständlich?
- [ ] **Kontext:** Habe ich genug Hintergrund gegeben?
- [ ] **Spezifität:** Ist die Anfrage spezifisch genug?
- [ ] **Format:** Habe ich das gewünschte Format beschrieben?
- [ ] **Beispiele:** Habe ich Beispiele gegeben?
- [ ] **Constraints:** Habe ich Limitationen genannt?

### Vorher & Nachher

#### ❌ Schlecht
```
Schreib mir Code
```

#### ✅ Gut
```
Schreib Python-Code für einen Email-Validator:

Anforderungen:
- Validiere Email-Format
- Prüfe auf häufige Fehler
- Implementiere Error Handling
- Schreib Tests

Nutze:
- regex für Validierung
- pytest für Tests
- Type Hints

Gib auch Docstrings und Beispiele.
```

---

## 🔍 Debugging von Prompts

### Problem: Zu vage Antwort

**Ursache:** Prompt ist zu offen

**Lösung:**
```
Vorher: "Erkläre Machine Learning"
Nachher: "Erkläre Machine Learning für Anfänger in 3 Sätzen mit einem praktischen Beispiel"
```

### Problem: Falsches Format

**Ursache:** Format nicht spezifiziert

**Lösung:**
```
Vorher: "Gib mir eine Liste"
Nachher: "Gib mir eine JSON-Liste mit Feldern: name, alter, stadt"
```

### Problem: Zu lange Antwort

**Ursache:** Keine Längenbeschränkung

**Lösung:**
```
Vorher: "Erkläre Python"
Nachher: "Erkläre Python in maximal 100 Wörtern"
```

---

## 💡 Pro-Tipps

### 1. Rollen nutzen
```
"Du bist ein erfahrener Softwareentwickler..."
```

### 2. Kontext geben
```
"Ich bin Anfänger mit 1 Monat Python-Erfahrung..."
```

### 3. Beispiele zeigen
```
"Hier ist ein gutes Beispiel: ..."
"Hier ist ein schlechtes Beispiel: ..."
```

### 4. Iterieren
```
"Das ist gut, aber..."
"Kannst du auch..."
"Mach es noch..."
```

### 5. Feedback geben
```
"Das ist zu komplex"
"Das ist zu simpel"
"Das ist nicht was ich wollte"
```

---

## 📊 Vergleich: Basis vs. Advanced

| Aspekt | Basis | Advanced |
|--------|-------|----------|
| Länge | 1-2 Sätze | 5-10 Sätze |
| Kontext | Minimal | Ausführlich |
| Beispiele | Keine | Mehrere |
| Iterationen | 1-2 | 3-5 |
| Qualität | 60% | 90%+ |

---

## 📚 Ressourcen

- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

**Merksatz:** "Ein grossartiger Prompt ist wie ein grossartiger Lehrer - klar, geduldig und hilfreich!" 🎓

