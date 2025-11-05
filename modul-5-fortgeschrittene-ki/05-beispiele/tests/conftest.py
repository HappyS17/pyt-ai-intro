"""
Pytest Konfiguration und Fixtures

Gemeinsame Fixtures für alle Tests.
"""

import pytest
from unittest.mock import MagicMock
import sys
import os

# Mock Anthropic vor allen Tests
sys.modules['anthropic'] = MagicMock()


@pytest.fixture
def mock_anthropic_client():
    """Mock Anthropic Client"""
    return MagicMock()


@pytest.fixture
def mock_response():
    """Mock API Response"""
    response = MagicMock()
    response.content = [MagicMock(text="Test Antwort")]
    return response


@pytest.fixture
def sample_documents():
    """Beispiel-Dokumente für Tests"""
    return [
        {
            "id": 1,
            "title": "Python Basics",
            "content": "Python ist eine Programmiersprache"
        },
        {
            "id": 2,
            "title": "Web Development",
            "content": "Flask ist ein Web-Framework"
        }
    ]


@pytest.fixture
def sample_query():
    """Beispiel-Abfrage"""
    return "Was ist Python?"


@pytest.fixture(autouse=True)
def reset_modules():
    """Setze Module vor jedem Test zurück"""
    yield
    # Cleanup nach Test
    pass

