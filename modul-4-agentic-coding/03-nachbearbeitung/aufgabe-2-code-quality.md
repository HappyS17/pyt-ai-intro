# Aufgabe 2: Code Quality & Refactoring

**Schwierigkeit:** ⭐⭐⭐  
**Zeitaufwand:** 120 Minuten  
**Deadline:** Vor Modul 5

## 🎯 Ziel

Einen bestehenden Code-Projekt verbessern: Refactoring, Testing, Dokumentation und Code-Quality.

## 📋 Aufgabenstellung

Wähle eines deiner bisherigen Projekte (oder nutze ein Beispiel-Projekt) und verbessere es nach folgenden Kriterien:

### Phase 1: Code-Analyse (30 Min.)
- [ ] Nutze `pylint` oder `ruff` zur Analyse
- [ ] Identifiziere Code-Smells
- [ ] Finde Duplikationen
- [ ] Prüfe auf Fehlerbehandlung

### Phase 2: Refactoring (45 Min.)
- [ ] Extrahiere Funktionen
- [ ] Vereinfache komplexe Logik
- [ ] Verbessere Variablennamen
- [ ] Entferne Duplikationen

### Phase 3: Testing (30 Min.)
- [ ] Schreib Unit Tests
- [ ] Erreiche mindestens 70% Coverage
- [ ] Teste Edge Cases
- [ ] Teste Fehlerbehandlung

### Phase 4: Dokumentation (15 Min.)
- [ ] Schreib Docstrings
- [ ] Füge Kommentare hinzu
- [ ] Erstelle README
- [ ] Dokumentiere API

## 🔧 Tools & Befehle

### Code-Analyse
```bash
# Alle Tools mit uv installieren
uv sync --group dev

# pylint
pylint src/

# ruff
ruff check src/

# black (Formatierung)
black src/
```

### Testing
```bash
# pytest (mit uv installiert)
pytest tests/
pytest --cov=src tests/
```

### Metriken
```bash
# Komplexität (radon ist in dev-dependencies)
radon cc src/ -a

# Wartbarkeit
radon mi src/
```

## 📊 Refactoring-Beispiel

### Vorher (Schlecht)
```python
def process_data(d):
    r = []
    for i in d:
        if i['age'] > 18 and i['status'] == 'active':
            x = i['salary'] * 1.1
            r.append({'name': i['n'], 'new_sal': x})
    return r
```

**Probleme:**
- Schlechte Variablennamen
- Keine Fehlerbehandlung
- Keine Dokumentation
- Zu viel Logik in einer Funktion

### Nachher (Gut)
```python
def process_employee_data(employees: list[dict]) -> list[dict]:
    """Verarbeite Mitarbeiterdaten und berechne neue Gehälter.
    
    Args:
        employees: Liste von Mitarbeiterdaten
        
    Returns:
        Liste mit Namen und neuen Gehältern
        
    Raises:
        ValueError: Wenn Daten ungültig
    """
    if not employees:
        raise ValueError("Mitarbeiterliste darf nicht leer sein")
    
    processed = []
    for employee in employees:
        if _is_eligible_for_raise(employee):
            new_salary = _calculate_new_salary(employee)
            processed.append({
                'name': employee['name'],
                'new_salary': new_salary
            })
    
    return processed

def _is_eligible_for_raise(employee: dict) -> bool:
    """Prüfe ob Mitarbeiter für Gehaltserhöhung berechtigt ist."""
    return (
        employee.get('age', 0) > 18 and
        employee.get('status') == 'active'
    )

def _calculate_new_salary(employee: dict) -> float:
    """Berechne neues Gehalt mit 10% Erhöhung."""
    base_salary = employee.get('salary', 0)
    return base_salary * 1.1
```

**Verbesserungen:**
- Aussagekräftige Namen
- Funktionen extrahiert
- Fehlerbehandlung
- Docstrings
- Type Hints

## ✅ Checkliste

### Code-Qualität
- [ ] pylint Score > 8.0
- [ ] Keine Warnungen von ruff
- [ ] Code mit black formatiert
- [ ] Komplexität < 10 pro Funktion

### Testing
- [ ] Mindestens 70% Coverage
- [ ] Alle Tests bestehen
- [ ] Edge Cases getestet
- [ ] Fehlerbehandlung getestet

### Dokumentation
- [ ] Alle Funktionen haben Docstrings
- [ ] README vorhanden
- [ ] API dokumentiert
- [ ] Beispiele gegeben

### Best Practices
- [ ] DRY-Prinzip befolgt
- [ ] SOLID-Prinzipien beachtet
- [ ] Aussagekräftige Variablennamen
- [ ] Fehlerbehandlung implementiert

## 📁 Deliverables

1. **refactored_code/** - Verbesserter Code
2. **tests/** - Unit Tests mit Coverage
3. **README.md** - Dokumentation
4. **REFACTORING_REPORT.md** - Was wurde verbessert?
5. **metrics.txt** - Code-Qualitäts-Metriken

## 🎓 Lernziele

Nach dieser Aufgabe kannst du:
- ✅ Code-Qualität messen und verbessern
- ✅ Refactoring-Techniken anwenden
- ✅ Tests schreiben und Coverage messen
- ✅ Code dokumentieren
- ✅ Best Practices befolgen

## 💡 Refactoring-Techniken

### 1. Extract Function
```python
# Vorher
if user.age > 18 and user.status == 'active':
    # 10 Zeilen Code

# Nachher
if is_eligible_user(user):
    # 10 Zeilen Code
```

### 2. Rename Variable
```python
# Vorher
x = calculate_total(items)

# Nachher
total_price = calculate_total(items)
```

### 3. Remove Duplication
```python
# Vorher
if x > 0:
    print(f"Value: {x}")
if y > 0:
    print(f"Value: {y}")

# Nachher
def print_if_positive(value):
    if value > 0:
        print(f"Value: {value}")

print_if_positive(x)
print_if_positive(y)
```

## 📚 Ressourcen

- [pylint Documentation](https://pylint.pycqa.org/)
- [ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)
- [Refactoring Guru](https://refactoring.guru/)

---

**Tipp:** Nutze KI-Tools um Refactoring-Vorschläge zu bekommen!

