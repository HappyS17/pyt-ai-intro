"""
Legacy Code - Vor Refactoring
Verwendung: Lektion 3 - Refactoring-Beispiel

Probleme:
- Keine Type Hints
- Keine Docstrings
- Lange Funktionen
- Keine Fehlerbehandlung
- Schlechte Variablennamen
- Code-Duplikation
"""


def process(d):
    r = []
    for i in d:
        if i['a'] > 18:
            x = i['n'].upper()
            y = i['c']
            z = f"{x} ({y})"
            r.append(z)
    return r


def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return 'Error'
        return a / b
    else:
        return 'Invalid'


def read_file(f):
    file = open(f, 'r')
    content = file.read()
    file.close()
    return content


def write_file(f, c):
    file = open(f, 'w')
    file.write(c)
    file.close()


class User:
    def __init__(self, n, a, e):
        self.n = n
        self.a = a
        self.e = e
    
    def get_info(self):
        return f"{self.n}, {self.a}, {self.e}"
    
    def is_adult(self):
        if self.a >= 18:
            return True
        else:
            return False
    
    def validate_email(self):
        if '@' in self.e and '.' in self.e:
            return True
        else:
            return False


# Verwendung
data = [
    {'n': 'anna', 'a': 25, 'c': 'Zürich'},
    {'n': 'bob', 'a': 17, 'c': 'Bern'},
    {'n': 'clara', 'a': 30, 'c': 'Basel'}
]

result = process(data)
print(result)

print(calc(10, 5, '+'))
print(calc(10, 0, '/'))

content = read_file('test.txt')
write_file('output.txt', content)

user = User('Anna', 25, 'anna@test.com')
print(user.get_info())
print(user.is_adult())
print(user.validate_email())
