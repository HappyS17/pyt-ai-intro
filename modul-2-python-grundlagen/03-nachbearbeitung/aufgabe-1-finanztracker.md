# Aufgabe 1: Persönlicher Finanztracker

**Zeitaufwand:** 120 Minuten
**Punkte:** 30% der Nachbearbeitung
**Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

Nach dieser Aufgabe können Sie:

- Komplexe Python-Programme mit mehreren Funktionen strukturieren
- Datenstrukturen (Listen und Dictionaries) kombiniert einsetzen
- Persistente Datenspeicherung mit JSON implementieren
- Benutzerinteraktion über ein Menüsystem realisieren
- Fehlerbehandlung für robuste Programme einbauen

## 📋 Aufgabenstellung

Entwickeln Sie ein Kommandozeilen-Programm zur Verwaltung persönlicher Finanzen. Das Programm soll Einnahmen und Ausgaben tracken, Kategorien verwalten und Statistiken anzeigen können.

### Kernfunktionalität

Das Programm soll folgende Operationen unterstützen:

1. **Transaktion hinzufügen** (Einnahme oder Ausgabe)
2. **Alle Transaktionen anzeigen**
3. **Transaktionen nach Kategorie filtern**
4. **Statistiken berechnen** (Summen, Durchschnitt, Saldo)
5. **Daten in Datei speichern** und laden

### Datenstruktur

Jede Transaktion sollte folgende Informationen enthalten:

```python
{
    "id": 1,                      # Eindeutige ID
    "datum": "2025-01-15",       # ISO-Format
    "typ": "Ausgabe",            # "Einnahme" oder "Ausgabe"
    "kategorie": "Lebensmittel", # z.B. Gehalt, Lebensmittel, Transport
    "betrag": 45.50,             # Float
    "beschreibung": "Wocheneinkauf"
}
```

## ✅ Muss-Kriterien (erforderlich für 70% der Punkte)

- [ ] **Menüsystem:** Interaktives Menü mit mindestens 6 Optionen
- [ ] **Transaktion hinzufügen:** Benutzer kann Einnahmen und Ausgaben eingeben
- [ ] **Transaktionsliste:** Alle Transaktionen anzeigen (formatiert als Tabelle)
- [ ] **Aktueller Saldo:** Berechnung von Gesamteinnahmen - Gesamtausgaben
- [ ] **Datenpersistenz:** Speichern in `finanzen.json` beim Beenden
- [ ] **Fehlerbehandlung:** Abfangen ungültiger Eingaben (z.B. negative Beträge, falsches Datum)
- [ ] **Code-Qualität:** Mindestens 5 Funktionen, Docstrings, Type Hints
- [ ] **Testdaten:** Programm funktioniert mit min. 10 Transaktionen

## 🌟 Kann-Kriterien (Bonus-Punkte, max. +30%)

- [ ] **Kategorie-Filter:** Transaktionen nach Kategorie filtern
- [ ] **Zeitraum-Filter:** Transaktionen nach Datum filtern (z.B. "letzte 30 Tage")
- [ ] **Statistiken:** Durchschnitt pro Kategorie, höchste Ausgabe, etc.
- [ ] **Transaktionen bearbeiten/löschen:** Nach ID suchen und ändern
- [ ] **Budget-Funktion:** Budget pro Kategorie setzen und Warnungen anzeigen
- [ ] **Export als CSV:** Daten in CSV-Format exportieren
- [ ] **Graphische Ausgabe:** Einfache ASCII-Balkendiagramme für Kategorien

## 📊 Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| **Funktionalität** | 12 | Alle Muss-Kriterien erfüllt, Programm läuft fehlerfrei |
| **Code-Struktur** | 8 | Klare Funktionen, gute Benennung, logische Organisation |
| **Fehlerbehandlung** | 4 | Robuste Eingabevalidierung, try-except-Blöcke |
| **Dokumentation** | 3 | Docstrings, Kommentare, README mit Anleitung |
| **KI-Nutzung** | 3 | Reflektierte KI-Nutzung dokumentiert |
| **Bonus** | +9 | Zusatzfunktionen implementiert (max. +30%) |
| **GESAMT** | **30** | |

## 💻 Beispiel-Interaktion

```text
=== PERSÖNLICHER FINANZTRACKER ===

1. Transaktion hinzufügen
2. Alle Transaktionen anzeigen
3. Statistiken anzeigen
4. Nach Kategorie filtern
5. Daten speichern
6. Programm beenden

Wählen Sie eine Option (1-6): 1

--- Neue Transaktion ---
Typ (Einnahme/Ausgabe): Ausgabe
Kategorie: Lebensmittel
Betrag: 45.50
Beschreibung: Wocheneinkauf
Datum (JJJJ-MM-TT, Enter für heute):

✓ Transaktion erfolgreich hinzugefügt!

[Menü wird erneut angezeigt]

Wählen Sie eine Option (1-6): 2

--- Alle Transaktionen ---

ID | Datum      | Typ      | Kategorie      | Betrag   | Beschreibung
---|------------|----------|----------------|----------|---------------
1  | 2025-01-15 | Einnahme | Gehalt         | 3200.00 € | Monatsgehalt
2  | 2025-01-16 | Ausgabe  | Miete          | 850.00 € | Wohnung
3  | 2025-01-16 | Ausgabe  | Lebensmittel   | 45.50 € | Wocheneinkauf

Aktueller Saldo: 2304.50 €

[Menü wird erneut angezeigt]

Wählen Sie eine Option (1-6): 3

--- Statistiken ---

Gesamteinnahmen:  3200.00 €
Gesamtausgaben:    895.50 €
Aktueller Saldo:  2304.50 €

Ausgaben nach Kategorie:
  Miete:          850.00 € (94.9%)
  Lebensmittel:    45.50 €  (5.1%)

Durchschnittliche Ausgabe: 447.75 €
```

## 🛠️ Technische Anforderungen

### Projektstruktur

```
aufgabe-1-finanztracker/
├── finanztracker.py       # Hauptprogramm
├── finanzen.json          # Datendatei (wird automatisch erstellt)
├── README.md              # Anleitung und Dokumentation
└── requirements.txt       # (leer, keine externen Pakete nötig)
```

### Empfohlene Funktionsstruktur

```python
def transaktion_hinzufuegen(transaktionen: list) -> None:
    """Fügt eine neue Transaktion zur Liste hinzu."""
    pass

def transaktionen_anzeigen(transaktionen: list) -> None:
    """Zeigt alle Transaktionen formatiert an."""
    pass

def statistiken_berechnen(transaktionen: list) -> dict:
    """Berechnet Statistiken (Summen, Durchschnitt, etc.)."""
    pass

def daten_speichern(transaktionen: list, dateiname: str = "finanzen.json") -> None:
    """Speichert Transaktionen in JSON-Datei."""
    pass

def daten_laden(dateiname: str = "finanzen.json") -> list:
    """Lädt Transaktionen aus JSON-Datei."""
    pass

def menue_anzeigen() -> str:
    """Zeigt das Hauptmenü und gibt die Auswahl zurück."""
    pass

def main() -> None:
    """Hauptfunktion mit Programmschleife."""
    pass

if __name__ == "__main__":
    main()
```

## 💡 Hinweise und Tipps

### Schritt-für-Schritt-Vorgehen

1. **Grundgerüst erstellen** (15 Min.)
   - `main()` Funktion mit Menüschleife
   - Leere Transaktionsliste initialisieren

2. **Transaktion hinzufügen** (30 Min.)
   - Benutzereingaben abfragen
   - Dictionary erstellen
   - Zur Liste hinzufügen

3. **Transaktionen anzeigen** (20 Min.)
   - Formatierte Ausgabe mit `f-strings`
   - Tabellenform mit festen Spaltenbreiten

4. **Statistiken** (25 Min.)
   - Summen berechnen mit `sum()`
   - Nach Kategorie gruppieren

5. **Datenpersistenz** (20 Min.)
   - JSON-Import: `import json`
   - Speichern: `json.dump()`
   - Laden: `json.load()`

6. **Fehlerbehandlung** (10 Min.)
   - Eingabevalidierung mit `try-except`
   - Prüfung auf leere Werte

### Nützliche Python-Funktionen

```python
# Datum
from datetime import date
heute = date.today().isoformat()  # "2025-01-15"

# Formatierung
betrag_formatiert = f"{betrag:.2f} €"  # "45.50 €"

# Tabelle (mit festen Breiten)
print(f"{id:3} | {datum:10} | {typ:8} | {betrag:>10.2f} €")

# JSON
import json
with open("finanzen.json", "w") as datei:
    json.dump(transaktionen, datei, indent=2)

# Statistiken
kategorien = {}
for t in transaktionen:
    kategorien[t["kategorie"]] = kategorien.get(t["kategorie"], 0) + t["betrag"]
```

### KI-Prompts (Beispiele)

**Für Code-Generierung:**
```
Erstelle eine Python-Funktion `transaktion_hinzufuegen`, die:
- Benutzereingaben für Typ, Kategorie, Betrag und Beschreibung abfragt
- Ein Dictionary mit den Daten und einer auto-inkrementierten ID erstellt
- Das Dictionary zur übergebenen Liste hinzufügt
- Fehlerhafte Eingaben (z.B. negative Beträge) abfängt
- Type Hints und Docstring verwendet
```

**Für Debugging:**
```
Mein Code gibt einen KeyError beim Laden der JSON-Datei.
Hier ist der relevante Code:
[Code einfügen]

Was könnte das Problem sein und wie behebe ich es?
```

**Für Code-Review:**
```
Bitte reviewe diese Funktion und schlage Verbesserungen vor:
[Code einfügen]

Achte auf:
- Code-Qualität und Lesbarkeit
- Fehlerbehandlung
- PEP 8 Konformität
- Type Hints
```

### Häufige Probleme

**Problem:** JSON-Datei existiert beim ersten Start nicht
```python
def daten_laden(dateiname: str = "finanzen.json") -> list:
    try:
        with open(dateiname, "r") as datei:
            return json.load(datei)
    except FileNotFoundError:
        return []  # Leere Liste zurückgeben
```

**Problem:** Benutzer gibt ungültigen Betrag ein
```python
while True:
    try:
        betrag = float(input("Betrag: "))
        if betrag <= 0:
            print("❌ Betrag muss positiv sein!")
            continue
        break
    except ValueError:
        print("❌ Bitte eine gültige Zahl eingeben!")
```

**Problem:** Auto-inkrementierende ID
```python
def naechste_id(transaktionen: list) -> int:
    if not transaktionen:
        return 1
    return max(t["id"] for t in transaktionen) + 1
```

## 📝 README-Vorlage

Ihr `README.md` sollte mindestens enthalten:

```markdown
# Persönlicher Finanztracker

## Beschreibung
[Kurze Beschreibung des Programms]

## Installation
```bash
# Keine externe Dependencies
python finanztracker.py
```

## Verwendung
[Schritte zur Benutzung]

## Features
- [ ] Transaktionen hinzufügen
- [ ] Statistiken anzeigen
- [ ] ...

## KI-Nutzung
[Dokumentieren Sie, wie Sie KI eingesetzt haben]

## Lernerkenntnisse
[Was haben Sie gelernt?]

## Autor
[Ihr Name]
```

## 🎯 Selbsttest vor Abgabe

Prüfen Sie folgende Punkte:

- [ ] Programm startet ohne Fehler
- [ ] Alle Menüoptionen funktionieren
- [ ] Daten werden korrekt gespeichert und geladen
- [ ] Ungültige Eingaben werden abgefangen
- [ ] Code hat Type Hints und Docstrings
- [ ] README ist vollständig
- [ ] Code ist auf GitHub gepusht

## 📚 Weiterführende Ressourcen

- **Python JSON:** [realpython.com/python-json](https://realpython.com/python-json/)
- **Datetime:** [docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)
- **String Formatting:** [realpython.com/python-f-strings](https://realpython.com/python-f-strings/)

## 🤝 Hilfe und Support

Bei Fragen:
1. Nutzen Sie KI-Tools (Claude, ChatGPT) für spezifische Probleme
2. Konsultieren Sie die Python-Dokumentation
3. Fragen Sie im Kurs-Forum
4. Kontaktieren Sie den Dozenten

---

**Viel Erfolg!** 🚀

**Zurück zur Nachbearbeitung:** [README](./README.md)
