"""
Tests für error_handling.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import error_handling


class TestRobustChatbot:
    """Tests für RobustChatbot Klasse"""
    
    def test_robust_chatbot_initialization(self):
        """Test: RobustChatbot wird initialisiert"""
        chatbot = error_handling.RobustChatbot(max_retries=3)
        assert chatbot.max_retries == 3
    
    def test_robust_chatbot_default_retries(self):
        """Test: Standard Retries"""
        chatbot = error_handling.RobustChatbot()
        assert chatbot.max_retries == 3


class TestChatWithRetry:
    """Tests für chat_with_retry() Methode"""
    
    @patch('error_handling.client')
    def test_chat_with_retry_success(self, mock_client):
        """Test: Erfolgreicher Chat"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        chatbot = error_handling.RobustChatbot()
        
        # Execute
        result = chatbot.chat_with_retry("Test")
        
        # Assert
        assert result == "Antwort"
    
    @patch('error_handling.client')
    def test_chat_with_retry_invalid_input(self, mock_client):
        """Test: Ungültige Eingabe"""
        chatbot = error_handling.RobustChatbot()
        
        # Execute & Assert
        with pytest.raises(ValueError):
            chatbot.chat_with_retry("")
    
    @patch('error_handling.client')
    def test_chat_with_retry_too_long_input(self, mock_client):
        """Test: Zu lange Eingabe"""
        chatbot = error_handling.RobustChatbot()
        long_message = "A" * 10001
        
        # Execute & Assert
        with pytest.raises(ValueError):
            chatbot.chat_with_retry(long_message)
    
    @patch('error_handling.client')
    def test_chat_with_retry_rate_limit_error(self, mock_client):
        """Test: Rate Limit Fehler mit Retry"""
        # Setup
        from anthropic import RateLimitError
        mock_client.messages.create.side_effect = RateLimitError("Rate limit")
        
        chatbot = error_handling.RobustChatbot(max_retries=1)
        
        # Execute & Assert
        with pytest.raises(RateLimitError):
            chatbot.chat_with_retry("Test")
    
    @patch('error_handling.client')
    def test_chat_with_retry_api_error(self, mock_client):
        """Test: API Fehler"""
        # Setup
        from anthropic import APIError
        mock_client.messages.create.side_effect = APIError("API Error")
        
        chatbot = error_handling.RobustChatbot(max_retries=1)
        
        # Execute & Assert
        with pytest.raises(APIError):
            chatbot.chat_with_retry("Test")
    
    @patch('error_handling.client')
    def test_chat_with_retry_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        chatbot = error_handling.RobustChatbot()
        
        # Execute
        chatbot.chat_with_retry("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"


class TestChatWithFallback:
    """Tests für chat_with_fallback() Methode"""
    
    @patch('error_handling.client')
    def test_chat_with_fallback_success(self, mock_client):
        """Test: Erfolgreicher Chat mit Fallback"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        chatbot = error_handling.RobustChatbot()
        
        # Execute
        result = chatbot.chat_with_fallback("Test")
        
        # Assert
        assert result == "Antwort"
    
    @patch('error_handling.client')
    def test_chat_with_fallback_error_fallback(self, mock_client):
        """Test: Fallback bei Fehler"""
        # Setup
        mock_client.messages.create.side_effect = Exception("Error")
        
        chatbot = error_handling.RobustChatbot(max_retries=1)
        
        # Execute
        result = chatbot.chat_with_fallback("Hallo")
        
        # Assert
        assert "Hallo" in result or "nicht verfügbar" in result
    
    @patch('error_handling.client')
    def test_chat_with_fallback_how_question(self, mock_client):
        """Test: Fallback für 'Wie' Fragen"""
        # Setup
        mock_client.messages.create.side_effect = Exception("Error")
        
        chatbot = error_handling.RobustChatbot(max_retries=1)
        
        # Execute
        result = chatbot.chat_with_fallback("Wie geht es dir?")
        
        # Assert
        assert "Fehler" in result or "nicht verfügbar" in result
    
    @patch('error_handling.client')
    def test_chat_with_fallback_generic_error(self, mock_client):
        """Test: Generischer Fehler Fallback"""
        # Setup
        mock_client.messages.create.side_effect = Exception("Error")
        
        chatbot = error_handling.RobustChatbot(max_retries=1)
        
        # Execute
        result = chatbot.chat_with_fallback("Unbekannte Frage")
        
        # Assert
        assert "Fehler" in result or "später" in result

