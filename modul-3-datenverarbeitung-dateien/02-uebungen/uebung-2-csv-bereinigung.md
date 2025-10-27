# Übung 2: CSV-Datenbereinigung

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Ziel

CSV-Daten bereinigen und verarbeiten.

## Wählen Sie EINE Option

### Option A: Duplikate entfernen

#### Anforderungen

- CSV-Datei mit Duplikaten einlesen
- Duplikate identifizieren
- Bereinigte Daten in neue Datei schreiben
- Statistik ausgeben (Original vs. Bereinigt)

#### Testdaten

Erstellen Sie `daten.csv`:

```csv
name,email,alter
Anna,anna@test.com,25
Bob,bob@test.com,30
Anna,anna@test.com,25
Clara,clara@test.com,28
Bob,bob@test.com,30
```

#### Prompt-Vorlage

```text
Erstelle ein Python-Programm zur CSV-Datenbereinigung:

Anforderungen:
- Liest "daten.csv" mit csv.DictReader
- Entfernt Duplikate basierend auf email
- Schreibt bereinigte Daten in "daten_clean.csv"
- Gibt Statistik aus:
  * Original: X Zeilen
  * Duplikate: Y Zeilen
  * Bereinigt: Z Zeilen

Verwende set() für Duplikat-Erkennung.
```

#### Erwartetes Ergebnis

```text
Original: 5 Zeilen
Duplikate: 2 Zeilen
Bereinigt: 3 Zeilen

Bereinigte Datei erstellt: daten_clean.csv
```

### Option B: Fehlende Werte behandeln

#### Anforderungen

- CSV mit fehlenden Werten einlesen
- Fehlende Werte identifizieren
- Strategie anwenden (z.B. Durchschnitt, "Unbekannt")
- Bereinigte Daten speichern

#### Testdaten

Erstellen Sie `verkauf.csv`:

```csv
produkt,preis,anzahl
Laptop,1200,5
Maus,,10
Tastatur,80,
Monitor,350,3
Headset,60,
```

#### Prompt-Vorlage

```text
Erstelle ein Python-Programm für fehlende Werte:

Anforderungen:
- Liest "verkauf.csv"
- Identifiziert fehlende Werte (leere Strings)
- Behandelt fehlende Werte:
  * preis: Durchschnitt der vorhandenen Preise
  * anzahl: 0 als Standard
- Schreibt "verkauf_clean.csv"
- Gibt Report aus

Verwende pandas oder csv-Modul.
```

### Option C: Daten filtern und sortieren

#### Anforderungen

- CSV-Datei einlesen
- Nach Kriterien filtern
- Sortieren
- Top N ausgeben

#### Testdaten

Erstellen Sie `produkte.csv`:

```csv
name,kategorie,preis,bewertung
Laptop,Elektronik,1200,4.5
Maus,Elektronik,25,4.2
Buch,Bücher,15,4.8
Tastatur,Elektronik,80,4.6
Roman,Bücher,12,4.3
Monitor,Elektronik,350,4.7
```

#### Prompt-Vorlage

```text
Erstelle ein Python-Programm für Datenfilterung:

Anforderungen:
- Liest "produkte.csv"
- Filtert nach kategorie="Elektronik"
- Sortiert nach bewertung (absteigend)
- Gibt Top 3 aus
- Berechnet Durchschnittspreis

Format:
Top 3 Elektronik-Produkte:
1. [Name] - [Preis]€ (⭐[Bewertung])
...

Durchschnittspreis: [X]€
```

## 💡 Tipps

- Nutzen Sie `csv.DictReader` für bessere Lesbarkeit
- Testen Sie mit kleinen Testdaten
- Fehlerbehandlung nicht vergessen
- Dokumentieren Sie Ihren Code

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] CSV-Datei korrekt eingelesen
- [ ] Datenbereinigung funktioniert
- [ ] Bereinigte Daten gespeichert
- [ ] Statistik/Report ausgegeben
- [ ] Code kommentiert

---

**Zurück zu:** [Übungen README](./README.md)
