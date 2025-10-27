# Lektion 1: Dateien lesen & schreiben

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Lernziele

- Dateien mit verschiedenen Modes öffnen
- with Statement verwenden
- Text lesen und schreiben
- Pfade korrekt handhaben

## 📚 Theorie (15 Min.)

### Dateien öffnen

```python
# Ohne with (nicht empfohlen)
file = open("datei.txt", "r")
inhalt = file.read()
file.close()

# Mit with (empfohlen)
with open("datei.txt", "r") as file:
    inhalt = file.read()
# Datei wird automatisch geschlossen
```

### File Modes

```python
"r"   # Read (Standard) - Fehler wenn nicht existiert
"w"   # Write - Überschreibt oder erstellt
"a"   # Append - Anhängen
"r+"  # Read + Write
"rb"  # Read Binary
```

### Lesen

```python
# Alles lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()

# Zeile für Zeile
with open("datei.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())

# Alle Zeilen als Liste
with open("datei.txt", "r") as f:
    zeilen = f.readlines()
```

### Schreiben

```python
# Überschreiben
with open("datei.txt", "w") as f:
    f.write("Hallo Welt\n")
    f.write("Zweite Zeile\n")

# Anhängen
with open("datei.txt", "a") as f:
    f.write("Neue Zeile\n")
```

### Pfade

```python
from pathlib import Path

# Pfad erstellen
pfad = Path("daten/datei.txt")

# Prüfen
if pfad.exists():
    print("Existiert")

# Verzeichnis erstellen
pfad.parent.mkdir(parents=True, exist_ok=True)
```

## 💻 Live-Demo (20 Min.)

### Demo 1: Log-Analyse

```python
"""Log-Datei analysieren"""

def analysiere_log(dateiname: str) -> dict:
    """Analysiert Log-Datei."""
    stats = {
        "zeilen": 0,
        "errors": 0,
        "warnings": 0
    }
    
    with open(dateiname, "r") as f:
        for zeile in f:
            stats["zeilen"] += 1
            if "ERROR" in zeile:
                stats["errors"] += 1
            elif "WARNING" in zeile:
                stats["warnings"] += 1
    
    return stats

# Verwenden
stats = analysiere_log("app.log")
print(f"Zeilen: {stats['zeilen']}")
print(f"Errors: {stats['errors']}")
```

### Demo 2: Backup erstellen

```python
"""Datei-Backup"""
from pathlib import Path
from datetime import datetime

def erstelle_backup(datei: str) -> str:
    """Erstellt Backup mit Zeitstempel."""
    pfad = Path(datei)
    
    if not pfad.exists():
        raise FileNotFoundError(f"{datei} nicht gefunden")
    
    # Backup-Name mit Zeitstempel
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{pfad.stem}_{timestamp}{pfad.suffix}"
    backup_pfad = pfad.parent / "backup" / backup_name
    
    # Backup-Verzeichnis erstellen
    backup_pfad.parent.mkdir(exist_ok=True)
    
    # Kopieren
    with open(pfad, "r") as quelle:
        with open(backup_pfad, "w") as ziel:
            ziel.write(quelle.read())
    
    return str(backup_pfad)
```

## ✏️ Übung (15 Min.)

Wählen Sie EINE Option:

### Option A: Wort-Zähler

Programm das:
- Text-Datei einliest
- Wörter zählt
- Häufigstes Wort findet
- Ergebnis in neue Datei schreibt

### Option B: Todo-Liste

Programm das:
- Todos aus Datei liest
- Neue Todos hinzufügt
- Todos als erledigt markiert
- In Datei speichert

---

**Weiter zu:** [Lektion 2 - CSV](./lektion-2-csv.md)
