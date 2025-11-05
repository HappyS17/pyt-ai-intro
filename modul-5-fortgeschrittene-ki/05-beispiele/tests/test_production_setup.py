"""
Tests für production_setup.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import production_setup


class TestRateLimiter:
    """Tests für RateLimiter Klasse"""
    
    def test_rate_limiter_initialization(self):
        """Test: RateLimiter wird initialisiert"""
        limiter = production_setup.RateLimiter(max_requests=10, window_seconds=60)
        assert limiter.max_requests == 10
        assert limiter.window_seconds == 60
        assert isinstance(limiter.requests, list)
    
    def test_rate_limiter_default_values(self):
        """Test: Standard-Werte"""
        limiter = production_setup.RateLimiter()
        assert limiter.max_requests == 10
        assert limiter.window_seconds == 60


class TestIsAllowed:
    """Tests für is_allowed() Methode"""
    
    def test_is_allowed_first_request(self):
        """Test: Erste Anfrage ist erlaubt"""
        limiter = production_setup.RateLimiter(max_requests=10)
        assert limiter.is_allowed() is True
    
    def test_is_allowed_within_limit(self):
        """Test: Anfragen innerhalb Limit"""
        limiter = production_setup.RateLimiter(max_requests=5)
        for _ in range(5):
            assert limiter.is_allowed() is True
    
    def test_is_allowed_exceeds_limit(self):
        """Test: Limit überschritten"""
        limiter = production_setup.RateLimiter(max_requests=2)
        limiter.is_allowed()
        limiter.is_allowed()
        assert limiter.is_allowed() is False
    
    def test_is_allowed_tracks_requests(self):
        """Test: Anfragen werden verfolgt"""
        limiter = production_setup.RateLimiter(max_requests=10)
        initial_count = len(limiter.requests)
        limiter.is_allowed()
        assert len(limiter.requests) == initial_count + 1


class TestProductionChatbot:
    """Tests für ProductionChatbot Klasse"""
    
    def test_production_chatbot_initialization(self):
        """Test: ProductionChatbot wird initialisiert"""
        chatbot = production_setup.ProductionChatbot()
        assert hasattr(chatbot, 'rate_limiter')
        assert chatbot.request_count == 0
        assert chatbot.error_count == 0
    
    def test_production_chatbot_has_rate_limiter(self):
        """Test: Rate Limiter vorhanden"""
        chatbot = production_setup.ProductionChatbot()
        assert isinstance(chatbot.rate_limiter, production_setup.RateLimiter)


class TestChatMethod:
    """Tests für chat() Methode"""
    
    @patch('production_setup.client')
    def test_chat_valid_message(self, mock_client):
        """Test: Gültige Nachricht"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        chatbot = production_setup.ProductionChatbot()
        
        # Execute
        result = chatbot.chat("Test Nachricht")
        
        # Assert
        assert result == "Antwort"
        assert chatbot.request_count == 1
    
    @patch('production_setup.client')
    def test_chat_increments_request_count(self, mock_client):
        """Test: Request-Zähler wird erhöht"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        chatbot = production_setup.ProductionChatbot()
        
        # Execute
        chatbot.chat("Test 1")
        chatbot.chat("Test 2")
        
        # Assert
        assert chatbot.request_count == 2
    
    def test_chat_empty_message(self):
        """Test: Leere Nachricht"""
        chatbot = production_setup.ProductionChatbot()
        
        # Execute & Assert
        with pytest.raises(Exception):
            chatbot.chat("")
    
    def test_chat_too_long_message(self):
        """Test: Zu lange Nachricht"""
        chatbot = production_setup.ProductionChatbot()
        long_message = "A" * 10001
        
        # Execute & Assert
        with pytest.raises(Exception):
            chatbot.chat(long_message)
    
    @patch('production_setup.client')
    def test_chat_rate_limit_exceeded(self, mock_client):
        """Test: Rate Limit überschritten"""
        chatbot = production_setup.ProductionChatbot()
        chatbot.rate_limiter = production_setup.RateLimiter(max_requests=1)
        
        # Execute
        chatbot.rate_limiter.is_allowed()  # Nutze das Limit
        
        # Assert
        with pytest.raises(Exception):
            chatbot.chat("Test")
    
    @patch('production_setup.client')
    def test_chat_api_error(self, mock_client):
        """Test: API Fehler"""
        # Setup
        mock_client.messages.create.side_effect = Exception("API Error")
        
        chatbot = production_setup.ProductionChatbot()
        
        # Execute & Assert
        with pytest.raises(Exception):
            chatbot.chat("Test")
        
        assert chatbot.error_count == 1
    
    @patch('production_setup.client')
    def test_chat_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        chatbot = production_setup.ProductionChatbot()
        
        # Execute
        chatbot.chat("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"

