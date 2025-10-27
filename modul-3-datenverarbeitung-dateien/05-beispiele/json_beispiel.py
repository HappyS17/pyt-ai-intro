"""
JSON-Daten verarbeiten
Verwendung: Lektion 3 - Live-Demo
"""
import json
from pathlib import Path


def lese_json(dateiname: str) -> dict:
    """
    Liest JSON-Datei.
    
    Args:
        dateiname: Pfad zur JSON-Datei
    
    Returns:
        Dictionary mit Daten
    """
    with open(dateiname, "r", encoding="utf-8") as f:
        return json.load(f)


def schreibe_json(dateiname: str, daten: dict) -> None:
    """
    Schreibt Daten in JSON-Datei.
    
    Args:
        dateiname: Pfad zur JSON-Datei
        daten: Dictionary mit Daten
    """
    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=2, ensure_ascii=False)


def json_string_zu_dict(json_string: str) -> dict:
    """
    Konvertiert JSON-String zu Dictionary.
    
    Args:
        json_string: JSON als String
    
    Returns:
        Dictionary
    """
    return json.loads(json_string)


def dict_zu_json_string(daten: dict) -> str:
    """
    Konvertiert Dictionary zu JSON-String.
    
    Args:
        daten: Dictionary
    
    Returns:
        JSON als String
    """
    return json.dumps(daten, indent=2, ensure_ascii=False)


def main():
    """Hauptfunktion."""
    # Beispiel-Daten
    config = {
        "app_name": "Meine App",
        "version": "1.0.0",
        "settings": {
            "debug": True,
            "port": 8080,
            "allowed_hosts": ["localhost", "127.0.0.1"]
        },
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        }
    }
    
    # JSON schreiben
    schreibe_json("config.json", config)
    print("JSON erstellt: config.json")
    
    # JSON lesen
    gelesene_config = lese_json("config.json")
    print("\nGelesene Konfiguration:")
    print(f"App: {gelesene_config['app_name']}")
    print(f"Version: {gelesene_config['version']}")
    print(f"Debug: {gelesene_config['settings']['debug']}")
    
    # JSON-String
    json_str = dict_zu_json_string(config)
    print("\nAls JSON-String:")
    print(json_str[:100] + "...")


if __name__ == "__main__":
    main()
