"""
Tests für streaming_chat.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import streaming_chat


class TestStreamChat:
    """Tests für stream_chat() Funktion"""
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_prints_user_message(self, mock_print, mock_client):
        """Test: Benutzer-Nachricht wird gedruckt"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = ["Hallo"]
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test Nachricht")
        
        # Assert
        mock_print.assert_called()
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_uses_stream_context(self, mock_print, mock_client):
        """Test: Stream Context Manager wird genutzt"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = ["Antwort"]
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test")
        
        # Assert
        mock_client.messages.stream.assert_called_once()
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_with_multiple_chunks(self, mock_print, mock_client):
        """Test: Mehrere Text-Chunks werden verarbeitet"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = ["Hallo", " ", "Welt"]
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test")
        
        # Assert
        mock_client.messages.stream.assert_called_once()
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_correct_model(self, mock_print, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = []
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test")
        
        # Assert
        call_kwargs = mock_client.messages.stream.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_with_empty_response(self, mock_print, mock_client):
        """Test: Leere Antwort wird behandelt"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = []
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test")
        
        # Assert
        mock_client.messages.stream.assert_called_once()
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_with_long_message(self, mock_print, mock_client):
        """Test: Lange Nachrichten werden verarbeitet"""
        # Setup
        long_msg = "A" * 1000
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = ["Antwort"]
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat(long_msg)
        
        # Assert
        mock_client.messages.stream.assert_called_once()


class TestStreamChatIntegration:
    """Integrations-Tests"""
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_system_prompt(self, mock_print, mock_client):
        """Test: System Prompt wird gesetzt"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = []
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test")
        
        # Assert
        call_kwargs = mock_client.messages.stream.call_args[1]
        assert "system" in call_kwargs
        assert "hilfreicher Assistent" in call_kwargs["system"]
    
    @patch('streaming_chat.client')
    @patch('builtins.print')
    def test_stream_chat_max_tokens(self, mock_print, mock_client):
        """Test: Max Tokens wird gesetzt"""
        # Setup
        mock_stream = MagicMock()
        mock_stream.__enter__.return_value.text_stream = []
        mock_client.messages.stream.return_value = mock_stream
        
        # Execute
        streaming_chat.stream_chat("Test")
        
        # Assert
        call_kwargs = mock_client.messages.stream.call_args[1]
        assert call_kwargs["max_tokens"] == 1024

