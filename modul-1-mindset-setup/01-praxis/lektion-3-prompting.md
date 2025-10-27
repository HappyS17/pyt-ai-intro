# Lektion 3: Effektives Prompting

**Dauer:** 50 Minuten  
**Ziel:** Lernen, wie man effektive Prompts für KI-Coding-Assistenten formuliert

## 📋 Ablauf

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-5 Min. | Recap & Einstieg | Diskussion |
| 5-20 Min. | Prompt Engineering Grundlagen | Vortrag |
| 20-35 Min. | Live-Demo: Prompt-Iteration | Live-Coding |
| 35-50 Min. | Übung: Prompting-Challenge | Hands-on |

---

## 🎯 Lernziele

Nach dieser Lektion können die Studierenden:

- Effektive Prompts für Code-Generierung formulieren
- Kontext richtig bereitstellen
- Prompts iterativ verbessern
- Schlechte von guten Prompts unterscheiden

---

## 🔄 Teil 1: Recap & Einstieg (5 Min.)

### Quick Check

**Fragen an die Studierenden:**

- Was haben wir in den letzten Lektionen gelernt?
- Wer hat bereits mit KI-Tools experimentiert?
- Welche Erfahrungen habt ihr gemacht?

### Heute: Prompting meistern

**Kernbotschaft:**

> Ein guter Prompt ist der Schlüssel zu gutem Code!

**Was wir lernen:**

- Wie formuliere ich klare Anfragen?
- Wie gebe ich genug Kontext?
- Wie verbessere ich Prompts iterativ?

---

## 📚 Teil 2: Prompt Engineering Grundlagen (15 Min.)

### Was ist ein Prompt?

**Definition:**

Ein Prompt ist die Anweisung oder Frage, die Sie an eine KI stellen.

**Beispiel:**

```text
Schlechter Prompt: "Mach ein Programm"
Guter Prompt: "Erstelle ein Python-Programm, das zwei Zahlen vom 
Benutzer einliest und deren Summe berechnet und ausgibt."
```

### Die 5 Elemente eines guten Prompts

#### 1. Klarheit

**Was bedeutet das?**

- Eindeutige, präzise Formulierung
- Keine Mehrdeutigkeiten
- Konkrete Anforderungen

**Beispiel:**

```text
❌ Unklar: "Sortiere die Liste"
✅ Klar: "Sortiere die Liste von Zahlen aufsteigend"
```

#### 2. Kontext

**Was bedeutet das?**

- Hintergrundinformationen bereitstellen
- Verwendungszweck erklären
- Einschränkungen nennen

**Beispiel:**

```text
❌ Ohne Kontext: "Erstelle eine Funktion zum Validieren"
✅ Mit Kontext: "Erstelle eine Python-Funktion, die eine E-Mail-Adresse 
validiert. Die Funktion soll True zurückgeben, wenn die E-Mail gültig 
ist (enthält @ und .), sonst False."
```

#### 3. Spezifität

**Was bedeutet das?**

- Genaue Anforderungen
- Erwartete Ein- und Ausgaben
- Gewünschtes Format

**Beispiel:**

```text
❌ Unspezifisch: "Lies eine Datei"
✅ Spezifisch: "Lies eine CSV-Datei namens 'daten.csv' ein und gib 
die erste Spalte als Liste zurück"
```

#### 4. Beispiele

**Was bedeutet das?**

- Konkrete Beispiele für Ein- und Ausgaben
- Zeigt erwartetes Verhalten
- Reduziert Missverständnisse

**Beispiel:**

```text
Erstelle eine Funktion, die einen String umdreht.

Beispiel:
Eingabe: "Hallo"
Ausgabe: "ollaH"
```

#### 5. Einschränkungen

**Was bedeutet das?**

- Was NICHT gemacht werden soll
- Technische Einschränkungen
- Stilrichtlinien

**Beispiel:**

```text
Erstelle ein Programm zur Passwort-Generierung.
- Verwende KEINE externen Bibliotheken
- Passwort soll 12 Zeichen lang sein
- Muss Gross- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten
```

### Prompt-Template

**Grundstruktur:**

```text
[Aufgabe]: Was soll gemacht werden?
[Kontext]: Warum? Wofür?
[Anforderungen]: Spezifische Details
[Beispiel]: Ein- und Ausgabe
[Einschränkungen]: Was zu beachten ist
```

**Konkretes Beispiel:**

```text
[Aufgabe]: Erstelle eine Python-Funktion zur Berechnung des Durchschnitts

[Kontext]: Ich möchte die Durchschnittsnote meiner Prüfungen berechnen

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

### Häufige Fehler

#### Fehler 1: Zu vage

```text
❌ "Schreib mir was mit Daten"
✅ "Erstelle ein Python-Programm, das eine CSV-Datei einliest und 
die Anzahl der Zeilen ausgibt"
```

#### Fehler 2: Zu komplex

```text
❌ "Erstelle eine vollständige Webanwendung mit Login, Datenbank, 
API, Frontend und Backend"
✅ "Erstelle eine einfache Flask-Route, die 'Hello World' zurückgibt"
```

Tipp: Grosse Aufgaben in kleine Schritte zerlegen!

#### Fehler 3: Fehlender Kontext

```text
❌ "Wie sortiere ich das?"
✅ "Wie sortiere ich eine Liste von Dictionaries in Python nach dem 
Wert des Keys 'name'?"
```

#### Fehler 4: Keine Beispiele

```text
❌ "Formatiere den String"
✅ "Formatiere den String so, dass der erste Buchstabe gross ist.
Beispiel: 'hallo' → 'Hallo'"
```

---

## 💻 Teil 3: Live-Demo - Prompt-Iteration (15 Min.)

### Aufgabe: Zahlenraten-Spiel

**Ziel:** Ein Programm erstellen, bei dem der Computer eine Zahl zwischen 1 und 100 wählt und der Benutzer raten muss.

### Iteration 1: Schlechter Prompt

**Prompt:**

```text
Mach ein Ratespiel
```

**Problem:** Viel zu vage!

**Ergebnis:** KI weiss nicht, was gemeint ist

### Iteration 2: Besser, aber unvollständig

**Prompt:**

```text
Erstelle ein Zahlenraten-Spiel in Python
```

**Problem:** Fehlen wichtige Details

**Ergebnis:** KI erstellt etwas, aber nicht das, was wir wollen

### Iteration 3: Gut strukturiert

**Prompt:**

```text
Erstelle ein Zahlenraten-Spiel in Python mit folgenden Anforderungen:

1. Computer wählt zufällig eine Zahl zwischen 1 und 100
2. Benutzer kann raten
3. Nach jedem Versuch: Hinweis ob zu hoch oder zu niedrig
4. Bei richtigem Raten: Glückwunsch und Anzahl Versuche anzeigen
5. Benutzer kann jederzeit mit 'quit' aufhören

Beispiel-Ablauf:
Computer: "Ich habe eine Zahl zwischen 1 und 100 gewählt."
Benutzer: 50
Computer: "Zu niedrig!"
Benutzer: 75
Computer: "Zu hoch!"
Benutzer: 60
Computer: "Richtig! Du hast 3 Versuche gebraucht."
```

**Ergebnis:** Genau das, was wir wollen!

### Live-Coding

**Zeigen Sie den Studierenden:**

1. Ersten Prompt eingeben
2. Code generieren lassen
3. Code testen
4. Probleme identifizieren
5. Prompt verbessern
6. Erneut generieren

**Wichtige Erkenntnisse:**

- Iteration ist normal und erwünscht
- Jede Verbesserung bringt besseren Code
- Testen ist wichtig

---

## 👥 Teil 4: Übung - Prompting-Challenge (15 Min.)

### Aufgabe

Formulieren Sie Prompts für 3 verschiedene Programme. Vergleichen Sie dann mit Ihrem Partner.

### Challenge 1: Einkaufsliste

**Anforderungen:**

- Artikel hinzufügen
- Artikel entfernen
- Alle Artikel anzeigen
- Programm läuft in Schleife bis Benutzer 'quit' eingibt

**Ihre Aufgabe:** Schreiben Sie einen vollständigen Prompt

**Zeit:** 5 Minuten

### Challenge 2: Temperatur-Umrechner

**Anforderungen:**

- Celsius in Fahrenheit umrechnen
- Fahrenheit in Celsius umrechnen
- Benutzer wählt Richtung
- Eingabe validieren (nur Zahlen)

**Ihre Aufgabe:** Schreiben Sie einen vollständigen Prompt

**Zeit:** 5 Minuten

### Challenge 3: Wort-Zähler

**Anforderungen:**

- Text vom Benutzer einlesen
- Anzahl Wörter zählen
- Anzahl Zeichen zählen (mit und ohne Leerzeichen)
- Längstes Wort finden

**Ihre Aufgabe:** Schreiben Sie einen vollständigen Prompt

**Zeit:** 5 Minuten

### Bewertungskriterien

Ihr Prompt sollte enthalten:

- [ ] Klare Aufgabenbeschreibung
- [ ] Kontext/Zweck
- [ ] Spezifische Anforderungen
- [ ] Beispiel Ein-/Ausgabe
- [ ] Einschränkungen (falls nötig)

### Partner-Review

**Tauschen Sie Ihre Prompts aus:**

1. Lesen Sie den Prompt Ihres Partners
2. Würden Sie verstehen, was zu tun ist?
3. Fehlt etwas Wichtiges?
4. Geben Sie konstruktives Feedback

---

## 🎯 Zusammenfassung (5 Min.)

### Key Takeaways

**Die 5 Elemente:**

1. **Klarheit** - Eindeutig formulieren
2. **Kontext** - Hintergrund geben
3. **Spezifität** - Genau beschreiben
4. **Beispiele** - Ein-/Ausgabe zeigen
5. **Einschränkungen** - Grenzen setzen

**Der Prozess:**

```text
Prompt schreiben → Code generieren → Testen → 
Probleme finden → Prompt verbessern → Wiederholen
```

**Best Practices:**

- Starten Sie einfach, verfeinern Sie iterativ
- Testen Sie den generierten Code immer
- Lernen Sie aus erfolgreichen Prompts
- Bauen Sie eine Prompt-Bibliothek auf

### Prompt-Cheatsheet

**Template:**

```text
Erstelle [Was] in [Sprache/Framework].

Kontext: [Warum/Wofür]

Anforderungen:
- [Anforderung 1]
- [Anforderung 2]
- [Anforderung 3]

Beispiel:
Eingabe: [Beispiel]
Ausgabe: [Beispiel]

Einschränkungen:
- [Was zu beachten ist]
```

### Hausaufgabe

**Prompt-Portfolio erstellen:**

- Sammeln Sie 10 effektive Prompts
- Dokumentieren Sie, was funktioniert hat
- Notieren Sie Verbesserungen

Mehr Details in der Nachbearbeitung!

### Fragen?

---

## 📎 Anhang für Dozenten

### Timing-Tipps

- **Live-Demo:** Nicht zu lange - max. 15 Min.
- **Übung:** Herumgehen und Prompts anschauen
- **Partner-Review:** Aktiv moderieren

### Häufige Fragen

#### Frage 1: Wie lang sollte ein Prompt sein?

- So lang wie nötig, so kurz wie möglich
- Lieber zu viel Information als zu wenig
- Bei komplexen Aufgaben: Schrittweise vorgehen

#### Frage 2: Kann ich Prompts wiederverwenden?

- Ja! Bauen Sie eine Bibliothek auf
- Passen Sie sie an neue Situationen an
- Teilen Sie gute Prompts mit anderen

#### Frage 3: Was, wenn die KI nicht versteht?

- Prompt umformulieren
- Mehr Kontext geben
- In kleinere Schritte aufteilen
- Beispiele hinzufügen

### Materialien vorbereiten

- [ ] Prompt-Template als Handout
- [ ] Beispiel-Prompts bereithalten
- [ ] Challenge-Aufgaben vorbereiten
- [ ] Musterlösungen haben

### Backup-Plan

Falls Zeit knapp:

- Challenge auf 2 Aufgaben reduzieren
- Partner-Review weglassen
- Als Hausaufgabe geben

---

**Nächste Lektion:** [Lektion 4: Von der Idee zur App](./lektion-4-idee-zur-app.md)
