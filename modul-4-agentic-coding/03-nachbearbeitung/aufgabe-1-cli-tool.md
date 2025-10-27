# Aufgabe 1: CLI-Tool

**Zeitaufwand:** 180 Minuten | **Punkte:** 35% | **Schwierigkeit:** ⭐⭐⭐

## 🎯 Ziel

Erstellen Sie ein vollständiges Command-Line Tool mit KI-Unterstützung.

## Anforderungen

### Funktional

- Mehrere Commands (mindestens 3)
- Argument-Parsing (click oder argparse)
- Konfigurationsdatei (JSON/YAML)
- Fehlerbehandlung
- Logging

### Technisch

- Python 3.11+
- Type Hints
- Docstrings
- Unit Tests (pytest)
- CI/CD (GitHub Actions)

## Beispiel-Tool: Task Manager CLI

```bash
# Tasks erstellen
task add "Code reviewen" --priority high

# Tasks auflisten
task list --status open

# Task als erledigt markieren
task complete 1

# Statistik
task stats
```

## Prompt-Vorlage

```text
Erstelle ein vollständiges CLI-Tool: Task Manager

Features:
1. add <task> [--priority high|medium|low]
2. list [--status open|done|all]
3. complete <id>
4. delete <id>
5. stats

Technologie:
- click für CLI
- JSON für Storage
- pytest für Tests
- Type Hints
- Logging

Struktur:
task_manager/
  __init__.py
  cli.py          # Click Commands
  storage.py      # JSON Storage
  models.py       # Task Model
tests/
  test_cli.py
  test_storage.py
README.md
requirements.txt
.github/workflows/test.yml
```

## Bewertung

| Kriterium | Punkte |
|-----------|--------|
| Funktionalität | 10 |
| Code-Qualität | 8 |
| Tests | 7 |
| Dokumentation | 5 |
| CI/CD | 5 |

**Gesamt:** 35 Punkte

---

**Zurück zu:** [Nachbearbeitung README](./README.md)
