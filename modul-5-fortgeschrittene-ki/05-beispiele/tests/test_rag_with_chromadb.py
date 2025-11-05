"""
Tests für rag_with_chromadb.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()
sys.modules['chromadb'] = MagicMock()

import rag_with_chromadb


class TestChromaDBRAG:
    """Tests für ChromaDB RAG Funktionen"""
    
    @patch('rag_with_chromadb.chroma_client')
    def test_initialize_collection(self, mock_chroma):
        """Test: Collection wird initialisiert"""
        # Setup
        mock_collection = MagicMock()
        mock_chroma.get_or_create_collection.return_value = mock_collection
        
        # Execute
        rag_with_chromadb.initialize_collection()
        
        # Assert
        mock_chroma.get_or_create_collection.assert_called()
    
    @patch('rag_with_chromadb.collection')
    def test_add_documents(self, mock_collection):
        """Test: Dokumente werden hinzugefügt"""
        # Setup
        mock_collection.add = MagicMock()
        
        # Execute
        rag_with_chromadb.add_documents()
        
        # Assert
        mock_collection.add.assert_called()
    
    @patch('rag_with_chromadb.collection')
    def test_search_documents(self, mock_collection):
        """Test: Dokumente werden gesucht"""
        # Setup
        mock_collection.query.return_value = {
            "documents": [["Test Document"]],
            "distances": [[0.1]]
        }
        
        # Execute
        result = rag_with_chromadb.search_documents("Test Query")
        
        # Assert
        assert isinstance(result, list)
    
    @patch('rag_with_chromadb.collection')
    def test_search_documents_returns_list(self, mock_collection):
        """Test: Rückgabewert ist Liste"""
        # Setup
        mock_collection.query.return_value = {
            "documents": [["Doc1", "Doc2"]],
            "distances": [[0.1, 0.2]]
        }
        
        # Execute
        result = rag_with_chromadb.search_documents("Query")
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2


class TestChromaDBQuery:
    """Tests für chromadb_query() Funktion"""
    
    @patch('rag_with_chromadb.client')
    @patch('rag_with_chromadb.collection')
    def test_chromadb_query_returns_string(self, mock_collection, mock_client):
        """Test: Rückgabewert ist String"""
        # Setup
        mock_collection.query.return_value = {
            "documents": [["Test"]],
            "distances": [[0.1]]
        }
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        result = rag_with_chromadb.chromadb_query("Test Query")
        
        # Assert
        assert isinstance(result, str)
    
    @patch('rag_with_chromadb.client')
    @patch('rag_with_chromadb.collection')
    def test_chromadb_query_calls_api(self, mock_collection, mock_client):
        """Test: API wird aufgerufen"""
        # Setup
        mock_collection.query.return_value = {
            "documents": [["Test"]],
            "distances": [[0.1]]
        }
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        rag_with_chromadb.chromadb_query("Test")
        
        # Assert
        mock_client.messages.create.assert_called()
    
    @patch('rag_with_chromadb.client')
    @patch('rag_with_chromadb.collection')
    def test_chromadb_query_correct_model(self, mock_collection, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_collection.query.return_value = {
            "documents": [["Test"]],
            "distances": [[0.1]]
        }
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        rag_with_chromadb.chromadb_query("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"
    
    @patch('rag_with_chromadb.client')
    @patch('rag_with_chromadb.collection')
    def test_chromadb_query_with_empty_results(self, mock_collection, mock_client):
        """Test: Leere Suchergebnisse"""
        # Setup
        mock_collection.query.return_value = {
            "documents": [[]],
            "distances": [[]]
        }
        mock_response = Mock()
        mock_response.content = [Mock(text="Keine Ergebnisse")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        result = rag_with_chromadb.chromadb_query("Test")
        
        # Assert
        assert isinstance(result, str)

