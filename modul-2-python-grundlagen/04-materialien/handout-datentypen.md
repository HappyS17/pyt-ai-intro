# Handout: Python-Datentypen

Umfassender Leitfaden für Python-Datentypen aus Modul 2.

## 🎯 Lernziele

Nach diesem Handout können Sie:
- Alle grundlegenden Python-Datentypen verstehen und anwenden
- Zwischen Datentypen konvertieren
- Die richtige Datenstruktur für Ihr Problem wählen
- Typische Fehler vermeiden

## 📊 Übersicht der Datentypen

| Kategorie | Datentyp | Veränderbar | Geordnet | Beispiel |
|-----------|----------|-------------|----------|----------|
| **Numerisch** | `int` | Ja (immutable) | - | `42` |
|  | `float` | Ja (immutable) | - | `3.14` |
|  | `complex` | Ja (immutable) | - | `1+2j` |
| **Text** | `str` | Nein (immutable) | Ja | `"Hello"` |
| **Sequenzen** | `list` | Ja (mutable) | Ja | `[1, 2, 3]` |
|  | `tuple` | Nein (immutable) | Ja | `(1, 2, 3)` |
|  | `range` | Nein (immutable) | Ja | `range(10)` |
| **Mappings** | `dict` | Ja (mutable) | Nein* | `{"a": 1}` |
| **Mengen** | `set` | Ja (mutable) | Nein | `{1, 2, 3}` |
|  | `frozenset` | Nein (immutable) | Nein | `frozenset({1, 2})` |
| **Boolean** | `bool` | Nein (immutable) | - | `True`, `False` |
| **None** | `NoneType` | Nein (immutable) | - | `None` |

*Ab Python 3.7+ sind Dictionaries insertion-ordered

## 🔢 Numerische Datentypen

### Integer (int)

Ganzzahlen unbegrenzter Grösse.

```python
# Dezimal
zahl = 42

# Binär (Präfix 0b)
binär = 0b1010  # 10

# Oktal (Präfix 0o)
oktal = 0o12    # 10

# Hexadezimal (Präfix 0x)
hex = 0x0A      # 10

# Unterstriche zur Lesbarkeit (ab Python 3.6)
million = 1_000_000
```

**Operationen:**
```python
a = 10
b = 3

a + b    # 13 (Addition)
a - b    # 7  (Subtraktion)
a * b    # 30 (Multiplikation)
a / b    # 3.333... (Division → float)
a // b   # 3  (Ganzzahldivision)
a % b    # 1  (Modulo/Rest)
a ** b   # 1000 (Potenz)
```

### Float

Dezimalzahlen (64-bit Fliesskomma).

```python
pi = 3.14159
wissenschaft = 1.5e-3  # 0.0015
negativ = -2.5
```

**Wichtig: Rundungsfehler!**
```python
0.1 + 0.2  # 0.30000000000000004 (nicht exakt 0.3!)

# Lösung: Decimal-Modul für präzise Berechnungen
from decimal import Decimal
Decimal('0.1') + Decimal('0.2')  # Decimal('0.3')
```

### Complex

Komplexe Zahlen (selten verwendet).

```python
z = 1 + 2j
z.real  # 1.0
z.imag  # 2.0
```

## 📝 String (str)

Unveränderliche Textsequenz.

### String erstellen

```python
# Einfache Anführungszeichen
text1 = 'Hallo'

# Doppelte Anführungszeichen
text2 = "Welt"

# Mehrzeilig
text3 = """Das ist
ein mehrzeiliger
Text"""

# Raw String (keine Escape-Sequenzen)
pfad = r"C:\Users\name"  # Backslash wird nicht escaped
```

### Wichtige String-Methoden

```python
text = "  Python ist toll!  "

# Transformationen
text.upper()        # "  PYTHON IST TOLL!  "
text.lower()        # "  python ist toll!  "
text.capitalize()   # "  python ist toll!  "
text.title()        # "  Python Ist Toll!  "
text.strip()        # "Python ist toll!" (Leerzeichen entfernen)
text.lstrip()       # "Python ist toll!  " (links)
text.rstrip()       # "  Python ist toll!" (rechts)

# Suchen & Ersetzen
text.find("toll")          # 14 (Index, -1 wenn nicht gefunden)
text.index("toll")         # 14 (ValueError wenn nicht gefunden)
text.count("t")            # 3
text.replace("toll", "super")  # "  Python ist super!  "

# Teilen & Verbinden
text.split()               # ["Python", "ist", "toll!"]
"a,b,c".split(",")         # ["a", "b", "c"]
" ".join(["a", "b", "c"])  # "a b c"

# Prüfungen
text.startswith("  Py")    # True
text.endswith("!  ")       # True
"toll" in text             # True
text.isdigit()             # False
text.isalpha()             # False
text.isalnum()             # False
text.islower()             # False
text.isupper()             # False
```

### String-Formatierung

```python
name = "Anna"
alter = 25

# 1. f-strings (Python 3.6+, empfohlen!)
text = f"Hallo {name}, du bist {alter} Jahre alt."
text = f"In 10 Jahren: {alter + 10}"
text = f"Preis: {19.99:.2f} CHF"  # Formatierung

# 2. format()
text = "Hallo {}, du bist {} Jahre alt.".format(name, alter)
text = "Hallo {name}, du bist {alter} Jahre alt.".format(name=name, alter=alter)

# 3. % (veraltet)
text = "Hallo %s, du bist %d Jahre alt." % (name, alter)
```

## 📚 List

Veränderbare, geordnete Sammlung beliebiger Objekte.

### Listen erstellen

```python
# Leer
liste = []
liste = list()

# Mit Werten
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "zwei", 3.0, True]
verschachtelt = [[1, 2], [3, 4]]

# List Comprehension
quadrate = [x**2 for x in range(10)]
gerade = [x for x in range(10) if x % 2 == 0]
```

### Listen manipulieren

```python
liste = [1, 2, 3]

# Hinzufügen
liste.append(4)           # [1, 2, 3, 4]
liste.insert(0, 0)        # [0, 1, 2, 3, 4]
liste.extend([5, 6])      # [0, 1, 2, 3, 4, 5, 6]

# Entfernen
liste.remove(0)           # Ersten Wert 0 entfernen
element = liste.pop()     # Letztes Element entfernen und zurückgeben
element = liste.pop(0)    # Element an Index 0
del liste[0]              # Element an Index 0 löschen
liste.clear()             # Alles löschen

# Suchen
liste.index(3)            # Index von Wert 3
liste.count(3)            # Anzahl des Werts 3
3 in liste                # True/False

# Sortieren
liste.sort()              # In-place sortieren (ändert Liste)
liste.sort(reverse=True)  # Absteigend
sortiert = sorted(liste)  # Neue sortierte Liste
liste.reverse()           # Umkehren
```

### Slicing

```python
liste = [0, 1, 2, 3, 4, 5]

liste[0]       # 0 (erstes Element)
liste[-1]      # 5 (letztes Element)
liste[1:4]     # [1, 2, 3] (Index 1-3)
liste[:3]      # [0, 1, 2] (Anfang bis Index 2)
liste[3:]      # [3, 4, 5] (Index 3 bis Ende)
liste[::2]     # [0, 2, 4] (jedes 2. Element)
liste[::-1]    # [5, 4, 3, 2, 1, 0] (rückwärts)
```

## 📖 Dictionary (dict)

Veränderbare Sammlung von Key-Value-Paaren.

### Dictionaries erstellen

```python
# Leer
dict1 = {}
dict1 = dict()

# Mit Werten
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}

# Dict Comprehension
quadrate = {x: x**2 for x in range(5)}
```

### Dictionaries manipulieren

```python
person = {"name": "Anna", "alter": 25}

# Zugriff
name = person["name"]              # KeyError wenn nicht vorhanden
name = person.get("name")          # None wenn nicht vorhanden
name = person.get("beruf", "Unbekannt")  # Default-Wert

# Hinzufügen/Ändern
person["stadt"] = "Zürich"
person["alter"] = 26

# Entfernen
del person["stadt"]
wert = person.pop("alter")         # Entfernen und Wert zurückgeben
person.popitem()                   # Letztes Item entfernen
person.clear()                     # Alles löschen

# Prüfen
"name" in person                   # True/False
len(person)                        # Anzahl Items

# Alle Keys/Values/Items
person.keys()                      # dict_keys(['name', 'alter'])
person.values()                    # dict_values(['Anna', 25])
person.items()                     # dict_items([('name', 'Anna'), ('alter', 25)])

# Iteration
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

## 📦 Tuple

Unveränderbare, geordnete Sammlung.

```python
# Erstellen
koordinaten = (3, 4)
einzelwert = (42,)  # Komma wichtig!
leer = ()

# Unpacking
x, y = koordinaten  # x=3, y=4

# Verwendung
# - Als Dictionary-Keys (da unveränderbar)
# - Für Return-Werte von Funktionen
# - Wenn Daten nicht geändert werden sollen
```

## 🎲 Set

Veränderbare, ungeordnete Sammlung **einzigartiger** Elemente.

```python
# Erstellen
zahlen = {1, 2, 3, 3, 3}  # {1, 2, 3} (Duplikate entfernt)
leer = set()  # NICHT {} (das ist ein dict!)

# Operationen
a = {1, 2, 3}
b = {3, 4, 5}

a | b  # {1, 2, 3, 4, 5} (Vereinigung)
a & b  # {3} (Schnittmenge)
a - b  # {1, 2} (Differenz)
a ^ b  # {1, 2, 4, 5} (Symmetrische Differenz)

# Hinzufügen/Entfernen
a.add(4)
a.remove(1)      # KeyError wenn nicht vorhanden
a.discard(1)     # Kein Error
a.clear()
```

## ✅ Boolean (bool)

Wahrheitswerte `True` oder `False`.

### Truthiness

```python
# Falsy-Werte (werden als False interpretiert)
bool(0)         # False
bool(0.0)       # False
bool("")        # False (leerer String)
bool([])        # False (leere Liste)
bool({})        # False (leeres Dict)
bool(None)      # False

# Truthy-Werte (alles andere)
bool(1)         # True
bool("text")    # True
bool([1, 2])    # True
```

## 🚫 None

Repräsentiert "kein Wert" oder "nichts".

```python
ergebnis = None

if ergebnis is None:
    print("Kein Ergebnis")

# Nicht verwechseln mit:
if ergebnis == None:  # Funktioniert, aber nicht idiomatisch
if not ergebnis:      # Prüft auf Falsy (None, 0, "", [], etc.)
```

## 🔄 Type Conversion

### Implizite Konvertierung

```python
zahl = 5 + 2.5  # 7.5 (int → float automatisch)
```

### Explizite Konvertierung

```python
# Zu String
str(42)           # "42"
str(3.14)         # "3.14"
str([1, 2])       # "[1, 2]"

# Zu Integer
int("42")         # 42
int(3.7)          # 3 (abgeschnitten!)
int("10", 2)      # 2 (Binär zu Dezimal)

# Zu Float
float("3.14")     # 3.14
float(42)         # 42.0

# Zu Liste
list("abc")       # ['a', 'b', 'c']
list((1, 2, 3))   # [1, 2, 3]
list({1, 2, 3})   # [1, 2, 3]

# Zu Set (Duplikate entfernen)
set([1, 2, 2, 3]) # {1, 2, 3}

# Zu Dictionary
dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
```

## 🎯 Welchen Datentyp wählen?

### Entscheidungshilfe

**Liste verwenden wenn:**
- Reihenfolge wichtig ist
- Duplikate erlaubt sind
- Daten verändert werden sollen
- Index-Zugriff nötig ist

**Dictionary verwenden wenn:**
- Key-Value-Zuordnung nötig ist
- Schneller Zugriff per Key wichtig ist
- Strukturierte Daten gespeichert werden

**Set verwenden wenn:**
- Duplikate nicht erlaubt sind
- Membership-Tests (x in set) häufig sind
- Mengen-Operationen (Vereinigung, Schnittmenge) nötig sind

**Tuple verwenden wenn:**
- Daten unveränderbar sein sollen
- Als Dictionary-Key verwendet werden soll
- Funktion mehrere Werte zurückgibt

## 🐛 Häufige Fehler

### 1. List vs. Tuple Verwechslung

```python
# ❌ Falsch
tuple = [1, 2, 3]  # Das ist eine Liste!

# ✅ Richtig
tuple = (1, 2, 3)
```

### 2. Leeres Set erstellen

```python
# ❌ Falsch
empty = {}  # Das ist ein Dictionary!

# ✅ Richtig
empty = set()
```

### 3. Mutable Default Arguments

```python
# ❌ Falsch (Bug!)
def add_item(item, liste=[]):
    liste.append(item)
    return liste

# ✅ Richtig
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

### 4. String Konkatenation in Schleifen

```python
# ❌ Ineffizient
text = ""
for i in range(1000):
    text += str(i)  # Jedes Mal neuer String!

# ✅ Effizient
text = "".join(str(i) for i in range(1000))
```

## 📚 Weiterführende Ressourcen

- [Python Docs: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Real Python: Data Types](https://realpython.com/python-data-types/)
- [PEP 8: Style Guide](https://pep8.org/)

---

**Zurück zu Materialien:** [README](./README.md)
