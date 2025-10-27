"""
Log-Datei-Analyse
Verwendung: Lektion 1 - Live-Demo
"""
from pathlib import Path
from collections import Counter


def analysiere_log(dateiname: str) -> dict:
    """
    Analysiert eine Log-Datei und gibt Statistiken zurück.
    
    Args:
        dateiname: Pfad zur Log-Datei
    
    Returns:
        Dictionary mit Statistiken
    """
    stats = {
        "zeilen": 0,
        "errors": 0,
        "warnings": 0,
        "info": 0,
        "error_messages": []
    }
    
    pfad = Path(dateiname)
    
    if not pfad.exists():
        raise FileNotFoundError(f"Datei {dateiname} nicht gefunden")
    
    with open(pfad, "r", encoding="utf-8") as f:
        for zeile in f:
            stats["zeilen"] += 1
            
            if "ERROR" in zeile:
                stats["errors"] += 1
                stats["error_messages"].append(zeile.strip())
            elif "WARNING" in zeile:
                stats["warnings"] += 1
            elif "INFO" in zeile:
                stats["info"] += 1
    
    return stats


def erstelle_report(stats: dict, output_datei: str) -> None:
    """
    Erstellt einen Report aus den Statistiken.
    
    Args:
        stats: Statistik-Dictionary
        output_datei: Pfad für Report-Datei
    """
    with open(output_datei, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("LOG-ANALYSE REPORT\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"Gesamte Zeilen: {stats['zeilen']}\n")
        f.write(f"Errors: {stats['errors']}\n")
        f.write(f"Warnings: {stats['warnings']}\n")
        f.write(f"Info: {stats['info']}\n\n")
        
        if stats['error_messages']:
            f.write("Error-Messages:\n")
            f.write("-" * 50 + "\n")
            for msg in stats['error_messages'][:10]:  # Nur erste 10
                f.write(f"- {msg}\n")


def main():
    """Hauptfunktion."""
    try:
        # Log-Datei analysieren
        stats = analysiere_log("app.log")
        
        # Statistiken ausgeben
        print("=" * 50)
        print("LOG-ANALYSE")
        print("=" * 50)
        print(f"Zeilen: {stats['zeilen']}")
        print(f"Errors: {stats['errors']}")
        print(f"Warnings: {stats['warnings']}")
        print(f"Info: {stats['info']}")
        
        # Report erstellen
        erstelle_report(stats, "log_report.txt")
        print("\nReport erstellt: log_report.txt")
        
    except FileNotFoundError as e:
        print(f"Fehler: {e}")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")


if __name__ == "__main__":
    main()
