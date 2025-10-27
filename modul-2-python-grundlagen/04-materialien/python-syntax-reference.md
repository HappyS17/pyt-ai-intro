# Python-Syntax Quick Reference

Schnellreferenz für Python-Grundlagen aus Modul 2.

## 📚 Variablen & Datentypen

### Variablen deklarieren

```python
# Variablen (ohne Typdeklaration)
name = "Anna"
alter = 25
groesse = 1.75
ist_student = True

# Mit Type Hints (empfohlen)
name: str = "Anna"
alter: int = 25
groesse: float = 1.75
ist_student: bool = True
```

### Datentypen

| Typ | Beispiel | Beschreibung |
|-----|----------|--------------|
| `int` | `42` | Ganzzahl |
| `float` | `3.14` | Dezimalzahl |
| `str` | `"Hello"` | Text |
| `bool` | `True` / `False` | Wahrheitswert |
| `list` | `[1, 2, 3]` | Geordnete Sammlung |
| `dict` | `{"key": "value"}` | Key-Value-Paare |
| `tuple` | `(1, 2, 3)` | Unveränderliche Liste |
| `set` | `{1, 2, 3}` | Menge (keine Duplikate) |
| `None` | `None` | Kein Wert |

### Type Conversion

```python
# String → Int/Float
zahl = int("42")         # 42
dezimal = float("3.14")  # 3.14

# Int/Float → String
text = str(42)           # "42"

# List → Set (Duplikate entfernen)
unique = set([1, 2, 2, 3])  # {1, 2, 3}
```

## 🔢 Operatoren

### Arithmetische Operatoren

```python
a + b      # Addition
a - b      # Subtraktion
a * b      # Multiplikation
a / b      # Division (ergibt float)
a // b     # Ganzzahldivision
a % b      # Modulo (Rest)
a ** b     # Potenz
```

### Vergleichsoperatoren

```python
a == b     # Gleich
a != b     # Ungleich
a < b      # Kleiner als
a <= b     # Kleiner oder gleich
a > b      # Grösser als
a >= b     # Grösser oder gleich
```

### Logische Operatoren

```python
a and b    # Logisches UND
a or b     # Logisches ODER
not a      # Logisches NICHT
```

## 📝 Strings

### String-Methoden

```python
text = "  Python ist toll!  "

text.strip()               # Leerzeichen entfernen: "Python ist toll!"
text.upper()               # Grossbuchstaben: "  PYTHON IST TOLL!  "
text.lower()               # Kleinbuchstaben: "  python ist toll!  "
text.replace("toll", "super")  # Ersetzen
text.split()               # Liste: ["Python", "ist", "toll!"]
"".join(["a", "b", "c"])   # Verbinden: "abc"

# String-Prüfungen
text.startswith("  Py")    # True
text.endswith("!  ")       # True
"toll" in text             # True
text.isdigit()             # False
text.isalpha()             # False (wegen Leerzeichen)
```

### String-Formatierung

```python
name = "Anna"
alter = 25

# f-strings (modern, empfohlen)
f"Hallo {name}, du bist {alter}"
f"In 10 Jahren: {alter + 10}"
f"Preis: {19.99:.2f} CHF"

# format()
"Hallo {}, du bist {}".format(name, alter)

# % (veraltet)
"Hallo %s, du bist %d" % (name, alter)
```

### String-Slicing

```python
text = "Python"

text[0]       # 'P' (erstes Zeichen)
text[-1]      # 'n' (letztes Zeichen)
text[0:3]     # 'Pyt' (Index 0-2)
text[:3]      # 'Pyt' (Anfang bis 3)
text[3:]      # 'hon' (3 bis Ende)
text[::2]     # 'Pto' (jedes 2. Zeichen)
text[::-1]    # 'nohtyP' (rückwärts)
```

## 🔀 Kontrollstrukturen

### if-elif-else

```python
if bedingung1:
    # Code
elif bedingung2:
    # Code
else:
    # Code

# Einzeiler (ternärer Operator)
ergebnis = "Ja" if bedingung else "Nein"
```

### for-Schleifen

```python
# Liste durchlaufen
for item in liste:
    print(item)

# Range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# Mit Index (enumerate)
for index, item in enumerate(liste):
    print(f"{index}: {item}")

# Dictionary durchlaufen
for key, value in dict.items():
    print(f"{key}: {value}")
```

### while-Schleifen

```python
while bedingung:
    # Code
    if abbruch_bedingung:
        break     # Schleife beenden
    if ueberspringen:
        continue  # Zur nächsten Iteration
```

## 📚 Listen

### Listen erstellen und manipulieren

```python
# Erstellen
liste = [1, 2, 3, 4, 5]
leer = []

# Hinzufügen
liste.append(6)           # Am Ende: [1, 2, 3, 4, 5, 6]
liste.insert(0, 0)        # An Position 0: [0, 1, 2, 3, 4, 5, 6]
liste.extend([7, 8])      # Mehrere: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Entfernen
liste.remove(0)           # Wert entfernen: [1, 2, 3, 4, 5, 6, 7, 8]
element = liste.pop()     # Letztes entfernen: element=8
element = liste.pop(0)    # An Position 0: element=1
del liste[0]              # An Position 0 löschen

# Prüfen
3 in liste                # True
len(liste)                # Länge
liste.index(5)            # Index von Wert 5
liste.count(3)            # Anzahl des Werts 3

# Sortieren
liste.sort()              # In-place sortieren
sortiert = sorted(liste)  # Neue sortierte Liste
liste.reverse()           # Umkehren
```

### List Comprehensions

```python
# Grundform
quadrate = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Mit Bedingung
gerade = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Mit if-else
kategorisiert = ["Gerade" if x % 2 == 0 else "Ungerade" for x in range(5)]
# ['Gerade', 'Ungerade', 'Gerade', 'Ungerade', 'Gerade']
```

## 📖 Dictionaries

### Dictionary erstellen und manipulieren

```python
# Erstellen
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}
leer = {}

# Zugriff
name = person["name"]              # KeyError wenn nicht vorhanden
name = person.get("name")          # None wenn nicht vorhanden
name = person.get("name", "Unbekannt")  # Default-Wert

# Hinzufügen/Ändern
person["email"] = "anna@example.com"
person["alter"] = 26

# Entfernen
del person["email"]
wert = person.pop("stadt")         # Entfernen und Wert zurückgeben
person.clear()                     # Alles löschen

# Prüfen
"name" in person                   # Key vorhanden?
person.keys()                      # Alle Keys
person.values()                    # Alle Values
person.items()                     # Key-Value-Paare

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehensions

```python
# Grundform
quadrate = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Mit Bedingung
gerade = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## 🔧 Funktionen

### Funktionen definieren

```python
# Einfache Funktion
def gruss(name):
    return f"Hallo {name}"

# Mit Type Hints
def addiere(a: int, b: int) -> int:
    return a + b

# Mit Default-Werten
def gruss(name: str, sprache: str = "DE") -> str:
    if sprache == "DE":
        return f"Hallo {name}"
    else:
        return f"Hello {name}"

# Variable Anzahl Argumente
def summe(*zahlen):
    return sum(zahlen)

# Keyword Arguments
def person(**infos):
    for key, value in infos.items():
        print(f"{key}: {value}")
```

### Docstrings

```python
def berechne_flaeche(laenge: float, breite: float) -> float:
    """
    Berechnet die Fläche eines Rechtecks.

    Args:
        laenge: Länge des Rechtecks in Metern
        breite: Breite des Rechtecks in Metern

    Returns:
        Fläche in Quadratmetern

    Examples:
        >>> berechne_flaeche(5, 3)
        15.0
    """
    return laenge * breite
```

## ⚠️ Fehlerbehandlung

### try-except

```python
try:
    # Code der Fehler verursachen könnte
    zahl = int(input("Zahl: "))
    ergebnis = 10 / zahl
except ValueError:
    # Spezifischer Fehler
    print("Keine gültige Zahl!")
except ZeroDivisionError:
    # Anderer spezifischer Fehler
    print("Division durch 0!")
except Exception as e:
    # Alle anderen Fehler
    print(f"Fehler: {e}")
else:
    # Wird ausgeführt wenn kein Fehler
    print(f"Ergebnis: {ergebnis}")
finally:
    # Wird immer ausgeführt
    print("Fertig!")
```

## 📁 File I/O

### Dateien lesen

```python
# Methode 1: with (empfohlen)
with open("datei.txt", "r") as datei:
    inhalt = datei.read()           # Alles lesen
    zeilen = datei.readlines()      # Als Liste
    zeile = datei.readline()        # Eine Zeile

# Methode 2: Explizit schliessen
datei = open("datei.txt", "r")
inhalt = datei.read()
datei.close()
```

### Dateien schreiben

```python
# Überschreiben
with open("datei.txt", "w") as datei:
    datei.write("Hallo Welt\n")

# Anhängen
with open("datei.txt", "a") as datei:
    datei.write("Neue Zeile\n")
```

### JSON

```python
import json

# Speichern
data = {"name": "Anna", "alter": 25}
with open("data.json", "w") as datei:
    json.dump(data, datei, indent=2)

# Laden
with open("data.json", "r") as datei:
    data = json.load(datei)
```

## 📦 Module importieren

```python
# Ganzes Modul
import math
print(math.pi)

# Spezifische Funktionen
from math import pi, sqrt
print(pi)

# Mit Alias
import datetime as dt
heute = dt.date.today()

# Alles importieren (nicht empfohlen)
from math import *
```

## 💡 Best Practices

### PEP 8 Style Guide

```python
# Naming Conventions
variable_name = "snake_case"
KONSTANTE = "UPPERCASE"
def funktions_name():
    pass
class KlassenName:
    pass

# Einrückung: 4 Leerzeichen
if bedingung:
    code()

# Leerzeilen
def funktion1():
    pass


def funktion2():  # 2 Leerzeilen zwischen Top-Level-Funktionen
    pass

# Leerzeichen um Operatoren
x = 5
y = x + 1
z = x * 2 - y

# Kommentare
# Das ist ein Kommentar

# Zeilenlänge: max. 79 Zeichen
```

### Code-Organisation

```python
"""
Modul-Docstring am Anfang
"""

# Imports
import standard_library
import third_party
import local_module

# Konstanten
MAX_VERSUCHE = 3

# Funktionen
def funktion():
    pass

# Hauptprogramm
if __name__ == "__main__":
    funktion()
```

---

**Zurück zu Materialien:** [README](./README.md)
