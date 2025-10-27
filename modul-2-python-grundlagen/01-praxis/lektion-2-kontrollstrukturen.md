# Lektion 2: Kontrollstrukturen

**Dauer:** 50 Minuten  
**Ziel:** Bedingungen und Schleifen in Python beherrschen

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- if/elif/else Bedingungen schreiben
- for-Schleifen für Iterationen nutzen
- while-Schleifen für bedingte Wiederholungen einsetzen
- break, continue und pass verwenden
- Die range()-Funktion nutzen

## 📚 Theorie (20 Min.)

### if/elif/else - Bedingte Ausführung

**Grundstruktur:**

```python
alter = 18

if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

**Mehrere Bedingungen:**

```python
punkte = 85

if punkte >= 90:
    note = "A"
elif punkte >= 80:
    note = "B"
elif punkte >= 70:
    note = "C"
elif punkte >= 60:
    note = "D"
else:
    note = "F"

print(f"Note: {note}")
```

**Verschachtelte Bedingungen:**

```python
alter = 20
hat_ausweis = True

if alter >= 18:
    if hat_ausweis:
        print("Eintritt erlaubt")
    else:
        print("Ausweis erforderlich")
else:
    print("Zu jung")
```

**Ternärer Operator (Kurzform):**

```python
# Langform
if alter >= 18:
    status = "Erwachsen"
else:
    status = "Kind"

# Kurzform
status = "Erwachsen" if alter >= 18 else "Kind"
```

### Vergleichsoperatoren

```python
# Vergleiche
x == y   # Gleich
x != y   # Ungleich
x > y    # Grösser
x < y    # Kleiner
x >= y   # Grösser oder gleich
x <= y   # Kleiner oder gleich

# Logische Verknüpfungen
alter >= 18 and hat_ausweis  # Beide müssen True sein
ist_student or ist_senior    # Mindestens eines True
not ist_gesperrt             # Negation
```

### for-Schleifen

**Über Listen iterieren:**

```python
namen = ["Anna", "Bob", "Clara"]

for name in namen:
    print(f"Hallo {name}")
```

**Mit range():**

```python
# 0 bis 4
for i in range(5):
    print(i)

# 1 bis 5
for i in range(1, 6):
    print(i)

# Mit Schrittweite
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

**Mit enumerate():**

```python
namen = ["Anna", "Bob", "Clara"]

for index, name in enumerate(namen):
    print(f"{index + 1}. {name}")
```

**Über Strings iterieren:**

```python
wort = "Python"

for buchstabe in wort:
    print(buchstabe)
```

### while-Schleifen

**Grundstruktur:**

```python
zaehler = 0

while zaehler < 5:
    print(zaehler)
    zaehler += 1
```

**Mit Bedingung:**

```python
antwort = ""

while antwort != "quit":
    antwort = input("Befehl (quit zum Beenden): ")
    print(f"Du hast eingegeben: {antwort}")
```

**Endlosschleife (mit break):**

```python
while True:
    antwort = input("Weiter? (ja/nein): ")
    if antwort == "nein":
        break
    print("OK, weiter geht's!")
```

### break, continue, pass

**break - Schleife beenden:**

```python
for i in range(10):
    if i == 5:
        break  # Stoppt bei 5
    print(i)
```

**continue - Iteration überspringen:**

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print(i)  # Gibt nur ungerade Zahlen aus
```

**pass - Platzhalter:**

```python
for i in range(5):
    if i == 3:
        pass  # Macht nichts, Platzhalter
    else:
        print(i)
```

## 💻 Live-Demo (15 Min.)

### Demo 1: Notenklassifikation

```python
"""
Notenklassifikation basierend auf Punkten
"""

def klassifiziere_note(punkte: int) -> str:
    """Gibt Note basierend auf Punkten zurück."""
    if punkte >= 90:
        return "A - Ausgezeichnet"
    elif punkte >= 80:
        return "B - Sehr gut"
    elif punkte >= 70:
        return "C - Gut"
    elif punkte >= 60:
        return "D - Befriedigend"
    else:
        return "F - Nicht bestanden"

# Testen
test_punkte = [95, 85, 75, 65, 55]

for punkte in test_punkte:
    note = klassifiziere_note(punkte)
    print(f"{punkte} Punkte → {note}")
```

### Demo 2: FizzBuzz-Problem

```python
"""
FizzBuzz: Klassisches Programmier-Problem
- Bei Vielfachen von 3: "Fizz"
- Bei Vielfachen von 5: "Buzz"
- Bei Vielfachen von 3 und 5: "FizzBuzz"
- Sonst: Die Zahl
"""

for zahl in range(1, 31):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)
```

### Demo 3: Passwort-Validator

```python
"""
Passwort-Validator mit mehreren Kriterien
"""

def validiere_passwort(passwort: str) -> tuple[bool, list[str]]:
    """
    Validiert ein Passwort.
    
    Returns:
        (ist_gueltig, fehler_liste)
    """
    fehler = []
    
    # Mindestlänge
    if len(passwort) < 8:
        fehler.append("Mindestens 8 Zeichen erforderlich")
    
    # Grossbuchstabe
    if not any(c.isupper() for c in passwort):
        fehler.append("Mindestens ein Grossbuchstabe erforderlich")
    
    # Kleinbuchstabe
    if not any(c.islower() for c in passwort):
        fehler.append("Mindestens ein Kleinbuchstabe erforderlich")
    
    # Zahl
    if not any(c.isdigit() for c in passwort):
        fehler.append("Mindestens eine Zahl erforderlich")
    
    ist_gueltig = len(fehler) == 0
    return ist_gueltig, fehler

# Testen
test_passwoerter = [
    "schwach",
    "Besser123",
    "NochBesser123!"
]

for pw in test_passwoerter:
    gueltig, fehler = validiere_passwort(pw)
    print(f"\nPasswort: '{pw}'")
    if gueltig:
        print("✓ Gültig!")
    else:
        print("✗ Ungültig:")
        for fehler_text in fehler:
            print(f"  - {fehler_text}")
```

### Demo 4: Zahlenratespiel

```python
"""
Einfaches Zahlenratespiel
"""
import random

def zahlenraten():
    """Zahlenratespiel 1-100."""
    ziel = random.randint(1, 100)
    versuche = 0
    
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt.")
    print("Versuche sie zu erraten!")
    
    while True:
        try:
            tipp = int(input("\nDein Tipp: "))
            versuche += 1
            
            if tipp < ziel:
                print("Zu niedrig!")
            elif tipp > ziel:
                print("Zu hoch!")
            else:
                print(f"Richtig! Du hast {versuche} Versuche gebraucht.")
                break
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

# Spiel starten (auskommentiert für Demo)
# zahlenraten()
```

## ✏️ Übung (15 Min.)

Entwickeln Sie mit KI-Unterstützung **EINES** der folgenden Programme:

### Option A: Primzahl-Checker

**Anforderungen:**

- Zahl vom Benutzer einlesen
- Prüfen, ob die Zahl eine Primzahl ist
- Ergebnis ausgeben
- Programm läuft in Schleife bis 'quit'

**Beispiel:**

```text
Zahl (oder 'quit'): 17
17 ist eine Primzahl!

Zahl (oder 'quit'): 20
20 ist keine Primzahl.

Zahl (oder 'quit'): quit
Auf Wiedersehen!
```

**Hinweis:** Eine Primzahl ist nur durch 1 und sich selbst teilbar.

### Option B: Menü-System

**Anforderungen:**

- Menü mit 3 Optionen anzeigen
- Benutzerwahl einlesen
- Entsprechende Aktion ausführen
- Programm läuft bis Beenden gewählt wird

**Beispiel:**

```text
=== MENÜ ===
1. Begrüssung
2. Datum anzeigen
3. Beenden

Wahl: 1
Hallo! Willkommen!

=== MENÜ ===
...
```

### Option C: Fibonacci-Folge

**Anforderungen:**

- Die ersten 10 Zahlen der Fibonacci-Folge ausgeben
- Jede Zahl auf neuer Zeile
- Mit Index nummerieren

**Beispiel:**

```text
Fibonacci-Folge (erste 10 Zahlen):
1. 0
2. 1
3. 1
4. 2
5. 3
6. 5
7. 8
8. 13
9. 21
10. 34
```

**Hinweis:** Fibonacci: Jede Zahl ist die Summe der beiden vorherigen (0, 1, 1, 2, 3, 5, ...)

### Prompt-Vorlage

```text
Erstelle ein Python-Programm: [Ihre gewählte Option]

Anforderungen:
- [Spezifische Anforderungen]
- Fehlerbehandlung für ungültige Eingaben
- Benutzerfreundliche Ausgabe
- Kommentare auf Deutsch

Beispiel:
[Zeigen Sie die erwartete Interaktion]
```

## 🎓 Zusammenfassung

### Wichtigste Konzepte

- **if/elif/else:** Bedingte Ausführung
- **for-Schleife:** Über Sequenzen iterieren
- **while-Schleife:** Bedingte Wiederholung
- **break:** Schleife vorzeitig beenden
- **continue:** Iteration überspringen
- **range():** Zahlensequenzen generieren

### Wann was verwenden?

**for-Schleife:**

- Wenn Sie wissen, wie oft wiederholt wird
- Über Listen, Strings, etc. iterieren
- Mit range() für feste Anzahl

**while-Schleife:**

- Wenn Anzahl Wiederholungen unbekannt
- Bis Bedingung erfüllt ist
- Benutzerinteraktion (bis 'quit')

### Best Practices

- ✅ Aussagekräftige Bedingungen
- ✅ Einrückung korrekt (4 Leerzeichen)
- ✅ Endlosschleifen vermeiden
- ✅ break für vorzeitigen Abbruch
- ✅ Fehlerbehandlung bei Eingaben

### Häufige Fehler

- ❌ Falsche Einrückung
- ❌ `=` statt `==` in Bedingungen
- ❌ Endlosschleifen ohne break
- ❌ Off-by-one Fehler bei range()

## 📎 Anhang für Dozenten

### Timing-Tipps

- **Theorie:** Konzepte mit Live-Beispielen zeigen
- **Demo:** FizzBuzz ist immer beliebt!
- **Übung:** Primzahl-Checker ist gute Herausforderung

### Häufige Fragen

#### Frage 1: for vs. while?

- for: Anzahl bekannt, über Sequenz
- while: Anzahl unbekannt, bis Bedingung

#### Frage 2: Wann break vs. return?

- break: Nur Schleife beenden
- return: Ganze Funktion beenden

#### Frage 3: range(5) vs. range(1, 6)?

- range(5): 0, 1, 2, 3, 4
- range(1, 6): 1, 2, 3, 4, 5

### Materialien vorbereiten

- [ ] FizzBuzz-Demo vorbereitet
- [ ] Zahlenratespiel getestet
- [ ] Übungsaufgaben bereit
- [ ] Lösungen vorbereitet

---

**Weiter zu:** [Lektion 3 - Listen & Dictionaries](./lektion-3-listen-dictionaries.md)  
**Zurück zu:** [Lektion 1 - Variablen & Datentypen](./lektion-1-variablen-datentypen.md)
