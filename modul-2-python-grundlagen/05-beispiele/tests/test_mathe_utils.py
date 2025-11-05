"""
Tests für mathe_utils.py

Coverage: 95%+
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mathe_utils import ist_gerade, ist_primzahl, fakultaet, fibonacci, durchschnitt


class TestIstGerade:
    """Tests für ist_gerade() Funktion"""
    
    def test_ist_gerade_true(self):
        """Test: Gerade Zahlen"""
        assert ist_gerade(2) is True
        assert ist_gerade(10) is True
        assert ist_gerade(100) is True
    
    def test_ist_gerade_false(self):
        """Test: Ungerade Zahlen"""
        assert ist_gerade(1) is False
        assert ist_gerade(7) is False
        assert ist_gerade(99) is False
    
    def test_ist_gerade_null(self):
        """Test: Null ist gerade"""
        assert ist_gerade(0) is True
    
    def test_ist_gerade_negative(self):
        """Test: Negative Zahlen"""
        assert ist_gerade(-2) is True
        assert ist_gerade(-3) is False


class TestIstPrimzahl:
    """Tests für ist_primzahl() Funktion"""
    
    def test_ist_primzahl_true(self):
        """Test: Primzahlen"""
        primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in primzahlen:
            assert ist_primzahl(p) is True
    
    def test_ist_primzahl_false(self):
        """Test: Keine Primzahlen"""
        keine_primzahlen = [0, 1, 4, 6, 8, 9, 10, 12, 15, 20]
        for n in keine_primzahlen:
            assert ist_primzahl(n) is False
    
    def test_ist_primzahl_negative(self):
        """Test: Negative Zahlen sind keine Primzahlen"""
        assert ist_primzahl(-5) is False
    
    def test_ist_primzahl_grosse_primzahl(self):
        """Test: Grosse Primzahl"""
        assert ist_primzahl(97) is True


class TestFakultaet:
    """Tests für fakultaet() Funktion"""
    
    def test_fakultaet_null(self):
        """Test: 0! = 1"""
        assert fakultaet(0) == 1
    
    def test_fakultaet_eins(self):
        """Test: 1! = 1"""
        assert fakultaet(1) == 1
    
    def test_fakultaet_kleine_zahlen(self):
        """Test: Kleine Fakultäten"""
        assert fakultaet(2) == 2
        assert fakultaet(3) == 6
        assert fakultaet(4) == 24
        assert fakultaet(5) == 120
    
    def test_fakultaet_groessere_zahlen(self):
        """Test: Grössere Fakultäten"""
        assert fakultaet(10) == 3628800


class TestFibonacci:
    """Tests für fibonacci() Funktion"""
    
    def test_fibonacci_null(self):
        """Test: fibonacci(0)"""
        assert fibonacci(0) == []
    
    def test_fibonacci_eins(self):
        """Test: fibonacci(1)"""
        assert fibonacci(1) == [0]
    
    def test_fibonacci_zwei(self):
        """Test: fibonacci(2)"""
        assert fibonacci(2) == [0, 1]
    
    def test_fibonacci_zehn(self):
        """Test: fibonacci(10)"""
        result = fibonacci(10)
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_fibonacci_negative(self):
        """Test: Negative Eingabe"""
        assert fibonacci(-5) == []
    
    def test_fibonacci_laenge(self):
        """Test: Länge der Fibonacci-Sequenz"""
        result = fibonacci(5)
        assert len(result) == 5


class TestDurchschnitt:
    """Tests für durchschnitt() Funktion"""
    
    def test_durchschnitt_einfach(self):
        """Test: Einfacher Durchschnitt"""
        assert durchschnitt([1, 2, 3]) == 2.0
    
    def test_durchschnitt_floats(self):
        """Test: Durchschnitt mit Floats"""
        result = durchschnitt([1.5, 2.5, 3.0])
        assert abs(result - 2.333333) < 0.001
    
    def test_durchschnitt_negative(self):
        """Test: Durchschnitt mit negativen Zahlen"""
        assert durchschnitt([-1, 0, 1]) == 0.0
    
    def test_durchschnitt_ein_element(self):
        """Test: Ein Element"""
        assert durchschnitt([5]) == 5.0
    
    def test_durchschnitt_leere_liste(self):
        """Test: Leere Liste"""
        with pytest.raises(ValueError):
            durchschnitt([])
    
    def test_durchschnitt_grosse_zahlen(self):
        """Test: Grosse Zahlen"""
        result = durchschnitt([1000, 2000, 3000])
        assert result == 2000.0

