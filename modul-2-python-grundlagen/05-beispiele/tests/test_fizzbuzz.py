"""
Tests für fizzbuzz.py

Coverage: 95%+
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fizzbuzz import fizzbuzz


class TestFizzbuzz:
    """Tests für fizzbuzz() Funktion"""

    def test_fizzbuzz_eins(self):
        """Test: FizzBuzz für 1"""
        result = fizzbuzz(1)
        assert result == "1"

    def test_fizzbuzz_drei(self):
        """Test: FizzBuzz für 3 (Fizz)"""
        result = fizzbuzz(3)
        assert result == "Fizz"

    def test_fizzbuzz_fuenf(self):
        """Test: FizzBuzz für 5 (Buzz)"""
        result = fizzbuzz(5)
        assert result == "Buzz"

    def test_fizzbuzz_fuenfzehn(self):
        """Test: FizzBuzz für 15 (FizzBuzz)"""
        result = fizzbuzz(15)
        assert result == "FizzBuzz"

    def test_fizzbuzz_zwei(self):
        """Test: FizzBuzz für 2 (Zahl)"""
        result = fizzbuzz(2)
        assert result == "2"

    def test_fizzbuzz_sechs(self):
        """Test: FizzBuzz für 6 (Fizz)"""
        result = fizzbuzz(6)
        assert result == "Fizz"

    def test_fizzbuzz_zehn(self):
        """Test: FizzBuzz für 10 (Buzz)"""
        result = fizzbuzz(10)
        assert result == "Buzz"

    def test_fizzbuzz_dreissig(self):
        """Test: FizzBuzz für 30 (FizzBuzz)"""
        result = fizzbuzz(30)
        assert result == "FizzBuzz"


