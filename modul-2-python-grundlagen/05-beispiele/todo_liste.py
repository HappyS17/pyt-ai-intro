"""
Todo-Listen-Verwaltung
Demonstriert: Listen, Dictionaries, CRUD-Operationen
"""

from datetime import datetime


def erstelle_todo(beschreibung: str, prioritaet: str = "normal") -> dict:
    """
    Erstellt ein neues Todo-Item.

    Args:
        beschreibung: Beschreibung der Aufgabe
        prioritaet: Priorität ("niedrig", "normal", "hoch")

    Returns:
        Todo-Dictionary
    """
    return {
        "id": None,  # Wird später gesetzt
        "beschreibung": beschreibung,
        "prioritaet": prioritaet,
        "erledigt": False,
        "erstellt": datetime.now().isoformat(),
        "erledigt_am": None,
    }


def naechste_id(todos: list) -> int:
    """
    Generiert die nächste verfügbare ID.

    Args:
        todos: Liste der Todos

    Returns:
        Nächste freie ID
    """
    if not todos:
        return 1
    return max(todo["id"] for todo in todos) + 1


def todo_hinzufuegen(todos: list, beschreibung: str, prioritaet: str = "normal") -> None:
    """
    Fügt ein neues Todo hinzu.

    Args:
        todos: Liste der Todos
        beschreibung: Beschreibung der Aufgabe
        prioritaet: Priorität
    """
    todo = erstelle_todo(beschreibung, prioritaet)
    todo["id"] = naechste_id(todos)
    todos.append(todo)
    print(f"✓ Todo #{todo['id']} hinzugefügt")


def todo_anzeigen(todos: list, filter: str = "alle") -> None:
    """
    Zeigt Todos an.

    Args:
        todos: Liste der Todos
        filter: "alle", "offen", "erledigt"
    """
    # Filtern
    if filter == "offen":
        gefiltert = [t for t in todos if not t["erledigt"]]
    elif filter == "erledigt":
        gefiltert = [t for t in todos if t["erledigt"]]
    else:
        gefiltert = todos

    if not gefiltert:
        print(f"📋 Keine Todos ({filter})")
        return

    # Sortieren nach Priorität
    prioritaet_wert = {"hoch": 3, "normal": 2, "niedrig": 1}
    gefiltert.sort(
        key=lambda t: (t["erledigt"], -prioritaet_wert.get(t["prioritaet"], 0))
    )

    # Ausgabe
    print(f"\n📋 TODO-LISTE ({filter.upper()})")
    print("=" * 70)

    for todo in gefiltert:
        # Symbol
        symbol = "✓" if todo["erledigt"] else "☐"

        # Priorität-Emoji
        prio_emoji = {"hoch": "🔴", "normal": "🟡", "niedrig": "🟢"}
        prio = prio_emoji.get(todo["prioritaet"], "⚪")

        # Beschreibung (durchgestrichen wenn erledigt)
        beschreibung = todo["beschreibung"]
        if todo["erledigt"]:
            beschreibung = f"~~{beschreibung}~~"

        print(f"{symbol} {prio} #{todo['id']:2} | {beschreibung}")

    print()


def todo_als_erledigt_markieren(todos: list, todo_id: int) -> bool:
    """
    Markiert ein Todo als erledigt.

    Args:
        todos: Liste der Todos
        todo_id: ID des Todos

    Returns:
        True wenn erfolgreich
    """
    for todo in todos:
        if todo["id"] == todo_id:
            if todo["erledigt"]:
                print(f"⚠️  Todo #{todo_id} ist bereits erledigt")
                return False

            todo["erledigt"] = True
            todo["erledigt_am"] = datetime.now().isoformat()
            print(f"✓ Todo #{todo_id} als erledigt markiert")
            return True

    print(f"❌ Todo #{todo_id} nicht gefunden")
    return False


def todo_loeschen(todos: list, todo_id: int) -> bool:
    """
    Löscht ein Todo.

    Args:
        todos: Liste der Todos
        todo_id: ID des Todos

    Returns:
        True wenn erfolgreich
    """
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            print(f"✓ Todo #{todo_id} gelöscht")
            return True

    print(f"❌ Todo #{todo_id} nicht gefunden")
    return False


def statistik_anzeigen(todos: list) -> None:
    """
    Zeigt Statistiken der Todo-Liste.

    Args:
        todos: Liste der Todos
    """
    if not todos:
        print("📊 Keine Todos vorhanden")
        return

    gesamt = len(todos)
    erledigt = sum(1 for t in todos if t["erledigt"])
    offen = gesamt - erledigt

    # Nach Priorität
    prioritaeten = {}
    for todo in todos:
        prio = todo["prioritaet"]
        prioritaeten[prio] = prioritaeten.get(prio, 0) + 1

    # Ausgabe
    print(f"\n📊 STATISTIK")
    print("=" * 30)
    print(f"Gesamt:    {gesamt}")
    print(f"Offen:     {offen}")
    print(f"Erledigt:  {erledigt}")

    if gesamt > 0:
        prozent = (erledigt / gesamt) * 100
        print(f"Fortschritt: {prozent:.1f}%")

        # Balken
        balken_voll = int(prozent / 10)
        balken_leer = 10 - balken_voll
        print(f"[{'█' * balken_voll}{'░' * balken_leer}]")

    print(f"\nPrioritäten:")
    for prio, anzahl in sorted(prioritaeten.items(), reverse=True):
        emoji = {"hoch": "🔴", "normal": "🟡", "niedrig": "🟢"}
        print(f"  {emoji.get(prio, '⚪')} {prio.capitalize()}: {anzahl}")


def main() -> None:
    """Hauptfunktion - Interaktive Todo-Verwaltung."""
    todos = []

    # Demo-Daten
    todos.append(erstelle_todo("Python Modul 2 abschließen", "hoch"))
    todos[0]["id"] = 1
    todos.append(erstelle_todo("Einkaufen gehen", "normal"))
    todos[1]["id"] = 2
    todos.append(erstelle_todo("Dokumentation schreiben", "niedrig"))
    todos[2]["id"] = 3

    print("=" * 40)
    print("  📝 TODO-LISTEN-VERWALTUNG")
    print("=" * 40)

    while True:
        print("\n1. Todo hinzufügen")
        print("2. Alle Todos anzeigen")
        print("3. Offene Todos anzeigen")
        print("4. Todo als erledigt markieren")
        print("5. Todo löschen")
        print("6. Statistik anzeigen")
        print("7. Beenden")

        wahl = input("\nWähle (1-7): ")

        if wahl == "1":
            beschreibung = input("Beschreibung: ")
            prioritaet = input("Priorität (niedrig/normal/hoch, Enter für normal): ") or "normal"

            if prioritaet not in ["niedrig", "normal", "hoch"]:
                print("⚠️  Ungültige Priorität, verwende 'normal'")
                prioritaet = "normal"

            todo_hinzufuegen(todos, beschreibung, prioritaet)

        elif wahl == "2":
            todo_anzeigen(todos, "alle")

        elif wahl == "3":
            todo_anzeigen(todos, "offen")

        elif wahl == "4":
            try:
                todo_id = int(input("Todo-ID: "))
                todo_als_erledigt_markieren(todos, todo_id)
            except ValueError:
                print("❌ Bitte eine gültige Zahl eingeben")

        elif wahl == "5":
            try:
                todo_id = int(input("Todo-ID: "))
                todo_loeschen(todos, todo_id)
            except ValueError:
                print("❌ Bitte eine gültige Zahl eingeben")

        elif wahl == "6":
            statistik_anzeigen(todos)

        elif wahl == "7":
            print("\n👋 Auf Wiedersehen!")
            break

        else:
            print("❌ Ungültige Wahl!")


if __name__ == "__main__":
    main()
