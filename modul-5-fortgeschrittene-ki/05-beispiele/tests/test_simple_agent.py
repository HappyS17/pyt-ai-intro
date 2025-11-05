"""
Tests für simple_agent.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import simple_agent


class TestSimpleAgent:
    """Tests für SimpleAgent Klasse"""
    
    def test_simple_agent_initialization(self):
        """Test: SimpleAgent wird initialisiert"""
        agent = simple_agent.SimpleAgent("TestAgent")
        assert agent.name == "TestAgent"
        assert isinstance(agent.memory, list)
    
    def test_simple_agent_memory_empty(self):
        """Test: Memory ist leer"""
        agent = simple_agent.SimpleAgent("TestAgent")
        assert len(agent.memory) == 0


class TestThinkMethod:
    """Tests für think() Methode"""
    
    @patch('simple_agent.client')
    def test_think_returns_string(self, mock_client):
        """Test: Rückgabewert ist String"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Analyse")]
        mock_client.messages.create.return_value = mock_response
        
        agent = simple_agent.SimpleAgent("TestAgent")
        
        # Execute
        result = agent.think("Test Situation")
        
        # Assert
        assert isinstance(result, str)
        assert result == "Analyse"
    
    @patch('simple_agent.client')
    def test_think_adds_to_memory(self, mock_client):
        """Test: Gedanke wird zum Memory hinzugefügt"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Analyse")]
        mock_client.messages.create.return_value = mock_response
        
        agent = simple_agent.SimpleAgent("TestAgent")
        
        # Execute
        agent.think("Test")
        
        # Assert
        assert len(agent.memory) == 1
        assert agent.memory[0]["type"] == "thought"
    
    @patch('simple_agent.client')
    def test_think_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Analyse")]
        mock_client.messages.create.return_value = mock_response
        
        agent = simple_agent.SimpleAgent("TestAgent")
        
        # Execute
        agent.think("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"


class TestActMethod:
    """Tests für act() Methode"""
    
    def test_act_returns_string(self):
        """Test: Rückgabewert ist String"""
        agent = simple_agent.SimpleAgent("TestAgent")
        result = agent.act("Test Action")
        assert isinstance(result, str)
    
    def test_act_adds_to_memory(self):
        """Test: Aktion wird zum Memory hinzugefügt"""
        agent = simple_agent.SimpleAgent("TestAgent")
        agent.act("Test Action")
        
        assert len(agent.memory) == 1
        assert agent.memory[0]["type"] == "action"
    
    def test_act_includes_agent_name(self):
        """Test: Agent-Name ist in Aktion enthalten"""
        agent = simple_agent.SimpleAgent("TestAgent")
        result = agent.act("Test")
        
        assert "TestAgent" in result


class TestRunMethod:
    """Tests für run() Methode"""
    
    @patch('simple_agent.client')
    @patch('builtins.print')
    def test_run_executes_task(self, mock_print, mock_client):
        """Test: Task wird ausgeführt"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Analyse")]
        mock_client.messages.create.return_value = mock_response
        
        agent = simple_agent.SimpleAgent("TestAgent")
        
        # Execute
        agent.run("Test Task")
        
        # Assert
        assert len(agent.memory) >= 2  # Mindestens Gedanke und Aktion
    
    @patch('simple_agent.client')
    @patch('builtins.print')
    def test_run_calls_think_and_act(self, mock_print, mock_client):
        """Test: think() und act() werden aufgerufen"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Analyse")]
        mock_client.messages.create.return_value = mock_response
        
        agent = simple_agent.SimpleAgent("TestAgent")
        
        # Execute
        agent.run("Test Task")
        
        # Assert
        mock_client.messages.create.assert_called()

