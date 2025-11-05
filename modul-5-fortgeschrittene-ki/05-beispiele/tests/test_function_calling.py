"""
Tests für function_calling.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import function_calling


class TestCalculator:
    """Tests für calculator() Funktion"""
    
    def test_calculator_simple_addition(self):
        """Test: Einfache Addition"""
        result = function_calling.calculator("2 + 3")
        assert "5" in result
    
    def test_calculator_multiplication(self):
        """Test: Multiplikation"""
        result = function_calling.calculator("3 * 4")
        assert "12" in result
    
    def test_calculator_complex_expression(self):
        """Test: Komplexer Ausdruck"""
        result = function_calling.calculator("2 + 3 * 4")
        assert "14" in result
    
    def test_calculator_division(self):
        """Test: Division"""
        result = function_calling.calculator("10 / 2")
        assert "5" in result
    
    def test_calculator_invalid_expression(self):
        """Test: Ungültiger Ausdruck"""
        result = function_calling.calculator("invalid")
        assert "Fehler" in result
    
    def test_calculator_division_by_zero(self):
        """Test: Division durch Null"""
        result = function_calling.calculator("1 / 0")
        assert "Fehler" in result


class TestGetWeather:
    """Tests für get_weather() Funktion"""
    
    def test_get_weather_berlin(self):
        """Test: Wetter für Berlin"""
        result = function_calling.get_weather("Berlin")
        assert "Sonnig" in result or "22" in result
    
    def test_get_weather_munich(self):
        """Test: Wetter für München"""
        result = function_calling.get_weather("München")
        assert "Bewölkt" in result or "18" in result
    
    def test_get_weather_hamburg(self):
        """Test: Wetter für Hamburg"""
        result = function_calling.get_weather("Hamburg")
        assert "Regnerisch" in result or "15" in result
    
    def test_get_weather_unknown_city(self):
        """Test: Unbekannte Stadt"""
        result = function_calling.get_weather("UnbekannteStadt")
        assert "Keine Daten" in result


class TestProcessToolCall:
    """Tests für process_tool_call() Funktion"""
    
    def test_process_tool_call_calculator(self):
        """Test: Calculator Tool wird verarbeitet"""
        result = function_calling.process_tool_call(
            "calculator",
            {"expression": "2 + 2"}
        )
        assert "4" in result
    
    def test_process_tool_call_weather(self):
        """Test: Weather Tool wird verarbeitet"""
        result = function_calling.process_tool_call(
            "get_weather",
            {"city": "Berlin"}
        )
        assert "Sonnig" in result or "22" in result
    
    def test_process_tool_call_unknown_tool(self):
        """Test: Unbekanntes Tool"""
        result = function_calling.process_tool_call(
            "unknown_tool",
            {}
        )
        assert "Unbekanntes Tool" in result


class TestToolDefinitions:
    """Tests für Tool-Definitionen"""
    
    def test_tools_list_exists(self):
        """Test: Tools Liste existiert"""
        assert hasattr(function_calling, 'tools')
        assert isinstance(function_calling.tools, list)
    
    def test_tools_count(self):
        """Test: Richtige Anzahl von Tools"""
        assert len(function_calling.tools) == 2
    
    def test_calculator_tool_definition(self):
        """Test: Calculator Tool Definition"""
        calc_tool = next(t for t in function_calling.tools if t["name"] == "calculator")
        assert "description" in calc_tool
        assert "input_schema" in calc_tool
    
    def test_weather_tool_definition(self):
        """Test: Weather Tool Definition"""
        weather_tool = next(t for t in function_calling.tools if t["name"] == "get_weather")
        assert "description" in weather_tool
        assert "input_schema" in weather_tool


class TestChatWithTools:
    """Tests für chat_with_tools() Funktion"""
    
    @patch('function_calling.client')
    def test_chat_with_tools_no_tool_use(self, mock_client):
        """Test: Chat ohne Tool-Aufruf"""
        # Setup
        mock_response = Mock()
        mock_response.stop_reason = "end_turn"
        mock_response.content = [Mock(text="Antwort")]
        mock_client.messages.create.return_value = mock_response
        
        # Execute
        result = function_calling.chat_with_tools("Hallo")
        
        # Assert
        assert result == "Antwort"
    
    @patch('function_calling.client')
    def test_chat_with_tools_with_tool_use(self, mock_client):
        """Test: Chat mit Tool-Aufruf"""
        # Setup
        tool_use_block = Mock()
        tool_use_block.type = "tool_use"
        tool_use_block.name = "calculator"
        tool_use_block.input = {"expression": "2 + 2"}
        tool_use_block.id = "tool_123"
        
        # Erste Response mit Tool-Aufruf
        response1 = Mock()
        response1.stop_reason = "tool_use"
        response1.content = [tool_use_block]
        
        # Zweite Response mit Antwort
        response2 = Mock()
        response2.stop_reason = "end_turn"
        response2.content = [Mock(text="Das Ergebnis ist 4")]
        
        mock_client.messages.create.side_effect = [response1, response2]
        
        # Execute
        result = function_calling.chat_with_tools("Was ist 2 + 2?")
        
        # Assert
        assert "4" in result or "Ergebnis" in result

