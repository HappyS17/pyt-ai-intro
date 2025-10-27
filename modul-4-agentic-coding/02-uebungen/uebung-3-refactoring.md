# Übung 3: Legacy Code Refactoring

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Legacy Code mit KI-Unterstützung refactoren.

## Legacy Code

```python
def process(d):
    r = []
    for i in d:
        if i['a'] > 18 and i['s'] == 'active':
            x = i['n'].upper()
            y = i['e']
            z = i['p']
            if z > 50000:
                r.append({'name': x, 'email': y, 'salary': z, 'bonus': z * 0.1})
            else:
                r.append({'name': x, 'email': y, 'salary': z, 'bonus': 0})
    return r

def calc(items):
    t = 0
    for i in items:
        if i['t'] == 'A':
            t += i['p'] * 0.9
        elif i['t'] == 'B':
            t += i['p'] * 0.95
        else:
            t += i['p']
    return t

class User:
    def __init__(self, n, a, e, p):
        self.n = n
        self.a = a
        self.e = e
        self.p = p
    
    def get_data(self):
        return f"{self.n},{self.a},{self.e},{self.p}"
```

## Aufgabe

Refactoren Sie den Code mit KI-Unterstützung.

## Schritt 1: Code Review (5 Min.)

### Prompt für Review

```text
Reviewe folgenden Legacy Code und identifiziere Probleme:

[KOPIERE CODE HIER EIN]

Analysiere:
1. Code Smells
2. Naming Issues
3. Fehlende Dokumentation
4. Fehlende Type Hints
5. Potenzielle Bugs
6. Performance-Probleme

Gib strukturiertes Feedback.
```

### Erwartetes Feedback

```text
Probleme:
1. Unklare Variablennamen (d, r, i, x, y, z)
2. Keine Type Hints
3. Keine Docstrings
4. Magic Numbers (18, 50000, 0.1, 0.9, 0.95)
5. Lange Funktion mit mehreren Verantwortlichkeiten
6. Keine Fehlerbehandlung
7. Duplizierter Code

Empfehlungen:
- Aussagekräftige Namen
- Funktionen aufteilen
- Konstanten definieren
- Type Hints hinzufügen
- Dokumentation
```

## Schritt 2: Refactoring-Plan (3 Min.)

### Prompt für Plan

```text
Erstelle einen Refactoring-Plan für den Code.

Schritte:
1. Was zuerst?
2. Was danach?
3. Wie testen?

Priorität:
- Sicherheit (keine Bugs einführen)
- Lesbarkeit
- Wartbarkeit
```

## Schritt 3: Refactoring durchführen (7 Min.)

### Prompt für Refactoring

```text
Refactore den Code Schritt für Schritt:

[KOPIERE CODE HIER EIN]

Anforderungen:
1. Aussagekräftige Namen
2. Type Hints
3. Docstrings
4. Funktionen aufteilen
5. Konstanten extrahieren
6. SOLID Principles
7. Fehlerbehandlung

Behalte die Funktionalität bei!
```

### Erwartetes Ergebnis

```python
from typing import List, Dict
from dataclasses import dataclass

# Konstanten
MIN_AGE = 18
HIGH_SALARY_THRESHOLD = 50000
HIGH_SALARY_BONUS_RATE = 0.1

DISCOUNT_RATES = {
    'A': 0.10,  # 10% Rabatt
    'B': 0.05,  # 5% Rabatt
}

@dataclass
class Employee:
    """Repräsentiert einen Mitarbeiter."""
    name: str
    age: int
    email: str
    salary: float
    status: str

def calculate_bonus(salary: float) -> float:
    """
    Berechnet Bonus basierend auf Gehalt.
    
    Args:
        salary: Jahresgehalt
    
    Returns:
        Bonus-Betrag
    """
    if salary > HIGH_SALARY_THRESHOLD:
        return salary * HIGH_SALARY_BONUS_RATE
    return 0.0

def process_active_employees(employees: List[Dict]) -> List[Dict]:
    """
    Verarbeitet aktive Mitarbeiter über 18.
    
    Args:
        employees: Liste von Mitarbeiter-Dictionaries
    
    Returns:
        Liste von verarbeiteten Mitarbeitern mit Bonus
    """
    result = []
    
    for emp_data in employees:
        if emp_data['age'] > MIN_AGE and emp_data['status'] == 'active':
            employee = {
                'name': emp_data['name'].upper(),
                'email': emp_data['email'],
                'salary': emp_data['salary'],
                'bonus': calculate_bonus(emp_data['salary'])
            }
            result.append(employee)
    
    return result

def calculate_total_with_discount(items: List[Dict]) -> float:
    """
    Berechnet Gesamtpreis mit Rabatten.
    
    Args:
        items: Liste von Items mit 'type' und 'price'
    
    Returns:
        Gesamtpreis nach Rabatten
    """
    total = 0.0
    
    for item in items:
        price = item['price']
        item_type = item['type']
        
        discount_rate = DISCOUNT_RATES.get(item_type, 0.0)
        discounted_price = price * (1 - discount_rate)
        total += discounted_price
    
    return total

@dataclass
class User:
    """Repräsentiert einen Benutzer."""
    name: str
    age: int
    email: str
    phone: str
    
    def to_csv(self) -> str:
        """
        Konvertiert User zu CSV-Format.
        
        Returns:
            CSV-String
        """
        return f"{self.name},{self.age},{self.email},{self.phone}"
```

## Vergleich

### Vorher

- ❌ Unklare Namen
- ❌ Keine Type Hints
- ❌ Keine Dokumentation
- ❌ Magic Numbers
- ❌ Lange Funktionen

### Nachher

- ✅ Klare Namen
- ✅ Type Hints
- ✅ Docstrings
- ✅ Konstanten
- ✅ Kleine Funktionen
- ✅ Dataclasses

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] Code reviewed
- [ ] Probleme identifiziert
- [ ] Refactoring-Plan erstellt
- [ ] Code refactored
- [ ] Funktionalität erhalten
- [ ] Code besser lesbar

---

**Zurück zu:** [Übungen README](./README.md)
