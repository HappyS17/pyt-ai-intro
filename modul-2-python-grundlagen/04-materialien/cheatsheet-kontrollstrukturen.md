# Cheat Sheet: Kontrollstrukturen

Schnellreferenz für if/elif/else und Schleifen.

## if/elif/else

### Einfache Bedingung

```python
if bedingung:
    # Code wenn True
```

### if-else

```python
if bedingung:
    # Code wenn True
else:
    # Code wenn False
```

### if-elif-else

```python
if bedingung1:
    # Code wenn bedingung1 True
elif bedingung2:
    # Code wenn bedingung2 True
else:
    # Code wenn alle False
```

### Ternärer Operator

```python
wert = a if bedingung else b
```

## for-Schleifen

### Über Liste

```python
for item in liste:
    print(item)
```

### Mit range()

```python
for i in range(10):      # 0-9
    print(i)

for i in range(1, 11):   # 1-10
    print(i)

for i in range(0, 10, 2): # 0,2,4,6,8
    print(i)
```

### Mit enumerate()

```python
for index, item in enumerate(liste):
    print(f"{index}: {item}")
```

### Über Dictionary

```python
for key in dict:
    print(key)

for key, value in dict.items():
    print(f"{key}: {value}")
```

## while-Schleifen

### Grundform

```python
while bedingung:
    # Code
```

### Mit Zähler

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### Endlosschleife

```python
while True:
    if bedingung:
        break
```

## Schleifensteuerung

### break

```python
for i in range(10):
    if i == 5:
        break  # Stoppt Schleife
```

### continue

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Überspringt Rest
    print(i)
```

### pass

```python
for i in range(10):
    if i == 5:
        pass  # Macht nichts
    else:
        print(i)
```

## Häufige Patterns

### Zählen

```python
count = 0
for item in liste:
    if bedingung:
        count += 1
```

### Filtern

```python
ergebnis = []
for item in liste:
    if bedingung:
        ergebnis.append(item)
```

### Summieren

```python
total = 0
for zahl in zahlen:
    total += zahl
```

---

**Zurück zu:** [Materialien README](./README.md)
