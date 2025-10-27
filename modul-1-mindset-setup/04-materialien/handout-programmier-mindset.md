# Handout: Programmier-Mindset

Grundlegende Konzepte für erfolgreiches Programmieren.

## 🎯 Kernbotschaft

> **Programmieren ist Problemlösung, nicht Syntax-Memorierung!**

## 🏛️ Die 4 Säulen des Programmierens

### 1. Problemdekomposition

**Was ist das?**

Grosse Probleme in kleinere, lösbare Teilprobleme zerlegen.

**Warum wichtig?**

- Komplexe Aufgaben werden handhabbar
- Jedes Teilproblem kann einzeln gelöst werden
- Einfacher zu testen und zu debuggen

#### Beispiel: Kaffee kochen

```text
Grosses Problem: Kaffee kochen

Teilprobleme:
1. Wasser holen
2. Wasser in Maschine füllen
3. Kaffeepulver einfüllen
4. Maschine einschalten
5. Warten
6. Kaffee einschenken
```

#### Anwendung beim Programmieren

```text
Problem: Einkaufsliste verwalten

Teilprobleme:
1. Datenstruktur wählen (Liste/Dictionary)
2. Funktion: Artikel hinzufügen
3. Funktion: Artikel entfernen
4. Funktion: Artikel anzeigen
5. Funktion: Artikel suchen
6. Hauptprogramm: Menü und Schleife
```

### 2. Algorithmisches Denken

**Was ist das?**

Schritt-für-Schritt-Anweisungen erstellen, die klar und eindeutig sind.

**Warum wichtig?**

- Computer brauchen präzise Anweisungen
- Keine Annahmen oder Interpretationen
- Wiederholbare Prozesse

#### Beispiel: Route zur Uni

```text
1. Aus der Haustür gehen
2. Nach links abbiegen
3. 200m geradeaus
4. An der Ampel rechts
5. Bis zum Haupteingang
```

#### Anwendung beim Programmieren: Algorithmus

```text
Algorithmus: Durchschnitt berechnen

1. Liste von Zahlen einlesen
2. Summe = 0 setzen
3. Für jede Zahl in der Liste:
   - Summe = Summe + Zahl
4. Anzahl = Länge der Liste
5. Durchschnitt = Summe / Anzahl
6. Durchschnitt ausgeben
```

### 3. Abstraktion

**Was ist das?**

Unwichtige Details weglassen und auf das Wesentliche fokussieren.

**Warum wichtig?**

- Reduziert Komplexität
- Ermöglicht Wiederverwendung
- Macht Code verständlicher

#### Beispiel: Auto fahren

```text
Abstraktion: "Auto fahren"
- Sie müssen nicht wissen, wie der Motor funktioniert
- Sie müssen nur wissen: Gas, Bremse, Lenkrad

Details (versteckt):
- Verbrennungsprozess
- Getriebe
- Elektronik
```

**Anwendung beim Programmieren:**

```python
# Abstraktion: Funktion verwenden
result = calculate_average([5, 4, 6, 5])

# Details (in der Funktion versteckt):
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
```

### 4. Musterkennung

**Was ist das?**

Ähnliche Probleme erkennen und bekannte Lösungen wiederverwenden.

**Warum wichtig?**

- Spart Zeit
- Bewährte Lösungen nutzen
- Nicht jedes Mal von vorne anfangen

#### Beispiel: Summe berechnen

```text
Muster: "Summe berechnen"
- Funktioniert für: Zahlen, Preise, Punkte, Zeiten
- Das Muster ist immer gleich: Addiere alle Werte

Anwendungen:
- Gesamtpreis im Warenkorb
- Gesamtpunkte in einem Spiel
- Gesamtzeit für Aufgaben
```

#### Anwendung beim Programmieren: Muster

```python
# Muster: Liste durchgehen und summieren
# Kann für verschiedene Zwecke verwendet werden

# Preise summieren
prices = [10.50, 5.20, 8.90]
total_price = sum(prices)

# Punkte summieren
points = [100, 85, 92]
total_points = sum(points)

# Zeiten summieren
times = [30, 45, 60]  # Minuten
total_time = sum(times)
```

## 🤖 KI als Werkzeug

### Was KI kann

- ✅ Code basierend auf Beschreibungen generieren
- ✅ Komplexen Code erklären
- ✅ Verbesserungsvorschläge machen
- ✅ Beim Debugging helfen
- ✅ Syntax-Details nachschlagen

### Was KI NICHT ersetzt

- ❌ Problemverständnis
- ❌ Kreative Lösungsansätze
- ❌ Entscheidungen treffen
- ❌ Code-Qualität bewerten
- ❌ Kritisches Denken

### Der richtige Ansatz

**Traditionell (ohne KI):**

```text
1. Problem verstehen
2. Lösung konzipieren
3. Syntax nachschlagen
4. Code schreiben
5. Testen
6. Debuggen
```

**Modern (mit KI):**

```text
1. Problem verstehen          ← Sie
2. Lösung konzipieren         ← Sie
3. Prompt formulieren         ← Sie
4. Code generieren            ← KI
5. Code verstehen             ← Sie
6. Code anpassen              ← Sie + KI
7. Testen                     ← Sie
8. Debuggen                   ← Sie + KI
```

## 💡 Praktische Tipps

### Tipp 1: Denken vor Coden

```text
❌ Sofort mit Coden beginnen
✅ Problem erst durchdenken
✅ Lösung skizzieren
✅ Dann coden
```

### Tipp 2: Klein anfangen

```text
❌ Alles auf einmal lösen
✅ Mit kleinstem Teilproblem starten
✅ Schrittweise erweitern
✅ Regelmässig testen
```

### Tipp 3: Code verstehen

```text
❌ KI-Code blind kopieren
✅ Jede Zeile verstehen
✅ Bei Unklarheiten nachfragen
✅ Code anpassen können
```

### Tipp 4: Fehler als Lernchance

```text
❌ Fehler vermeiden wollen
✅ Fehler als normal akzeptieren
✅ Aus Fehlern lernen
✅ Debugging-Skills entwickeln
```

## 🎯 Übungen zum Mindset

### Übung 1: Problemdekomposition

Zerlegen Sie folgende Probleme in Teilprobleme:

1. **Passwort-Generator**
2. **Kontaktliste**
3. **Notizen-App**

### Übung 2: Algorithmisches Denken

Schreiben Sie Schritt-für-Schritt-Anweisungen für:

1. **Tee kochen**
2. **E-Mail senden**
3. **Buch aus Bibliothek ausleihen**

### Übung 3: Abstraktion

Identifizieren Sie die Abstraktion:

1. **"Datei speichern"** - Was wird versteckt?
2. **"E-Mail senden"** - Was wird versteckt?
3. **"Bild hochladen"** - Was wird versteckt?

### Übung 4: Musterkennung

Finden Sie das gemeinsame Muster:

1. **Liste sortieren, Texte sortieren, Zahlen sortieren**
2. **Datei lesen, URL lesen, Datenbank lesen**
3. **Zahl validieren, E-Mail validieren, Datum validieren**

## 📚 Weiterführende Konzepte

### Computational Thinking

Die 4 Säulen sind Teil des "Computational Thinking":

- **Decomposition** = Problemdekomposition
- **Pattern Recognition** = Musterkennung
- **Abstraction** = Abstraktion
- **Algorithm Design** = Algorithmisches Denken

### Growth Mindset

**Fixed Mindset:**

- "Ich kann nicht programmieren"
- "Ich bin nicht gut in Mathe"
- "Das ist zu schwer für mich"

**Growth Mindset:**

- "Ich kann programmieren lernen"
- "Mit Übung werde ich besser"
- "Das ist eine Herausforderung, die ich meistern kann"

## ✅ Checkliste: Gutes Programmier-Mindset

- [ ] Ich verstehe, dass Programmieren Problemlösung ist
- [ ] Ich zerlege grosse Probleme in kleine Teile
- [ ] Ich denke in Schritt-für-Schritt-Anweisungen
- [ ] Ich fokussiere auf das Wesentliche
- [ ] Ich erkenne Muster und nutze sie
- [ ] Ich nutze KI als Werkzeug, nicht als Ersatz
- [ ] Ich verstehe den Code, den ich schreibe
- [ ] Ich sehe Fehler als Lernchancen
- [ ] Ich teste regelmässig
- [ ] Ich bleibe geduldig und ausdauernd

---

**Zurück zu Materialien:** [Materialien README](./README.md)
