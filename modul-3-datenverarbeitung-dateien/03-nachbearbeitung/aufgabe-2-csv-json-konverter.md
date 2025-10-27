# Aufgabe 2: CSV-zu-JSON-Konverter

**Zeitaufwand:** 60 Minuten | **Punkte:** 20% | **Schwierigkeit:** ⭐⭐☆

## 🎯 Ziel

Erstellen Sie einen universellen Konverter, der CSV-Dateien in verschiedene JSON-Formate umwandeln kann.

## 📋 Anforderungen

### Funktionale Anforderungen

1. **Basis-Konvertierung**
   - CSV → JSON Array
   - Automatische Header-Erkennung
   - Type Detection (Zahlen, Booleans)

2. **Optionen**
   - `--format`: array, object, nested
   - `--indent`: JSON-Formatierung
   - `--output`: Ausgabedatei

3. **Validierung**
   - CSV-Format prüfen
   - Konsistente Spalten
   - Fehlerbehandlung

## 🏗️ Struktur

```python
# converter.py

import csv
import json
import argparse
from typing import List, Dict, Any

def detect_type(value: str) -> Any:
    """Erkennt Datentyp."""
    # Versuche int
    try:
        return int(value)
    except ValueError:
        pass
    
    # Versuche float
    try:
        return float(value)
    except ValueError:
        pass
    
    # Boolean
    if value.lower() in ['true', 'false']:
        return value.lower() == 'true'
    
    # String
    return value

def csv_to_array(filename: str) -> List[Dict]:
    """Konvertiert CSV zu Array."""
    pass

def csv_to_object(filename: str, key_field: str) -> Dict:
    """Konvertiert CSV zu Object (mit Key)."""
    pass

def main():
    parser = argparse.ArgumentParser(description='CSV zu JSON Konverter')
    parser.add_argument('input', help='Input CSV-Datei')
    parser.add_argument('--format', choices=['array', 'object'], default='array')
    parser.add_argument('--indent', type=int, default=2)
    parser.add_argument('--output', help='Output JSON-Datei')
    
    args = parser.parse_args()
    
    # Konvertierung...

if __name__ == "__main__":
    main()
```

## 📊 Beispiele

### Eingabe: personen.csv

```csv
id,name,alter,aktiv
1,Anna,25,true
2,Bob,30,false
3,Clara,28,true
```

### Format: array

```json
[
  {
    "id": 1,
    "name": "Anna",
    "alter": 25,
    "aktiv": true
  },
  {
    "id": 2,
    "name": "Bob",
    "alter": 30,
    "aktiv": false
  }
]
```

### Format: object (key=id)

```json
{
  "1": {
    "name": "Anna",
    "alter": 25,
    "aktiv": true
  },
  "2": {
    "name": "Bob",
    "alter": 30,
    "aktiv": false
  }
}
```

## 🎯 Verwendung

```bash
# Basis
python converter.py personen.csv

# Mit Optionen
python converter.py personen.csv --format object --output personen.json

# Mit Indent
python converter.py personen.csv --indent 4
```

## ✅ Bewertungskriterien

| Kriterium | Punkte |
|-----------|--------|
| Basis-Konvertierung | 8 |
| Type Detection | 4 |
| CLI-Optionen | 4 |
| Fehlerbehandlung | 2 |
| Dokumentation | 2 |

**Gesamt:** 20 Punkte

## 💡 Tipps

- Nutzen Sie `argparse` für CLI
- Type Detection mit try/except
- JSON-Ausgabe mit `indent` Parameter
- Testen Sie mit verschiedenen CSV-Dateien

## 📤 Abgabe

- `converter.py` - Hauptprogramm
- `README.md` - Verwendungsanleitung
- Beispiel-CSV und -JSON

---

**Zurück zu:** [Nachbearbeitung README](./README.md)
