# Beispiel: Vollständiges README

**Für:** Modul 4 - Agentic Coding  
**Zweck:** Zeigt ein professionelles README-Beispiel

---

# 📊 Data Pipeline - CSV zu Insights

Eine Python-Anwendung, die CSV-Daten lädt, bereinigt, analysiert und visualisiert.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)

## 🎯 Features

- ✅ CSV-Dateien laden und validieren
- ✅ Daten automatisch bereinigen (Duplikate, fehlende Werte)
- ✅ Statistische Analysen durchführen
- ✅ Interaktive Visualisierungen erstellen
- ✅ Ergebnisse in verschiedene Formate exportieren
- ✅ Umfassende Fehlerbehandlung
- ✅ Logging für Debugging

## 📋 Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [API](#api)
- [Beispiele](#beispiele)
- [Tests](#tests)
- [Beitragen](#beitragen)
- [Lizenz](#lizenz)

## 🚀 Installation

### Voraussetzungen

- Python 3.11 oder höher
- uv

### Schritt-für-Schritt

1. **Repository klonen**
   ```bash
   git clone https://github.com/user/data-pipeline.git
   cd data-pipeline
   ```

2. **Abhängigkeiten installieren**
   ```bash
   uv sync
   ```

3. **Umgebungsvariablen konfigurieren** (optional)
   ```bash
   cp .env.example .env
   # Bearbeite .env nach Bedarf
   ```

4. **Installation überprüfen**
   ```bash
   python -m pytest tests/
   ```

## 💻 Verwendung

### Basis-Beispiel

```python
from data_pipeline import Pipeline

# Pipeline erstellen
pipeline = Pipeline()

# Daten laden
data = pipeline.load_csv('data.csv')

# Daten bereinigen
cleaned = pipeline.clean_data(data)

# Analyse durchführen
stats = pipeline.analyze(cleaned)

# Visualisieren
pipeline.visualize(cleaned, output='report.html')

print(stats)
```

### Kommandozeile

```bash
# Datei verarbeiten
python -m data_pipeline process data.csv --output results.csv

# Bericht generieren
python -m data_pipeline report data.csv --format html

# Hilfe anzeigen
python -m data_pipeline --help
```

## 📚 API

### Pipeline Klasse

```python
class Pipeline:
    """Hauptklasse für Datenverarbeitung"""
    
    def load_csv(self, filepath: str) -> pd.DataFrame:
        """Lade CSV-Datei"""
        
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Bereinige Daten"""
        
    def analyze(self, df: pd.DataFrame) -> dict:
        """Führe Analysen durch"""
        
    def visualize(self, df: pd.DataFrame, output: str) -> None:
        """Erstelle Visualisierungen"""
```

## 🔍 Beispiele

### Beispiel 1: Verkaufsdaten analysieren

```python
from data_pipeline import Pipeline

pipeline = Pipeline()

# Daten laden
sales = pipeline.load_csv('sales.csv')

# Bereinigen
sales_clean = pipeline.clean_data(sales)

# Analysieren
stats = pipeline.analyze(sales_clean)

print(f"Durchschnittlicher Umsatz: ${stats['mean_revenue']:.2f}")
print(f"Top Produkt: {stats['top_product']}")
```

### Beispiel 2: Bericht generieren

```python
from data_pipeline import Pipeline

pipeline = Pipeline()
data = pipeline.load_csv('data.csv')
cleaned = pipeline.clean_data(data)

# HTML-Bericht mit Visualisierungen
pipeline.visualize(cleaned, output='report.html')
```

## ✅ Tests

### Tests ausführen

```bash
# Alle Tests
pytest

# Mit Coverage
pytest --cov=src tests/

# Spezifische Test-Datei
pytest tests/test_pipeline.py

# Verbose Output
pytest -v
```

### Test-Struktur

```
tests/
├── test_pipeline.py
├── test_data_cleaning.py
├── test_analysis.py
└── fixtures/
    └── sample_data.csv
```

## 📊 Beispiel-Output

### Eingabe (data.csv)
```
name,age,salary,department
Alice,30,50000,Engineering
Bob,25,45000,Sales
Charlie,35,60000,Engineering
```

### Ausgabe (stats)
```json
{
  "total_records": 3,
  "average_salary": 51666.67,
  "by_department": {
    "Engineering": 55000,
    "Sales": 45000
  },
  "age_range": [25, 35]
}
```

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'pandas'"

**Lösung:**
```bash
uv sync
```

### Problem: "FileNotFoundError: data.csv"

**Lösung:**
```bash
# Prüfe ob Datei existiert
ls -la data.csv

# Nutze absoluten Pfad
pipeline.load_csv('/absolute/path/to/data.csv')
```

### Problem: "Encoding Error"

**Lösung:**
```python
# Spezifiziere Encoding
data = pipeline.load_csv('data.csv', encoding='utf-8')
```

## 🤝 Beitragen

Wir freuen uns über Beiträge! Bitte:

1. Fork das Projekt
2. Feature-Branch erstellen (`git checkout -b feature/amazing`)
3. Änderungen committen (`git commit -m 'Add amazing feature'`)
4. Tests schreiben
5. Push (`git push origin feature/amazing`)
6. Pull Request öffnen

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Details.

## 📝 Changelog

Siehe [CHANGELOG.md](CHANGELOG.md) für Versionshistorie.

## 📄 Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei.

## 👤 Autor

**Daniel Senften**
- GitHub: [@dsenften](https://github.com/dsenften)
- Email: daniel@example.com

## 🙏 Danksagungen

- pandas Team für grossartige Dokumentation
- matplotlib für Visualisierungen
- pytest für Testing-Framework

## 📞 Support

- 📧 Email: support@example.com
- 💬 Issues: [GitHub Issues](https://github.com/user/data-pipeline/issues)
- 📖 Dokumentation: [docs/](./docs/)

---

**Zuletzt aktualisiert:** 2025-11-05  
**Version:** 1.0.0

