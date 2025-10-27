# Aufgabe 1: Prompt-Portfolio

**Zeitaufwand:** 60 Minuten  
**Abgabe:** Vor Modul 2  
**Punkte:** 25% der Nachbearbeitung

## 🎯 Ziel

Erstellen Sie eine Sammlung von 10 effektiven Prompts, die Sie während des Moduls oder danach formuliert haben.

## 📋 Aufgabenstellung

### Was zu tun ist

1. **Sammeln Sie 10 Prompts**, die Sie für verschiedene Programmieraufgaben verwendet haben
2. **Dokumentieren Sie** jeden Prompt vollständig
3. **Reflektieren Sie** über die Qualität und mögliche Verbesserungen
4. **Kategorisieren Sie** die Prompts nach Themen

### Anforderungen

- Mindestens 10 verschiedene Prompts
- Verschiedene Kategorien (z.B. Datenverarbeitung, Benutzerinteraktion, etc.)
- Für jeden Prompt: Aufgabe, Kontext, Anforderungen, Beispiel
- Reflexion über Verbesserungsmöglichkeiten

## 📝 Template

Nutzen Sie folgendes Template für jeden Prompt:

```markdown
## Prompt [Nummer]: [Titel]

### Kategorie

[z.B. Datenverarbeitung, Benutzerinteraktion, Algorithmen]

### Aufgabe

[Was sollte das Programm tun?]

### Vollständiger Prompt

```text
[Hier den kompletten Prompt einfügen]
```

### Generierter Code (Auszug)

```python
# Zeigen Sie einen relevanten Ausschnitt des generierten Codes
```

### Funktioniert?

- [ ] Ja, auf Anhieb
- [ ] Ja, nach Anpassungen
- [ ] Nein, musste neu formuliert werden

### Was hat gut funktioniert?

[Ihre Beobachtungen]

### Was könnte verbessert werden?

[Verbesserungsvorschläge für den Prompt]

### Verbesserter Prompt (optional)

```text
[Falls Sie den Prompt verbessert haben]
```

---
```

## 💡 Beispiel

```markdown
## Prompt 1: Temperatur-Umrechner

### Kategorie

Benutzerinteraktion

### Aufgabe

Ein Programm erstellen, das Temperaturen zwischen Celsius und Fahrenheit umrechnet.

### Vollständiger Prompt

```text
Erstelle ein Python-Programm zur Temperatur-Umrechnung:

Anforderungen:
- Benutzer wählt Richtung (C→F oder F→C)
- Temperatur eingeben
- Ergebnis auf 2 Dezimalstellen runden
- Eingabe validieren (nur Zahlen)
- Programm läuft in Schleife bis 'quit'

Beispiel:
Richtung (1=C→F, 2=F→C): 1
Temperatur in Celsius: 25
Ergebnis: 25°C = 77.00°F

Einschränkungen:
- Keine externen Bibliotheken
- Kommentare auf Deutsch
```

### Generierter Code (Auszug)

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\n=== Temperatur-Umrechner ===")
    choice = input("Richtung (1=C→F, 2=F→C, quit): ")
    # ... rest des Codes
```

### Funktioniert?

- [x] Ja, auf Anhieb
- [ ] Ja, nach Anpassungen
- [ ] Nein, musste neu formuliert werden

### Was hat gut funktioniert?

- Klare Anforderungen
- Beispiel-Interaktion gezeigt
- Einschränkungen genannt
- Code war sofort lauffähig

### Was könnte verbessert werden?

- Fehlerbehandlung für ungültige Auswahl könnte expliziter sein
- Könnte Formatierung der Ausgabe detaillierter beschreiben

### Verbesserter Prompt (optional)

```text
[Gleicher Prompt, aber mit zusätzlicher Anforderung:]
- Bei ungültiger Auswahl: Fehlermeldung und erneut fragen
- Ausgabe formatiert mit Rahmen
```

---
```

## 📂 Kategorien

Verteilen Sie Ihre 10 Prompts auf mindestens 4 verschiedene Kategorien:

### Vorgeschlagene Kategorien

1. **Datenverarbeitung**
   - CSV/JSON lesen
   - Daten filtern/sortieren
   - Statistiken berechnen

2. **Benutzerinteraktion**
   - Eingabe/Ausgabe
   - Menüs
   - Validierung

3. **Algorithmen**
   - Sortieren
   - Suchen
   - Berechnungen

4. **Datei-Operationen**
   - Lesen/Schreiben
   - Verarbeiten
   - Formatieren

5. **Text-Verarbeitung**
   - String-Manipulation
   - Parsing
   - Formatierung

6. **Mathematik**
   - Berechnungen
   - Formeln
   - Statistik

## ✅ Checkliste

- [ ] 10 Prompts dokumentiert
- [ ] Mindestens 4 verschiedene Kategorien
- [ ] Jeder Prompt vollständig (alle Felder ausgefüllt)
- [ ] Code-Auszüge eingefügt
- [ ] Reflexion für jeden Prompt
- [ ] Verbesserungsvorschläge notiert
- [ ] Dokument sauber formatiert
- [ ] Rechtschreibung geprüft

## 📤 Abgabe

### Format

- **Markdown-Datei:** `prompt-portfolio.md`
- **Oder PDF:** `prompt-portfolio.pdf`

### Struktur

```markdown
# Mein Prompt-Portfolio
## Modul 1: Programmier-Mindset & KI-Tools

**Name:** [Ihr Name]
**Datum:** [Datum]

---

## Inhaltsverzeichnis

1. [Prompt 1: Titel](#prompt-1-titel)
2. [Prompt 2: Titel](#prompt-2-titel)
...
10. [Prompt 10: Titel](#prompt-10-titel)

---

## Prompt 1: [Titel]
[Template hier einfügen]

---

## Prompt 2: [Titel]
[Template hier einfügen]

...

---

## Zusammenfassung

### Was habe ich gelernt?

[Ihre Erkenntnisse über Prompt Engineering]

### Meine besten Prompts

[Die 3 besten Prompts und warum]

### Verbesserungspotenzial

[Was möchten Sie beim Prompting noch verbessern?]
```

## 🎓 Bewertungskriterien

### Vollständigkeit (40%)

- [ ] 10 Prompts vorhanden
- [ ] Alle Felder ausgefüllt
- [ ] Code-Beispiele enthalten

### Qualität der Prompts (30%)

- [ ] Prompts sind klar und spezifisch
- [ ] Enthalten alle 5 Elemente (Klarheit, Kontext, Spezifität, Beispiele, Einschränkungen)
- [ ] Verschiedene Schwierigkeitsgrade

### Reflexion (20%)

- [ ] Ehrliche Selbsteinschätzung
- [ ] Konkrete Verbesserungsvorschläge
- [ ] Lernerkenntnisse dokumentiert

### Präsentation (10%)

- [ ] Saubere Formatierung
- [ ] Übersichtliche Struktur
- [ ] Keine Rechtschreibfehler

## 💡 Tipps

### Tipp 1: Prompts sammeln

Beginnen Sie frühzeitig mit dem Sammeln von Prompts während des Moduls.

### Tipp 2: Vielfalt

Wählen Sie Prompts mit verschiedenen Schwierigkeitsgraden und Themen.

### Tipp 3: Ehrlichkeit

Seien Sie ehrlich bei der Bewertung - auch "gescheiterte" Prompts sind lehrreich!

### Tipp 4: Details

Je detaillierter Ihre Reflexion, desto mehr lernen Sie.

## 🆘 Häufige Fragen

### Frage 1: Müssen alle Prompts erfolgreich gewesen sein?

Nein! Auch Prompts, die nicht funktioniert haben, sind wertvoll. Wichtig ist die Reflexion darüber, warum nicht.

### Frage 2: Kann ich Prompts aus den Übungen verwenden?

Ja, aber zeigen Sie, wie Sie sie verbessert oder angepasst haben.

### Frage 3: Wie lang sollte die Reflexion sein?

Pro Prompt: 2-3 Sätze für "Was hat gut funktioniert?" und "Was könnte verbessert werden?"

### Frage 4: Kann ich KI nutzen, um meine Prompts zu verbessern?

Ja! Aber dokumentieren Sie den Prozess und Ihre eigenen Überlegungen.

---

**Zurück zur Nachbearbeitung:** [Nachbearbeitung README](./README.md)
