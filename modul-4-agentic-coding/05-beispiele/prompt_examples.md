# Prompt Engineering Beispiele

**Für:** Modul 4 - Agentic Coding  
**Version:** 1.0

---

## 🎯 Gute vs. Schlechte Prompts

### ❌ Schlechter Prompt

```
Schreib mir ein Python-Programm
```

**Probleme:**
- Zu vage
- Keine Anforderungen
- Keine Kontext
- Unerwartete Ergebnisse

---

### ✅ Guter Prompt

```
Schreib ein Python-Programm, das:
1. Eine CSV-Datei mit Kundendaten liest
2. Kunden nach Alter filtert (> 25 Jahre)
3. Die gefilterten Daten in eine neue CSV speichert
4. Fehlerbehandlung für fehlende Dateien implementiert

Anforderungen:
- Nutze pandas für CSV-Verarbeitung
- Schreibe aussagekräftige Variablennamen
- Füge Docstrings hinzu
- Implementiere Logging

Beispiel-Input:
name,age,city
Alice,30,Berlin
Bob,22,Munich
Charlie,28,Hamburg
```

**Vorteile:**
- Klar definierte Anforderungen
- Kontext und Beispiele
- Erwartete Qualität
- Weniger Iterationen nötig

---

## 📋 Prompt-Patterns

### 1. Role-Based Prompting

```
Du bist ein erfahrener Python-Entwickler mit 10 Jahren Erfahrung.
Du schreibst sauberen, wartbaren Code mit Best Practices.

Schreib eine Funktion, die...
```

**Effekt:** KI passt Stil und Komplexität an die Rolle an.

---

### 2. Chain-of-Thought

```
Ich möchte einen Web-Scraper schreiben.

Denk Schritt für Schritt:
1. Welche Libraries brauche ich?
2. Wie hole ich die HTML-Seite?
3. Wie parse ich die HTML?
4. Wie speichere ich die Daten?
5. Wie handle ich Fehler?

Erkläre jeden Schritt, dann schreib den Code.
```

**Effekt:** Bessere Qualität durch strukturiertes Denken.

---

### 3. Few-Shot Learning

```
Hier sind Beispiele für gute Funktionsnamen:

Schlecht → Gut:
- calc() → calculate_average()
- proc() → process_user_data()
- do_stuff() → validate_email_format()

Jetzt schreib eine Funktion für: Konvertiere Celsius zu Fahrenheit
Nutze die gleiche Naming-Konvention.
```

**Effekt:** KI lernt von Beispielen.

---

### 4. Iterative Refinement

```
Erste Iteration:
"Schreib einen Chatbot"

Feedback:
"Der Chatbot ist zu simpel. Füge Kontext-Speicher hinzu."

Zweite Iteration:
"Schreib einen Chatbot, der:
- Frühere Nachrichten speichert
- Kontext in Antworten nutzt
- Maximal 5 Nachrichten speichert"
```

**Effekt:** Schrittweise Verbesserung.

---

## 🔍 Konkrete Beispiele

### Beispiel 1: Datenverarbeitung

#### ❌ Schlecht
```
Verarbeite diese Daten
```

#### ✅ Gut
```
Ich habe eine CSV-Datei mit Verkaufsdaten:
- Spalten: date, product, quantity, price
- Format: YYYY-MM-DD
- Grösse: ~10.000 Zeilen

Schreib ein Python-Skript, das:
1. Die Datei lädt
2. Umsatz pro Produkt berechnet (quantity * price)
3. Top 5 Produkte nach Umsatz findet
4. Ergebnisse in JSON speichert

Nutze pandas und gib mir auch ein Beispiel-Output.
```

---

### Beispiel 2: Bug-Fixing

#### ❌ Schlecht
```
Mein Code funktioniert nicht. Hilf mir!
```

#### ✅ Gut
```
Ich habe diesen Code:

\`\`\`python
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

result = calculate_average([1, 2, 3, 0])
print(result)
\`\`\`

Fehler: ZeroDivisionError wenn die Liste leer ist

Anforderungen:
- Behandle leere Listen
- Gib aussagekräftige Fehlermeldung
- Schreib auch einen Test

Erkläre das Problem und die Lösung.
```

---

### Beispiel 3: Code Review

#### ❌ Schlecht
```
Überprüf meinen Code
```

#### ✅ Gut
```
Überprüf diesen Code auf:
1. Performance-Probleme
2. Sicherheitslücken
3. Best Practices
4. Fehlerbehandlung

\`\`\`python
def fetch_user_data(user_id):
    import requests
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()
\`\`\`

Gib mir konkrete Verbesserungsvorschläge mit Code-Beispielen.
```

---

### Beispiel 4: Erklärung

#### ❌ Schlecht
```
Erkläre Decorators
```

#### ✅ Gut
```
Erkläre Python Decorators:
1. Für Anfänger (einfache Erklärung)
2. Mit konkretem Beispiel
3. Mit Use Cases
4. Mit häufigen Fehlern

Zielgruppe: Anfänger mit 1 Monat Python-Erfahrung
```

---

## 🎯 Prompt-Checkliste

Bevor du einen Prompt sendest, prüfe:

- [ ] **Kontext:** Habe ich genug Hintergrund gegeben?
- [ ] **Anforderungen:** Sind die Anforderungen klar?
- [ ] **Format:** Habe ich das gewünschte Format beschrieben?
- [ ] **Beispiele:** Habe ich Beispiele gegeben?
- [ ] **Constraints:** Habe ich Limitationen genannt?
- [ ] **Qualität:** Habe ich Qualitätsanforderungen definiert?

---

## 💡 Pro-Tipps

### 1. Kontext ist König
```
❌ "Schreib einen API-Endpoint"
✅ "Schreib einen Flask-API-Endpoint für User-Registrierung mit:
    - Email-Validierung
    - Password-Hashing
    - Error-Handling"
```

### 2. Beispiele helfen
```
❌ "Formatiere diese Daten"
✅ "Formatiere diese Daten wie folgt:
    Input: 'john_doe'
    Output: 'John Doe'"
```

### 3. Rollen nutzen
```
❌ "Schreib einen Test"
✅ "Du bist ein QA-Engineer mit 5 Jahren Erfahrung.
    Schreib einen umfassenden Test für..."
```

### 4. Iterieren
```
Erste Antwort: "Das ist gut, aber..."
Zweite Antwort: "Besser! Jetzt noch..."
Dritte Antwort: "Perfekt!"
```

---

## 📚 Ressourcen

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/prompt-engineering-for-developers/)

---

**Merksatz:** "Ein guter Prompt spart 10 Iterationen!" - Erfahrung

