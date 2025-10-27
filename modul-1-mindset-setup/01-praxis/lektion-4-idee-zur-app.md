# Lektion 4: Von der Idee zur App

**Dauer:** 50 Minuten  
**Ziel:** Den kompletten Entwicklungsworkflow mit KI durchlaufen

## 📋 Ablauf

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-5 Min. | Recap & Workflow-Übersicht | Vortrag |
| 5-15 Min. | Code-Review & Debugging | Vortrag + Beispiele |
| 15-25 Min. | Live-Coding: Mini-App | Live-Demo |
| 25-50 Min. | Übung: Taschenrechner | Hands-on |

---

## 🎯 Lernziele

Nach dieser Lektion können die Studierenden:

- Den Entwicklungsworkflow mit KI anwenden
- Code auf Qualität überprüfen
- Einfache Debugging-Strategien einsetzen
- Eine kleine Anwendung von Grund auf erstellen

---

## 🔄 Teil 1: Recap & Workflow-Übersicht (5 Min.)

### Was haben wir gelernt?

**Modul 1 Zusammenfassung:**

- ✅ Programmieren = Problemlösung
- ✅ Entwicklungsumgebung (VS Code, Git)
- ✅ Effektive Prompts formulieren

### Der Entwicklungsworkflow

**Von der Idee zum fertigen Programm:**

```text
1. Problem verstehen
   ↓
2. In Teilprobleme zerlegen
   ↓
3. Für jedes Teilproblem:
   - Prompt formulieren
   - Code generieren
   - Code verstehen
   - Code testen
   - Bei Bedarf: Anpassen
   ↓
4. Teilösungen zusammenführen
   ↓
5. Gesamtes Programm testen
   ↓
6. Code committen (Git)
```

---

## 🔍 Teil 2: Code-Review & Debugging (10 Min.)

### Code-Review: Was prüfen?

#### 1. Funktionalität

**Fragen:**

- Macht der Code, was er soll?
- Funktionieren alle Features?
- Gibt es Edge Cases?

**Beispiel:**

```python
# Funktion zum Teilen von Zahlen
def divide(a, b):
    return a / b

# Problem: Was passiert bei b = 0?
```

**Besser:**

```python
def divide(a, b):
    if b == 0:
        return "Fehler: Division durch Null"
    return a / b
```

#### 2. Lesbarkeit

**Fragen:**

- Sind Variablennamen aussagekräftig?
- Ist der Code gut strukturiert?
- Gibt es Kommentare wo nötig?

**Beispiel:**

```python
# Schlecht
def f(x, y):
    return x * y * 0.19

# Gut
def calculate_tax(price, quantity):
    tax_rate = 0.19
    return price * quantity * tax_rate
```

#### 3. Fehlerbehandlung

**Fragen:**

- Werden Fehler abgefangen?
- Sind Fehlermeldungen hilfreich?
- Stürzt das Programm ab?

**Beispiel:**

```python
# Ohne Fehlerbehandlung
age = int(input("Alter: "))  # Crash bei "abc"

# Mit Fehlerbehandlung
try:
    age = int(input("Alter: "))
except ValueError:
    print("Bitte eine Zahl eingeben!")
    age = 0
```

#### 4. Effizienz

**Fragen:**

- Ist der Code unnötig kompliziert?
- Gibt es einfachere Lösungen?
- Werden Ressourcen verschwendet?

**Beispiel:**

```python
# Kompliziert
numbers = [1, 2, 3, 4, 5]
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)

# Einfacher
numbers = [1, 2, 3, 4, 5]
even = [n for n in numbers if n % 2 == 0]
```

### Debugging-Strategien

#### Strategie 1: Print-Debugging

**Einfachste Methode:**

```python
def calculate_total(prices):
    print(f"Eingabe: {prices}")  # Debug
    total = sum(prices)
    print(f"Summe: {total}")  # Debug
    return total
```

#### Strategie 2: Fehler lesen

**Fehlermeldungen verstehen:**

```python
# Fehler: NameError: name 'x' is not defined
# Bedeutung: Variable x wurde nicht definiert
# Lösung: Variable definieren oder Tippfehler korrigieren
```

#### Strategie 3: Schrittweise testen

**Kleine Teile einzeln testen:**

```python
# Statt alles auf einmal:
result = complex_function(data)

# Schritt für Schritt:
step1 = prepare_data(data)
print(f"Nach Schritt 1: {step1}")
step2 = process_data(step1)
print(f"Nach Schritt 2: {step2}")
result = finalize_data(step2)
```

#### Strategie 4: KI um Hilfe fragen

**Prompt-Beispiel:**

```text
Ich habe folgenden Python-Code, der einen Fehler wirft:

[Code hier einfügen]

Fehlermeldung:
[Fehlermeldung hier einfügen]

Was ist das Problem und wie kann ich es beheben?
```

---

## 💻 Teil 3: Live-Coding - Mini-App (10 Min.)

### Aufgabe: Notenverwaltung

**Anforderungen:**

- Noten eingeben (1-6)
- Durchschnitt berechnen
- Bestanden/Nicht bestanden (≥4.0)

### Schritt 1: Problem zerlegen

```text
1. Noten eingeben (Schleife)
2. Noten speichern (Liste)
3. Durchschnitt berechnen
4. Ergebnis ausgeben
```

### Schritt 2: Prompt formulieren

```text
Erstelle ein Python-Programm zur Notenverwaltung:

1. Benutzer kann mehrere Noten eingeben (1-6)
2. Eingabe mit 'fertig' beenden
3. Durchschnitt berechnen
4. Ausgabe: Durchschnitt und "Bestanden" (≥4.0) oder "Nicht bestanden"

Beispiel:
Note: 5
Note: 4
Note: 6
Note: fertig
Durchschnitt: 5.0
Ergebnis: Bestanden
```

### Schritt 3: Code generieren & verstehen

**Zeigen Sie den Studierenden:**

1. Prompt an KI senden
2. Generierten Code durchgehen
3. Jeden Teil erklären
4. Fragen beantworten

### Schritt 4: Testen

**Testfälle:**

- Normale Noten (4, 5, 6)
- Grenzfall (genau 4.0)
- Ungültige Eingabe ("abc")
- Keine Noten (direkt "fertig")

### Schritt 5: Verbessern

**Mögliche Verbesserungen:**

- Eingabe-Validierung
- Bessere Fehlermeldungen
- Formatierte Ausgabe

### Schritt 6: Git Commit

```bash
git add notenverwaltung.py
git commit -m "feat: Notenverwaltung mit Durchschnittsberechnung"
```

---

## 👥 Teil 4: Übung - Einfacher Taschenrechner (25 Min.)

### Aufgabe

Erstellen Sie einen Taschenrechner mit KI-Unterstützung.

### Anforderungen

**Grundfunktionen:**

- Addition (+)
- Subtraktion (-)
- Multiplikation (*)
- Division (/)

**Features:**

- Benutzer gibt zwei Zahlen ein
- Benutzer wählt Operation
- Ergebnis wird angezeigt
- Programm läuft in Schleife
- Beenden mit 'quit'

**Fehlerbehandlung:**

- Division durch Null abfangen
- Ungültige Eingaben behandeln
- Hilfreiche Fehlermeldungen

### Schritt-für-Schritt-Anleitung

#### Schritt 1: Prompt formulieren (5 Min.)

**Nutzen Sie das Prompt-Template:**

```text
[Aufgabe]: ...
[Kontext]: ...
[Anforderungen]: ...
[Beispiel]: ...
[Einschränkungen]: ...
```

#### Schritt 2: Code generieren (5 Min.)

- Prompt an KI senden
- Code erhalten
- Code durchlesen und verstehen

#### Schritt 3: Code testen (5 Min.)

**Testfälle:**

- [ ] Addition: 5 + 3 = 8
- [ ] Subtraktion: 10 - 4 = 6
- [ ] Multiplikation: 7 * 2 = 14
- [ ] Division: 15 / 3 = 5
- [ ] Division durch Null: 10 / 0 → Fehler
- [ ] Ungültige Eingabe: "abc" → Fehler
- [ ] Beenden: 'quit' → Programm endet

#### Schritt 4: Verbessern (5 Min.)

**Mögliche Verbesserungen:**

- Dezimalzahlen unterstützen
- Mehr Operationen (Potenz, Wurzel)
- Verlauf anzeigen
- Formatierte Ausgabe

#### Schritt 5: Git Commit (5 Min.)

```bash
# Repository erstellen (falls noch nicht vorhanden)
git init

# .gitignore erstellen
echo "__pycache__/" > .gitignore

# Dateien hinzufügen
git add taschenrechner.py .gitignore

# Commit erstellen
git commit -m "feat: Einfacher Taschenrechner mit Grundrechenarten"
```

### Checkliste

- [ ] Prompt formuliert
- [ ] Code generiert
- [ ] Code verstanden
- [ ] Alle Testfälle durchgeführt
- [ ] Code funktioniert
- [ ] Git Commit erstellt
- [ ] Verbesserungen dokumentiert

### Hilfestellung

**Bei Problemen:**

1. **Code funktioniert nicht:**
   - Fehlermeldung lesen
   - KI um Erklärung bitten
   - Schrittweise debuggen

2. **Prompt zu vage:**
   - Mehr Details hinzufügen
   - Beispiele geben
   - Anforderungen präzisieren

3. **Nicht sicher, wie weiter:**
   - Dozent fragen
   - Mit Partner diskutieren
   - KI um Vorschläge bitten

---

## 🎯 Zusammenfassung (5 Min.)

### Key Takeaways

**Der Workflow:**

```text
Verstehen → Zerlegen → Prompts → Code → Testen → Verbessern → Committen
```

**Code-Review Checkliste:**

- [ ] Funktionalität korrekt?
- [ ] Code lesbar?
- [ ] Fehler behandelt?
- [ ] Effizient genug?

**Debugging-Strategien:**

1. Print-Debugging
2. Fehlermeldungen lesen
3. Schrittweise testen
4. KI um Hilfe fragen

### Was haben wir erreicht?

**Modul 1 abgeschlossen!**

- ✅ Programmier-Mindset verstanden
- ✅ Entwicklungsumgebung eingerichtet
- ✅ Git-Grundlagen gelernt
- ✅ Effektives Prompting gemeistert
- ✅ Erste Programme erstellt

### Nächste Schritte

**Nachbearbeitung:**

- Prompt-Portfolio erstellen
- Persönliches Projekt aufsetzen
- Code-Review-Übung
- Reflexion schreiben

**Modul 2 Vorschau:**

- Python-Grundlagen vertiefen
- Datentypen und Strukturen
- Funktionen und Module
- Mehr komplexe Programme

### Fragen?

---

## 📎 Anhang für Dozenten

### Timing-Tipps

- **Live-Coding:** Nicht zu perfekt - Fehler zeigen ist gut!
- **Übung:** Genug Zeit lassen, aber Zeitlimit einhalten
- **Herumgehen:** Aktiv helfen und Fortschritt prüfen

### Häufige Probleme

#### Problem 1: Mein Code funktioniert nicht

- Gemeinsam Fehlermeldung anschauen
- Schritt für Schritt durchgehen
- Nicht die Lösung geben, sondern zum Denken anregen

#### Problem 2: Ich weiss nicht, wie ich anfangen soll

- Zurück zur Problemzerlegung
- Ersten kleinen Schritt identifizieren
- Prompt gemeinsam formulieren

#### Problem 3: Ist mein Code gut genug?

- Code-Review Checkliste durchgehen
- Funktioniert es? → Ja = gut genug für jetzt
- Verbesserungen können später kommen

### Materialien vorbereiten

- [ ] Live-Coding-Beispiel vorbereitet
- [ ] Taschenrechner-Musterlösung bereit
- [ ] Git-Repository-Vorlage
- [ ] Troubleshooting-Guide

### Erfolg messen

**Studierende sollten können:**

- [ ] Einfache Programme mit KI erstellen
- [ ] Code verstehen und erklären
- [ ] Grundlegende Fehler finden und beheben
- [ ] Git für Versionskontrolle nutzen

---

**Modul 1 abgeschlossen!** 🎉

**Weiter zur Nachbearbeitung:** [Nachbearbeitung](../03-nachbearbeitung/README.md)
