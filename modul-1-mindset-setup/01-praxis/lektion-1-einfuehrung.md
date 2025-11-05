# Lektion 1: Einführung & Mindset

**Dauer:** 50 Minuten  
**Ziel:** Verstehen, was Programmieren wirklich bedeutet und wie KI dabei hilft

## 📋 Ablauf

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-10 Min. | Begrüssung & Kursübersicht | Vortrag |
| 10-25 Min. | Was ist Programmieren? | Vortrag + Diskussion |
| 25-35 Min. | Live-Demo: Problem mit/ohne KI | Live-Coding |
| 35-50 Min. | Übung: Einkaufsliste durchdenken | Gruppenarbeit |

---

## 🎯 Lernziele

Nach dieser Lektion können die Studierenden:
- Erklären, was Programmieren im Kern bedeutet
- Den Unterschied zwischen traditionellem und KI-gestütztem Programmieren beschreiben
- Ein Problem in kleinere Teilprobleme zerlegen (Problemdekomposition)

---

## 📚 Teil 1: Begrüssung & Kursübersicht (10 Min.)

### Willkommen

**Vorstellung:**
- Dozent vorstellen
- Kurze Vorstellungsrunde (Name, Hintergrund, Motivation)

**Kursübersicht:**
- 5 Module über X Wochen
- Fokus auf **praktisches Lernen** mit KI-Unterstützung
- Ziel: Eigenständig Software entwickeln können

**Erwartungen klären:**
- Was erwarten die Studierenden?
- Was wird der Kurs bieten?
- Was wird der Kurs NICHT bieten?

**Organisatorisches:**
- Präsenzzeiten, Pausen
- Nachbearbeitung & Abgaben
- Kommunikationskanäle (Forum, E-Mail)
- Bewertungskriterien

---

## 💡 Teil 2: Was ist Programmieren? (15 Min.)

### Kernbotschaft

> **Programmieren ist Problemlösung, nicht Syntax-Memorierung!**

### Die 4 Säulen des Programmierens

#### 1. Problemdekomposition
**Was ist das?**
- Grosse Probleme in kleinere, lösbare Teilprobleme zerlegen
- Jedes Teilproblem einzeln angehen

**Beispiel: "Kaffee kochen"**
```
Grosses Problem: Kaffee kochen

Teilprobleme:
1. Wasser holen
2. Wasser in Maschine füllen
3. Kaffeepulver einfüllen
4. Maschine einschalten
5. Warten
6. Kaffee einschenken
```

**Diskussion:** Warum ist das wichtig?

#### 2. Algorithmisches Denken
**Was ist das?**
- Schritt-für-Schritt-Anweisungen erstellen
- Klare, eindeutige Abfolge
- Wiederholbare Prozesse

**Beispiel: "Route zur Uni"**
```
1. Aus der Haustür gehen
2. Nach links abbiegen
3. 200m geradeaus
4. An der Ampel rechts
5. Bis zum Haupteingang
```

**Diskussion:** Was passiert, wenn Schritte fehlen oder unklar sind?

#### 3. Abstraktion
**Was ist das?**
- Unwichtige Details weglassen
- Auf das Wesentliche fokussieren
- Muster erkennen

**Beispiel: "Auto fahren"**
- Sie müssen nicht wissen, wie der Motor funktioniert
- Sie müssen nur wissen: Gas, Bremse, Lenkrad

#### 4. Musterkennung
**Was ist das?**
- Ähnliche Probleme erkennen
- Bekannte Lösungen wiederverwenden
- Nicht jedes Mal von vorne anfangen

**Beispiel:**
- "Summe berechnen" funktioniert für Zahlen, Preise, Punkte, etc.
- Das Muster ist immer gleich: Addiere alle Werte

### Programmieren ≠ Syntax auswendig lernen

**Traditioneller Ansatz:**
- ❌ Syntax-Regeln auswendig lernen
- ❌ Stundenlang Dokumentation lesen
- ❌ Jede Funktion kennen

**Moderner Ansatz mit KI:**
- ✅ Problem verstehen
- ✅ Lösung konzipieren
- ✅ KI für Syntax-Details nutzen
- ✅ Code verstehen und anpassen

### Die Rolle von KI

**KI als Werkzeug:**
- 🤖 Generiert Code basierend auf Beschreibungen
- 🤖 Erklärt komplexen Code
- 🤖 Schlägt Verbesserungen vor
- 🤖 Hilft beim Debugging

**Was KI NICHT ersetzt:**
- 🧠 Problemverständnis
- 🧠 Kreative Lösungsansätze
- 🧠 Entscheidungen treffen
- 🧠 Code-Qualität bewerten

**Diskussion:** Welche Bedenken haben die Studierenden?

---

## 💻 Teil 3: Live-Demo (10 Min.)

### Problem: "Zahlen filtern"

**Aufgabe:** Aus einer Liste von Zahlen nur die geraden Zahlen behalten.

#### Ohne KI (traditionell)

**Schritt 1: Problem verstehen**
- Was sind gerade Zahlen? (Teilbar durch 2)
- Was ist eine Liste?
- Wie iteriere ich über eine Liste?

**Schritt 2: Syntax nachschlagen**
- Wie schreibt man eine Schleife in Python?
- Wie prüft man auf Teilbarkeit?
- Wie fügt man Elemente zu einer neuen Liste hinzu?

**Schritt 3: Code schreiben**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
```

**Zeit:** ~15-30 Minuten für Anfänger

#### Mit KI

**Schritt 1: Problem beschreiben**

**Prompt:**
```text
Ich habe eine Liste von Zahlen. Erstelle ein Python-Programm, 
das nur die geraden Zahlen behält und ausgibt.
```

**Schritt 2: Code erhalten & verstehen**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

**Schritt 3: Erklärung einholen**

**Prompt:**
```text
Erkläre mir diesen Code Zeile für Zeile.
```

**Zeit:** ~2-5 Minuten

### Diskussion

**Fragen an die Studierenden:**
- Was sind die Unterschiede?
- Was ist besser/schlechter?
- Wann würden Sie welchen Ansatz wählen?
- Was müssen Sie trotzdem verstehen?

**Wichtige Erkenntnisse:**
- ✅ KI beschleunigt die Entwicklung
- ✅ Sie müssen das Problem trotzdem verstehen
- ✅ Sie müssen den generierten Code verstehen
- ✅ Sie müssen beurteilen können, ob der Code gut ist

---

## 👥 Teil 4: Übung - Einkaufsliste durchdenken (15 Min.)

### Aufgabe

**Szenario:** Sie möchten ein Programm schreiben, das eine Einkaufsliste verwaltet.

**Funktionen:**
- Artikel hinzufügen
- Artikel entfernen
- Alle Artikel anzeigen
- Prüfen, ob ein Artikel auf der Liste ist

### Arbeitsauftrag

**Einzelarbeit (5 Min.):**
1. Zerlegen Sie das Problem in Teilprobleme
2. Überlegen Sie, welche Daten Sie speichern müssen
3. Welche Schritte sind nötig für jede Funktion?

**Gruppenarbeit (5 Min.):**
- Bilden Sie 2er-Gruppen
- Vergleichen Sie Ihre Ansätze
- Diskutieren Sie Unterschiede

**Plenum (5 Min.):**
- 2-3 Gruppen präsentieren kurz (1-2 Min.)
- Gemeinsame Diskussion

### Leitfragen

1. **Datenstruktur:**
   - Wie speichern Sie die Artikel?
   - Brauchen Sie nur Namen oder auch Mengen?

2. **Artikel hinzufügen:**
   - Was passiert, wenn der Artikel schon existiert?
   - Wie vermeiden Sie Duplikate?

3. **Artikel entfernen:**
   - Was passiert, wenn der Artikel nicht existiert?
   - Fehlermeldung oder ignorieren?

4. **Artikel anzeigen:**
   - In welcher Reihenfolge?
   - Wie formatieren Sie die Ausgabe?

### Musterlösung (nicht zeigen, nur für Dozent)

**Problemdekomposition:**
```
1. Datenstruktur wählen (Liste)
2. Funktion: Artikel hinzufügen
   - Prüfen, ob schon vorhanden
   - Wenn nicht: hinzufügen
3. Funktion: Artikel entfernen
   - Prüfen, ob vorhanden
   - Wenn ja: entfernen
4. Funktion: Alle anzeigen
   - Über Liste iterieren
   - Jeden Artikel ausgeben
5. Funktion: Artikel suchen
   - In Liste suchen
   - Ja/Nein zurückgeben
```

---

## 🎯 Zusammenfassung (5 Min.)

### Key Takeaways

1. **Programmieren = Problemlösung**
   - Nicht Syntax auswendig lernen
   - Probleme verstehen und zerlegen

2. **Die 4 Säulen:**
   - Problemdekomposition
   - Algorithmisches Denken
   - Abstraktion
   - Musterkennung

3. **KI als Werkzeug:**
   - Beschleunigt Entwicklung
   - Ersetzt nicht das Denken
   - Sie müssen Code verstehen können

4. **Nächste Schritte:**
   - Entwicklungsumgebung einrichten
   - Git-Grundlagen lernen
   - Erste Programme mit KI schreiben

### Hausaufgabe

Falls noch nicht erledigt:
- ✅ Vorbereitung abschliessen (Installation, Leseauftrag)
- ✅ Erste Schritte mit KI durchführen

### Fragen?

Zeit für offene Fragen und Diskussion.

---

## 📎 Anhang für Dozenten

### Timing-Tipps

- **Flexibel bleiben:** Diskussionen können länger dauern
- **Übung kürzen:** Falls Zeit knapp wird, Gruppenarbeit weglassen
- **Puffer einplanen:** Technische Probleme einkalkulieren

### Häufige Fragen

**"Muss ich dann gar keine Syntax mehr lernen?"**
- Nein, Sie werden Syntax lernen, aber durch Anwendung, nicht durch Auswendiglernen
- KI hilft beim Nachschlagen, aber Sie müssen verstehen, was der Code macht

**"Ist das nicht Schummeln?"**
- Nein, KI ist ein Werkzeug wie Google oder Stack Overflow
- Wichtig ist, dass Sie den Code verstehen und anpassen können
- In der Praxis nutzen alle Entwickler solche Tools

**"Was, wenn die KI Fehler macht?"**
- KI macht Fehler, deshalb müssen Sie den Code verstehen
- Sie lernen, Code zu überprüfen und zu testen
- Das ist Teil des Lernprozesses

### Materialien vorbereiten

- [ ] Beamer/Projektor testen
- [ ] Live-Coding-Umgebung vorbereiten
- [ ] Beispiel-Code bereithalten
- [ ] Flipchart/Whiteboard für Diskussion
- [ ] Übungsblätter ausdrucken (optional)

---

**Nächste Lektion:** [Lektion 2: Setup-Vertiefung & Git Basics](./lektion-2-setup-git.md)
