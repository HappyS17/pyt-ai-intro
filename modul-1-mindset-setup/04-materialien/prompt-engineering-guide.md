# Prompt Engineering Guide

Leitfaden für effektive Prompts beim KI-gestützten Programmieren.

## 🎯 Was ist Prompt Engineering?

Prompt Engineering ist die Kunst, klare und effektive Anweisungen für KI-Tools zu formulieren, um optimale Ergebnisse zu erzielen.

## 📋 Die 5 Elemente eines guten Prompts

### 1. Klarheit

**Definition:** Eindeutige, präzise Formulierung ohne Mehrdeutigkeiten.

**Beispiel:**

```text
❌ Schlecht: "Sortiere die Liste"
✅ Gut: "Sortiere die Liste von Zahlen aufsteigend"
```

### 2. Kontext

**Definition:** Hintergrundinformationen und Verwendungszweck bereitstellen.

**Beispiel:**

```text
❌ Ohne Kontext: "Erstelle eine Funktion zum Validieren"
✅ Mit Kontext: "Erstelle eine Python-Funktion, die eine E-Mail-Adresse 
validiert. Die Funktion soll True zurückgeben, wenn die E-Mail gültig 
ist (enthält @ und .), sonst False."
```

### 3. Spezifität

**Definition:** Genaue Anforderungen mit erwarteten Ein- und Ausgaben.

**Beispiel:**

```text
❌ Unspezifisch: "Lies eine Datei"
✅ Spezifisch: "Lies eine CSV-Datei namens 'daten.csv' ein und gib 
die erste Spalte als Liste zurück"
```

### 4. Beispiele

**Definition:** Konkrete Beispiele für erwartetes Verhalten.

**Beispiel:**

```text
Erstelle eine Funktion, die einen String umdreht.

Beispiel:
Eingabe: "Hallo"
Ausgabe: "ollaH"
```

### 5. Einschränkungen

**Definition:** Was NICHT gemacht werden soll und technische Grenzen.

**Beispiel:**

```text
Erstelle ein Programm zur Passwort-Generierung.
- Verwende KEINE externen Bibliotheken
- Passwort soll 12 Zeichen lang sein
- Muss Gross- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten
```

## 📝 Prompt-Template

### Grundstruktur

```text
[Aufgabe]: Was soll gemacht werden?

[Kontext]: Warum? Wofür?

[Anforderungen]:
- Anforderung 1
- Anforderung 2
- Anforderung 3

[Beispiel]:
Eingabe: ...
Ausgabe: ...

[Einschränkungen]:
- Was zu beachten ist
```

### Ausgefülltes Beispiel

```text
[Aufgabe]: 
Erstelle eine Python-Funktion zur Berechnung des Durchschnitts

[Kontext]: 
Ich möchte die Durchschnittsnote meiner Prüfungen berechnen

[Anforderungen]:
- Funktion heisst calculate_average
- Nimmt eine Liste von Zahlen als Parameter
- Gibt den Durchschnitt als Float zurück
- Behandelt leere Listen (gibt 0 zurück)

[Beispiel]:
Eingabe: [5, 4, 6, 5]
Ausgabe: 5.0

[Einschränkungen]:
- Keine externen Bibliotheken
- Kommentare auf Deutsch
```

## ❌ Häufige Fehler

### Fehler 1: Zu vage

```text
❌ "Schreib mir was mit Daten"
✅ "Erstelle ein Python-Programm, das eine CSV-Datei einliest und 
die Anzahl der Zeilen ausgibt"
```

### Fehler 2: Zu komplex

```text
❌ "Erstelle eine vollständige Webanwendung mit Login, Datenbank, 
API, Frontend und Backend"
✅ "Erstelle eine einfache Flask-Route, die 'Hello World' zurückgibt"
```

**Tipp:** Grosse Aufgaben in kleine Schritte zerlegen!

### Fehler 3: Fehlender Kontext

```text
❌ "Wie sortiere ich das?"
✅ "Wie sortiere ich eine Liste von Dictionaries in Python nach dem 
Wert des Keys 'name'?"
```

### Fehler 4: Keine Beispiele

```text
❌ "Formatiere den String"
✅ "Formatiere den String so, dass der erste Buchstabe gross ist.
Beispiel: 'hallo' → 'Hallo'"
```

## ✅ Best Practices

### 1. Iterativ verfeinern

**Prozess:**

```text
Erster Versuch → Testen → Probleme identifizieren → 
Prompt verbessern → Erneut testen
```

**Beispiel:**

```text
Version 1: "Mach ein Ratespiel"
→ Zu vage

Version 2: "Erstelle ein Zahlenraten-Spiel in Python"
→ Besser, aber Details fehlen

Version 3: "Erstelle ein Zahlenraten-Spiel in Python:
- Computer wählt Zahl zwischen 1-100
- Benutzer rät
- Hinweise: zu hoch/niedrig
- Anzahl Versuche zählen"
→ Perfekt!
```

### 2. Sprache und Ton

**Klar und direkt:**

```text
✅ "Erstelle eine Funktion, die..."
❌ "Könntest du vielleicht eventuell..."
```

**Imperativ verwenden:**

```text
✅ "Erstelle", "Implementiere", "Berechne"
❌ "Würdest du", "Kannst du"
```

### 3. Technische Details

**Sprache/Framework angeben:**

```text
✅ "Erstelle in Python..."
✅ "Nutze Flask für..."
❌ "Erstelle ein Programm..." (welche Sprache?)
```

**Version spezifizieren (falls wichtig):**

```text
✅ "Nutze Python 3.11 Features"
✅ "Kompatibel mit Python 3.8+"
```

### 4. Code-Stil

**Stil-Präferenzen angeben:**

```text
"Erstelle eine Funktion mit folgenden Anforderungen:
- Type Hints verwenden
- Docstrings im Google-Stil
- Kommentare auf Deutsch
- PEP 8 konform"
```

## 🔄 Prompt-Iteration Beispiel

### Aufgabe: Wort-Zähler

#### Iteration 1: Zu vage

```text
"Zähle Wörter"
```

**Problem:** Keine Details, keine Sprache, kein Kontext.

#### Iteration 2: Besser

```text
"Erstelle ein Python-Programm, das Wörter in einem Text zählt"
```

**Problem:** Wie wird der Text eingegeben? Was wird ausgegeben?

#### Iteration 3: Gut

```text
"Erstelle ein Python-Programm, das:
- Text vom Benutzer einliest
- Anzahl Wörter zählt
- Ergebnis ausgibt

Beispiel:
Eingabe: 'Hallo Welt, wie geht es dir?'
Ausgabe: 'Der Text enthält 6 Wörter.'"
```

**Problem:** Funktioniert, aber könnte mehr Features haben.

#### Iteration 4: Optimal

```text
"Erstelle ein Python-Programm zur Textanalyse:

Anforderungen:
- Text vom Benutzer einlesen
- Anzahl Wörter zählen
- Anzahl Zeichen zählen (mit und ohne Leerzeichen)
- Längstes Wort finden
- Ergebnisse formatiert ausgeben

Beispiel:
Eingabe: 'Hallo Welt'
Ausgabe:
  Wörter: 2
  Zeichen (mit Leerzeichen): 10
  Zeichen (ohne Leerzeichen): 9
  Längstes Wort: 'Hallo' (5 Zeichen)

Einschränkungen:
- Keine externen Bibliotheken
- Kommentare auf Deutsch"
```

## 💡 Prompt-Bibliothek aufbauen

### Erfolgreiche Prompts sammeln

**Erstellen Sie eine Datei `prompts.md`:**

```markdown
# Meine Prompt-Bibliothek

## Datenverarbeitung

### CSV einlesen
Erstelle eine Python-Funktion, die...
[Vollständiger Prompt]

### JSON parsen
Erstelle eine Python-Funktion, die...
[Vollständiger Prompt]

## Benutzerinteraktion

### Eingabe validieren
Erstelle eine Python-Funktion, die...
[Vollständiger Prompt]
```

### Kategorien

- Datenverarbeitung
- Benutzerinteraktion
- Datei-Operationen
- Algorithmen
- Web-Entwicklung
- Testing

## 🎓 Übung macht den Meister

### Übungsaufgaben

1. **Einfach:** Formulieren Sie einen Prompt für einen Taschenrechner
2. **Mittel:** Formulieren Sie einen Prompt für eine Einkaufsliste
3. **Schwer:** Formulieren Sie einen Prompt für ein Quiz-Programm

### Selbst-Review

Prüfen Sie Ihre Prompts:

- [ ] Ist die Aufgabe klar?
- [ ] Ist genug Kontext vorhanden?
- [ ] Sind alle Anforderungen spezifisch?
- [ ] Gibt es Beispiele?
- [ ] Sind Einschränkungen genannt?

## 📚 Weiterführende Ressourcen

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [GitHub Copilot Best Practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

---

**Zurück zu Materialien:** [Materialien README](./README.md)
