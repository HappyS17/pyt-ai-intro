# Aufgabe 3: Code-Review-Übung

**Zeitaufwand:** 45 Minuten  
**Abgabe:** Vor Modul 2  
**Punkte:** 20% der Nachbearbeitung

## 🎯 Ziel

Analysieren Sie bereitgestellten Code und dokumentieren Sie Ihre Erkenntnisse.

## 📋 Aufgabenstellung

Führen Sie ein Code-Review für das folgende Programm durch und dokumentieren Sie:

1. Was der Code macht
2. Was gut ist
3. Was verbessert werden könnte
4. Ihre Verbesserungsvorschläge

## 💻 Zu reviewender Code

```python
# Programm zur Verwaltung einer Bücherliste

b = []

while True:
    print("1. Buch hinzufügen")
    print("2. Alle Bücher anzeigen")
    print("3. Beenden")
    
    c = input("Wahl: ")
    
    if c == "1":
        t = input("Titel: ")
        a = input("Autor: ")
        b.append({"t": t, "a": a})
        print("OK")
    elif c == "2":
        for x in b:
            print(x["t"] + " von " + x["a"])
    elif c == "3":
        break
```

## 📝 Review-Template

Nutzen Sie folgendes Template für Ihr Review:

```markdown
# Code-Review: Bücherliste

**Reviewer:** [Ihr Name]  
**Datum:** [Datum]

## 1. Funktionalität

### Was macht der Code?

[Beschreiben Sie in eigenen Worten, was das Programm tut]

### Funktioniert der Code?

- [ ] Ja, ohne Probleme
- [ ] Ja, aber mit Einschränkungen
- [ ] Nein, es gibt Fehler

[Falls Probleme: Beschreiben Sie diese]

## 2. Code-Qualität

### Was ist gut?

[Listen Sie positive Aspekte auf]

1. ...
2. ...
3. ...

### Was könnte verbessert werden?

[Listen Sie Verbesserungspotenzial auf]

1. ...
2. ...
3. ...

## 3. Detaillierte Analyse

### Lesbarkeit

**Bewertung:** ⭐⭐⭐☆☆ (3/5)

**Begründung:**
[Ihre Analyse zur Lesbarkeit]

**Verbesserungsvorschläge:**
- ...
- ...

### Variablennamen

**Bewertung:** ⭐⭐☆☆☆ (2/5)

**Begründung:**
[Ihre Analyse zu Variablennamen]

**Verbesserungsvorschläge:**
- ...
- ...

### Fehlerbehandlung

**Bewertung:** ⭐☆☆☆☆ (1/5)

**Begründung:**
[Ihre Analyse zur Fehlerbehandlung]

**Verbesserungsvorschläge:**
- ...
- ...

### Dokumentation

**Bewertung:** ⭐☆☆☆☆ (1/5)

**Begründung:**
[Ihre Analyse zur Dokumentation]

**Verbesserungsvorschläge:**
- ...
- ...

### Code-Struktur

**Bewertung:** ⭐⭐⭐☆☆ (3/5)

**Begründung:**
[Ihre Analyse zur Code-Struktur]

**Verbesserungsvorschläge:**
- ...
- ...

## 4. Verbesserter Code

### Meine Verbesserungen

[Beschreiben Sie, was Sie verbessert haben]

### Verbesserter Code

```python
# Hier Ihren verbesserten Code einfügen
```

### Erklärung der Änderungen

1. **Änderung 1:** [Was und warum]
2. **Änderung 2:** [Was und warum]
3. **Änderung 3:** [Was und warum]

## 5. Zusammenfassung

### Wichtigste Erkenntnisse

[3-5 wichtigste Punkte aus dem Review]

### Was habe ich gelernt?

[Ihre persönlichen Lernerkenntnisse]
```

## 💡 Review-Checkliste

Prüfen Sie folgende Aspekte:

### Funktionalität

- [ ] Macht der Code, was er soll?
- [ ] Gibt es Bugs?
- [ ] Funktionieren alle Features?
- [ ] Werden Edge Cases behandelt?

### Lesbarkeit

- [ ] Sind Variablennamen aussagekräftig?
- [ ] Ist der Code gut strukturiert?
- [ ] Gibt es Kommentare?
- [ ] Ist die Einrückung korrekt?

### Fehlerbehandlung

- [ ] Werden Fehler abgefangen?
- [ ] Sind Fehlermeldungen hilfreich?
- [ ] Stürzt das Programm ab?
- [ ] Wird Benutzereingabe validiert?

### Best Practices

- [ ] Folgt der Code Python-Konventionen?
- [ ] Sind Funktionen sinnvoll eingesetzt?
- [ ] Gibt es Code-Duplikation?
- [ ] Ist der Code wartbar?

## 🔍 Hilfreiche Fragen

### Zur Funktionalität

- Was passiert bei leerer Bücherliste?
- Was passiert bei ungültiger Eingabe?
- Kann man Bücher löschen?
- Kann man nach Büchern suchen?

### Zur Code-Qualität

- Was bedeuten die Variablennamen `b`, `c`, `t`, `a`, `x`?
- Warum gibt es keine Funktionen?
- Wo sind die Kommentare?
- Wie könnte man den Code strukturieren?

### Zur Fehlerbehandlung

- Was passiert bei Eingabe von "4"?
- Was passiert bei Eingabe von "abc"?
- Wird die Eingabe validiert?

## ✅ Bewertungskriterien

### Vollständigkeit (30%)

- [ ] Alle Abschnitte ausgefüllt
- [ ] Detaillierte Analyse
- [ ] Verbesserter Code vorhanden

### Qualität der Analyse (40%)

- [ ] Probleme erkannt
- [ ] Begründungen nachvollziehbar
- [ ] Konkrete Verbesserungsvorschläge

### Verbesserter Code (20%)

- [ ] Code funktioniert
- [ ] Verbesserungen umgesetzt
- [ ] Änderungen erklärt

### Reflexion (10%)

- [ ] Persönliche Erkenntnisse
- [ ] Lerneffekt dokumentiert

## 💡 Tipps

### Tipp 1: Code ausführen

Führen Sie den Code aus und testen Sie ihn gründlich.

### Tipp 2: Systematisch vorgehen

Gehen Sie die Checkliste Punkt für Punkt durch.

### Tipp 3: Konkret sein

Statt "Code ist schlecht" → "Variablennamen sind nicht aussagekräftig"

### Tipp 4: Konstruktiv bleiben

Fokus auf Verbesserung, nicht auf Kritik.

## 📤 Abgabe

### Format

- **Markdown-Datei:** `code-review.md`
- **Oder PDF:** `code-review.pdf`

### Inhalt

- Vollständiges Review nach Template
- Verbesserter Code
- Erklärung der Änderungen

---

**Zurück zur Nachbearbeitung:** [Nachbearbeitung README](./README.md)
