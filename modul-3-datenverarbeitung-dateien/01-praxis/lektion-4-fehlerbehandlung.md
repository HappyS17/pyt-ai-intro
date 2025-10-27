# Lektion 4: Fehlerbehandlung & Logging

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Lernziele

- try/except/finally verwenden
- Spezifische Exceptions behandeln
- logging-Modul nutzen

## 📚 Theorie (15 Min.)

### try/except

```python
try:
    datei = open("datei.txt", "r")
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
except IOError:
    print("Fehler beim Lesen")
finally:
    datei.close()
```

### Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logging.info("Programm gestartet")
logging.warning("Warnung")
logging.error("Fehler aufgetreten")
```

## 💻 Live-Demo (20 Min.)

### Demo: Robuste Datei-Verarbeitung

```python
"""Robuste CSV-Verarbeitung"""
import csv
import logging

def verarbeite_csv(datei: str) -> list:
    """Verarbeitet CSV mit Fehlerbehandlung."""
    logging.info(f"Verarbeite {datei}")
    
    try:
        with open(datei, "r") as f:
            reader = csv.DictReader(f)
            daten = list(reader)
            logging.info(f"{len(daten)} Zeilen gelesen")
            return daten
    
    except FileNotFoundError:
        logging.error(f"Datei {datei} nicht gefunden")
        return []
    
    except Exception as e:
        logging.error(f"Unerwarteter Fehler: {e}")
        return []
```

## ✏️ Übung (15 Min.)

Fehlerbehandlung mit KI implementieren.

---

**Zurück zu:** [Praxis README](./README.md)
