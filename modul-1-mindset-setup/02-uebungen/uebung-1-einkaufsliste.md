# Übung 1: Einkaufsliste durchdenken

**Dauer:** 15 Minuten  
**Lektion:** 1  
**Sozialform:** Einzel → Gruppe → Plenum

## 🎯 Lernziel

Problemdekomposition üben - ein grosses Problem in kleine, lösbare Teilprobleme zerlegen.

## 📝 Aufgabenstellung

Sie möchten ein Programm schreiben, das eine Einkaufsliste verwaltet.

### Funktionen

Das Programm soll folgende Funktionen haben:

- Artikel hinzufügen
- Artikel entfernen
- Alle Artikel anzeigen
- Prüfen, ob ein Artikel auf der Liste ist

### Ihre Aufgabe

**WICHTIG:** Schreiben Sie noch KEINEN Code! Denken Sie nur über die Lösung nach.

1. **Zerlegen Sie das Problem** in Teilprobleme
2. **Überlegen Sie:** Welche Daten müssen gespeichert werden?
3. **Planen Sie:** Welche Schritte sind für jede Funktion nötig?

## 🔄 Ablauf

### Phase 1: Einzelarbeit (5 Min.)

Notieren Sie Ihre Überlegungen:

#### Frage 1: Datenstruktur

Wie speichern Sie die Artikel?

- Option A: Liste
- Option B: Dictionary
- Option C: Etwas anderes?

**Ihre Wahl und Begründung:**

```text
[Hier notieren]
```

#### Frage 2: Artikel hinzufügen

Welche Schritte sind nötig?

```text
Schritt 1: ...
Schritt 2: ...
Schritt 3: ...
```

**Besondere Überlegungen:**

- Was passiert, wenn der Artikel schon existiert?
- Soll die Menge gespeichert werden?

#### Frage 3: Artikel entfernen

Welche Schritte sind nötig?

```text
Schritt 1: ...
Schritt 2: ...
Schritt 3: ...
```

**Besondere Überlegungen:**

- Was passiert, wenn der Artikel nicht existiert?
- Fehlermeldung oder ignorieren?

#### Frage 4: Artikel anzeigen

Wie soll die Ausgabe aussehen?

```text
Beispiel:
[Ihre Idee hier]
```

### Phase 2: Gruppenarbeit (5 Min.)

Bilden Sie 2er-Gruppen.

**Aufgaben:**

1. Vergleichen Sie Ihre Ansätze
2. Diskutieren Sie Unterschiede
3. Einigen Sie sich auf eine Lösung
4. Notieren Sie offene Fragen

### Phase 3: Plenum (5 Min.)

2-3 Gruppen präsentieren kurz (1-2 Min. pro Gruppe).

**Diskussionspunkte:**

- Welche Datenstruktur wurde gewählt? Warum?
- Wie werden Duplikate behandelt?
- Wie sieht die Benutzerinteraktion aus?

## 💡 Leitfragen

### Zur Datenstruktur

**Liste:**

```python
einkaufsliste = ["Milch", "Brot", "Eier"]
```

**Vorteile:**

- Einfach
- Reihenfolge erhalten

**Nachteile:**

- Duplikate möglich
- Keine Mengenangaben

**Dictionary:**

```python
einkaufsliste = {"Milch": 2, "Brot": 1, "Eier": 12}
```

**Vorteile:**

- Mengen speicherbar
- Keine Duplikate

**Nachteile:**

- Komplexer

### Zur Logik

**Artikel hinzufügen:**

```text
1. Artikel-Name vom Benutzer einlesen
2. Prüfen: Ist Artikel schon in Liste?
   - Ja: Menge erhöhen ODER Meldung "Schon vorhanden"
   - Nein: Artikel hinzufügen
3. Bestätigung ausgeben
```

**Artikel entfernen:**

```text
1. Artikel-Name vom Benutzer einlesen
2. Prüfen: Ist Artikel in Liste?
   - Ja: Artikel entfernen
   - Nein: Fehlermeldung
3. Bestätigung ausgeben
```

**Artikel anzeigen:**

```text
1. Prüfen: Ist Liste leer?
   - Ja: "Liste ist leer"
   - Nein: Alle Artikel durchgehen und ausgeben
2. Optional: Nummerierung, Formatierung
```

## ✅ Checkliste

Nach der Übung sollten Sie:

- [ ] Verstehen, was Problemdekomposition bedeutet
- [ ] Ein Problem in Teilprobleme zerlegt haben
- [ ] Verschiedene Lösungsansätze verglichen haben
- [ ] Offene Fragen identifiziert haben

## 🎓 Reflexion

**Wichtige Erkenntnisse:**

1. **Vor dem Coden denken:** Planung spart Zeit
2. **Mehrere Lösungen möglich:** Es gibt nicht DIE eine Lösung
3. **Details wichtig:** Edge Cases bedenken
4. **Austausch hilft:** Andere Perspektiven sind wertvoll

## 📎 Hinweis

In späteren Modulen werden Sie diese Einkaufsliste tatsächlich programmieren!

Bewahren Sie Ihre Notizen auf.

---

**Zurück zur Übungsübersicht:** [Übungen README](./README.md)
