# Lektion 3: Datenstrukturen - Listen & Dictionaries

**Dauer:** 50 Minuten  
**Ziel:** Mit Listen und Dictionaries effektiv arbeiten

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Listen erstellen, indexieren und slicen
- List Methods anwenden
- List Comprehensions nutzen
- Dictionaries erstellen und verwenden
- Nested Data Structures verstehen

## 📚 Theorie (20 Min.)

### Listen

**Erstellung:**

```python
# Leere Liste
zahlen = []
namen = list()

# Mit Werten
zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Bob", "Clara"]
gemischt = [1, "zwei", 3.0, True]
```

**Indexierung:**

```python
namen = ["Anna", "Bob", "Clara", "David"]

# Positiver Index (von vorne)
print(namen[0])   # "Anna" (erstes Element)
print(namen[1])   # "Bob"

# Negativer Index (von hinten)
print(namen[-1])  # "David" (letztes Element)
print(namen[-2])  # "Clara"
```

**Slicing:**

```python
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [start:end] - end ist exklusiv
print(zahlen[2:5])    # [2, 3, 4]
print(zahlen[:3])     # [0, 1, 2] (von Anfang)
print(zahlen[7:])     # [7, 8, 9] (bis Ende)
print(zahlen[-3:])    # [7, 8, 9] (letzte 3)
print(zahlen[::2])    # [0, 2, 4, 6, 8] (jedes 2.)
print(zahlen[::-1])   # [9, 8, 7, ...] (umgekehrt)
```

**List Methods:**

```python
zahlen = [1, 2, 3]

# Hinzufügen
zahlen.append(4)        # [1, 2, 3, 4]
zahlen.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
zahlen.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]

# Entfernen
zahlen.remove(3)        # Entfernt erste 3
letztes = zahlen.pop()  # Entfernt und gibt letztes zurück
erstes = zahlen.pop(0)  # Entfernt und gibt erstes zurück

# Suchen
index = zahlen.index(4)  # Index von 4
anzahl = zahlen.count(2) # Wie oft kommt 2 vor?

# Sortieren
zahlen.sort()            # Sortiert aufsteigend
zahlen.sort(reverse=True) # Sortiert absteigend
zahlen.reverse()         # Kehrt Reihenfolge um

# Weitere
laenge = len(zahlen)     # Anzahl Elemente
summe = sum(zahlen)      # Summe aller Zahlen
maximum = max(zahlen)    # Grösstes Element
minimum = min(zahlen)    # Kleinstes Element
```

**List Comprehensions:**

```python
# Traditionell
quadrate = []
for i in range(10):
    quadrate.append(i ** 2)

# List Comprehension
quadrate = [i ** 2 for i in range(10)]

# Mit Bedingung
gerade = [i for i in range(20) if i % 2 == 0]

# Mit Transformation
namen = ["anna", "bob", "clara"]
gross = [name.upper() for name in namen]
```

### Dictionaries

**Erstellung:**

```python
# Leeres Dictionary
person = {}
person = dict()

# Mit Werten
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}
```

**Zugriff:**

```python
# Mit []
name = person["name"]  # "Anna"
# Fehler wenn Key nicht existiert!

# Mit get() (sicherer)
name = person.get("name")           # "Anna"
beruf = person.get("beruf", "N/A")  # "N/A" (Default)
```

**Ändern und Hinzufügen:**

```python
# Wert ändern
person["alter"] = 26

# Neuen Key hinzufügen
person["beruf"] = "Entwicklerin"

# Mehrere auf einmal
person.update({"email": "anna@example.com", "telefon": "123"})
```

**Dictionary Methods:**

```python
# Keys, Values, Items
keys = person.keys()      # dict_keys(['name', 'alter', ...])
values = person.values()  # dict_values(['Anna', 26, ...])
items = person.items()    # dict_items([('name', 'Anna'), ...])

# Über Dictionary iterieren
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Entfernen
beruf = person.pop("beruf")  # Entfernt und gibt Wert zurück
person.clear()               # Leert Dictionary
```

**Nested Data Structures:**

```python
# Liste von Dictionaries
personen = [
    {"name": "Anna", "alter": 25},
    {"name": "Bob", "alter": 30},
    {"name": "Clara", "alter": 28}
]

# Zugriff
print(personen[0]["name"])  # "Anna"

# Dictionary mit Listen
kontakt = {
    "name": "Anna",
    "telefone": ["123", "456"],
    "emails": ["anna@work.com", "anna@home.com"]
}

print(kontakt["telefone"][0])  # "123"
```

## 💻 Live-Demo (15 Min.)

### Demo 1: Todo-Liste

```python
"""
Einfache Todo-Listen-Verwaltung
"""

def zeige_todos(todos: list[str]) -> None:
    """Zeigt alle Todos an."""
    if not todos:
        print("Keine Todos vorhanden.")
        return
    
    print("\n=== TODOS ===")
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")
    print("=" * 20)

def main():
    todos = []
    
    while True:
        print("\n1. Todo hinzufügen")
        print("2. Todo entfernen")
        print("3. Alle anzeigen")
        print("4. Beenden")
        
        wahl = input("\nWahl: ")
        
        if wahl == "1":
            todo = input("Todo: ")
            todos.append(todo)
            print("✓ Hinzugefügt!")
        
        elif wahl == "2":
            zeige_todos(todos)
            try:
                index = int(input("Nummer: ")) - 1
                entfernt = todos.pop(index)
                print(f"✓ '{entfernt}' entfernt!")
            except (ValueError, IndexError):
                print("✗ Ungültige Nummer!")
        
        elif wahl == "3":
            zeige_todos(todos)
        
        elif wahl == "4":
            print("Auf Wiedersehen!")
            break

# main()  # Auskommentiert für Demo
```

### Demo 2: Kontaktbuch

```python
"""
Kontaktbuch mit Dictionaries
"""

def zeige_kontakt(kontakt: dict) -> None:
    """Zeigt einen Kontakt formatiert an."""
    print(f"\nName: {kontakt['name']}")
    print(f"Email: {kontakt.get('email', 'N/A')}")
    print(f"Telefon: {kontakt.get('telefon', 'N/A')}")
    print(f"Stadt: {kontakt.get('stadt', 'N/A')}")

# Kontaktbuch
kontakte = [
    {
        "name": "Anna Müller",
        "email": "anna@example.com",
        "telefon": "123-456",
        "stadt": "Zürich"
    },
    {
        "name": "Bob Schmidt",
        "email": "bob@example.com",
        "stadt": "Bern"
    }
]

# Alle Kontakte anzeigen
print("=== KONTAKTBUCH ===")
for kontakt in kontakte:
    zeige_kontakt(kontakt)

# Suche
suchbegriff = "Anna"
gefunden = [k for k in kontakte if suchbegriff.lower() in k["name"].lower()]

print(f"\nSuche nach '{suchbegriff}':")
for kontakt in gefunden:
    print(f"- {kontakt['name']}")
```

### Demo 3: Datenanalyse

```python
"""
Verkaufsdaten analysieren
"""

# Verkaufsdaten
verkaeufe = [
    {"produkt": "Laptop", "preis": 999, "anzahl": 5},
    {"produkt": "Maus", "preis": 25, "anzahl": 20},
    {"produkt": "Tastatur", "preis": 75, "anzahl": 15},
    {"produkt": "Monitor", "preis": 299, "anzahl": 8}
]

# Gesamtumsatz berechnen
gesamtumsatz = sum(v["preis"] * v["anzahl"] for v in verkaeufe)
print(f"Gesamtumsatz: CHF {gesamtumsatz}")

# Durchschnittspreis
durchschnitt = sum(v["preis"] for v in verkaeufe) / len(verkaeufe)
print(f"Durchschnittspreis: CHF {durchschnitt:.2f}")

# Teuerstes Produkt
teuerstes = max(verkaeufe, key=lambda v: v["preis"])
print(f"Teuerstes Produkt: {teuerstes['produkt']} (CHF {teuerstes['preis']})")

# Meistverkauft
meistverkauft = max(verkaeufe, key=lambda v: v["anzahl"])
print(f"Meistverkauft: {meistverkauft['produkt']} ({meistverkauft['anzahl']} Stück)")

# Sortiert nach Umsatz
nach_umsatz = sorted(verkaeufe, 
                     key=lambda v: v["preis"] * v["anzahl"], 
                     reverse=True)

print("\nTop-Seller nach Umsatz:")
for verkauf in nach_umsatz:
    umsatz = verkauf["preis"] * verkauf["anzahl"]
    print(f"{verkauf['produkt']}: CHF {umsatz}")
```

## ✏️ Übung (15 Min.)

Entwickeln Sie mit KI **EINES** der folgenden:

### Option A: Inventar-System

**Anforderungen:**

- Dictionary mit 3-5 Produkten
- Jedes Produkt hat: name, preis, anzahl
- Funktionen: hinzufügen, entfernen, anzeigen
- Gesamtwert berechnen

**Beispiel:**

```python
inventar = {
    "laptop": {"preis": 999, "anzahl": 5},
    "maus": {"preis": 25, "anzahl": 20}
}
```

### Option B: Duplikat-Entferner

**Anforderungen:**

- Liste mit Duplikaten einlesen
- Duplikate entfernen
- Sortierte Liste ausgeben
- Anzahl entfernter Duplikate anzeigen

**Beispiel:**

```text
Eingabe: [1, 2, 2, 3, 3, 3, 4]
Ausgabe: [1, 2, 3, 4]
Entfernt: 3 Duplikate
```

### Option C: Mini-Kontaktliste

**Anforderungen:**

- Liste von 2-3 Kontakt-Dictionaries
- Jeder Kontakt: name, email, telefon
- Suche nach Namen
- Alle Kontakte anzeigen

## 🎓 Zusammenfassung

### Listen

- **Geordnete** Sammlung
- **Veränderbar** (mutable)
- **Duplikate** erlaubt
- **Indexierung** mit [0], [-1]
- **Slicing** mit [start:end]

### Dictionaries

- **Key-Value** Paare
- **Ungeordnet** (ab Python 3.7: Einfügereihenfolge)
- **Keys eindeutig**
- **Schneller Zugriff** über Keys

### Wann was?

- **Liste:** Geordnete Sammlung, Reihenfolge wichtig
- **Dictionary:** Zuordnung, schneller Zugriff über Namen

## 📎 Anhang für Dozenten

### Timing-Tipps

- List Comprehensions: Kurz zeigen, nicht vertiefen
- Nested Structures: Nur Basics
- Fokus auf praktische Anwendung

### Häufige Fragen

#### Frage 1: Liste vs. Dictionary?

- Liste: Reihenfolge, Index
- Dictionary: Zuordnung, Keys

#### Frage 2: append vs. extend?

- append: Fügt Element hinzu
- extend: Fügt mehrere hinzu

#### Frage 3: [] vs. get()?

- []: Fehler wenn Key fehlt
- get(): Gibt None oder Default

---

**Weiter zu:** [Lektion 4 - Funktionen & Module](./lektion-4-funktionen-module.md)  
**Zurück zu:** [Lektion 2 - Kontrollstrukturen](./lektion-2-kontrollstrukturen.md)
