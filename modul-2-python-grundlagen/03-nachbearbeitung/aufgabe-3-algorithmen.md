# Aufgabe 3: Klassische Algorithmen implementieren

**Zeitaufwand:** 90 Minuten
**Punkte:** 25% der Nachbearbeitung
**Schwierigkeit:** ⭐⭐⭐

## 🎯 Lernziele

Nach dieser Aufgabe können Sie:

- Klassische Algorithmen in Python implementieren
- Algorithmische Problemlösung systematisch angehen
- Komplexität und Effizienz von Lösungen einschätzen
- KI als Lernpartner für Algorithmen nutzen
- Code mit Unit Tests validieren

## 📋 Aufgabenstellung

Implementieren Sie **3 von 5** klassischen Algorithmen mit KI-Unterstützung. Nutzen Sie KI, um die Konzepte zu verstehen, aber schreiben Sie den finalen Code selbst.

## 🎯 Wählen Sie 3 Algorithmen

### Option 1: Binary Search (Binäre Suche) ⭐⭐

**Problem:** Suchen Sie einen Wert in einer sortierten Liste effizient.

**Anforderung:**
```python
def binary_search(sorted_list: list, target: int) -> int:
    """
    Sucht target in sorted_list und gibt den Index zurück.

    Args:
        sorted_list: Sortierte Liste von Zahlen
        target: Zu suchender Wert

    Returns:
        Index des Werts, oder -1 wenn nicht gefunden

    Examples:
        >>> binary_search([1, 3, 5, 7, 9], 5)
        2
        >>> binary_search([1, 3, 5, 7, 9], 4)
        -1
    """
    pass
```

**Testfälle:**
```python
assert binary_search([1, 3, 5, 7, 9], 5) == 2
assert binary_search([1, 3, 5, 7, 9], 1) == 0
assert binary_search([1, 3, 5, 7, 9], 9) == 4
assert binary_search([1, 3, 5, 7, 9], 4) == -1
assert binary_search([], 5) == -1
```

---

### Option 2: Palindrome Checker ⭐

**Problem:** Prüfen Sie, ob ein String ein Palindrom ist (vorwärts = rückwärts).

**Anforderung:**
```python
def is_palindrome(text: str) -> bool:
    """
    Prüft, ob ein String ein Palindrom ist.

    Ignoriert Gross-/Kleinschreibung und Leerzeichen.

    Args:
        text: Zu prüfender String

    Returns:
        True wenn Palindrom, sonst False

    Examples:
        >>> is_palindrome("Anna")
        True
        >>> is_palindrome("Ein Neger mit Gazelle zagt im Regen nie")
        True
        >>> is_palindrome("Hallo")
        False
    """
    pass
```

**Testfälle:**
```python
assert is_palindrome("Anna") == True
assert is_palindrome("A man a plan a canal Panama") == True
assert is_palindrome("racecar") == True
assert is_palindrome("Hallo") == False
assert is_palindrome("") == True
```

---

### Option 3: Fibonacci-Zahlen (mit Memoization) ⭐⭐⭐

**Problem:** Berechnen Sie die n-te Fibonacci-Zahl effizient.

**Anforderung:**
```python
def fibonacci(n: int, memo: dict = None) -> int:
    """
    Berechnet die n-te Fibonacci-Zahl mit Memoization.

    Fibonacci-Folge: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Formel: fib(n) = fib(n-1) + fib(n-2)
    Basisfall: fib(0) = 0, fib(1) = 1

    Args:
        n: Position in der Fibonacci-Folge (>= 0)
        memo: Dictionary für Memoization (optional)

    Returns:
        n-te Fibonacci-Zahl

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    pass
```

**Testfälle:**
```python
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5
assert fibonacci(10) == 55
assert fibonacci(20) == 6765
```

---

### Option 4: Anagramm-Finder ⭐⭐

**Problem:** Prüfen Sie, ob zwei Strings Anagramme sind (gleiche Buchstaben, andere Reihenfolge).

**Anforderung:**
```python
def are_anagrams(str1: str, str2: str) -> bool:
    """
    Prüft, ob zwei Strings Anagramme sind.

    Ignoriert Gross-/Kleinschreibung und Leerzeichen.

    Args:
        str1: Erster String
        str2: Zweiter String

    Returns:
        True wenn Anagramme, sonst False

    Examples:
        >>> are_anagrams("listen", "silent")
        True
        >>> are_anagrams("Astronomer", "Moon starer")
        True
        >>> are_anagrams("hello", "world")
        False
    """
    pass
```

**Testfälle:**
```python
assert are_anagrams("listen", "silent") == True
assert are_anagrams("Astronomer", "Moon starer") == True
assert are_anagrams("hello", "world") == False
assert are_anagrams("", "") == True
```

---

### Option 5: Prime Number Checker ⭐⭐

**Problem:** Prüfen Sie effizient, ob eine Zahl eine Primzahl ist.

**Anforderung:**
```python
def is_prime(n: int) -> bool:
    """
    Prüft, ob eine Zahl eine Primzahl ist.

    Verwendet optimierte Methode (nur bis √n prüfen).

    Args:
        n: Zu prüfende Zahl

    Returns:
        True wenn Primzahl, sonst False

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(20)
        False
    """
    pass
```

**Testfälle:**
```python
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(17) == True
assert is_prime(100) == False
assert is_prime(1) == False
```

## ✅ Anforderungen

Für jeden der 3 gewählten Algorithmen:

### Code (8 Punkte pro Algorithmus)

- [ ] **Funktionsignatur:** Korrekte Parameter und Rückgabewert
- [ ] **Type Hints:** Vollständige Type Annotations
- [ ] **Docstring:** Ausführliche Dokumentation mit Examples
- [ ] **Implementierung:** Funktioniert korrekt für alle Testfälle
- [ ] **Effizienz:** Nutzt optimierte Algorithmen (nicht naive Brute-Force)

### Dokumentation (3 Punkte pro Algorithmus)

- [ ] **Erklärung:** 3-5 Sätze über den Algorithmus
- [ ] **Zeitkomplexität:** Big-O-Notation (z.B. O(log n))
- [ ] **Lernprozess:** Wie haben Sie KI eingesetzt?

### Tests (2 Punkte pro Algorithmus)

- [ ] **Testfälle:** Alle vorgegebenen Tests bestehen
- [ ] **Eigene Tests:** Mindestens 2 zusätzliche Edge Cases

## 📊 Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| **Algorithmus 1** | 8 | Code korrekt, effizient, dokumentiert |
| **Algorithmus 2** | 8 | Code korrekt, effizient, dokumentiert |
| **Algorithmus 3** | 8 | Code korrekt, effizient, dokumentiert |
| **Gesamt-Dokumentation** | 1 | README mit Übersicht |
| **GESAMT** | **25** | |

## 💻 Projektstruktur

```
aufgabe-3-algorithmen/
├── algorithms.py          # Ihre Implementierungen
├── test_algorithms.py     # Unit Tests
├── README.md              # Dokumentation
└── lernprozess.md         # KI-Nutzung dokumentieren
```

## 📝 Template für algorithms.py

```python
"""
Klassische Algorithmen-Implementierungen
Autor: [Ihr Name]
Datum: [Datum]
"""

# Algorithmus 1: Binary Search
def binary_search(sorted_list: list, target: int) -> int:
    """
    Sucht target in sorted_list mit binärer Suche.

    Zeitkomplexität: O(log n)
    Raumkomplexität: O(1)

    Args:
        sorted_list: Sortierte Liste von Zahlen
        target: Zu suchender Wert

    Returns:
        Index des Werts, oder -1 wenn nicht gefunden

    Examples:
        >>> binary_search([1, 3, 5, 7, 9], 5)
        2
    """
    # Ihr Code hier
    pass


# Algorithmus 2: [Ihr gewählter Algorithmus]
# ...


# Algorithmus 3: [Ihr gewählter Algorithmus]
# ...


if __name__ == "__main__":
    # Manuelle Tests für schnelles Feedback
    print("Test Binary Search:")
    print(binary_search([1, 3, 5, 7, 9], 5))  # Erwartet: 2

    # Weitere Tests...
```

## 📝 Template für test_algorithms.py

```python
"""
Unit Tests für Algorithmen
"""
import pytest
from algorithms import binary_search, is_palindrome, fibonacci


class TestBinarySearch:
    def test_found_middle(self):
        assert binary_search([1, 3, 5, 7, 9], 5) == 2

    def test_found_start(self):
        assert binary_search([1, 3, 5, 7, 9], 1) == 0

    def test_found_end(self):
        assert binary_search([1, 3, 5, 7, 9], 9) == 4

    def test_not_found(self):
        assert binary_search([1, 3, 5, 7, 9], 4) == -1

    def test_empty_list(self):
        assert binary_search([], 5) == -1

    # Ihre eigenen Tests
    def test_single_element(self):
        assert binary_search([5], 5) == 0

    def test_large_list(self):
        large_list = list(range(0, 10000, 2))  # Gerade Zahlen
        assert binary_search(large_list, 5000) == 2500


# Tests für weitere Algorithmen...
```

## 💡 Schritt-für-Schritt-Anleitung

### Phase 1: Verstehen (20 Min.)

**Für jeden Algorithmus:**

1. **Konzept verstehen mit KI:**
```
Erkläre mir den [Algorithmus-Name] Algorithmus:
- Wie funktioniert er?
- Warum ist er effizient?
- Welche Edge Cases gibt es?
- Zeige ein Beispiel Schritt für Schritt
```

2. **Pseudocode erstellen:**
```
Gib mir Pseudocode (NICHT Python) für [Algorithmus]:
- In einfachen, logischen Schritten
- Mit Kommentaren für jeden Schritt
```

3. **Stift & Papier:** Zeichnen Sie den Ablauf für ein Beispiel

### Phase 2: Implementieren (40 Min.)

**Für jeden Algorithmus (ca. 13 Min.):**

1. **Funktionsgerüst erstellen** (2 Min.)
   - Signatur mit Type Hints
   - Docstring mit Examples
   - `pass` als Platzhalter

2. **Basis-Implementierung** (6 Min.)
   - Übersetzen Sie Pseudocode in Python
   - Fokus auf Korrektheit, nicht Perfektion

3. **Testen & Debuggen** (5 Min.)
   - Führen Sie vorgegebene Tests aus
   - Beheben Sie Fehler
   - Nutzen Sie KI für Debugging-Hilfe

### Phase 3: Optimieren & Dokumentieren (30 Min.)

1. **Code-Review mit KI:**
```
Reviewe meinen Code für [Algorithmus]:

[Code einfügen]

Prüfe:
- Korrektheit
- Effizienz (Zeitkomplexität)
- Code-Qualität
- Edge Cases

Gibt es Verbesserungsmöglichkeiten?
```

2. **Dokumentation schreiben:**
   - README mit Algorithmus-Übersicht
   - Lernprozess dokumentieren
   - Zeitkomplexität angeben

3. **Zusätzliche Tests:**
   - Mindestens 2 eigene Edge Cases pro Algorithmus

## 💡 Algorithmus-spezifische Tipps

### Binary Search

**Konzept:** Halbiere den Suchbereich in jedem Schritt.

**Pseudocode:**
```
1. Setze left = 0, right = länge der Liste - 1
2. Solange left <= right:
   a. Berechne middle = (left + right) // 2
   b. Wenn liste[middle] == target: Gib middle zurück
   c. Wenn liste[middle] < target: Setze left = middle + 1
   d. Sonst: Setze right = middle - 1
3. Gib -1 zurück (nicht gefunden)
```

**Häufiger Fehler:**
```python
# ❌ Falsch (Endlosschleife möglich)
while left < right:

# ✅ Richtig
while left <= right:
```

---

### Palindrome Checker

**Konzept:** Vergleiche String von beiden Enden.

**Tipp:** String normalisieren:
```python
# Leerzeichen entfernen, Kleinbuchstaben
clean = text.lower().replace(" ", "")
```

**Zwei Ansätze:**
```python
# Ansatz 1: Umkehren
return clean == clean[::-1]

# Ansatz 2: Two-Pointer
left, right = 0, len(clean) - 1
while left < right:
    if clean[left] != clean[right]:
        return False
    left += 1
    right -= 1
return True
```

---

### Fibonacci mit Memoization

**Konzept:** Speichere bereits berechnete Werte.

**Ohne Memoization (LANGSAM für grosse n):**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # Viele doppelte Berechnungen!
```

**Mit Memoization (SCHNELL):**
```python
def fibonacci(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]  # Schon berechnet

    if n <= 1:
        return n

    # Berechne und speichere
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

**Komplexität:**
- Ohne Memoization: O(2^n) - extrem langsam!
- Mit Memoization: O(n) - sehr schnell!

---

### Anagramm-Checker

**Konzept:** Zwei Strings sind Anagramme, wenn sie die gleichen Buchstaben haben.

**Ansatz 1: Sortieren**
```python
def are_anagrams(str1: str, str2: str) -> bool:
    # Normalisieren: Kleinbuchstaben, keine Leerzeichen
    clean1 = str1.lower().replace(" ", "")
    clean2 = str2.lower().replace(" ", "")

    # Sortieren und vergleichen
    return sorted(clean1) == sorted(clean2)
```

**Ansatz 2: Buchstaben zählen**
```python
from collections import Counter

def are_anagrams(str1: str, str2: str) -> bool:
    clean1 = str1.lower().replace(" ", "")
    clean2 = str2.lower().replace(" ", "")

    return Counter(clean1) == Counter(clean2)
```

---

### Primzahlen-Check

**Naive Methode (LANGSAM):**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # Prüft ALLE Zahlen bis n
        if n % i == 0:
            return False
    return True
```

**Optimierte Methode (SCHNELL):**
```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Nur bis √n prüfen
    import math
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
```

**Warum nur bis √n?**
Wenn n = a × b, dann ist mindestens einer der Faktoren ≤ √n.

## 🧪 Testing mit pytest

**Installation:**
```bash
pip install pytest
```

**Tests ausführen:**
```bash
# Alle Tests
pytest test_algorithms.py

# Mit Details
pytest test_algorithms.py -v

# Nur ein Test
pytest test_algorithms.py::TestBinarySearch::test_found_middle
```

## 📚 Zeitkomplexität (Big-O)

Geben Sie für jeden Algorithmus die Zeitkomplexität an:

| Algorithmus | Zeitkomplexität | Erklärung |
|-------------|----------------|-----------|
| Binary Search | O(log n) | Halbiert Suchbereich in jedem Schritt |
| Palindrome Check | O(n) | Durchläuft String einmal |
| Fibonacci (Memo) | O(n) | Berechnet jede Zahl nur einmal |
| Anagramm-Check | O(n log n) | Wegen Sortierung |
| Prime Check (optimiert) | O(√n) | Prüft nur bis Wurzel |

## 📝 lernprozess.md Template

```markdown
# Lernprozess: Algorithmen-Implementierung

## Gewählte Algorithmen
1. [Algorithmus 1]
2. [Algorithmus 2]
3. [Algorithmus 3]

## KI-Nutzung

### Algorithmus 1: [Name]

**Prompt 1: Konzept verstehen**
```
[Ihr Prompt]
```

**Was habe ich gelernt?**
[Ihre Erkenntnisse]

**Prompt 2: Debugging**
```
[Ihr Prompt]
```

**Wie hat KI geholfen?**
[Ihre Erfahrung]

[Wiederholen für alle 3 Algorithmen]

## Herausforderungen & Lösungen

### Herausforderung 1
**Problem:** [Beschreibung]
**Lösung:** [Wie Sie es gelöst haben]
**Rolle der KI:** [Wie KI geholfen hat]

## Wichtigste Erkenntnisse

1. [Erkenntnis 1]
2. [Erkenntnis 2]
3. [Erkenntnis 3]

## Nächste Schritte

[Was möchten Sie als nächstes über Algorithmen lernen?]
```

## ✅ Selbsttest vor Abgabe

- [ ] 3 Algorithmen vollständig implementiert
- [ ] Alle vorgegebenen Tests bestehen
- [ ] Mindestens 2 eigene Tests pro Algorithmus
- [ ] Type Hints und Docstrings vollständig
- [ ] README.md mit Algorithmus-Übersicht
- [ ] lernprozess.md dokumentiert KI-Nutzung
- [ ] Zeitkomplexität für jeden Algorithmus angegeben

## 📤 Abgabe

Fügen Sie alle Dateien Ihrem Git-Repository hinzu:
```bash
git add aufgabe-3-algorithmen/
git commit -m "Aufgabe 3: Algorithmen implementiert"
git push
```

---

**Viel Erfolg beim Programmieren!** 💻

**Zurück zur Nachbearbeitung:** [README](./README.md)
