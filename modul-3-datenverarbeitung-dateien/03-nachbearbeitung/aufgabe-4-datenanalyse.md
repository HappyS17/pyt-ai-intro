# Aufgabe 4: Datenanalyse mit pandas

**Schwierigkeit:** ⭐⭐⭐  
**Zeitaufwand:** 120 Minuten  
**Deadline:** Vor Modul 4

## 🎯 Ziel

Eine umfassende Datenanalyse durchführen: Daten laden, bereinigen, explorieren und visualisieren.

## 📋 Aufgabenstellung

Wähle einen öffentlichen Datensatz (z.B. von Kaggle, UCI ML Repository oder GitHub) und führe folgende Analysen durch:

### Phase 1: Daten laden & erkunden
- [ ] CSV/JSON laden mit pandas
- [ ] Datentypen prüfen
- [ ] Fehlende Werte identifizieren
- [ ] Grundstatistiken berechnen

### Phase 2: Daten bereinigen
- [ ] Fehlende Werte behandeln (drop/fill)
- [ ] Duplikate entfernen
- [ ] Datentypen konvertieren
- [ ] Ausreisser identifizieren

### Phase 3: Exploratory Data Analysis (EDA)
- [ ] Verteilungen analysieren
- [ ] Korrelationen berechnen
- [ ] Gruppierungen durchführen
- [ ] Trends identifizieren

### Phase 4: Visualisierung
- [ ] Histogramme erstellen
- [ ] Scatter Plots
- [ ] Box Plots für Ausreisser
- [ ] Heatmaps für Korrelationen

## 💻 Beispiel-Struktur

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Daten laden
df = pd.read_csv('data.csv')

# 2. Erkunden
print(f"Shape: {df.shape}")
print(f"Datentypen:\n{df.dtypes}")
print(f"Fehlende Werte:\n{df.isnull().sum()}")
print(f"Statistiken:\n{df.describe()}")

# 3. Bereinigen
df = df.dropna()  # oder fillna()
df = df.drop_duplicates()

# 4. Analysieren
print(f"Korrelationen:\n{df.corr()}")
print(f"Gruppierung:\n{df.groupby('category').mean()}")

# 5. Visualisieren
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

df['column1'].hist(ax=axes[0, 0])
df.plot.scatter(x='col1', y='col2', ax=axes[0, 1])
df.boxplot(ax=axes[1, 0])
sns.heatmap(df.corr(), ax=axes[1, 1])

plt.tight_layout()
plt.savefig('analysis.png')
plt.show()
```

## 📊 Anforderungen

### Datenquellen (Wähle eine)
- Kaggle Datasets
- UCI Machine Learning Repository
- GitHub Public Datasets
- Öffentliche APIs (z.B. OpenWeather, COVID-19)
- Selbst generierte Daten

### Analyse-Umfang
- [ ] Mindestens 100 Zeilen Daten
- [ ] Mindestens 5 Spalten
- [ ] Mindestens 3 verschiedene Datentypen
- [ ] Mindestens 2 Visualisierungen

### Code-Qualität
- [ ] Funktionen für wiederverwendbare Logik
- [ ] Fehlerbehandlung
- [ ] Aussagekräftige Variablennamen
- [ ] Docstrings

## 📈 Analyse-Ideen

**Anfänger:**
- Wetter-Daten: Temperatur-Trends, Niederschlag-Muster
- Verkaufs-Daten: Top-Produkte, Umsatz nach Region
- Schüler-Daten: Noten-Verteilung, Korrelation Lernzeit-Erfolg

**Fortgeschrittene:**
- Zeitreihen-Analyse mit Trends
- Multivariate Analyse mit PCA
- Anomalie-Erkennung
- Prognose-Modelle

## 🎓 Lernziele

Nach dieser Aufgabe kannst du:
- ✅ Daten mit pandas laden und erkunden
- ✅ Datenqualität beurteilen und verbessern
- ✅ Statistische Analysen durchführen
- ✅ Daten visualisieren
- ✅ Insights aus Daten ableiten

## 📁 Deliverables

1. **analysis.py** - Hauptskript mit allen Analysen
2. **data.csv** - Eingabe-Datendatei (oder Link)
3. **results.csv** - Bereinigte/transformierte Daten
4. **analysis.png** - Visualisierungen
5. **ANALYSIS_REPORT.md** - Dokumentation mit Findings

## ✅ Checkliste

- [ ] Daten erfolgreich geladen
- [ ] Fehlende Werte behandelt
- [ ] Mindestens 5 Analysen durchgeführt
- [ ] Mindestens 3 Visualisierungen erstellt
- [ ] Findings dokumentiert
- [ ] Code kommentiert
- [ ] Git-Commit erstellt

## 📚 Ressourcen

- [pandas Documentation](https://pandas.pydata.org/docs/)
- [matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [seaborn Gallery](https://seaborn.pydata.org/examples.html)
- [Kaggle Datasets](https://www.kaggle.com/datasets)

---

**Tipp:** Nutze KI-Tools um komplexe pandas-Operationen zu verstehen!

