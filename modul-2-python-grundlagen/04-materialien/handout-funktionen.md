# Handout: Python-Funktionen

Umfassender Leitfaden für Funktionen in Python aus Modul 2.

## 🎯 Lernziele

Nach diesem Handout können Sie:
- Funktionen definieren und aufrufen
- Parameter und Rückgabewerte verwenden
- Docstrings schreiben
- Type Hints einsetzen
- Best Practices für Funktionen anwenden

## 📖 Grundlagen

### Einfache Funktion

```python
def gruss():
    print("Hallo Welt!")

# Aufruf
gruss()  # Ausgabe: Hallo Welt!
```

### Funktion mit Parameter

```python
def gruss(name):
    print(f"Hallo {name}!")

gruss("Anna")  # Ausgabe: Hallo Anna!
```

### Funktion mit Rückgabewert

```python
def addiere(a, b):
    return a + b

ergebnis = addiere(5, 3)  # 8
```

## 📝 Parameter

### Positions-Parameter

```python
def vollstaendiger_name(vorname, nachname):
    return f"{vorname} {nachname}"

vollstaendiger_name("Anna", "Müller")  # "Anna Müller"
```

### Keyword-Parameter

```python
def beschreibe_person(name, alter, stadt):
    return f"{name}, {alter} Jahre, aus {stadt}"

# Mit Keywords (Reihenfolge egal)
beschreibe_person(stadt="Zürich", name="Anna", alter=25)
```

### Default-Werte

```python
def gruss(name, sprache="DE"):
    if sprache == "DE":
        return f"Hallo {name}"
    elif sprache == "EN":
        return f"Hello {name}"
    else:
        return f"Hi {name}"

gruss("Anna")           # "Hallo Anna" (Default)
gruss("Anna", "EN")     # "Hello Anna"
```

### *args (Variable Positional Arguments)

```python
def summe(*zahlen):
    """Summiert beliebig viele Zahlen."""
    return sum(zahlen)

summe(1, 2, 3)        # 6
summe(1, 2, 3, 4, 5)  # 15
```

### **kwargs (Variable Keyword Arguments)

```python
def person_info(**infos):
    """Zeigt beliebig viele Person-Infos."""
    for key, value in infos.items():
        print(f"{key}: {value}")

person_info(name="Anna", alter=25, stadt="Zürich")
# name: Anna
# alter: 25
# stadt: Zürich
```

### Kombiniert

```python
def funktion(a, b, *args, key1="default", **kwargs):
    """
    a, b: Pflicht-Parameter
    *args: Variable Positional Arguments
    key1: Keyword mit Default
    **kwargs: Variable Keyword Arguments
    """
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"key1: {key1}")
    print(f"kwargs: {kwargs}")

funktion(1, 2, 3, 4, key1="wert", key2="extra")
# a: 1, b: 2
# args: (3, 4)
# key1: wert
# kwargs: {'key2': 'extra'}
```

## 🔙 Return Statement

### Einzelner Rückgabewert

```python
def quadrat(x):
    return x ** 2

ergebnis = quadrat(5)  # 25
```

### Mehrere Rückgabewerte (Tuple)

```python
def teile_mit_rest(dividend, divisor):
    quotient = dividend // divisor
    rest = dividend % divisor
    return quotient, rest

q, r = teile_mit_rest(17, 5)  # q=3, r=2
```

### Früher Return

```python
def ist_positiv(zahl):
    if zahl <= 0:
        return False
    return True
```

### Kein Return (implizit None)

```python
def print_nachricht(text):
    print(text)
    # Kein return → gibt None zurück

ergebnis = print_nachricht("Hallo")  # None
```

## 📚 Type Hints

### Grundlegende Type Hints

```python
def addiere(a: int, b: int) -> int:
    return a + b

def gruss(name: str) -> str:
    return f"Hallo {name}"

def ist_erwachsen(alter: int) -> bool:
    return alter >= 18
```

### Listen und Dictionaries

```python
from typing import List, Dict, Tuple, Optional

def verarbeite_zahlen(zahlen: List[int]) -> int:
    return sum(zahlen)

def person_erstellen(name: str, alter: int) -> Dict[str, any]:
    return {"name": name, "alter": alter}

def koordinaten() -> Tuple[float, float]:
    return (3.14, 2.71)

def finde_person(name: str) -> Optional[Dict[str, any]]:
    # Optional bedeutet: Dict oder None
    return None  # Wenn nicht gefunden
```

### Union Types

```python
from typing import Union

def formatiere_wert(wert: Union[int, float, str]) -> str:
    return str(wert)

# Ab Python 3.10: Syntax mit |
def formatiere_wert(wert: int | float | str) -> str:
    return str(wert)
```

## 📖 Docstrings

### Google Style (empfohlen)

```python
def berechne_flaeche(laenge: float, breite: float) -> float:
    """
    Berechnet die Fläche eines Rechtecks.

    Args:
        laenge: Länge des Rechtecks in Metern
        breite: Breite des Rechtecks in Metern

    Returns:
        Fläche in Quadratmetern

    Raises:
        ValueError: Wenn Länge oder Breite negativ

    Examples:
        >>> berechne_flaeche(5, 3)
        15.0
        >>> berechne_flaeche(10, 2)
        20.0
    """
    if laenge < 0 or breite < 0:
        raise ValueError("Länge und Breite müssen positiv sein")
    return laenge * breite
```

### NumPy Style

```python
def berechne_flaeche(laenge, breite):
    """
    Berechnet die Fläche eines Rechtecks.

    Parameters
    ----------
    laenge : float
        Länge des Rechtecks in Metern
    breite : float
        Breite des Rechtecks in Metern

    Returns
    -------
    float
        Fläche in Quadratmetern

    Examples
    --------
    >>> berechne_flaeche(5, 3)
    15.0
    """
    return laenge * breite
```

### Einzeiler

```python
def quadrat(x):
    """Gibt das Quadrat von x zurück."""
    return x ** 2
```

## 🔧 Lambda-Funktionen

### Grundsyntax

```python
# Normale Funktion
def quadrat(x):
    return x ** 2

# Als Lambda
quadrat = lambda x: x ** 2

# Verwendung
quadrat(5)  # 25
```

### Praktische Anwendungen

```python
# Mit sorted()
paare = [(1, 'eins'), (3, 'drei'), (2, 'zwei')]
sortiert = sorted(paare, key=lambda x: x[0])
# [(1, 'eins'), (2, 'zwei'), (3, 'drei')]

# Mit map()
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x**2, zahlen))
# [1, 4, 9, 16, 25]

# Mit filter()
gerade = list(filter(lambda x: x % 2 == 0, zahlen))
# [2, 4]
```

## 🎯 Scope und Namespaces

### Lokale vs. Globale Variablen

```python
global_var = "global"

def funktion():
    lokal_var = "lokal"
    print(global_var)   # Lesezugriff auf global
    print(lokal_var)

funktion()
# print(lokal_var)  # NameError! Nicht ausserhalb sichtbar
```

### Global Keyword

```python
zaehler = 0

def inkrementiere():
    global zaehler
    zaehler += 1

inkrementiere()
print(zaehler)  # 1
```

### Nonlocal Keyword

```python
def aeussere():
    x = "aussen"

    def innere():
        nonlocal x
        x = "innen"

    innere()
    print(x)  # "innen"
```

## 🏗️ Funktions-Design Best Practices

### 1. Single Responsibility Principle

```python
# ❌ Schlecht: Funktion macht zu viel
def verarbeite_daten_und_speichere(daten, dateiname):
    # Validierung
    if not daten:
        raise ValueError("Keine Daten")
    # Verarbeitung
    verarbeitet = [d * 2 for d in daten]
    # Speichern
    with open(dateiname, 'w') as f:
        for d in verarbeitet:
            f.write(str(d) + '\n')

# ✅ Gut: Aufgeteilt in separate Funktionen
def validiere_daten(daten):
    if not daten:
        raise ValueError("Keine Daten")

def verarbeite_daten(daten):
    return [d * 2 for d in daten]

def speichere_daten(daten, dateiname):
    with open(dateiname, 'w') as f:
        for d in daten:
            f.write(str(d) + '\n')
```

### 2. Kurze Funktionen (max. 20-30 Zeilen)

```python
# ❌ Zu lang
def grosse_funktion():
    # 100 Zeilen Code...
    pass

# ✅ In kleinere Funktionen aufteilen
def teilfunktion1():
    pass

def teilfunktion2():
    pass

def hauptfunktion():
    teilfunktion1()
    teilfunktion2()
```

### 3. Aussagekräftige Namen

```python
# ❌ Schlecht
def f(x, y):
    return x + y

# ✅ Gut
def addiere_zahlen(erste_zahl, zweite_zahl):
    return erste_zahl + zweite_zahl
```

### 4. Vermeide Seiteneffekte

```python
# ❌ Schlecht: Ändert globalen Zustand
ergebnisse = []

def addiere_zu_ergebnissen(wert):
    ergebnisse.append(wert)  # Seiteneffekt!

# ✅ Gut: Pure Function
def addiere_zu_liste(liste, wert):
    neue_liste = liste.copy()
    neue_liste.append(wert)
    return neue_liste
```

### 5. Defensive Programmierung

```python
def dividiere(dividend, divisor):
    """Dividiert zwei Zahlen mit Fehlerbehandlung."""
    if not isinstance(dividend, (int, float)):
        raise TypeError("dividend muss eine Zahl sein")
    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor muss eine Zahl sein")
    if divisor == 0:
        raise ValueError("Division durch 0 nicht erlaubt")

    return dividend / divisor
```

## 🎨 Dekoratoren (Fortgeschritten)

### Einfacher Dekorator

```python
def mein_dekorator(func):
    def wrapper():
        print("Vor der Funktion")
        func()
        print("Nach der Funktion")
    return wrapper

@mein_dekorator
def sag_hallo():
    print("Hallo!")

sag_hallo()
# Ausgabe:
# Vor der Funktion
# Hallo!
# Nach der Funktion
```

### Timer-Dekorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ergebnis = func(*args, **kwargs)
        ende = time.time()
        print(f"{func.__name__} dauerte {ende - start:.4f} Sekunden")
        return ergebnis
    return wrapper

@timer
def langsame_funktion():
    time.sleep(1)
    return "Fertig"
```

## 🐛 Häufige Fehler

### 1. Mutable Default Arguments

```python
# ❌ BUG!
def add_item(item, liste=[]):
    liste.append(item)
    return liste

add_item(1)  # [1]
add_item(2)  # [1, 2] <- Unerwartet!

# ✅ Richtig
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

### 2. Vergessenes Return

```python
# ❌ Falsch
def addiere(a, b):
    a + b  # Kein return!

ergebnis = addiere(5, 3)  # None

# ✅ Richtig
def addiere(a, b):
    return a + b
```

### 3. Global ohne global Keyword

```python
zaehler = 0

# ❌ Falsch
def inkrementiere():
    zaehler += 1  # UnboundLocalError!

# ✅ Richtig
def inkrementiere():
    global zaehler
    zaehler += 1
```

## 📊 Code-Beispiel: Vollständige Funktion

```python
from typing import List, Optional


def berechne_durchschnitt(zahlen: List[float], runden: bool = True) -> Optional[float]:
    """
    Berechnet den Durchschnitt einer Zahlenliste.

    Args:
        zahlen: Liste von Zahlen
        runden: Wenn True, rundet auf 2 Dezimalstellen (Standard: True)

    Returns:
        Durchschnitt oder None wenn Liste leer

    Raises:
        TypeError: Wenn zahlen keine Liste ist
        ValueError: Wenn Liste nicht-numerische Werte enthält

    Examples:
        >>> berechne_durchschnitt([1, 2, 3, 4, 5])
        3.0
        >>> berechne_durchschnitt([1.5, 2.5, 3.5], runden=False)
        2.5
        >>> berechne_durchschnitt([])
        None
    """
    # Validierung
    if not isinstance(zahlen, list):
        raise TypeError("zahlen muss eine Liste sein")

    if not zahlen:
        return None

    if not all(isinstance(z, (int, float)) for z in zahlen):
        raise ValueError("Alle Elemente müssen Zahlen sein")

    # Berechnung
    durchschnitt = sum(zahlen) / len(zahlen)

    # Runden wenn gewünscht
    if runden:
        durchschnitt = round(durchschnitt, 2)

    return durchschnitt


# Tests
if __name__ == "__main__":
    assert berechne_durchschnitt([1, 2, 3, 4, 5]) == 3.0
    assert berechne_durchschnitt([1.5, 2.5, 3.5], runden=False) == 2.5
    assert berechne_durchschnitt([]) is None
    print("✓ Alle Tests bestanden")
```

## 🎓 Zusammenfassung

### Gute Funktion ✅

- **Ein klarer Zweck** (Single Responsibility)
- **Aussagekräftiger Name** (Verb + Subjekt)
- **Type Hints** für Parameter und Return
- **Docstring** mit Beschreibung, Args, Returns, Examples
- **Fehlerbehandlung** mit Validierung
- **Kurz** (max. 20-30 Zeilen)
- **Pure** (keine Seiteneffekte wenn möglich)
- **Testbar** (mit klaren Input/Output)

### Schlechte Funktion ❌

- Macht zu viel
- Unklarer Name (z.B. `process_data()`)
- Keine Type Hints
- Kein Docstring
- Keine Fehlerbehandlung
- Zu lang (>50 Zeilen)
- Viele Seiteneffekte
- Schwer testbar

## 📚 Weiterführende Ressourcen

- [Python Docs: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Functions](https://realpython.com/defining-your-own-python-function/)
- [PEP 257: Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484: Type Hints](https://peps.python.org/pep-0484/)

---

**Zurück zu Materialien:** [README](./README.md)
