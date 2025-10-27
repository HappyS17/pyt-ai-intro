# Lektion 1: Variablen, Datentypen & Operatoren

**Dauer:** 50 Minuten  
**Ziel:** Grundlegende Python-Datentypen verstehen und anwenden

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Variablen nach Python-Konventionen benennen
- Mit verschiedenen Datentypen arbeiten
- Type Hints verstehen und nutzen
- Operatoren korrekt einsetzen
- Type Conversion durchführen

## 📚 Theorie (20 Min.)

### Variablen

**Was sind Variablen?**

Variablen sind "Behälter" für Werte.

```python
# Variable erstellen
name = "Anna"
alter = 25
groesse = 1.75
ist_student = True
```

**Naming Conventions (PEP 8):**

```python
# ✅ Gut
benutzer_name = "Anna"
max_versuche = 3
ist_aktiv = True

# ❌ Schlecht
BenutzerName = "Anna"  # CamelCase nur für Klassen
maxVersuche = 3        # camelCase nicht in Python
ist-aktiv = True       # Bindestriche nicht erlaubt
2name = "Bob"          # Darf nicht mit Zahl beginnen
```

**Regeln:**

- Kleinbuchstaben mit Unterstrichen
- Aussagekräftige Namen
- Keine Python-Keywords (if, for, etc.)
- Keine Sonderzeichen ausser Unterstrich

### Datentypen

#### 1. Zahlen

**Integer (int):**

```python
alter = 25
anzahl = 100
temperatur = -5
```

**Float:**

```python
preis = 19.99
pi = 3.14159
temperatur = 36.5
```

#### 2. Strings (str)

```python
name = "Anna"
nachricht = 'Hallo Welt'
mehrzeilig = """Dies ist
ein mehrzeiliger
String"""

# String-Operationen
vorname = "Anna"
nachname = "Müller"
vollname = vorname + " " + nachname  # Konkatenation
wiederholung = "Ha" * 3  # "HaHaHa"

# F-Strings (modern)
alter = 25
text = f"Ich bin {alter} Jahre alt"
berechnung = f"2 + 2 = {2 + 2}"
```

#### 3. Boolean (bool)

```python
ist_aktiv = True
ist_fertig = False

# Boolean aus Vergleichen
ist_erwachsen = alter >= 18
ist_leer = len(name) == 0
```

#### 4. None

```python
ergebnis = None  # Kein Wert
```

### Type Hints

```python
# Type Hints für bessere Lesbarkeit
name: str = "Anna"
alter: int = 25
groesse: float = 1.75
ist_student: bool = True

# Bei Funktionen (später mehr)
def begruessung(name: str) -> str:
    return f"Hallo {name}"
```

### Operatoren

#### Arithmetische Operatoren

```python
# Grundrechenarten
summe = 5 + 3        # 8
differenz = 10 - 4   # 6
produkt = 7 * 6      # 42
quotient = 20 / 4    # 5.0 (immer float)

# Spezielle Operatoren
ganzzahl_division = 20 // 3  # 6 (ohne Rest)
rest = 20 % 3                # 2 (Modulo)
potenz = 2 ** 8              # 256
```

#### Vergleichsoperatoren

```python
# Vergleiche (Ergebnis: bool)
gleich = 5 == 5           # True
ungleich = 5 != 3         # True
groesser = 10 > 5         # True
kleiner = 3 < 7           # True
groesser_gleich = 5 >= 5  # True
kleiner_gleich = 3 <= 7   # True
```

#### Logische Operatoren

```python
# and, or, not
ist_erwachsen = alter >= 18
hat_ausweis = True

darf_eintreten = ist_erwachsen and hat_ausweis  # Beide müssen True sein
darf_rabatt = ist_student or alter >= 65        # Eines muss True sein
ist_nicht_aktiv = not ist_aktiv                 # Negation
```

### Type Conversion (Casting)

```python
# String zu Zahl
alter_str = "25"
alter_int = int(alter_str)      # 25
preis_str = "19.99"
preis_float = float(preis_str)  # 19.99

# Zahl zu String
zahl = 42
text = str(zahl)  # "42"

# Zu Boolean
bool(1)      # True
bool(0)      # False
bool("")     # False
bool("text") # True

# Fehlerbehandlung
try:
    zahl = int("abc")  # ValueError!
except ValueError:
    print("Keine gültige Zahl")
```

## 💻 Live-Demo (15 Min.)

### Demo 1: Temperaturumrechner

```python
"""
Temperaturumrechner: Celsius ↔ Fahrenheit
"""

def celsius_zu_fahrenheit(celsius: float) -> float:
    """Wandelt Celsius in Fahrenheit um."""
    return (celsius * 9/5) + 32

def fahrenheit_zu_celsius(fahrenheit: float) -> float:
    """Wandelt Fahrenheit in Celsius um."""
    return (fahrenheit - 32) * 5/9

# Verwendung
temp_c = 25.0
temp_f = celsius_zu_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77.0
temp_c = fahrenheit_zu_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")
```

### Demo 2: BMI-Rechner

```python
"""
BMI-Rechner mit Interpretation
"""

def berechne_bmi(gewicht: float, groesse: float) -> float:
    """Berechnet den Body Mass Index."""
    return gewicht / (groesse ** 2)

def interpretiere_bmi(bmi: float) -> str:
    """Gibt Interpretation des BMI zurück."""
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"

# Verwendung
gewicht = 75.0  # kg
groesse = 1.80  # m

bmi = berechne_bmi(gewicht, groesse)
kategorie = interpretiere_bmi(bmi)

print(f"BMI: {bmi:.1f}")
print(f"Kategorie: {kategorie}")
```

### Demo 3: String-Manipulationen

```python
"""
Textverarbeitung mit Strings
"""

text = "  Python ist TOLL!  "

# String-Methoden
print(f"Original: '{text}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Stripped: '{text.strip()}'")
print(f"Replaced: '{text.replace('TOLL', 'super')}'")

# String-Analyse
email = "anna.mueller@example.com"
print(f"Enthält @: {email.count('@')}")
print(f"Startet mit 'anna': {email.startswith('anna')}")
print(f"Endet mit '.com': {email.endswith('.com')}")

# String-Zerlegung
name = "Anna Müller"
teile = name.split()
print(f"Vorname: {teile[0]}")
print(f"Nachname: {teile[1]}")
```

## ✏️ Übung (15 Min.)

Erstellen Sie mit KI-Unterstützung **EINES** der folgenden Programme:

### Option A: Altersrechner

**Anforderungen:**

- Geburtsjahr vom Benutzer einlesen
- Aktuelles Jahr verwenden (2025)
- Alter berechnen
- Alter in Tagen berechnen (ca. 365 Tage/Jahr)
- Formatierte Ausgabe

**Beispiel:**

```text
Geburtsjahr: 1990
Du bist 35 Jahre alt.
Das sind ungefähr 12775 Tage!
```

### Option B: Währungsrechner

**Anforderungen:**

- Betrag in EUR eingeben
- Umrechnung in CHF (Kurs: 1 EUR = 0.95 CHF)
- Ergebnis auf 2 Dezimalstellen runden
- Formatierte Ausgabe

**Beispiel:**

```text
Betrag in EUR: 100
100.00 EUR = 95.00 CHF
```

### Option C: Textanalyse-Tool

**Anforderungen:**

- Text vom Benutzer einlesen
- Anzahl Wörter zählen
- Anzahl Zeichen zählen (mit und ohne Leerzeichen)
- Formatierte Ausgabe

**Beispiel:**

```text
Text: Hallo Welt
Wörter: 2
Zeichen (mit Leerzeichen): 10
Zeichen (ohne Leerzeichen): 9
```

### Vorgehen

1. Wählen Sie EINE Option
2. Formulieren Sie einen Prompt für ChatGPT/Claude
3. Lassen Sie Code generieren
4. Verstehen Sie den Code
5. Testen Sie das Programm
6. Passen Sie es an (z.B. andere Texte)

### Prompt-Vorlage

```text
Erstelle ein Python-Programm: [Ihre gewählte Option]

Anforderungen:
- [Anforderung 1]
- [Anforderung 2]
- [Anforderung 3]

Beispiel:
Eingabe: ...
Ausgabe: ...

Einschränkungen:
- Kommentare auf Deutsch
- Type Hints verwenden
- Benutzerfreundliche Ausgabe
```

## 🎓 Zusammenfassung

### Wichtigste Konzepte

- **Variablen:** Behälter für Werte mit aussagekräftigen Namen
- **Datentypen:** int, float, str, bool, None
- **Type Hints:** Optionale Typ-Angaben für bessere Lesbarkeit
- **Operatoren:** Arithmetisch, Vergleich, logisch
- **Type Conversion:** Umwandlung zwischen Typen

### Best Practices

- ✅ Aussagekräftige Variablennamen
- ✅ snake_case für Variablen
- ✅ Type Hints verwenden
- ✅ F-Strings für Formatierung
- ✅ Fehlerbehandlung bei Conversion

### Häufige Fehler

- ❌ CamelCase statt snake_case
- ❌ Nicht-aussagekräftige Namen (a, x, temp)
- ❌ Division durch Null nicht abfangen
- ❌ String-Conversion ohne Fehlerbehandlung

## 📎 Anhang für Dozenten

### Timing-Tipps

- **Theorie:** Nicht zu lange - max. 20 Min.
- **Live-Demo:** Interaktiv gestalten, Fragen stellen
- **Übung:** Herumgehen und helfen

### Häufige Fragen

#### Frage 1: Wann int vs. float?

- int: Ganze Zahlen (Alter, Anzahl)
- float: Dezimalzahlen (Preis, Messwerte)

#### Frage 2: Warum Type Hints?

- Bessere Lesbarkeit
- IDE-Unterstützung
- Dokumentation
- Aber: Nicht erzwungen!

#### Frage 3: // vs. / ?

- `/`: Normale Division (Ergebnis immer float)
- `//`: Ganzzahlige Division (ohne Rest)

### Materialien vorbereiten

- [ ] Code-Beispiele bereit
- [ ] Live-Demo getestet
- [ ] Übungsaufgaben ausgedruckt
- [ ] Lösungen vorbereitet

---

**Weiter zu:** [Lektion 2 - Kontrollstrukturen](./lektion-2-kontrollstrukturen.md)  
**Zurück zu:** [Praxis README](./README.md)
