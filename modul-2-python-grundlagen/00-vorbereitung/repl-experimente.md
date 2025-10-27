# Python REPL Experimente

**Zeitaufwand:** 45 Minuten  
**Ziel:** Praktische Erfahrung mit Python sammeln

## 🎯 Was ist die REPL?

**REPL** = Read-Eval-Print-Loop

Eine interaktive Python-Umgebung, in der Sie Code direkt ausführen können.

## 🚀 REPL starten

### Option 1: Python-Konsole

```bash
# Terminal öffnen und eingeben:
python

# Oder:
python3
```

Sie sehen:

```text
Python 3.11.0 (main, Oct 24 2022, 18:26:48)
>>>
```

### Option 2: VS Code Python Interactive

1. VS Code öffnen
2. Command Palette (Cmd/Ctrl + Shift + P)
3. "Python: Start REPL" eingeben

### Option 3: Jupyter Notebook (optional)

Falls installiert, können Sie auch Jupyter nutzen.

## 📝 Experimente durchführen

### Experiment 1: Zahlen (10 Min.)

Probieren Sie folgendes aus:

```python
# Einfache Berechnungen
>>> 5 + 3
>>> 10 - 4
>>> 7 * 6
>>> 20 / 4
>>> 20 // 3  # Ganzzahlige Division
>>> 20 % 3   # Modulo (Rest)
>>> 2 ** 8   # Potenz

# Verschiedene Zahlentypen
>>> type(5)
>>> type(5.0)
>>> type(5 + 3.0)

# Grosse Zahlen
>>> 999999999999999999999 * 2
```

**Dokumentieren Sie:**

- Was ist der Unterschied zwischen `/` und `//`?
- Was macht der `%` Operator?
- Was passiert bei `int + float`?

### Experiment 2: Strings (10 Min.)

```python
# String-Operationen
>>> "Hallo" + " " + "Welt"
>>> "Python" * 3
>>> "GROSS".lower()
>>> "klein".upper()
>>> "  Leerzeichen  ".strip()

# String-Methoden
>>> text = "Python ist toll"
>>> text.split()
>>> text.replace("toll", "super")
>>> text.startswith("Python")
>>> text.endswith("toll")

# String-Formatierung
>>> name = "Anna"
>>> alter = 25
>>> f"Ich heisse {name} und bin {alter} Jahre alt"
```

**Dokumentieren Sie:**

- Wie kombiniert man Strings?
- Was macht `.split()`?
- Wie funktioniert f-String-Formatierung?

### Experiment 3: Listen (10 Min.)

```python
# Listen erstellen
>>> zahlen = [1, 2, 3, 4, 5]
>>> namen = ["Anna", "Bob", "Clara"]
>>> gemischt = [1, "zwei", 3.0, True]

# Listen-Operationen
>>> zahlen[0]      # Erstes Element
>>> zahlen[-1]     # Letztes Element
>>> zahlen[1:3]    # Slicing
>>> zahlen + [6, 7, 8]
>>> zahlen * 2

# Listen-Methoden
>>> zahlen.append(6)
>>> zahlen.remove(3)
>>> zahlen.sort()
>>> len(zahlen)
>>> sum(zahlen)
>>> max(zahlen)
```

**Dokumentieren Sie:**

- Wie greift man auf Listenelemente zu?
- Was ist Slicing?
- Welche nützlichen Methoden gibt es?

### Experiment 4: Dictionaries (10 Min.)

```python
# Dictionary erstellen
>>> person = {"name": "Anna", "alter": 25, "stadt": "Zürich"}

# Zugriff
>>> person["name"]
>>> person.get("alter")
>>> person.get("beruf", "Unbekannt")  # Mit Default

# Ändern und hinzufügen
>>> person["alter"] = 26
>>> person["beruf"] = "Entwicklerin"

# Dictionary-Methoden
>>> person.keys()
>>> person.values()
>>> person.items()

# Verschachtelte Dictionaries
>>> personen = {
...     "anna": {"alter": 25, "stadt": "Zürich"},
...     "bob": {"alter": 30, "stadt": "Bern"}
... }
>>> personen["anna"]["stadt"]
```

**Dokumentieren Sie:**

- Wie unterscheiden sich Listen und Dictionaries?
- Wann würden Sie ein Dictionary verwenden?
- Was macht `.get()` mit Default-Wert?

### Experiment 5: Freies Experimentieren (5 Min.)

Probieren Sie eigene Ideen aus:

- Kombinieren Sie verschiedene Datentypen
- Verschachteln Sie Listen und Dictionaries
- Testen Sie, was funktioniert und was nicht

## 📊 Dokumentation

### Template für Ihre Notizen

```markdown
# Meine Python REPL Experimente

## 5 Interessante Entdeckungen

1. [Entdeckung 1]
   - Was ich ausprobiert habe: ...
   - Was passiert ist: ...
   - Warum das interessant ist: ...

2. [Entdeckung 2]
   ...

3. [Entdeckung 3]
   ...

4. [Entdeckung 4]
   ...

5. [Entdeckung 5]
   ...

## 3 Dinge, die ich nicht verstehe

1. [Unklarheit 1]
   - Was ich versucht habe: ...
   - Was unklar ist: ...

2. [Unklarheit 2]
   ...

3. [Unklarheit 3]
   ...

## Screenshots

[Hier Screenshots Ihrer interessantesten Experimente einfügen]
```

## ✅ Checkliste

- [ ] REPL gestartet
- [ ] Zahlen-Experimente durchgeführt
- [ ] String-Experimente durchgeführt
- [ ] Listen-Experimente durchgeführt
- [ ] Dictionary-Experimente durchgeführt
- [ ] Freies Experimentieren
- [ ] 5 Entdeckungen dokumentiert
- [ ] 3 Unklarheiten notiert
- [ ] Screenshots gemacht

## 💡 Tipps

### Tipp 1: Fehler sind OK

Wenn etwas nicht funktioniert, ist das eine Lernchance! Lesen Sie die Fehlermeldung.

### Tipp 2: Tab-Completion

Drücken Sie Tab nach einem Punkt, um verfügbare Methoden zu sehen:

```python
>>> "text".  # Jetzt Tab drücken
```

### Tipp 3: Hilfe nutzen

```python
>>> help(str)
>>> help(list.append)
```

### Tipp 4: Verlauf nutzen

Mit Pfeiltasten ↑↓ können Sie vorherige Befehle wiederholen.

## 🆘 Troubleshooting

### Problem: REPL startet nicht

```bash
# Prüfen Sie die Python-Installation
python --version

# Oder versuchen Sie:
python3 --version
```

### Problem: Syntax-Fehler

Das ist normal beim Lernen! Lesen Sie die Fehlermeldung genau.

### Problem: REPL beenden

```python
>>> exit()
# Oder Ctrl+D (Mac/Linux) / Ctrl+Z (Windows)
```

---

**Weiter zu:** [KI-Erklärungen](./ki-erklaerungen.md)  
**Zurück zu:** [Leseauftrag](./leseauftrag.md)
