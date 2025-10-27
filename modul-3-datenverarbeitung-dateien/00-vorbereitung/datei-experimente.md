# Datei-Experimente

**Zeitaufwand:** 60 Minuten  
**Ziel:** Praktische Erfahrung mit Datei-Operationen sammeln

## 🎯 Aufgabe

Führen Sie die folgenden Experimente durch und dokumentieren Sie Ihre Beobachtungen.

## Experiment 1: Text-Datei erstellen (15 Min.)

### Aufgabe

Erstellen Sie eine Python-Datei, die:

1. Eine Text-Datei `notizen.txt` erstellt
2. 5 Zeilen Text hineinschreibt
3. Die Datei wieder einliest
4. Den Inhalt auf der Konsole ausgibt

### Mit KI

```text
Erstelle ein Python-Skript das:
- Eine Text-Datei "notizen.txt" erstellt
- 5 Zeilen mit verschiedenen Notizen schreibt
- Die Datei wieder einliest
- Jede Zeile nummeriert ausgibt

Verwende with-Statement für sichere Datei-Operationen.
```

### Dokumentation

**Was haben Sie gelernt?**

```text
[Ihre Notizen]
```

**Welche Fehler sind aufgetreten?**

```text
[Ihre Notizen]
```

## Experiment 2: CSV-Daten lesen (15 Min.)

### Aufgabe

Erstellen Sie manuell eine CSV-Datei `personen.csv`:

```csv
name,alter,stadt
Anna,25,Zürich
Bob,30,Bern
Clara,28,Basel
```

Schreiben Sie dann ein Python-Skript, das:

1. Die CSV-Datei einliest
2. Alle Personen über 25 Jahre filtert
3. Das Ergebnis ausgibt

### Mit KI

```text
Ich habe eine CSV-Datei "personen.csv" mit Spalten: name, alter, stadt

Erstelle ein Python-Skript das:
- Die CSV-Datei mit dem csv-Modul einliest
- Alle Personen über 25 Jahre filtert
- Name und Stadt dieser Personen ausgibt

Verwende DictReader für bessere Lesbarkeit.
```

### Dokumentation

**Wie funktioniert csv.DictReader?**

```text
[Ihre Notizen]
```

## Experiment 3: JSON parsen (15 Min.)

### Aufgabe

Erstellen Sie eine JSON-Datei `config.json`:

```json
{
  "app_name": "Meine App",
  "version": "1.0.0",
  "debug": true,
  "database": {
    "host": "localhost",
    "port": 5432
  }
}
```

Schreiben Sie ein Python-Skript, das:

1. Die JSON-Datei einliest
2. Den App-Namen ausgibt
3. Die Debug-Einstellung ändert
4. Die Datei wieder speichert

### Mit KI

```text
Erstelle ein Python-Skript für JSON-Konfiguration:

1. Liest "config.json" ein
2. Gibt app_name und version aus
3. Ändert debug von true zu false
4. Speichert die Änderung zurück

Verwende json.load() und json.dump() mit indent=2.
```

### Dokumentation

**Unterschied zwischen load() und loads()?**

```text
[Ihre Notizen]
```

## Experiment 4: Fehler provozieren (15 Min.)

### Aufgabe

Experimentieren Sie mit Fehlern:

1. Versuchen Sie, eine nicht existierende Datei zu öffnen
2. Schreiben Sie in eine Datei ohne Schreibrechte
3. Lesen Sie eine korrupte JSON-Datei

Dokumentieren Sie die Fehlermeldungen.

### Mit KI

```text
Erstelle ein Python-Skript das verschiedene Datei-Fehler demonstriert:

1. FileNotFoundError - nicht existierende Datei
2. PermissionError - keine Schreibrechte
3. JSONDecodeError - ungültiges JSON

Fange jeden Fehler mit try/except ab und gib eine hilfreiche Nachricht aus.
```

### Dokumentation

**Welche Exceptions gibt es?**

```text
[Ihre Notizen]
```

**Wie behandelt man sie richtig?**

```text
[Ihre Notizen]
```

## ✅ Checkliste

- [ ] Experiment 1: Text-Datei erstellt
- [ ] Experiment 2: CSV gelesen
- [ ] Experiment 3: JSON bearbeitet
- [ ] Experiment 4: Fehler behandelt
- [ ] Alle Notizen dokumentiert

---

**Zurück zu:** [Vorbereitung README](./README.md)
