"""
Robuste Datei-Verarbeitung mit Exception Handling und Logging
Verwendung: Lektion 4 - Live-Demo
"""
import csv
import logging
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('verarbeitung.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class DateiVerarbeiter:
    """Robuster Datei-Verarbeiter mit Fehlerbehandlung."""
    
    def __init__(self):
        """Initialisiert Verarbeiter."""
        self.erfolge = 0
        self.fehler = 0
        self.gesamt = 0
    
    def verarbeite_csv(self, dateiname: str) -> Optional[List[Dict]]:
        """
        Verarbeitet CSV-Datei mit Fehlerbehandlung.
        
        Args:
            dateiname: Pfad zur CSV-Datei
        
        Returns:
            Liste von Dictionaries oder None bei Fehler
        """
        logger.info(f"Verarbeite CSV: {dateiname}")
        self.gesamt += 1
        
        pfad = Path(dateiname)
        
        # Prüfe ob Datei existiert
        if not pfad.exists():
            logger.error(f"Datei nicht gefunden: {dateiname}")
            self.fehler += 1
            return None
        
        # Prüfe ob Datei lesbar
        if not pfad.is_file():
            logger.error(f"Kein gültiger Datei-Pfad: {dateiname}")
            self.fehler += 1
            return None
        
        try:
            with open(pfad, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                daten = list(reader)
                
                if not daten:
                    logger.warning(f"Datei ist leer: {dateiname}")
                
                logger.info(f"✓ {len(daten)} Zeilen gelesen aus {dateiname}")
                self.erfolge += 1
                return daten
        
        except PermissionError:
            logger.error(f"Keine Leserechte für: {dateiname}")
            self.fehler += 1
            return None
        
        except UnicodeDecodeError as e:
            logger.error(f"Encoding-Problem in {dateiname}: {e}")
            logger.info("Versuche mit latin-1 Encoding...")
            
            try:
                with open(pfad, 'r', encoding='latin-1') as f:
                    reader = csv.DictReader(f)
                    daten = list(reader)
                    logger.info(f"✓ Erfolgreich mit latin-1: {len(daten)} Zeilen")
                    self.erfolge += 1
                    return daten
            except Exception as e2:
                logger.error(f"Auch latin-1 fehlgeschlagen: {e2}")
                self.fehler += 1
                return None
        
        except csv.Error as e:
            logger.error(f"CSV-Format-Fehler in {dateiname}: {e}")
            self.fehler += 1
            return None
        
        except Exception as e:
            logger.error(f"Unerwarteter Fehler bei {dateiname}: {e}")
            self.fehler += 1
            return None
    
    def bereinige_daten(self, daten: List[Dict]) -> List[Dict]:
        """
        Bereinigt Daten.
        
        Args:
            daten: Liste von Dictionaries
        
        Returns:
            Bereinigte Daten
        """
        logger.info("Bereinige Daten...")
        original_anzahl = len(daten)
        
        # Entferne leere Zeilen
        daten = [row for row in daten if any(row.values())]
        
        if len(daten) < original_anzahl:
            entfernt = original_anzahl - len(daten)
            logger.warning(f"{entfernt} leere Zeilen entfernt")
        
        logger.info(f"✓ Bereinigung abgeschlossen: {len(daten)} Zeilen")
        return daten
    
    def speichere_ergebnis(self, daten: List[Dict], ausgabe: str):
        """
        Speichert Ergebnis in CSV.
        
        Args:
            daten: Zu speichernde Daten
            ausgabe: Ausgabe-Dateiname
        """
        if not daten:
            logger.warning("Keine Daten zum Speichern")
            return
        
        try:
            pfad = Path(ausgabe)
            pfad.parent.mkdir(parents=True, exist_ok=True)
            
            with open(pfad, 'w', newline='', encoding='utf-8') as f:
                fieldnames = daten[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(daten)
            
            logger.info(f"✓ Ergebnis gespeichert: {ausgabe}")
        
        except Exception as e:
            logger.error(f"Fehler beim Speichern: {e}")
    
    def zeige_statistik(self):
        """Zeigt Verarbeitungs-Statistik."""
        print("\n" + "=" * 50)
        print("VERARBEITUNGS-STATISTIK")
        print("=" * 50)
        print(f"Gesamt: {self.gesamt}")
        print(f"Erfolge: {self.erfolge}")
        print(f"Fehler: {self.fehler}")
        
        if self.gesamt > 0:
            erfolgsrate = (self.erfolge / self.gesamt) * 100
            print(f"Erfolgsrate: {erfolgsrate:.1f}%")
        
        print("=" * 50)


def main():
    """Hauptfunktion."""
    logger.info("=" * 50)
    logger.info("STARTE ROBUSTE DATEI-VERARBEITUNG")
    logger.info("=" * 50)
    
    verarbeiter = DateiVerarbeiter()
    
    # Liste von Dateien (einige existieren nicht)
    dateien = [
        "daten1.csv",
        "daten2.csv",
        "nicht_vorhanden.csv",
        "daten3.csv"
    ]
    
    alle_daten = []
    
    # Verarbeite alle Dateien
    for datei in dateien:
        daten = verarbeiter.verarbeite_csv(datei)
        if daten:
            alle_daten.extend(daten)
    
    # Bereinige kombinierte Daten
    if alle_daten:
        bereinigte_daten = verarbeiter.bereinige_daten(alle_daten)
        verarbeiter.speichere_ergebnis(bereinigte_daten, "output/ergebnis.csv")
    
    # Statistik
    verarbeiter.zeige_statistik()
    
    logger.info("VERARBEITUNG ABGESCHLOSSEN")
    logger.info(f"Log-Datei: verarbeitung.log")


if __name__ == "__main__":
    main()
