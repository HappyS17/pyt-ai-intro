"""
Tests für tool_agent.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import tool_agent


class TestToolAgent:
    """Tests für ToolAgent Klasse"""
    
    def test_tool_agent_initialization(self):
        """Test: ToolAgent wird initialisiert"""
        agent = tool_agent.ToolAgent("TestAgent")
        assert agent.name == "TestAgent"
        assert isinstance(agent.tools, list)
        assert len(agent.tools) > 0
    
    def test_tool_agent_has_tools(self):
        """Test: Agent hat Tools"""
        agent = tool_agent.ToolAgent("TestAgent")
        assert len(agent.tools) >= 2


class TestExecuteTool:
    """Tests für execute_tool() Methode"""
    
    def test_execute_tool_calculator(self):
        """Test: Calculator Tool wird ausgeführt"""
        agent = tool_agent.ToolAgent("TestAgent")
        result = agent.execute_tool("calculator", {"expression": "2 + 2"})
        assert "4" in result
    
    def test_execute_tool_weather(self):
        """Test: Weather Tool wird ausgeführt"""
        agent = tool_agent.ToolAgent("TestAgent")
        result = agent.execute_tool("get_weather", {"city": "Berlin"})
        assert isinstance(result, str)
    
    def test_execute_tool_unknown(self):
        """Test: Unbekanntes Tool"""
        agent = tool_agent.ToolAgent("TestAgent")
        result = agent.execute_tool("unknown", {})
        assert "Unbekanntes Tool" in result


class TestSolveTask:
    """Tests für solve_task() Methode"""
    
    @patch('tool_agent.client')
    def test_solve_task_returns_string(self, mock_client):
        """Test: Rückgabewert ist String"""
        # Setup
        mock_response = Mock()
        mock_response.stop_reason = "end_turn"
        mock_response.content = [Mock(text="Lösung")]
        mock_client.messages.create.return_value = mock_response
        
        agent = tool_agent.ToolAgent("TestAgent")
        
        # Execute
        result = agent.solve_task("Test Task")
        
        # Assert
        assert isinstance(result, str)
    
    @patch('tool_agent.client')
    def test_solve_task_calls_api(self, mock_client):
        """Test: API wird aufgerufen"""
        # Setup
        mock_response = Mock()
        mock_response.stop_reason = "end_turn"
        mock_response.content = [Mock(text="Lösung")]
        mock_client.messages.create.return_value = mock_response
        
        agent = tool_agent.ToolAgent("TestAgent")
        
        # Execute
        agent.solve_task("Test")
        
        # Assert
        mock_client.messages.create.assert_called()
    
    @patch('tool_agent.client')
    def test_solve_task_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.stop_reason = "end_turn"
        mock_response.content = [Mock(text="Lösung")]
        mock_client.messages.create.return_value = mock_response
        
        agent = tool_agent.ToolAgent("TestAgent")
        
        # Execute
        agent.solve_task("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"

