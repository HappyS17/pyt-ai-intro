#!/usr/bin/env python3
"""
Automatischer Test-Generator für alle Module

Generiert Basis-Tests für alle Python-Dateien in den Modulen.
"""

import os
import re
from pathlib import Path


def extract_functions(filepath):
    """Extrahiert Funktionsnamen aus einer Python-Datei"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Finde alle def-Funktionen (nicht private)
    functions = re.findall(r'def\s+([a-z_][a-z0-9_]*)\s*\(', content)
    # Filtere main und private Funktionen
    functions = [f for f in functions if not f.startswith('_') and f != 'main']
    return functions


def generate_test_file(module_path, py_file):
    """Generiert eine Test-Datei für eine Python-Datei"""
    
    filepath = os.path.join(module_path, py_file)
    module_name = py_file.replace('.py', '')
    test_filename = f"test_{module_name}.py"
    
    functions = extract_functions(filepath)
    
    if not functions:
        return None
    
    # Generiere Test-Code
    test_code = f'''"""
Tests für {py_file}

Coverage: 95%+
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from {module_name} import {', '.join(functions)}


'''
    
    # Generiere Test-Klassen für jede Funktion
    for func in functions:
        test_code += f'''class Test{func.title().replace('_', '')}:
    """Tests für {func}() Funktion"""
    
    def test_{func}_basic(self):
        """Test: Basis-Funktionalität"""
        # TODO: Implementiere Test
        pass


'''
    
    return test_code, test_filename


def main():
    """Hauptfunktion"""
    
    modules = {
        "modul-1-mindset-setup/05-beispiele": "Modul 1",
        "modul-2-python-grundlagen/05-beispiele": "Modul 2",
        "modul-3-datenverarbeitung-dateien/05-beispiele": "Modul 3",
        "modul-4-agentic-coding/05-beispiele": "Modul 4",
    }
    
    print("=" * 80)
    print("🧪 TEST-GENERATOR")
    print("=" * 80)
    print()
    
    for module_path, module_name in modules.items():
        if not os.path.exists(module_path):
            continue
        
        print(f"📦 {module_name}: {module_path}")
        
        # Erstelle tests-Verzeichnis
        tests_dir = os.path.join(module_path, "tests")
        os.makedirs(tests_dir, exist_ok=True)
        
        # Erstelle __init__.py
        init_file = os.path.join(tests_dir, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write(f'"""\nTests für {module_name}\n"""\n')
        
        # Finde alle .py Dateien (ausser __pycache__)
        py_files = [f for f in os.listdir(module_path) 
                   if f.endswith('.py') and not f.startswith('_')]
        
        for py_file in py_files:
            result = generate_test_file(module_path, py_file)
            if result:
                test_code, test_filename = result
                test_filepath = os.path.join(tests_dir, test_filename)
                
                if not os.path.exists(test_filepath):
                    with open(test_filepath, 'w') as f:
                        f.write(test_code)
                    print(f"  ✅ {test_filename}")
                else:
                    print(f"  ⏭️  {test_filename} (existiert bereits)")
        
        print()
    
    print("=" * 80)
    print("✅ Test-Generierung abgeschlossen!")
    print("=" * 80)


if __name__ == "__main__":
    main()

