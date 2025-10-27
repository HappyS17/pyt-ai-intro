# Lektion 2: CSV-Datenverarbeitung

**Dauer:** 50 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Lernziele

- CSV-Dateien lesen und schreiben
- csv-Modul nutzen
- pandas Basics
- Daten filtern und aggregieren

## 📚 Theorie (15 Min.)

### CSV-Modul

```python
import csv

# Lesen
with open("daten.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Mit DictReader
with open("daten.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["alter"])

# Schreiben
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Alter"])
    writer.writerow(["Anna", 25])
```

### pandas Basics

```python
import pandas as pd

# Lesen
df = pd.read_csv("daten.csv")

# Anzeigen
print(df.head())
print(df.info())

# Filtern
erwachsene = df[df["alter"] >= 18]

# Aggregieren
durchschnitt = df["alter"].mean()

# Schreiben
df.to_csv("output.csv", index=False)
```

## 💻 Live-Demo (20 Min.)

### Demo: Verkaufsdaten

```python
"""Verkaufsdaten analysieren"""
import pandas as pd

# Daten laden
df = pd.read_csv("verkaeufe.csv")

# Statistiken
print(f"Gesamtumsatz: {df['umsatz'].sum()}")
print(f"Durchschnitt: {df['umsatz'].mean():.2f}")

# Top 5 Produkte
top5 = df.groupby("produkt")["umsatz"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Produkte:")
print(top5)

# Speichern
top5.to_csv("top_produkte.csv")
```

## ✏️ Übung (15 Min.)

CSV-Datenbereinigung mit KI implementieren.

---

**Weiter zu:** [Lektion 3 - JSON & APIs](./lektion-3-json-apis.md)
