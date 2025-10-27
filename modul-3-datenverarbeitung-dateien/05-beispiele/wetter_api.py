"""
Wetter-API Beispiel
Verwendung: Lektion 3 - Live-Demo

Nutzt OpenWeatherMap API (kostenloser Account nötig)
"""
import requests
import json
from datetime import datetime
from typing import Dict, Optional


class WetterClient:
    """Client für Wetter-API."""
    
    def __init__(self, api_key: str):
        """
        Initialisiert Client.
        
        Args:
            api_key: OpenWeatherMap API Key
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    def hole_aktuelles_wetter(self, stadt: str) -> Optional[Dict]:
        """
        Holt aktuelles Wetter für Stadt.
        
        Args:
            stadt: Name der Stadt
        
        Returns:
            Wetter-Daten als Dictionary oder None bei Fehler
        """
        url = f"{self.base_url}/weather"
        params = {
            "q": stadt,
            "appid": self.api_key,
            "units": "metric",  # Celsius
            "lang": "de"
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f"Stadt '{stadt}' nicht gefunden")
            else:
                print(f"HTTP-Fehler: {e}")
            return None
        
        except requests.exceptions.Timeout:
            print("Timeout: API antwortet nicht")
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Netzwerkfehler: {e}")
            return None
    
    def formatiere_wetter(self, daten: Dict) -> str:
        """
        Formatiert Wetter-Daten für Ausgabe.
        
        Args:
            daten: Wetter-Daten von API
        
        Returns:
            Formatierter String
        """
        stadt = daten['name']
        land = daten['sys']['country']
        temp = daten['main']['temp']
        gefuehlt = daten['main']['feels_like']
        beschreibung = daten['weather'][0]['description']
        luftfeuchtigkeit = daten['main']['humidity']
        wind = daten['wind']['speed']
        
        output = f"""
=== WETTER FÜR {stadt.upper()}, {land} ===

Temperatur: {temp}°C (gefühlt: {gefuehlt}°C)
Bedingungen: {beschreibung}
Luftfeuchtigkeit: {luftfeuchtigkeit}%
Wind: {wind} m/s
"""
        return output
    
    def speichere_wetter(self, daten: Dict, dateiname: str = "wetter.json"):
        """
        Speichert Wetter-Daten in JSON-Datei.
        
        Args:
            daten: Wetter-Daten
            dateiname: Name der Ausgabedatei
        """
        # Füge Zeitstempel hinzu
        daten['abgerufen_am'] = datetime.now().isoformat()
        
        with open(dateiname, 'w', encoding='utf-8') as f:
            json.dump(daten, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Wetter-Daten gespeichert in: {dateiname}")


def demo_ohne_api_key():
    """Demo mit Mock-Daten (ohne echten API Key)."""
    print("=" * 50)
    print("DEMO: WETTER-API (MOCK-DATEN)")
    print("=" * 50)
    
    # Mock-Daten (Beispiel-Response)
    mock_daten = {
        "name": "Zürich",
        "sys": {"country": "CH"},
        "main": {
            "temp": 18.5,
            "feels_like": 17.2,
            "humidity": 65
        },
        "weather": [
            {"description": "leicht bewölkt"}
        ],
        "wind": {"speed": 3.5}
    }
    
    client = WetterClient("DEMO_KEY")
    
    # Formatieren und ausgeben
    print(client.formatiere_wetter(mock_daten))
    
    # Speichern
    client.speichere_wetter(mock_daten, "wetter_demo.json")


def main():
    """Hauptfunktion."""
    print("=" * 50)
    print("WETTER-API CLIENT")
    print("=" * 50)
    
    # API Key aus Umgebungsvariable oder Input
    import os
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("\n⚠ Kein API Key gefunden!")
        print("Setze OPENWEATHER_API_KEY Umgebungsvariable")
        print("Oder hole kostenlosen Key: https://openweathermap.org/api")
        print("\nFühre Demo mit Mock-Daten aus...\n")
        demo_ohne_api_key()
        return
    
    # Mit echtem API Key
    client = WetterClient(api_key)
    
    # Städte abfragen
    staedte = ["Zürich", "Bern", "Basel", "Genf"]
    
    for stadt in staedte:
        print(f"\nHole Wetter für {stadt}...")
        daten = client.hole_aktuelles_wetter(stadt)
        
        if daten:
            print(client.formatiere_wetter(daten))
            client.speichere_wetter(daten, f"wetter_{stadt.lower()}.json")
        
        print("-" * 50)


if __name__ == "__main__":
    main()
