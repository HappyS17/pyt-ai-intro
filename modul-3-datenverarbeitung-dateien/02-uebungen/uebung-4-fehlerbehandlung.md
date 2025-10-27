# Übung 4: Robuste Datei-Verarbeitung

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐☆

## 🎯 Ziel

Fehlerbehandlung und Logging für Datei-Operationen implementieren.

## Wählen Sie EINE Option

### Option A: Datei-Verarbeitung mit Exception Handling

#### Anforderungen

Erstellen Sie ein Programm, das:

- Mehrere Dateien verarbeitet
- Alle möglichen Fehler abfängt
- Hilfreiche Fehlermeldungen ausgibt
- Trotz Fehlern weiterläuft

#### Prompt-Vorlage

```text
Erstelle ein robustes Datei-Verarbeitungs-Programm:

Funktion: process_files(file_list)

Für jede Datei:
1. Versuche zu öffnen und zu lesen
2. Zähle Zeilen und Wörter
3. Gib Statistik aus

Exception Handling:
- FileNotFoundError: "Datei nicht gefunden"
- PermissionError: "Keine Leserechte"
- UnicodeDecodeError: "Encoding-Problem"
- Andere: Generische Fehlermeldung

Nach allen Dateien:
- Erfolgreiche: X
- Fehler: Y
- Gesamt: Z

Verwende try/except/finally.
```

#### Test-Szenario

```python
files = [
    "existiert.txt",      # OK
    "nicht_da.txt",       # FileNotFoundError
    "kein_zugriff.txt",   # PermissionError (simuliert)
    "binary.bin"          # UnicodeDecodeError
]
```

#### Erwartete Ausgabe

```text
=== DATEI-VERARBEITUNG ===

✓ existiert.txt
  Zeilen: 10
  Wörter: 85

✗ nicht_da.txt
  Fehler: Datei nicht gefunden

✗ kein_zugriff.txt
  Fehler: Keine Leserechte

✗ binary.bin
  Fehler: Encoding-Problem

=== ZUSAMMENFASSUNG ===
Erfolgreich: 1
Fehler: 3
Gesamt: 4
```

### Option B: Logging-System

#### Anforderungen

Implementieren Sie ein Logging-System für Datei-Operationen:

- Verschiedene Log-Level (INFO, WARNING, ERROR)
- Logs in Datei schreiben
- Formatierte Log-Nachrichten
- Zeitstempel

#### Prompt-Vorlage

```text
Erstelle ein Datei-Verarbeitungs-Programm mit Logging:

Setup:
- logging-Modul konfigurieren
- Log-Datei: "app.log"
- Format: "[ZEIT] LEVEL - Nachricht"
- Level: INFO und höher

Programm:
- Liest mehrere CSV-Dateien
- Loggt jeden Schritt:
  * INFO: "Verarbeite datei.csv"
  * INFO: "X Zeilen gelesen"
  * WARNING: "Leere Zeilen gefunden"
  * ERROR: "Fehler beim Lesen"

Nach Verarbeitung:
- Zeige Log-Datei-Inhalt
- Statistik (INFO/WARNING/ERROR)
```

#### Erwartetes Log

```text
[2025-10-27 10:30:15] INFO - Starte Verarbeitung
[2025-10-27 10:30:15] INFO - Verarbeite daten1.csv
[2025-10-27 10:30:15] INFO - 100 Zeilen gelesen
[2025-10-27 10:30:16] WARNING - 3 leere Zeilen übersprungen
[2025-10-27 10:30:16] INFO - Verarbeite daten2.csv
[2025-10-27 10:30:16] ERROR - Datei nicht gefunden: daten2.csv
[2025-10-27 10:30:16] INFO - Verarbeitung abgeschlossen
```

### Option C: Retry-Mechanismus

#### Anforderungen

Implementieren Sie einen Retry-Mechanismus für fehleranfällige Operationen:

- Automatische Wiederholung bei Fehlern
- Exponential Backoff
- Maximale Versuche
- Logging

#### Prompt-Vorlage

```text
Erstelle eine retry_operation Funktion:

Parameter:
- operation: Funktion die ausgeführt wird
- max_retries: Maximale Versuche (default: 3)
- delay: Start-Verzögerung in Sekunden (default: 1)

Verhalten:
- Versucht operation() auszuführen
- Bei Fehler: Wartet delay Sekunden
- Verdoppelt delay bei jedem Versuch (Exponential Backoff)
- Nach max_retries: Wirft Exception

Beispiel-Anwendung:
- Datei von URL herunterladen
- Bei Netzwerkfehler: Retry
- Loggt jeden Versuch

Verwende time.sleep() und Exception Handling.
```

#### Erwartetes Verhalten

```text
Versuch 1/3: Fehler (Netzwerk-Timeout)
Warte 1 Sekunde...

Versuch 2/3: Fehler (Netzwerk-Timeout)
Warte 2 Sekunden...

Versuch 3/3: Erfolg!
Datei heruntergeladen: 1.2 MB
```

## 💡 Tipps

- Spezifische Exceptions vor generischen fangen
- `logging.basicConfig()` für einfaches Setup
- `time.sleep()` für Verzögerungen
- `finally` für Cleanup-Code

## ✅ Erfolg

Sie haben die Übung erfolgreich abgeschlossen, wenn:

- [ ] Alle Exceptions korrekt behandelt
- [ ] Hilfreiche Fehlermeldungen
- [ ] Logging implementiert (Option B)
- [ ] Retry-Logik funktioniert (Option C)
- [ ] Code gut dokumentiert

---

**Zurück zu:** [Übungen README](./README.md)
