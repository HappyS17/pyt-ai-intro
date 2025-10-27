# Quick Reference: CSV & JSON

Schnellreferenz für CSV und JSON in Python.

## CSV-Modul

### Lesen

```python
import csv

# Mit csv.reader
with open('daten.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Erste Zeile
    for row in reader:
        print(row)  # Liste

# Mit DictReader (empfohlen)
with open('daten.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'])  # Dictionary
```

### Schreiben

```python
# Mit csv.writer
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Alter'])
    writer.writerow(['Anna', 25])

# Mit DictWriter (empfohlen)
with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'alter']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Anna', 'alter': 25})
```

## JSON-Modul

### Lesen

```python
import json

# Aus Datei
with open('daten.json', 'r') as f:
    data = json.load(f)

# Aus String
json_string = '{"name": "Anna", "alter": 25}'
data = json.loads(json_string)
```

### Schreiben

```python
# In Datei
data = {'name': 'Anna', 'alter': 25}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Als String
json_string = json.dumps(data, indent=2)
```

## pandas Basics

### CSV

```python
import pandas as pd

# Lesen
df = pd.read_csv('daten.csv')

# Anzeigen
print(df.head())
print(df.info())

# Filtern
erwachsene = df[df['alter'] >= 18]

# Schreiben
df.to_csv('output.csv', index=False)
```

### JSON

```python
# Lesen
df = pd.read_json('daten.json')

# Schreiben
df.to_json('output.json', orient='records', indent=2)
```

## Häufige Operationen

### CSV: Duplikate entfernen

```python
seen = set()
unique_rows = []

for row in reader:
    key = row['email']  # Eindeutiges Feld
    if key not in seen:
        seen.add(key)
        unique_rows.append(row)
```

### JSON: Nested Access

```python
data = {
    'user': {
        'name': 'Anna',
        'address': {
            'city': 'Zürich'
        }
    }
}

# Sicher zugreifen
city = data.get('user', {}).get('address', {}).get('city')
```

### Type Conversion

```python
# String zu anderen Typen
alter = int(row['alter'])
preis = float(row['preis'])
aktiv = row['aktiv'].lower() == 'true'
```

## Fehlerbehandlung

```python
try:
    with open('daten.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
except FileNotFoundError:
    print("Datei nicht gefunden")
except csv.Error as e:
    print(f"CSV-Fehler: {e}")
```

## Best Practices

### CSV

- ✅ `DictReader` statt `reader` verwenden
- ✅ `newline=''` beim Schreiben
- ✅ Encoding angeben: `encoding='utf-8'`
- ✅ `with` Statement verwenden

### JSON

- ✅ `indent=2` für Lesbarkeit
- ✅ `ensure_ascii=False` für Umlaute
- ✅ `.get()` für sicheren Zugriff
- ✅ Validierung vor dem Parsen

---

**Zurück zu:** [Materialien README](./README.md)
