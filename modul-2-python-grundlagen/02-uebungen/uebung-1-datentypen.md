# Übung 1: Variablen & Datentypen

**Dauer:** 15 Minuten  
**Lektion:** 1  
**Schwierigkeit:** ⭐☆☆

## 🎯 Ziel

Mit verschiedenen Datentypen und Operatoren arbeiten.

## 📝 Aufgabenstellung

Wählen Sie **EINE** der folgenden Optionen und implementieren Sie diese mit KI-Unterstützung.

## Option A: Altersrechner

### Anforderungen

- Geburtsjahr vom Benutzer einlesen
- Aktuelles Jahr verwenden (2025)
- Alter in Jahren berechnen
- Alter in Tagen berechnen (ca. 365 Tage/Jahr)
- Formatierte Ausgabe

### Beispiel-Interaktion

```text
Geburtsjahr: 1990
Du bist 35 Jahre alt.
Das sind ungefähr 12775 Tage!
```

### Prompt-Vorlage

```text
Erstelle ein Python-Programm: Altersrechner

Anforderungen:
- Geburtsjahr vom Benutzer einlesen
- Aktuelles Jahr: 2025
- Alter in Jahren berechnen
- Alter in Tagen berechnen (365 Tage/Jahr)
- Formatierte Ausgabe mit f-Strings

Beispiel:
Eingabe: 1990
Ausgabe: 
  Du bist 35 Jahre alt.
  Das sind ungefähr 12775 Tage!

Einschränkungen:
- Type Hints verwenden
- Kommentare auf Deutsch
- Eingabe-Validierung (nur Zahlen)
```

## Option B: Währungsrechner

### Anforderungen

- Betrag in EUR vom Benutzer einlesen
- Umrechnung in CHF (Kurs: 1 EUR = 0.95 CHF)
- Ergebnis auf 2 Dezimalstellen runden
- Formatierte Ausgabe

### Beispiel-Interaktion

```text
Betrag in EUR: 100
100.00 EUR = 95.00 CHF
```

### Prompt-Vorlage

```text
Erstelle ein Python-Programm: Währungsrechner EUR → CHF

Anforderungen:
- Betrag in EUR einlesen
- Umrechnungskurs: 1 EUR = 0.95 CHF
- Ergebnis auf 2 Dezimalstellen runden
- Formatierte Ausgabe

Beispiel:
Eingabe: 100
Ausgabe: 100.00 EUR = 95.00 CHF

Einschränkungen:
- Type Hints verwenden
- Kommentare auf Deutsch
- Fehlerbehandlung für ungültige Eingaben
```

## Option C: Textanalyse-Tool

### Anforderungen

- Text vom Benutzer einlesen
- Anzahl Wörter zählen
- Anzahl Zeichen zählen (mit und ohne Leerzeichen)
- Formatierte Ausgabe

### Beispiel-Interaktion

```text
Text: Hallo Welt
Wörter: 2
Zeichen (mit Leerzeichen): 10
Zeichen (ohne Leerzeichen): 9
```

### Prompt-Vorlage

```text
Erstelle ein Python-Programm: Textanalyse-Tool

Anforderungen:
- Text vom Benutzer einlesen
- Anzahl Wörter zählen
- Anzahl Zeichen mit Leerzeichen zählen
- Anzahl Zeichen ohne Leerzeichen zählen
- Formatierte Ausgabe

Beispiel:
Eingabe: "Hallo Welt"
Ausgabe:
  Wörter: 2
  Zeichen (mit Leerzeichen): 10
  Zeichen (ohne Leerzeichen): 9

Einschränkungen:
- Type Hints verwenden
- Kommentare auf Deutsch
```

## ✅ Checkliste

- [ ] Option gewählt
- [ ] Prompt formuliert
- [ ] Code generiert
- [ ] Code verstanden
- [ ] Getestet mit verschiedenen Eingaben
- [ ] Funktioniert korrekt

## 💡 Tipps

- Nutzen Sie f-Strings für Formatierung
- Testen Sie mit verschiedenen Werten
- Fragen Sie KI bei Unklarheiten

---

**Zurück zu:** [Übungen README](./README.md)
