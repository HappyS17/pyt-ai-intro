#!/usr/bin/env python3
"""
Repariert generierte Test-Dateien

Entfernt private Funktionen und main() aus Imports.
"""

import os
import re
from pathlib import Path


def fix_test_file(filepath):
    """Repariert eine Test-Datei"""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Finde die from-import Zeile
    match = re.search(r'from (\w+) import (.+)', content)
    if not match:
        return False
    
    module_name = match.group(1)
    imports_str = match.group(2)
    
    # Parse imports
    imports = [i.strip() for i in imports_str.split(',')]
    
    # Filtere private Funktionen und main
    filtered_imports = [
        i for i in imports 
        if not i.startswith('_') and i != 'main'
    ]
    
    if len(filtered_imports) == len(imports):
        return False  # Keine Änderung nötig
    
    # Rekonstruiere import
    if filtered_imports:
        new_import = f"from {module_name} import {', '.join(filtered_imports)}"
    else:
        # Wenn keine Funktionen übrig, nur Module importieren
        new_import = f"# from {module_name} import ..."
    
    # Ersetze
    new_content = re.sub(
        r'from \w+ import .+',
        new_import,
        content,
        count=1
    )
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True


def main():
    """Hauptfunktion"""
    
    modules = {
        "modul-1-mindset-setup/05-beispiele": "Modul 1",
        "modul-2-python-grundlagen/05-beispiele": "Modul 2",
        "modul-3-datenverarbeitung-dateien/05-beispiele": "Modul 3",
        "modul-4-agentic-coding/05-beispiele": "Modul 4",
    }
    
    print("=" * 80)
    print("🔧 TEST-REPARATUR")
    print("=" * 80)
    print()
    
    fixed_count = 0
    
    for module_path, module_name in modules.items():
        if not os.path.exists(module_path):
            continue
        
        tests_dir = os.path.join(module_path, "tests")
        if not os.path.exists(tests_dir):
            continue
        
        print(f"📦 {module_name}")
        
        for test_file in os.listdir(tests_dir):
            if not test_file.startswith("test_") or not test_file.endswith(".py"):
                continue
            
            test_filepath = os.path.join(tests_dir, test_file)
            
            if fix_test_file(test_filepath):
                print(f"  ✅ {test_file}")
                fixed_count += 1
            else:
                print(f"  ⏭️  {test_file}")
        
        print()
    
    print("=" * 80)
    print(f"✅ {fixed_count} Test-Dateien repariert!")
    print("=" * 80)


if __name__ == "__main__":
    main()

