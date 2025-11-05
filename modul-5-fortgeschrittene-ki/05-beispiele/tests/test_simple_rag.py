"""
Tests für simple_rag.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import simple_rag


class TestSimpleSearch:
    """Tests für simple_search() Funktion"""
    
    def test_simple_search_returns_list(self):
        """Test: Rückgabewert ist Liste"""
        result = simple_rag.simple_search("Python")
        assert isinstance(result, list)
    
    def test_simple_search_respects_top_k(self):
        """Test: Top-K wird respektiert"""
        result = simple_rag.simple_search("Python", top_k=1)
        assert len(result) <= 1
    
    def test_simple_search_finds_relevant_docs(self):
        """Test: Relevante Dokumente werden gefunden"""
        result = simple_rag.simple_search("Python")
        assert len(result) > 0
    
    def test_simple_search_with_multiple_words(self):
        """Test: Suche mit mehreren Wörtern"""
        result = simple_rag.simple_search("Python Programmiersprache")
        assert len(result) > 0
    
    def test_simple_search_case_insensitive(self):
        """Test: Suche ist case-insensitive"""
        result1 = simple_rag.simple_search("python")
        result2 = simple_rag.simple_search("PYTHON")
        assert len(result1) == len(result2)
    
    def test_simple_search_empty_query(self):
        """Test: Leere Abfrage"""
        result = simple_rag.simple_search("")
        assert isinstance(result, list)


class TestDocuments:
    """Tests für Dokumente"""
    
    def test_documents_exist(self):
        """Test: Dokumente existieren"""
        assert hasattr(simple_rag, 'documents')
        assert len(simple_rag.documents) > 0
    
    def test_documents_have_required_fields(self):
        """Test: Dokumente haben erforderliche Felder"""
        for doc in simple_rag.documents:
            assert "id" in doc
            assert "title" in doc
            assert "content" in doc
    
    def test_documents_count(self):
        """Test: Richtige Anzahl von Dokumenten"""
        assert len(simple_rag.documents) == 3


class TestRagQuery:
    """Tests für rag_query() Funktion"""
    
    @patch('simple_rag.client')
    def test_rag_query_returns_string(self, mock_client):
        """Test: Rückgabewert ist String"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        result = simple_rag.rag_query("Was ist Python?")
        
        # Assert
        assert isinstance(result, string)
    
    @patch('simple_rag.client')
    def test_rag_query_calls_api(self, mock_client):
        """Test: API wird aufgerufen"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        simple_rag.rag_query("Test")
        
        # Assert
        mock_client.messages.create.assert_called_once()
    
    @patch('simple_rag.client')
    def test_rag_query_includes_context(self, mock_client):
        """Test: Kontext wird in Prompt eingebunden"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        simple_rag.rag_query("Was ist Python?")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        system_prompt = call_kwargs["system"]
        assert "Dokument" in system_prompt
    
    @patch('simple_rag.client')
    def test_rag_query_with_empty_query(self, mock_client):
        """Test: Leere Abfrage"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        result = simple_rag.rag_query("")
        
        # Assert
        assert isinstance(result, str)
    
    @patch('simple_rag.client')
    def test_rag_query_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        simple_rag.rag_query("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"


# Hilfsvariable für String-Typ
try:
    string = str
except:
    string = basestring

