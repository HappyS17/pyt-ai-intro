"""
Refactored Code - Nach Refactoring
Verwendung: Lektion 3 - Refactoring-Beispiel

Verbesserungen:
- Type Hints hinzugefügt
- Docstrings hinzugefügt
- Funktionen aufgeteilt
- Fehlerbehandlung implementiert
- Aussagekräftige Namen
- Code-Duplikation entfernt
- SOLID Principles angewendet
"""
from typing import List, Dict, Callable
from pathlib import Path
import re


def filter_adults(people: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Filtert Personen nach Alter >= 18.
    
    Args:
        people: Liste von Personen-Dictionaries
    
    Returns:
        Liste von erwachsenen Personen
    """
    return [person for person in people if person['age'] >= 18]


def format_person_info(person: Dict[str, any]) -> str:
    """
    Formatiert Personen-Information.
    
    Args:
        person: Dictionary mit name, age, city
    
    Returns:
        Formatierter String
    """
    name = person['name'].upper()
    city = person['city']
    return f"{name} ({city})"


def process_people(people: List[Dict[str, any]]) -> List[str]:
    """
    Verarbeitet Personen-Liste und gibt formatierte Strings zurück.
    
    Args:
        people: Liste von Personen-Dictionaries
    
    Returns:
        Liste von formatierten Strings für Erwachsene
    """
    adults = filter_adults(people)
    return [format_person_info(person) for person in adults]


class Calculator:
    """Verbesserte Calculator-Klasse mit SOLID Principles."""
    
    def __init__(self):
        """Initialisiert Calculator mit Operations-Mapping."""
        self.operations: Dict[str, Callable[[float, float], float]] = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
    
    def calculate(self, a: float, b: float, operator: str) -> float:
        """
        Führt Berechnung durch.
        
        Args:
            a: Erste Zahl
            b: Zweite Zahl
            operator: Operator (+, -, *, /)
        
        Returns:
            Ergebnis der Berechnung
        
        Raises:
            ValueError: Wenn Operator ungültig
            ZeroDivisionError: Bei Division durch Null
        """
        if operator not in self.operations:
            raise ValueError(f"Ungültiger Operator: {operator}")
        
        return self.operations[operator](a, b)
    
    def add(self, a: float, b: float) -> float:
        """Addiert zwei Zahlen."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtrahiert b von a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multipliziert zwei Zahlen."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Dividiert a durch b.
        
        Raises:
            ZeroDivisionError: Wenn b == 0
        """
        if b == 0:
            raise ZeroDivisionError("Division durch Null nicht erlaubt")
        return a / b


class FileHandler:
    """Klasse für sichere Datei-Operationen."""
    
    @staticmethod
    def read_file(filepath: str, encoding: str = 'utf-8') -> str:
        """
        Liest Datei-Inhalt.
        
        Args:
            filepath: Pfad zur Datei
            encoding: Encoding (default: utf-8)
        
        Returns:
            Datei-Inhalt als String
        
        Raises:
            FileNotFoundError: Wenn Datei nicht existiert
            IOError: Bei Lese-Fehler
        """
        path = Path(filepath)
        
        if not path.exists():
            raise FileNotFoundError(f"Datei nicht gefunden: {filepath}")
        
        try:
            with open(path, 'r', encoding=encoding) as file:
                return file.read()
        except IOError as e:
            raise IOError(f"Fehler beim Lesen: {e}")
    
    @staticmethod
    def write_file(filepath: str, content: str, encoding: str = 'utf-8') -> None:
        """
        Schreibt Inhalt in Datei.
        
        Args:
            filepath: Pfad zur Datei
            content: Zu schreibender Inhalt
            encoding: Encoding (default: utf-8)
        
        Raises:
            IOError: Bei Schreib-Fehler
        """
        path = Path(filepath)
        
        # Erstelle Verzeichnis falls nötig
        path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(path, 'w', encoding=encoding) as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Fehler beim Schreiben: {e}")


class User:
    """Repräsentiert einen Benutzer."""
    
    def __init__(self, name: str, age: int, email: str):
        """
        Initialisiert User.
        
        Args:
            name: Name des Benutzers
            age: Alter des Benutzers
            email: Email-Adresse
        
        Raises:
            ValueError: Bei ungültigen Eingaben
        """
        self._validate_inputs(name, age, email)
        self.name = name
        self.age = age
        self.email = email
    
    @staticmethod
    def _validate_inputs(name: str, age: int, email: str) -> None:
        """Validiert Eingaben."""
        if not name or not name.strip():
            raise ValueError("Name darf nicht leer sein")
        if age < 0 or age > 150:
            raise ValueError("Ungültiges Alter")
        if not User._is_valid_email(email):
            raise ValueError("Ungültige Email-Adresse")
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Prüft Email-Format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def get_info(self) -> str:
        """Gibt formatierte Benutzer-Info zurück."""
        return f"{self.name}, {self.age} Jahre, {self.email}"
    
    def is_adult(self) -> bool:
        """Prüft ob Benutzer volljährig ist."""
        return self.age >= 18
    
    def __repr__(self) -> str:
        """String-Repräsentation."""
        return f"User(name='{self.name}', age={self.age}, email='{self.email}')"


# Verwendung mit Fehlerbehandlung
if __name__ == "__main__":
    # Personen verarbeiten
    people = [
        {'name': 'Anna', 'age': 25, 'city': 'Zürich'},
        {'name': 'Bob', 'age': 17, 'city': 'Bern'},
        {'name': 'Clara', 'age': 30, 'city': 'Basel'}
    ]
    
    result = process_people(people)
    print("Erwachsene:", result)
    
    # Calculator verwenden
    calc = Calculator()
    try:
        print(f"10 + 5 = {calc.calculate(10, 5, '+')}")
        print(f"10 / 0 = {calc.calculate(10, 0, '/')}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Fehler: {e}")
    
    # Datei-Operationen
    file_handler = FileHandler()
    try:
        content = file_handler.read_file('test.txt')
        file_handler.write_file('output.txt', content)
    except (FileNotFoundError, IOError) as e:
        print(f"Datei-Fehler: {e}")
    
    # User erstellen
    try:
        user = User('Anna', 25, 'anna@test.com')
        print(user.get_info())
        print(f"Volljährig: {user.is_adult()}")
    except ValueError as e:
        print(f"User-Fehler: {e}")
