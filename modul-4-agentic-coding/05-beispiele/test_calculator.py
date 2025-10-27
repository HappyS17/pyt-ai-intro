"""
Test-Suite für Calculator-Klasse
Verwendung: Lektion 2 - TDD-Beispiel
"""
import pytest
from calculator import Calculator


class TestCalculator:
    """Test-Suite für Calculator."""
    
    def setup_method(self):
        """Setup vor jedem Test."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test: Addition positiver Zahlen."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test: Addition negativer Zahlen."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5
    
    def test_subtract(self):
        """Test: Subtraktion."""
        assert self.calc.subtract(10, 5) == 5
        assert self.calc.subtract(5, 10) == -5
    
    def test_multiply(self):
        """Test: Multiplikation."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 5) == -10
    
    def test_divide(self):
        """Test: Division."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test: Division durch Null wirft Exception."""
        with pytest.raises(ValueError, match="Division durch Null"):
            self.calc.divide(10, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Test: Addition mit verschiedenen Parametern."""
        assert self.calc.add(a, b) == expected
    
    @pytest.mark.parametrize("a,b,op,expected", [
        (10, 5, "add", 15),
        (10, 5, "subtract", 5),
        (10, 5, "multiply", 50),
        (10, 5, "divide", 2),
    ])
    def test_operations_parametrized(self, a, b, op, expected):
        """Test: Verschiedene Operationen."""
        method = getattr(self.calc, op)
        assert method(a, b) == expected


class TestCalculatorEdgeCases:
    """Test-Suite für Edge Cases."""
    
    def setup_method(self):
        """Setup vor jedem Test."""
        self.calc = Calculator()
    
    def test_very_large_numbers(self):
        """Test: Sehr grosse Zahlen."""
        large = 10**100
        assert self.calc.add(large, large) == 2 * large
    
    def test_floating_point_precision(self):
        """Test: Floating-Point-Präzision."""
        result = self.calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10
    
    def test_zero_operations(self):
        """Test: Operationen mit Null."""
        assert self.calc.add(0, 0) == 0
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.subtract(0, 5) == -5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
