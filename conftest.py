"""
Zentrale Pytest Konfiguration für alle Module

Enthält gemeinsame Fixtures und Konfiguration.
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import MagicMock, patch


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def temp_file(tmp_path):
    """Erstellt eine temporäre Datei"""
    return tmp_path / "test_file.txt"


@pytest.fixture
def temp_csv(tmp_path):
    """Erstellt eine temporäre CSV-Datei"""
    csv_file = tmp_path / "test_data.csv"
    csv_file.write_text("Name,Alter,Stadt\nAnna,25,Zürich\nBob,30,Bern\n")
    return csv_file


@pytest.fixture
def temp_json(tmp_path):
    """Erstellt eine temporäre JSON-Datei"""
    import json
    json_file = tmp_path / "test_data.json"
    data = {"name": "Test", "value": 42}
    json_file.write_text(json.dumps(data))
    return json_file


@pytest.fixture
def mock_input(monkeypatch):
    """Mock für input() Funktion"""
    def _mock_input(prompt=""):
        return "test_input"
    
    monkeypatch.setattr("builtins.input", _mock_input)
    return _mock_input


@pytest.fixture
def mock_print(monkeypatch):
    """Mock für print() Funktion"""
    printed = []
    
    def _mock_print(*args, **kwargs):
        printed.append(args)
    
    monkeypatch.setattr("builtins.print", _mock_print)
    return printed


@pytest.fixture
def mock_requests():
    """Mock für requests Bibliothek"""
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "ok"}
        mock_get.return_value = mock_response
        yield mock_get


@pytest.fixture
def mock_file_operations(monkeypatch):
    """Mock für Datei-Operationen"""
    files = {}
    
    def mock_open(filename, mode='r', *args, **kwargs):
        class MockFile:
            def __enter__(self):
                return self
            
            def __exit__(self, *args):
                pass
            
            def read(self):
                return files.get(filename, "")
            
            def write(self, content):
                files[filename] = content
            
            def __iter__(self):
                return iter(files.get(filename, "").split('\n'))
        
        return MockFile()
    
    monkeypatch.setattr("builtins.open", mock_open)
    return files


# ============================================================================
# HOOKS
# ============================================================================

def pytest_configure(config):
    """Pytest Konfiguration"""
    config.addinivalue_line(
        "markers", "unit: Unit Tests"
    )
    config.addinivalue_line(
        "markers", "integration: Integration Tests"
    )
    config.addinivalue_line(
        "markers", "slow: Langsame Tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modifiziert Test-Items"""
    for item in items:
        # Markiere Tests automatisch
        if "test_" in item.nodeid:
            item.add_marker(pytest.mark.unit)


# ============================================================================
# HELPER FUNKTIONEN
# ============================================================================

@pytest.fixture
def assert_output(capsys):
    """Helper für Output-Assertions"""
    def _assert_output(expected_text):
        captured = capsys.readouterr()
        assert expected_text in captured.out
    
    return _assert_output


@pytest.fixture
def assert_error(capsys):
    """Helper für Error-Output-Assertions"""
    def _assert_error(expected_text):
        captured = capsys.readouterr()
        assert expected_text in captured.err or expected_text in captured.out
    
    return _assert_error

