# Übung 3: JSON-Konfiguration

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

JSON-Konfigurationsdateien erstellen und verwalten.

## Wählen Sie EINE Option

### Option A: Konfigurations-Manager

#### Anforderungen

Erstellen Sie ein Programm, das:

- JSON-Konfiguration lädt
- Werte anzeigt
- Werte ändert
- Änderungen speichert

#### Testdaten

Erstellen Sie `config.json`:

```json
{
  "app": {
    "name": "Meine App",
    "version": "1.0.0",
    "debug": true
  },
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "mydb"
  },
  "features": {
    "login": true,
    "registration": false,
    "api": true
  }
}
```

#### Prompt-Vorlage

```text
Erstelle einen Konfigurations-Manager in Python:

Funktionen:
1. load_config(filename) - Lädt JSON
2. get_value(key_path) - Holt Wert (z.B. "app.name")
3. set_value(key_path, value) - Setzt Wert
4. save_config(filename) - Speichert Änderungen

Menü:
1. Zeige Konfiguration
2. Ändere Wert
3. Speichern
4. Beenden

Verwende json-Modul und dict-Navigation.
```

#### Erwartetes Verhalten

```text
=== KONFIGURATIONS-MANAGER ===
1. Zeige Konfiguration
2. Ändere Wert
3. Speichern
4. Beenden

Wahl: 1

App Name: Meine App
Version: 1.0.0
Debug: True
...
```

### Option B: API-Client für öffentliche API

#### Anforderungen

Nutzen Sie eine öffentliche API (z.B. JSONPlaceholder):

- GET-Request durchführen
- JSON-Response parsen
- Daten formatiert ausgeben
- Optional: In Datei speichern

#### API-Beispiel

```text
URL: https://jsonplaceholder.typicode.com/users
Gibt Liste von Benutzern zurück
```

#### Prompt-Vorlage

```text
Erstelle einen API-Client in Python:

Anforderungen:
- Nutzt requests-Library
- GET https://jsonplaceholder.typicode.com/users
- Parsed JSON-Response
- Gibt formatiert aus:
  * Name
  * Email
  * Stadt
- Optional: Speichert in "users.json"

Fehlerbehandlung:
- Netzwerkfehler
- Ungültige JSON-Response
```

#### Erwartete Ausgabe

```text
=== BENUTZER-LISTE ===

1. Leanne Graham
   Email: Sincere@april.biz
   Stadt: Gwenborough

2. Ervin Howell
   Email: Shanna@melissa.tv
   Stadt: Wisokyburgh

...

Gespeichert in: users.json
```

### Option C: JSON-zu-CSV-Konverter

#### Anforderungen

Konvertieren Sie JSON zu CSV:

- JSON-Array einlesen
- Felder extrahieren
- CSV-Datei erstellen

#### Testdaten

Erstellen Sie `daten.json`:

```json
[
  {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich",
    "beruf": "Entwicklerin"
  },
  {
    "name": "Bob",
    "alter": 30,
    "stadt": "Bern",
    "beruf": "Designer"
  },
  {
    "name": "Clara",
    "alter": 28,
    "stadt": "Basel",
    "beruf": "Managerin"
  }
]
```

#### Prompt-Vorlage

```text
Erstelle einen JSON-zu-CSV-Konverter:

Anforderungen:
- Liest "daten.json" (Array von Objekten)
- Extrahiert alle Keys als CSV-Header
- Schreibt Daten in "daten.csv"
- Gibt Statistik aus

Features:
- Automatische Header-Erkennung
- Fehlerbehandlung für inkonsistente Daten
- Optionale Feldauswahl

Verwende json und csv Module.
```

#### Erwartetes Ergebnis

`daten.csv`:

```csv
name,alter,stadt,beruf
Anna,25,Zürich,Entwicklerin
Bob,30,Bern,Designer
Clara,28,Basel,Managerin
```

## 💡 Tipps

- Für API-Calls: `uv sync` (requests ist bereits in pyproject.toml enthalten)
- JSON-Pfade mit `.get()` sicher navigieren
- Pretty-Print mit `json.dumps(data, indent=2)`
- Fehlerbehandlung für ungültiges JSON

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] JSON korrekt gelesen/geschrieben
- [ ] Daten verarbeitet
- [ ] Ausgabe formatiert
- [ ] Fehlerbehandlung implementiert
- [ ] Code dokumentiert

---

**Zurück zu:** [Übungen README](./README.md)
