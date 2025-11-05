# Aufgabe 3: Web-Scraper mit BeautifulSoup

**Schwierigkeit:** ⭐⭐⭐  
**Zeitaufwand:** 90 Minuten  
**Deadline:** Vor Modul 4

## 🎯 Ziel

Einen funktionsfähigen Web-Scraper entwickeln, der Daten von einer Website extrahiert und in eine CSV-Datei speichert.

## 📋 Aufgabenstellung

Schreibe ein Python-Programm, das:

1. **Eine Website scrapet** (z.B. eine Produktliste, News-Artikel oder Wetterdaten)
2. **Daten extrahiert** (Titel, Beschreibung, Links, Preise, etc.)
3. **Daten bereinigt** (Whitespace entfernen, Encoding-Probleme beheben)
4. **In CSV speichert** (mit pandas oder csv-Modul)
5. **Fehlerbehandlung** implementiert (404, Timeout, Parse-Fehler)

## 🔧 Anforderungen

### Technisch
- [ ] BeautifulSoup für HTML-Parsing
- [ ] requests für HTTP-Requests
- [ ] pandas oder csv für Datenexport
- [ ] Try-except für Fehlerbehandlung
- [ ] Logging für Debugging

### Code-Qualität
- [ ] Funktionen für verschiedene Aufgaben
- [ ] Aussagekräftige Variablennamen
- [ ] Docstrings für Funktionen
- [ ] Kommentare für komplexe Logik

### Dokumentation
- [ ] README mit Anleitung
- [ ] Beispiel-Output
- [ ] Bekannte Limitationen

## 💡 Beispiel-Struktur

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def fetch_page(url):
    """Hole HTML-Inhalt einer Seite"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Fehler beim Abrufen: {e}")
        return None

def parse_data(html):
    """Parse HTML und extrahiere Daten"""
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    
    # Beispiel: Extrahiere alle Links
    for link in soup.find_all('a', limit=10):
        data.append({
            'title': link.get_text(strip=True),
            'url': link.get('href')
        })
    
    return data

def save_to_csv(data, filename):
    """Speichere Daten in CSV"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    logging.info(f"Daten gespeichert: {filename}")

# Hauptprogramm
if __name__ == "__main__":
    url = "https://example.com"
    html = fetch_page(url)
    
    if html:
        data = parse_data(html)
        save_to_csv(data, "scraped_data.csv")
```

## 🎓 Lernziele

Nach dieser Aufgabe kannst du:
- ✅ HTML-Struktur verstehen und navigieren
- ✅ BeautifulSoup effektiv nutzen
- ✅ Daten bereinigen und transformieren
- ✅ Fehler in Web-Requests behandeln
- ✅ Daten persistent speichern

## 🚀 Erweiterungen

**Wenn du Zeit hast:**
- [ ] Mehrere Seiten scrapen (Pagination)
- [ ] Daten in Datenbank speichern (SQLite)
- [ ] Scraper als CLI-Tool mit Argumenten
- [ ] Automatische Ausführung mit Scheduler (APScheduler)
- [ ] Robots.txt beachten

## ⚠️ Wichtige Hinweise

- **Rechtliche Aspekte:** Beachte robots.txt und Terms of Service
- **Rate Limiting:** Nicht zu viele Requests zu schnell
- **User-Agent:** Setze einen aussagekräftigen User-Agent
- **Caching:** Speichere HTML lokal zum Testen

## ✅ Checkliste

- [ ] Code läuft ohne Fehler
- [ ] Mindestens 10 Datensätze extrahiert
- [ ] CSV-Datei korrekt formatiert
- [ ] Fehlerbehandlung implementiert
- [ ] Code dokumentiert
- [ ] Git-Commit mit aussagekräftiger Nachricht

## 📚 Ressourcen

- [BeautifulSoup Dokumentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests Library](https://requests.readthedocs.io/)
- [pandas to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

---

**Fragen?** Schreib im Kurs-Chat oder komm zur Sprechstunde!

