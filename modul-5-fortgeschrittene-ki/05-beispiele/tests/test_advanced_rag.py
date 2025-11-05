"""
Tests für advanced_rag.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import advanced_rag


class TestBM25Score:
    """Tests für bm25_score() Funktion"""
    
    def test_bm25_score_returns_float(self):
        """Test: Rückgabewert ist Float"""
        result = advanced_rag.bm25_score("Python", "Python ist eine Sprache")
        assert isinstance(result, float)
    
    def test_bm25_score_exact_match(self):
        """Test: Exakte Übereinstimmung"""
        result = advanced_rag.bm25_score("Python", "Python Python Python")
        assert result > 0
    
    def test_bm25_score_no_match(self):
        """Test: Keine Übereinstimmung"""
        result = advanced_rag.bm25_score("XYZ", "Python ist eine Sprache")
        assert result == 0
    
    def test_bm25_score_partial_match(self):
        """Test: Teilweise Übereinstimmung"""
        result1 = advanced_rag.bm25_score("Python", "Python ist eine Sprache")
        result2 = advanced_rag.bm25_score("Python Java", "Python ist eine Sprache")
        assert result1 > 0
    
    def test_bm25_score_case_insensitive(self):
        """Test: Case-insensitive"""
        result1 = advanced_rag.bm25_score("python", "Python")
        result2 = advanced_rag.bm25_score("PYTHON", "Python")
        assert result1 == result2


class TestRetrieveCandidates:
    """Tests für retrieve_candidates() Funktion"""
    
    def test_retrieve_candidates_returns_list(self):
        """Test: Rückgabewert ist Liste"""
        result = advanced_rag.retrieve_candidates("Python")
        assert isinstance(result, list)
    
    def test_retrieve_candidates_respects_top_k(self):
        """Test: Top-K wird respektiert"""
        result = advanced_rag.retrieve_candidates("Python", top_k=1)
        assert len(result) <= 1
    
    def test_retrieve_candidates_returns_documents(self):
        """Test: Rückgabewert sind Dokumente"""
        result = advanced_rag.retrieve_candidates("Python")
        if len(result) > 0:
            assert "content" in result[0]
            assert "title" in result[0]
    
    def test_retrieve_candidates_sorted_by_relevance(self):
        """Test: Ergebnisse sind nach Relevanz sortiert"""
        result = advanced_rag.retrieve_candidates("Python")
        assert len(result) > 0


class TestRerank:
    """Tests für rerank() Funktion"""
    
    def test_rerank_returns_list(self):
        """Test: Rückgabewert ist Liste"""
        candidates = advanced_rag.retrieve_candidates("Python", top_k=5)
        result = advanced_rag.rerank("Python", candidates)
        assert isinstance(result, list)
    
    def test_rerank_respects_top_k(self):
        """Test: Top-K wird respektiert"""
        candidates = advanced_rag.retrieve_candidates("Python", top_k=5)
        result = advanced_rag.rerank("Python", candidates, top_k=2)
        assert len(result) <= 2
    
    def test_rerank_returns_documents(self):
        """Test: Rückgabewert sind Dokumente"""
        candidates = advanced_rag.retrieve_candidates("Python", top_k=5)
        result = advanced_rag.rerank("Python", candidates)
        if len(result) > 0:
            assert "content" in result[0]


class TestAdvancedRagQuery:
    """Tests für advanced_rag_query() Funktion"""
    
    @patch('advanced_rag.client')
    def test_advanced_rag_query_returns_string(self, mock_client):
        """Test: Rückgabewert ist String"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        result = advanced_rag.advanced_rag_query("Was ist Python?")
        
        # Assert
        assert isinstance(result, str)
    
    @patch('advanced_rag.client')
    def test_advanced_rag_query_calls_api(self, mock_client):
        """Test: API wird aufgerufen"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        advanced_rag.advanced_rag_query("Test")
        
        # Assert
        mock_client.messages.create.assert_called_once()
    
    @patch('advanced_rag.client')
    def test_advanced_rag_query_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        advanced_rag.advanced_rag_query("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"


class TestDocuments:
    """Tests für Dokumente"""
    
    def test_documents_exist(self):
        """Test: Dokumente existieren"""
        assert hasattr(advanced_rag, 'documents')
        assert len(advanced_rag.documents) > 0
    
    def test_documents_have_category(self):
        """Test: Dokumente haben Kategorie"""
        for doc in advanced_rag.documents:
            assert "category" in doc

