# Lektion 3: JSON & APIs

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

- JSON parsen und erstellen
- API-Calls durchführen
- Response-Daten verarbeiten

## 📚 Theorie (15 Min.)

### JSON-Modul

```python
import json

# String → Python
json_string = '{"name": "Anna", "alter": 25}'
daten = json.loads(json_string)

# Python → String
daten = {"name": "Anna", "alter": 25}
json_string = json.dumps(daten, indent=2)

# Datei lesen
with open("config.json", "r") as f:
    config = json.load(f)

# Datei schreiben
with open("output.json", "w") as f:
    json.dump(daten, f, indent=2)
```

### requests-Library

```python
import requests

# GET Request
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    daten = response.json()

# POST Request
daten = {"name": "Anna"}
response = requests.post("https://api.example.com/users", json=daten)
```

## 💻 Live-Demo (20 Min.)

### Demo: Wetter-API

```python
"""Wetter-Daten abrufen"""
import requests
import json

def hole_wetter(stadt: str) -> dict:
    """Holt Wetter-Daten."""
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": stadt,
        "appid": "YOUR_API_KEY",
        "units": "metric"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Fehler: {response.status_code}")

# Verwenden
wetter = hole_wetter("Zürich")
print(f"Temperatur: {wetter['main']['temp']}°C")

# Speichern
with open("wetter.json", "w") as f:
    json.dump(wetter, f, indent=2)
```

## ✏️ Übung (15 Min.)

API-Integration mit KI implementieren.

---

**Weiter zu:** [Lektion 4 - Fehlerbehandlung](./lektion-4-fehlerbehandlung.md)
