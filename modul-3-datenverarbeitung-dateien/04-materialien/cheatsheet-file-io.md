# Cheat Sheet: File I/O

Schnellreferenz für Datei-Operationen.

## File Modes

```python
"r"   # Read (Standard)
"w"   # Write (überschreibt)
"a"   # Append (anhängen)
"r+"  # Read + Write
"rb"  # Read Binary
"wb"  # Write Binary
```

## Lesen

```python
# Alles lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()

# Zeile für Zeile
with open("datei.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())

# Alle Zeilen
with open("datei.txt", "r") as f:
    zeilen = f.readlines()
```

## Schreiben

```python
# Überschreiben
with open("datei.txt", "w") as f:
    f.write("Text\n")

# Anhängen
with open("datei.txt", "a") as f:
    f.write("Mehr Text\n")
```

## Pfade

```python
from pathlib import Path

pfad = Path("daten/datei.txt")

# Prüfen
if pfad.exists():
    print("Existiert")

# Erstellen
pfad.parent.mkdir(parents=True, exist_ok=True)
```

---

**Zurück zu:** [Materialien README](./README.md)
