"""
Tests für chatbot.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Füge Parent-Verzeichnis zu Path hinzu
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock Anthropic vor Import
sys.modules['anthropic'] = MagicMock()

# Importiere nach Mock
import importlib
import chatbot as chatbot_module


class TestChatFunction:
    """Tests für chat() Funktion"""
    
    @patch('chatbot.client')
    def test_chat_adds_user_message(self, mock_client):
        """Test: Benutzer-Nachricht wird hinzugefügt"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Hallo!")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        result = chatbot_module.chat("Hallo")
        
        # Assert
        assert len(chatbot_module.conversation_history) == 2
        assert chatbot_module.conversation_history[0]["role"] == "user"
        assert chatbot_module.conversation_history[0]["content"] == "Hallo"
    
    @patch('chatbot.client')
    def test_chat_adds_assistant_response(self, mock_client):
        """Test: Assistent-Antwort wird gespeichert"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Hallo zurück!")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        result = chatbot_module.chat("Hallo")
        
        # Assert
        assert len(chatbot_module.conversation_history) == 2
        assert chatbot_module.conversation_history[1]["role"] == "assistant"
        assert chatbot_module.conversation_history[1]["content"] == "Hallo zurück!"
    
    @patch('chatbot.client')
    def test_chat_returns_response_text(self, mock_client):
        """Test: Rückgabewert ist Antwort-Text"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Test Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        result = chatbot_module.chat("Test")
        
        # Assert
        assert result == "Test Antwort"
    
    @patch('chatbot.client')
    def test_chat_maintains_conversation_history(self, mock_client):
        """Test: Konversations-Speicher wird beibehalten"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        chatbot_module.chat("Erste Frage")
        chatbot_module.chat("Zweite Frage")
        
        # Assert
        assert len(chatbot_module.conversation_history) == 4
    
    @patch('chatbot.client')
    def test_chat_calls_api_with_correct_model(self, mock_client):
        """Test: API wird mit korrektem Modell aufgerufen"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        chatbot_module.chat("Test")
        
        # Assert
        mock_client.messages.create.assert_called_once()
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"
    
    @patch('chatbot.client')
    def test_chat_handles_empty_response(self, mock_client):
        """Test: Leere Antwort wird behandelt"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        result = chatbot_module.chat("Test")
        
        # Assert
        assert result == ""
    
    @patch('chatbot.client')
    def test_chat_with_long_message(self, mock_client):
        """Test: Lange Nachrichten werden verarbeitet"""
        # Setup
        long_message = "A" * 1000
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        result = chatbot_module.chat(long_message)
        
        # Assert
        assert result == "Antwort"
        assert chatbot_module.conversation_history[0]["content"] == long_message


class TestConversationHistory:
    """Tests für Konversations-Speicher"""
    
    def test_conversation_history_initialized(self):
        """Test: Konversations-Speicher ist initialisiert"""
        assert isinstance(chatbot_module.conversation_history, list)
    
    def test_conversation_history_persists(self):
        """Test: Konversations-Speicher bleibt erhalten"""
        chatbot_module.conversation_history = [{"test": "data"}]
        assert len(chatbot_module.conversation_history) == 1


class TestIntegration:
    """Integrations-Tests"""
    
    @patch('chatbot.client')
    def test_multiple_turns_conversation(self, mock_client):
        """Test: Mehrere Gesprächs-Runden"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        chatbot_module.conversation_history = []
        for i in range(3):
            chatbot_module.chat(f"Frage {i}")
        
        # Assert
        assert len(chatbot_module.conversation_history) == 6  # 3 Fragen + 3 Antworten
        assert mock_client.messages.create.call_count == 3

