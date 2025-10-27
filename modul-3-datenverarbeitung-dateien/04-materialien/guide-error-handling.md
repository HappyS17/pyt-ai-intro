# Error Handling Guide

Umfassender Guide für Exception Handling in Python.

## Grundlagen

### try/except

```python
try:
    # Code der Fehler werfen könnte
    datei = open('daten.txt', 'r')
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
except IOError as e:
    print(f"IO-Fehler: {e}")
finally:
    # Wird immer ausgeführt
    if 'datei' in locals():
        datei.close()
```

### Mit with-Statement (empfohlen)

```python
try:
    with open('daten.txt', 'r') as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
# Datei wird automatisch geschlossen
```

## Häufige Exceptions

### FileNotFoundError

```python
try:
    with open('nicht_da.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("Datei existiert nicht")
    # Erstelle Datei oder verwende Default
```

### PermissionError

```python
try:
    with open('/root/datei.txt', 'w') as f:
        f.write("Test")
except PermissionError:
    print("Keine Schreibrechte")
```

### ValueError

```python
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Bitte Zahl eingeben")
```

### JSONDecodeError

```python
import json

try:
    data = json.loads('ungültiges json')
except json.JSONDecodeError as e:
    print(f"JSON-Fehler: {e}")
```

## Best Practices

### 1. Spezifische Exceptions zuerst

```python
# ❌ Schlecht
try:
    # Code
except Exception:
    print("Fehler")

# ✅ Gut
try:
    # Code
except FileNotFoundError:
    print("Datei nicht gefunden")
except PermissionError:
    print("Keine Rechte")
except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
```

### 2. Nicht zu viel in try

```python
# ❌ Schlecht
try:
    datei = open('daten.txt', 'r')
    inhalt = datei.read()
    verarbeitet = verarbeite(inhalt)
    speichere(verarbeitet)
except Exception:
    print("Irgendwas ging schief")

# ✅ Gut
try:
    datei = open('daten.txt', 'r')
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
    return

try:
    verarbeitet = verarbeite(inhalt)
except ValueError:
    print("Ungültige Daten")
    return
```

### 3. Informative Fehlermeldungen

```python
# ❌ Schlecht
except Exception:
    print("Fehler")

# ✅ Gut
except FileNotFoundError as e:
    print(f"Datei '{filename}' nicht gefunden")
    print(f"Gesucht in: {os.getcwd()}")
```

### 4. Cleanup mit finally

```python
datei = None
try:
    datei = open('daten.txt', 'r')
    # Verarbeitung
except Exception as e:
    print(f"Fehler: {e}")
finally:
    if datei:
        datei.close()
```

## Eigene Exceptions

```python
class DatenValidierungsFehler(Exception):
    """Fehler bei Datenvalidierung."""
    pass

def validiere_alter(alter: int):
    if alter < 0 or alter > 150:
        raise DatenValidierungsFehler(
            f"Ungültiges Alter: {alter}"
        )

try:
    validiere_alter(-5)
except DatenValidierungsFehler as e:
    print(f"Validierung fehlgeschlagen: {e}")
```

## Exception Chaining

```python
try:
    # Ursprünglicher Fehler
    daten = json.loads(text)
except json.JSONDecodeError as e:
    # Neuer Fehler mit Kontext
    raise ValueError("Konfiguration ungültig") from e
```

## Logging statt print

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    # Code
except FileNotFoundError as e:
    logging.error(f"Datei nicht gefunden: {e}")
except Exception as e:
    logging.exception("Unerwarteter Fehler")
```

## Patterns

### Retry mit Exponential Backoff

```python
import time

def retry_operation(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            print(f"Versuch {attempt + 1} fehlgeschlagen, warte {wait_time}s")
            time.sleep(wait_time)
```

### Context Manager

```python
class DateiManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Exception nicht unterdrücken

with DateiManager('daten.txt') as f:
    data = f.read()
```

## Checkliste

- [ ] Spezifische Exceptions verwenden
- [ ] Informative Fehlermeldungen
- [ ] finally für Cleanup
- [ ] Nicht zu viel in try-Block
- [ ] Logging statt print
- [ ] Exceptions dokumentieren

---

**Zurück zu:** [Materialien README](./README.md)
