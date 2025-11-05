# pandas Handout - Schnellreferenz

**Für:** Modul 3 - Datenverarbeitung  
**Version:** 1.0

---

## 📦 Installation & Import

```bash
# Installation mit uv
uv sync
```

```python
# Import
import pandas as pd
```

---

## 📊 DataFrames erstellen

### Aus Dictionary
```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Alter': [25, 30, 35],
    'Stadt': ['Berlin', 'München', 'Hamburg']
}
df = pd.DataFrame(data)
```

### Aus CSV
```python
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', encoding='utf-8', sep=';')
```

### Aus JSON
```python
df = pd.read_json('data.json')
```

### Aus Liste von Dictionaries
```python
data = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'}
]
df = pd.DataFrame(data)
```

---

## 🔍 Daten erkunden

```python
# Erste/letzte Zeilen
df.head()      # Erste 5 Zeilen
df.tail(10)    # Letzte 10 Zeilen

# Informationen
df.shape       # (Zeilen, Spalten)
df.info()      # Datentypen, Speicher
df.dtypes      # Datentypen pro Spalte

# Statistiken
df.describe()  # Min, Max, Mean, Std
df.describe(include='object')  # Für Text-Spalten

# Fehlende Werte
df.isnull()    # Boolean DataFrame
df.isnull().sum()  # Anzahl pro Spalte
df.dropna()    # Zeilen mit NaN entfernen
```

---

## 📝 Daten auswählen

### Spalten
```python
df['Name']           # Eine Spalte (Series)
df[['Name', 'Alter']]  # Mehrere Spalten (DataFrame)
df.Name              # Dot-Notation (nur wenn gültig)
```

### Zeilen
```python
df.loc[0]            # Nach Index
df.iloc[0]           # Nach Position
df.loc[0:2]          # Slice (inklusive Ende!)
df.iloc[0:2]         # Slice (exklusive Ende)
```

### Bedingungen
```python
df[df['Alter'] > 25]
df[(df['Alter'] > 25) & (df['Stadt'] == 'Berlin')]
df[df['Name'].str.contains('A')]  # String-Matching
```

---

## ✏️ Daten ändern

### Neue Spalte hinzufügen
```python
df['Kategorie'] = 'Standard'
df['Alter_Gruppe'] = df['Alter'].apply(lambda x: 'Jung' if x < 30 else 'Alt')
```

### Werte ändern
```python
df.loc[0, 'Name'] = 'Alicia'
df['Alter'] = df['Alter'] + 1
df['Stadt'] = df['Stadt'].str.upper()
```

### Fehlende Werte füllen
```python
df.fillna(0)           # Mit Konstante
df.fillna(method='ffill')  # Forward fill
df.fillna(df.mean())   # Mit Durchschnitt
```

### Duplikate entfernen
```python
df.drop_duplicates()
df.drop_duplicates(subset=['Name'])
```

---

## 📊 Aggregationen & Gruppierungen

```python
# Einfache Aggregationen
df['Alter'].sum()
df['Alter'].mean()
df['Alter'].max()
df['Alter'].count()

# Gruppierung
df.groupby('Stadt')['Alter'].mean()
df.groupby('Stadt').agg({
    'Alter': 'mean',
    'Name': 'count'
})

# Pivot Table
pd.pivot_table(df, values='Alter', index='Stadt', aggfunc='mean')
```

---

## 🔗 Daten kombinieren

### Concatenate
```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
pd.concat([df1, df2])  # Vertikal
pd.concat([df1, df2], axis=1)  # Horizontal
```

### Merge (SQL-ähnlich)
```python
df1 = pd.DataFrame({'key': ['a', 'b'], 'val1': [1, 2]})
df2 = pd.DataFrame({'key': ['a', 'b'], 'val2': [3, 4]})
pd.merge(df1, df2, on='key')  # Inner Join
pd.merge(df1, df2, on='key', how='left')  # Left Join
```

---

## 💾 Daten speichern

```python
# CSV
df.to_csv('output.csv', index=False, encoding='utf-8')

# JSON
df.to_json('output.json')

# Excel
df.to_excel('output.xlsx', sheet_name='Daten')

# SQL
df.to_sql('table_name', con=connection, if_exists='replace')
```

---

## 🎯 Häufige Operationen

### Sortieren
```python
df.sort_values('Alter')
df.sort_values(['Stadt', 'Alter'], ascending=[True, False])
```

### Filtern & Transformieren
```python
df[df['Alter'] > 25].sort_values('Name')
df['Alter_Kategorie'] = pd.cut(df['Alter'], bins=[0, 25, 35, 100])
```

### String-Operationen
```python
df['Name'].str.lower()
df['Name'].str.replace('a', 'A')
df['Name'].str.split(' ')
```

### Datum & Zeit
```python
df['Datum'] = pd.to_datetime(df['Datum'])
df['Jahr'] = df['Datum'].dt.year
df['Monat'] = df['Datum'].dt.month
```

---

## ⚠️ Häufige Fehler

| Fehler | Lösung |
|--------|--------|
| `KeyError: 'Spalte'` | Spalte existiert nicht - `df.columns` prüfen |
| `SettingWithCopyWarning` | `.copy()` verwenden: `df = df[...].copy()` |
| `NaN` in Berechnungen | `.fillna()` oder `.dropna()` verwenden |
| Falsche Datentypen | `.astype()` verwenden: `df['Alter'].astype(int)` |

---

## 🚀 Performance-Tipps

```python
# Schneller: Vectorized Operations
df['Alter'] * 2  # Statt: df['Alter'].apply(lambda x: x * 2)

# Speicher sparen: Datentypen optimieren
df['Kategorie'] = df['Kategorie'].astype('category')

# Grosse Dateien: Chunks lesen
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)
```

---

## 📚 Weitere Ressourcen

- [pandas Dokumentation](https://pandas.pydata.org/docs/)
- [pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Real Python pandas Tutorials](https://realpython.com/learning-paths/pandas-data-science/)

---

**Tipp:** Nutze `df.info()` und `df.describe()` um schnell einen Überblick zu bekommen!

