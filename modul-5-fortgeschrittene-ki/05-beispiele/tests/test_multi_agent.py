"""
Tests für multi_agent.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import multi_agent


class TestAgent:
    """Tests für Agent Klasse"""
    
    def test_agent_initialization(self):
        """Test: Agent wird initialisiert"""
        agent = multi_agent.Agent("TestAgent", "Analyst")
        assert agent.name == "TestAgent"
        assert agent.role == "Analyst"
    
    def test_agent_has_role(self):
        """Test: Agent hat Rolle"""
        agent = multi_agent.Agent("TestAgent", "Developer")
        assert agent.role == "Developer"


class TestMultiAgentSystem:
    """Tests für MultiAgentSystem Klasse"""
    
    def test_multi_agent_system_initialization(self):
        """Test: MultiAgentSystem wird initialisiert"""
        system = multi_agent.MultiAgentSystem()
        assert isinstance(system.agents, list)
        assert len(system.agents) == 0
        assert system.shared_context == ""
    
    def test_multi_agent_system_empty_agents(self):
        """Test: Keine Agents initial"""
        system = multi_agent.MultiAgentSystem()
        assert len(system.agents) == 0


class TestAddAgent:
    """Tests für add_agent() Methode"""
    
    def test_add_agent_single(self):
        """Test: Ein Agent wird hinzugefügt"""
        system = multi_agent.MultiAgentSystem()
        agent = multi_agent.Agent("Agent1", "Analyst")
        system.add_agent(agent)
        
        assert len(system.agents) == 1
        assert system.agents[0].name == "Agent1"
    
    def test_add_agent_multiple(self):
        """Test: Mehrere Agents werden hinzugefügt"""
        system = multi_agent.MultiAgentSystem()
        agent1 = multi_agent.Agent("Agent1", "Analyst")
        agent2 = multi_agent.Agent("Agent2", "Developer")
        
        system.add_agent(agent1)
        system.add_agent(agent2)
        
        assert len(system.agents) == 2
    
    def test_add_agent_preserves_order(self):
        """Test: Reihenfolge wird beibehalten"""
        system = multi_agent.MultiAgentSystem()
        agent1 = multi_agent.Agent("Agent1", "Analyst")
        agent2 = multi_agent.Agent("Agent2", "Developer")
        
        system.add_agent(agent1)
        system.add_agent(agent2)
        
        assert system.agents[0].name == "Agent1"
        assert system.agents[1].name == "Agent2"


class TestUpdateContext:
    """Tests für update_context() Methode"""
    
    def test_update_context_sets_context(self):
        """Test: Context wird gesetzt"""
        system = multi_agent.MultiAgentSystem()
        system.update_context("Test Context")
        
        assert system.shared_context == "Test Context"
    
    def test_update_context_overwrites(self):
        """Test: Context wird überschrieben"""
        system = multi_agent.MultiAgentSystem()
        system.update_context("Context 1")
        system.update_context("Context 2")
        
        assert system.shared_context == "Context 2"
    
    def test_update_context_empty_string(self):
        """Test: Leerer Context"""
        system = multi_agent.MultiAgentSystem()
        system.update_context("")
        
        assert system.shared_context == ""


class TestCoordinate:
    """Tests für coordinate() Methode"""
    
    @patch('multi_agent.client')
    def test_coordinate_returns_string(self, mock_client):
        """Test: Rückgabewert ist String"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Koordination")]
        mock_client.messages.create.return_value = mock_response
        
        system = multi_agent.MultiAgentSystem()
        agent = multi_agent.Agent("Agent1", "Analyst")
        system.add_agent(agent)
        
        # Execute
        result = system.coordinate("Test Task")
        
        # Assert
        assert isinstance(result, str)
    
    @patch('multi_agent.client')
    def test_coordinate_with_no_agents(self, mock_client):
        """Test: Koordination ohne Agents"""
        system = multi_agent.MultiAgentSystem()
        
        # Execute & Assert
        with pytest.raises(Exception):
            system.coordinate("Test Task")
    
    @patch('multi_agent.client')
    def test_coordinate_calls_api(self, mock_client):
        """Test: API wird aufgerufen"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Koordination")]
        mock_client.messages.create.return_value = mock_response
        
        system = multi_agent.MultiAgentSystem()
        agent = multi_agent.Agent("Agent1", "Analyst")
        system.add_agent(agent)
        
        # Execute
        system.coordinate("Test")
        
        # Assert
        mock_client.messages.create.assert_called()
    
    @patch('multi_agent.client')
    def test_coordinate_correct_model(self, mock_client):
        """Test: Korrektes Modell wird verwendet"""
        # Setup
        mock_response = Mock()
        mock_response.content = [Mock(text="Koordination")]
        mock_client.messages.create.return_value = mock_response
        
        system = multi_agent.MultiAgentSystem()
        agent = multi_agent.Agent("Agent1", "Analyst")
        system.add_agent(agent)
        
        # Execute
        system.coordinate("Test")
        
        # Assert
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-3-5-sonnet-20241022"

