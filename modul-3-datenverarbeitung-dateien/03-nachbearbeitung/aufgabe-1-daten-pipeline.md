# Aufgabe 1: Daten-Pipeline

**Zeitaufwand:** 120 Minuten | **Punkte:** 30% | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Erstellen Sie eine vollständige Daten-Pipeline, die CSV-Daten einliest, bereinigt, transformiert und als JSON-Report ausgibt.

## 📋 Anforderungen

### Funktionale Anforderungen

1. **Daten einlesen**
   - CSV-Datei mit Verkaufsdaten einlesen
   - Fehlerbehandlung für fehlende Datei

2. **Datenbereinigung**
   - Duplikate entfernen
   - Fehlende Werte behandeln
   - Ungültige Einträge filtern

3. **Transformation**
   - Datumsformate standardisieren
   - Preise berechnen (Menge × Einzelpreis)
   - Kategorien gruppieren

4. **Report generieren**
   - JSON-Report mit Statistiken
   - Zusammenfassung pro Kategorie
   - Top 5 Produkte

5. **Logging**
   - Alle Schritte loggen
   - Fehler dokumentieren
   - Statistiken ausgeben

### Technische Anforderungen

- Python 3.11+
- Module: `csv`, `json`, `logging`, `datetime`
- Type Hints verwenden
- Docstrings für alle Funktionen
- Exception Handling

## 📊 Testdaten

Erstellen Sie `verkaufsdaten.csv`:

```csv
datum,produkt,kategorie,menge,einzelpreis
2024-01-15,Laptop,Elektronik,2,1200.00
2024-01-15,Maus,Elektronik,5,25.50
2024-01-16,Laptop,Elektronik,2,1200.00
2024-01-16,Buch,Bücher,3,15.99
2024-01-17,Tastatur,Elektronik,,80.00
2024-01-17,Monitor,Elektronik,1,350.00
2024-01-18,Roman,Bücher,2,
2024-01-18,Headset,Elektronik,3,60.00
```

## 🏗️ Struktur

```python
# pipeline.py

import csv
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='pipeline.log'
)

def load_csv(filename: str) -> List[Dict]:
    """Lädt CSV-Datei."""
    pass

def clean_data(data: List[Dict]) -> List[Dict]:
    """Bereinigt Daten."""
    pass

def transform_data(data: List[Dict]) -> List[Dict]:
    """Transformiert Daten."""
    pass

def generate_report(data: List[Dict]) -> Dict:
    """Generiert Report."""
    pass

def save_json(data: Dict, filename: str) -> None:
    """Speichert als JSON."""
    pass

def main():
    """Hauptfunktion."""
    logging.info("Pipeline gestartet")
    
    # 1. Laden
    data = load_csv("verkaufsdaten.csv")
    logging.info(f"{len(data)} Zeilen geladen")
    
    # 2. Bereinigen
    clean = clean_data(data)
    logging.info(f"{len(clean)} Zeilen nach Bereinigung")
    
    # 3. Transformieren
    transformed = transform_data(clean)
    
    # 4. Report
    report = generate_report(transformed)
    
    # 5. Speichern
    save_json(report, "report.json")
    logging.info("Pipeline abgeschlossen")

if __name__ == "__main__":
    main()
```

## 📤 Erwarteter Output

### report.json

```json
{
  "zusammenfassung": {
    "gesamtumsatz": 5891.47,
    "anzahl_verkauefe": 7,
    "durchschnitt": 841.64
  },
  "nach_kategorie": {
    "Elektronik": {
      "umsatz": 5831.50,
      "anzahl": 6
    },
    "Bücher": {
      "umsatz": 59.97,
      "anzahl": 1
    }
  },
  "top_produkte": [
    {
      "produkt": "Laptop",
      "umsatz": 2400.00,
      "anzahl": 2
    },
    {
      "produkt": "Monitor",
      "umsatz": 350.00,
      "anzahl": 1
    }
  ]
}
```

## ✅ Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| Funktionalität | 10 | Pipeline läuft vollständig |
| Datenbereinigung | 5 | Korrekte Behandlung von Problemen |
| Transformation | 5 | Richtige Berechnungen |
| Report | 5 | JSON-Format korrekt |
| Logging | 3 | Aussagekräftige Logs |
| Code-Qualität | 2 | Type Hints, Docstrings |

**Gesamt:** 30 Punkte

## 💡 Tipps

- Beginnen Sie mit KI: "Erstelle eine Daten-Pipeline..."
- Testen Sie jeden Schritt einzeln
- Nutzen Sie `try/except` für Robustheit
- Dokumentieren Sie Annahmen

## 📤 Abgabe

- `pipeline.py` - Hauptprogramm
- `verkaufsdaten.csv` - Testdaten
- `report.json` - Generierter Report
- `pipeline.log` - Log-Datei
- `README.md` - Dokumentation

---

**Zurück zu:** [Nachbearbeitung README](./README.md)
