# Übung 4: Einfacher Taschenrechner

**Dauer:** 25 Minuten  
**Lektion:** 4  
**Ziel:** Erste vollständige Anwendung mit KI entwickeln

## 🎯 Lernziel

Den kompletten Entwicklungsworkflow durchlaufen: Von der Idee über den Prompt zum funktionierenden Programm.

## 📝 Aufgabenstellung

Erstellen Sie einen einfachen Taschenrechner mit KI-Unterstützung.

## ✨ Anforderungen

### Grundfunktionen

Der Taschenrechner soll folgende Operationen unterstützen:

- Addition (+)
- Subtraktion (-)
- Multiplikation (*)
- Division (/)

### Features

- Benutzer gibt zwei Zahlen ein
- Benutzer wählt Operation
- Ergebnis wird angezeigt
- Programm läuft in Schleife
- Beenden mit 'quit' oder 'q'

### Fehlerbehandlung

- Division durch Null abfangen
- Ungültige Eingaben behandeln
- Hilfreiche Fehlermeldungen ausgeben

## 🔄 Schritt-für-Schritt-Anleitung

### Schritt 1: Prompt formulieren (5 Min.)

Nutzen Sie das Prompt-Template aus Lektion 3:

```text
[Aufgabe]: 
Erstelle einen einfachen Taschenrechner in Python

[Kontext]: 
Ich möchte die Grundrechenarten üben und ein interaktives 
Programm erstellen

[Anforderungen]:
- [Hier Ihre Anforderungen auflisten]

[Beispiel]:
- [Hier Beispiel-Interaktion zeigen]

[Einschränkungen]:
- [Hier Einschränkungen nennen]
```

**Ihr vollständiger Prompt:**

```text
[Hier Ihren Prompt schreiben]
```

### Schritt 2: Code generieren (5 Min.)

1. Öffnen Sie ChatGPT oder Claude
2. Geben Sie Ihren Prompt ein
3. Lassen Sie den Code generieren
4. Kopieren Sie den Code in eine neue Datei `taschenrechner.py`

### Schritt 3: Code verstehen (5 Min.)

**Lesen Sie den Code durch und beantworten Sie:**

- Wie werden die Eingaben eingelesen?
- Wie wird die Operation ausgewählt?
- Wie wird das Ergebnis berechnet?
- Wie werden Fehler behandelt?

**Wenn etwas unklar ist:**

Fragen Sie die KI: "Erkläre mir diesen Teil des Codes: [Code-Teil]"

### Schritt 4: Code testen (5 Min.)

Führen Sie folgende Tests durch:

#### Testfall 1: Addition

```text
Eingabe: 5 + 3
Erwartete Ausgabe: 8
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

#### Testfall 2: Subtraktion

```text
Eingabe: 10 - 4
Erwartete Ausgabe: 6
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

#### Testfall 3: Multiplikation

```text
Eingabe: 7 * 2
Erwartete Ausgabe: 14
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

#### Testfall 4: Division

```text
Eingabe: 15 / 3
Erwartete Ausgabe: 5
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

#### Testfall 5: Division durch Null

```text
Eingabe: 10 / 0
Erwartete Ausgabe: Fehlermeldung (kein Crash!)
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

#### Testfall 6: Ungültige Eingabe

```text
Eingabe: abc
Erwartete Ausgabe: Fehlermeldung (kein Crash!)
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

#### Testfall 7: Beenden

```text
Eingabe: quit
Erwartete Ausgabe: Programm endet
Tatsächliche Ausgabe: ___
Status: [ ] Bestanden [ ] Fehlgeschlagen
```

### Schritt 5: Git Commit (5 Min.)

```bash
# Falls noch kein Repository: initialisieren
git init

# .gitignore erstellen (falls noch nicht vorhanden)
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore

# Dateien hinzufügen
git add taschenrechner.py .gitignore

# Commit erstellen
git commit -m "feat: Einfacher Taschenrechner mit Grundrechenarten"

# Prüfen
git log --oneline
```

## ✅ Checkliste

- [ ] Prompt formuliert
- [ ] Code generiert
- [ ] Code verstanden
- [ ] Alle 7 Testfälle durchgeführt
- [ ] Code funktioniert korrekt
- [ ] Git Commit erstellt

## 🚀 Bonus-Aufgaben

Falls Sie früher fertig sind:

### Bonus 1: Dezimalzahlen

Erweitern Sie den Taschenrechner für Dezimalzahlen:

```text
Eingabe: 5.5 + 2.3
Ausgabe: 7.8
```

### Bonus 2: Mehr Operationen

Fügen Sie hinzu:

- Potenz (**)
- Modulo (%)
- Ganzzahlige Division (//)

### Bonus 3: Verlauf

Speichern Sie die letzten 5 Berechnungen und zeigen Sie sie an.

### Bonus 4: Formatierung

Verbessern Sie die Ausgabe:

```text
================================
    TASCHENRECHNER
================================
Erste Zahl: 5
Operation (+, -, *, /): +
Zweite Zahl: 3
--------------------------------
Ergebnis: 5 + 3 = 8
================================
```

## 🆘 Troubleshooting

### Problem: Code funktioniert nicht

**Lösung:**

1. Fehlermeldung genau lesen
2. KI fragen: "Ich habe folgenden Fehler: [Fehlermeldung]. Was ist das Problem?"
3. Schrittweise debuggen mit `print()`

### Problem: Prompt zu vage

**Lösung:**

1. Mehr Details hinzufügen
2. Beispiele geben
3. Anforderungen präzisieren
4. Erneut generieren lassen

### Problem: Division durch Null nicht abgefangen

**Lösung:**

Fragen Sie die KI:

```text
Wie kann ich in meinem Taschenrechner-Code die Division 
durch Null abfangen und eine Fehlermeldung ausgeben?
```

## 🎓 Reflexion

**Nach der Übung:**

1. Was hat gut funktioniert?
2. Wo gab es Schwierigkeiten?
3. Was haben Sie über Prompting gelernt?
4. Was haben Sie über Python gelernt?

**Notizen:**

```text
[Hier Ihre Gedanken notieren]
```

## 📎 Dateien

- `taschenrechner.py` - Ihr Hauptprogramm
- `loesung-beispiel.py` - Musterlösung (siehe separate Datei)

---

**Zurück zur Übungsübersicht:** [Übungen README](../README.md)
