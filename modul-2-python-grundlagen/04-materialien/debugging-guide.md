# Debugging-Guide

Strategien zum Finden und Beheben von Fehlern.

## 🐛 Häufige Fehler

### SyntaxError

```python
# Fehler: Doppelpunkt vergessen
if x > 5
    print("Gross")

# Lösung:
if x > 5:
    print("Gross")
```

### IndentationError

```python
# Fehler: Falsche Einrückung
def funktion():
print("Test")

# Lösung:
def funktion():
    print("Test")
```

### NameError

```python
# Fehler: Variable nicht definiert
print(name)

# Lösung:
name = "Anna"
print(name)
```

### TypeError

```python
# Fehler: Falscher Typ
"5" + 3

# Lösung:
int("5") + 3  # 8
"5" + str(3)  # "53"
```

### IndexError

```python
# Fehler: Index ausserhalb
liste = [1, 2, 3]
print(liste[5])

# Lösung:
if len(liste) > 5:
    print(liste[5])
```

## 🔍 Debugging-Strategien

### 1. Print-Debugging

```python
def berechne(x, y):
    print(f"x={x}, y={y}")  # Debug
    ergebnis = x + y
    print(f"ergebnis={ergebnis}")  # Debug
    return ergebnis
```

### 2. Schrittweise testen

```python
# Testen Sie jede Zeile einzeln
x = 5
print(x)  # OK?
y = x * 2
print(y)  # OK?
```

### 3. Vereinfachen

```python
# Komplex:
ergebnis = [x**2 for x in range(10) if x % 2 == 0]

# Vereinfacht zum Debuggen:
ergebnis = []
for x in range(10):
    print(f"x={x}")
    if x % 2 == 0:
        print(f"  gerade!")
        ergebnis.append(x**2)
```

### 4. KI um Hilfe fragen

```text
Ich habe folgenden Fehler:
[Fehlermeldung]

Mein Code:
[Code]

Was ist das Problem?
```

## ✅ Checkliste

- [ ] Fehlermeldung genau lesen
- [ ] Zeile mit Fehler identifizieren
- [ ] Print-Statements einfügen
- [ ] Schrittweise testen
- [ ] Bei Bedarf KI fragen

---

**Zurück zu:** [Materialien README](./README.md)
