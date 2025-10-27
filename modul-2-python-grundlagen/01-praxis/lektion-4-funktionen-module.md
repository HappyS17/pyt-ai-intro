# Lektion 4: Funktionen & Module

**Dauer:** 50 Minuten  
**Ziel:** Wiederverwendbaren Code mit Funktionen und Modulen erstellen

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Funktionen mit Parametern definieren
- Rückgabewerte nutzen
- Docstrings schreiben
- Lambda-Funktionen verstehen
- Module importieren und verwenden
- Eigene Module erstellen

## 📚 Theorie (20 Min.)

### Funktionen definieren

**Grundstruktur:**

```python
def begruessung():
    """Gibt eine Begrüssung aus."""
    print("Hallo Welt!")

# Funktion aufrufen
begruessung()
```

**Mit Parametern:**

```python
def begruessung(name):
    """Begrüsst eine Person."""
    print(f"Hallo {name}!")

begruessung("Anna")  # "Hallo Anna!"
```

**Mit Rückgabewert:**

```python
def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

ergebnis = addiere(5, 3)  # 8
```

**Mit Type Hints:**

```python
def addiere(a: int, b: int) -> int:
    """Addiert zwei Zahlen."""
    return a + b
```

### Parameter-Varianten

**Positionsparameter:**

```python
def person_info(name, alter, stadt):
    return f"{name}, {alter} Jahre, aus {stadt}"

info = person_info("Anna", 25, "Zürich")
```

**Keyword-Arguments:**

```python
# Reihenfolge egal
info = person_info(alter=25, stadt="Zürich", name="Anna")
```

**Default-Parameter:**

```python
def begruessung(name, gruss="Hallo"):
    return f"{gruss} {name}!"

print(begruessung("Anna"))              # "Hallo Anna!"
print(begruessung("Bob", "Hi"))         # "Hi Bob!"
print(begruessung("Clara", gruss="Hey")) # "Hey Clara!"
```

**args und **kwargs:**

```python
# *args - Variable Anzahl Positionsparameter
def summe(*zahlen):
    return sum(zahlen)

print(summe(1, 2, 3))        # 6
print(summe(1, 2, 3, 4, 5))  # 15

# **kwargs - Variable Anzahl Keyword-Parameter
def person_info(**daten):
    for key, value in daten.items():
        print(f"{key}: {value}")

person_info(name="Anna", alter=25, stadt="Zürich")
```

### Docstrings

```python
def berechne_bmi(gewicht: float, groesse: float) -> float:
    """
    Berechnet den Body Mass Index.
    
    Args:
        gewicht: Gewicht in Kilogramm
        groesse: Grösse in Metern
    
    Returns:
        BMI als Float
    
    Example:
        >>> berechne_bmi(75, 1.80)
        23.15
    """
    return gewicht / (groesse ** 2)

# Docstring anzeigen
print(berechne_bmi.__doc__)
help(berechne_bmi)
```

### Lambda-Funktionen

```python
# Normale Funktion
def quadrat(x):
    return x ** 2

# Lambda (anonyme Funktion)
quadrat = lambda x: x ** 2

# Verwendung
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x ** 2, zahlen))

# Mit sorted()
personen = [
    {"name": "Bob", "alter": 30},
    {"name": "Anna", "alter": 25},
    {"name": "Clara", "alter": 28}
]

nach_alter = sorted(personen, key=lambda p: p["alter"])
```

### Scope (Gültigkeitsbereich)

```python
# Global
x = 10

def funktion():
    # Local
    y = 20
    print(x)  # Zugriff auf global: OK
    print(y)  # Zugriff auf local: OK

funktion()
print(x)  # OK
# print(y)  # Fehler! y ist local

# Global ändern
def aendere_global():
    global x
    x = 100

aendere_global()
print(x)  # 100
```

### Module importieren

**Standard Library:**

```python
# Ganzes Modul
import math
print(math.pi)
print(math.sqrt(16))

# Spezifische Funktionen
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Mit Alias
import math as m
print(m.pi)

# Alles importieren (nicht empfohlen)
from math import *
```

**Häufige Module:**

```python
# math - Mathematik
import math
math.ceil(4.2)   # 5
math.floor(4.8)  # 4
math.pow(2, 3)   # 8.0

# random - Zufallszahlen
import random
random.randint(1, 10)      # Zufällige Zahl 1-10
random.choice([1, 2, 3])   # Zufälliges Element
random.shuffle(liste)      # Liste mischen

# datetime - Datum und Zeit
from datetime import datetime, timedelta
jetzt = datetime.now()
morgen = jetzt + timedelta(days=1)

# os - Betriebssystem
import os
os.getcwd()           # Aktuelles Verzeichnis
os.listdir('.')       # Dateien im Verzeichnis
os.path.exists(datei) # Prüft ob Datei existiert
```

### Eigene Module erstellen

**Datei: `mein_modul.py`**

```python
"""Mein erstes Modul."""

def begruessung(name):
    """Begrüsst eine Person."""
    return f"Hallo {name}!"

def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

PI = 3.14159
```

**Verwendung:**

```python
# In anderer Datei
import mein_modul

print(mein_modul.begruessung("Anna"))
print(mein_modul.addiere(5, 3))
print(mein_modul.PI)
```

## 💻 Live-Demo (15 Min.)

### Demo 1: Validierungsfunktionen

```python
"""
Wiederverwendbare Validierungsfunktionen
"""

def ist_email_gueltig(email: str) -> bool:
    """Prüft ob Email-Format gültig ist."""
    return "@" in email and "." in email.split("@")[1]

def ist_passwort_sicher(passwort: str) -> bool:
    """Prüft ob Passwort sicher ist."""
    if len(passwort) < 8:
        return False
    
    hat_gross = any(c.isupper() for c in passwort)
    hat_klein = any(c.islower() for c in passwort)
    hat_zahl = any(c.isdigit() for c in passwort)
    
    return hat_gross and hat_klein and hat_zahl

def ist_alter_gueltig(alter: int, min_alter: int = 0, max_alter: int = 150) -> bool:
    """Prüft ob Alter im gültigen Bereich ist."""
    return min_alter <= alter <= max_alter

# Tests
print(ist_email_gueltig("anna@example.com"))  # True
print(ist_email_gueltig("ungueltig"))         # False

print(ist_passwort_sicher("Sicher123"))       # True
print(ist_passwort_sicher("schwach"))         # False

print(ist_alter_gueltig(25))                  # True
print(ist_alter_gueltig(200))                 # False
```

### Demo 2: Mathematik-Utilities

**Datei: `mathe_utils.py`**

```python
"""
Mathematik-Utility-Funktionen
"""

def ist_gerade(zahl: int) -> bool:
    """Prüft ob Zahl gerade ist."""
    return zahl % 2 == 0

def ist_primzahl(zahl: int) -> bool:
    """Prüft ob Zahl eine Primzahl ist."""
    if zahl < 2:
        return False
    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return False
    return True

def fakultaet(n: int) -> int:
    """Berechnet die Fakultät von n."""
    if n == 0 or n == 1:
        return 1
    return n * fakultaet(n - 1)

def fibonacci(n: int) -> list[int]:
    """Gibt die ersten n Fibonacci-Zahlen zurück."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Tests
if __name__ == "__main__":
    print(f"10 ist gerade: {ist_gerade(10)}")
    print(f"17 ist Primzahl: {ist_primzahl(17)}")
    print(f"5! = {fakultaet(5)}")
    print(f"Fibonacci(10): {fibonacci(10)}")
```

### Demo 3: Datums-Operationen

```python
"""
Arbeiten mit datetime-Modul
"""
from datetime import datetime, timedelta

def tage_bis_geburtstag(geburtstag: str) -> int:
    """
    Berechnet Tage bis zum nächsten Geburtstag.
    
    Args:
        geburtstag: Datum im Format "DD.MM.YYYY"
    
    Returns:
        Anzahl Tage bis Geburtstag
    """
    # Geburtstag parsen
    tag, monat, jahr = map(int, geburtstag.split("."))
    
    # Aktuelles Datum
    heute = datetime.now()
    
    # Nächster Geburtstag
    naechster_gb = datetime(heute.year, monat, tag)
    
    # Falls schon vorbei, nächstes Jahr
    if naechster_gb < heute:
        naechster_gb = datetime(heute.year + 1, monat, tag)
    
    # Differenz berechnen
    diff = naechster_gb - heute
    return diff.days

def formatiere_datum(datum: datetime, format: str = "DE") -> str:
    """Formatiert Datum nach verschiedenen Standards."""
    if format == "DE":
        return datum.strftime("%d.%m.%Y")
    elif format == "US":
        return datum.strftime("%m/%d/%Y")
    elif format == "ISO":
        return datum.strftime("%Y-%m-%d")
    else:
        return str(datum)

# Tests
geburtstag = "15.06.1990"
tage = tage_bis_geburtstag(geburtstag)
print(f"Tage bis Geburtstag: {tage}")

jetzt = datetime.now()
print(f"DE: {formatiere_datum(jetzt, 'DE')}")
print(f"US: {formatiere_datum(jetzt, 'US')}")
print(f"ISO: {formatiere_datum(jetzt, 'ISO')}")
```

## ✏️ Übung (15 Min.)

Projekt: **Utility-Funktionen-Modul**

Erstellen Sie mit KI ein Modul mit 3-4 Funktionen:

### Anforderungen

**1. String-Utility (wählen Sie 1-2):**

- `ist_palindrom(text)` - Prüft ob Text ein Palindrom ist
- `zaehle_woerter(text)` - Zählt Wörter in Text
- `umkehren(text)` - Kehrt Text um

**2. Mathe-Utility (wählen Sie 1-2):**

- `ist_gerade(zahl)` - Prüft ob Zahl gerade
- `finde_max(liste)` - Findet Maximum in Liste
- `durchschnitt(liste)` - Berechnet Durchschnitt

**3. Listen-Utility (wählen Sie 1):**

- `entferne_duplikate(liste)` - Entfernt Duplikate
- `finde_gemeinsame(liste1, liste2)` - Findet gemeinsame Elemente

### Vorgaben

- Jede Funktion mit Docstring
- Type Hints verwenden
- Einfache Tests schreiben

### Beispiel-Struktur

```python
"""
Mein Utility-Modul
"""

def ist_palindrom(text: str) -> bool:
    """
    Prüft ob Text ein Palindrom ist.
    
    Args:
        text: Zu prüfender Text
    
    Returns:
        True wenn Palindrom, sonst False
    
    Example:
        >>> ist_palindrom("anna")
        True
    """
    # Implementierung hier
    pass

# Tests
if __name__ == "__main__":
    print(ist_palindrom("anna"))  # True
    print(ist_palindrom("test"))  # False
```

## 🎓 Zusammenfassung

### Funktionen

- **Wiederverwendbarkeit:** Code einmal schreiben, mehrfach nutzen
- **Abstraktion:** Komplexität verstecken
- **Organisation:** Code strukturieren

### Parameter

- **Positions-Parameter:** Reihenfolge wichtig
- **Keyword-Parameter:** Name wichtig
- **Default-Werte:** Optional mit Standardwert
- ***args, **kwargs:** Variable Anzahl

### Module

- **Standard Library:** Viele nützliche Module
- **Eigene Module:** Code organisieren
- **Import:** Funktionen wiederverwenden

### Best Practices

- ✅ Aussagekräftige Funktionsnamen
- ✅ Docstrings schreiben
- ✅ Type Hints verwenden
- ✅ Eine Aufgabe pro Funktion
- ✅ DRY: Don't Repeat Yourself

## 📎 Anhang für Dozenten

### Timing-Tipps

- Lambda-Funktionen: Nur kurz erwähnen
- Fokus auf praktische Funktionen
- Eigene Module: Wichtig für Organisation

### Häufige Fragen

#### Frage 1: Wann Funktion erstellen?

- Code wird mehrfach genutzt
- Logische Einheit
- Bessere Lesbarkeit

#### Frage 2: return vs. print?

- return: Wert zurückgeben (wiederverwendbar)
- print: Nur ausgeben (nicht wiederverwendbar)

#### Frage 3: Wann eigenes Modul?

- Mehrere zusammenhängende Funktionen
- Code in mehreren Dateien nutzen
- Bessere Organisation

### Materialien vorbereiten

- [ ] Utility-Beispiele bereit
- [ ] Module-Demo vorbereitet
- [ ] datetime-Beispiele getestet

---

**Zurück zu:** [Lektion 3 - Listen & Dictionaries](./lektion-3-listen-dictionaries.md)  
**Zurück zur Übersicht:** [Praxis README](./README.md)
