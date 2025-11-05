"""
Tests für cost_tracking.py

Coverage: 95%+
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.modules['anthropic'] = MagicMock()

import cost_tracking


class TestCostTracker:
    """Tests für CostTracker Klasse"""
    
    def test_cost_tracker_initialization(self):
        """Test: CostTracker wird initialisiert"""
        tracker = cost_tracking.CostTracker(budget=10.0)
        assert tracker.budget == 10.0
        assert tracker.spent == 0.0
        assert isinstance(tracker.requests, list)
    
    def test_cost_tracker_default_budget(self):
        """Test: Standard-Budget"""
        tracker = cost_tracking.CostTracker()
        assert tracker.budget == 10.0


class TestCalculateCost:
    """Tests für calculate_cost() Methode"""
    
    def test_calculate_cost_returns_float(self):
        """Test: Rückgabewert ist Float"""
        tracker = cost_tracking.CostTracker()
        result = tracker.calculate_cost(1000, 500)
        assert isinstance(result, float)
    
    def test_calculate_cost_zero_tokens(self):
        """Test: Null Tokens"""
        tracker = cost_tracking.CostTracker()
        result = tracker.calculate_cost(0, 0)
        assert result == 0.0
    
    def test_calculate_cost_input_tokens(self):
        """Test: Input Token Kosten"""
        tracker = cost_tracking.CostTracker()
        result = tracker.calculate_cost(1000, 0)
        expected = (1000 / 1000) * 0.003
        assert result == expected
    
    def test_calculate_cost_output_tokens(self):
        """Test: Output Token Kosten"""
        tracker = cost_tracking.CostTracker()
        result = tracker.calculate_cost(0, 1000)
        expected = (1000 / 1000) * 0.015
        assert result == expected
    
    def test_calculate_cost_combined(self):
        """Test: Kombinierte Kosten"""
        tracker = cost_tracking.CostTracker()
        result = tracker.calculate_cost(1000, 1000)
        expected = (1000 / 1000) * 0.003 + (1000 / 1000) * 0.015
        assert result == expected


class TestTrackRequest:
    """Tests für track_request() Methode"""
    
    def test_track_request_returns_dict(self):
        """Test: Rückgabewert ist Dict"""
        tracker = cost_tracking.CostTracker()
        result = tracker.track_request("Test message", "Test response")
        assert isinstance(result, dict)
    
    def test_track_request_has_required_fields(self):
        """Test: Erforderliche Felder vorhanden"""
        tracker = cost_tracking.CostTracker()
        result = tracker.track_request("Test", "Response")
        assert "timestamp" in result
        assert "input_tokens" in result
        assert "output_tokens" in result
        assert "cost" in result
        assert "total_spent" in result
        assert "budget_remaining" in result
    
    def test_track_request_updates_spent(self):
        """Test: Spent wird aktualisiert"""
        tracker = cost_tracking.CostTracker()
        initial_spent = tracker.spent
        tracker.track_request("Test", "Response")
        assert tracker.spent > initial_spent
    
    def test_track_request_adds_to_list(self):
        """Test: Request wird zur Liste hinzugefügt"""
        tracker = cost_tracking.CostTracker()
        initial_count = len(tracker.requests)
        tracker.track_request("Test", "Response")
        assert len(tracker.requests) == initial_count + 1
    
    def test_track_request_multiple_requests(self):
        """Test: Mehrere Requests"""
        tracker = cost_tracking.CostTracker()
        tracker.track_request("Test 1", "Response 1")
        tracker.track_request("Test 2", "Response 2")
        assert len(tracker.requests) == 2
        assert tracker.spent > 0


class TestCheckBudget:
    """Tests für check_budget() Methode"""
    
    def test_check_budget_within_limit(self):
        """Test: Budget nicht überschritten"""
        tracker = cost_tracking.CostTracker(budget=100.0)
        tracker.spent = 50.0
        assert tracker.check_budget() is True
    
    def test_check_budget_at_limit(self):
        """Test: Budget erreicht"""
        tracker = cost_tracking.CostTracker(budget=100.0)
        tracker.spent = 100.0
        assert tracker.check_budget() is False
    
    def test_check_budget_exceeded(self):
        """Test: Budget überschritten"""
        tracker = cost_tracking.CostTracker(budget=100.0)
        tracker.spent = 150.0
        assert tracker.check_budget() is False


class TestGetStats:
    """Tests für get_stats() Methode"""
    
    def test_get_stats_returns_dict(self):
        """Test: Rückgabewert ist Dict"""
        tracker = cost_tracking.CostTracker()
        result = tracker.get_stats()
        assert isinstance(result, dict)
    
    def test_get_stats_has_required_fields(self):
        """Test: Erforderliche Felder vorhanden"""
        tracker = cost_tracking.CostTracker()
        result = tracker.get_stats()
        assert "total_requests" in result
        assert "total_spent" in result
        assert "budget" in result
        assert "remaining" in result
        assert "percentage_used" in result
    
    def test_get_stats_initial_values(self):
        """Test: Initiale Werte"""
        tracker = cost_tracking.CostTracker(budget=10.0)
        result = tracker.get_stats()
        assert result["total_requests"] == 0
        assert result["total_spent"] == 0.0
        assert result["budget"] == 10.0
        assert result["remaining"] == 10.0
        assert result["percentage_used"] == 0.0
    
    def test_get_stats_after_requests(self):
        """Test: Werte nach Requests"""
        tracker = cost_tracking.CostTracker(budget=10.0)
        tracker.track_request("Test", "Response")
        result = tracker.get_stats()
        assert result["total_requests"] == 1
        assert result["total_spent"] > 0
        assert result["percentage_used"] > 0

