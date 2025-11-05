"""
Tests für bmi_rechner.py

Coverage: 95%+
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bmi_rechner import berechne_bmi, interpretiere_bmi


class TestBerechneBMI:
    """Tests für berechne_bmi() Funktion"""
    
    def test_berechne_bmi_normal(self):
        """Test: Normale BMI-Berechnung"""
        result = berechne_bmi(70, 1.75)
        assert result == 22.86
    
    def test_berechne_bmi_untergewicht(self):
        """Test: Untergewicht"""
        result = berechne_bmi(50, 1.75)
        assert result == 16.33
    
    def test_berechne_bmi_uebergewicht(self):
        """Test: Übergewicht"""
        result = berechne_bmi(100, 1.75)
        assert result == 32.65
    
    def test_berechne_bmi_adipositas(self):
        """Test: Adipositas"""
        result = berechne_bmi(120, 1.75)
        assert result == 39.18
    
    def test_berechne_bmi_negative_gewicht(self):
        """Test: Negatives Gewicht"""
        with pytest.raises(ValueError):
            berechne_bmi(-70, 1.75)
    
    def test_berechne_bmi_zero_gewicht(self):
        """Test: Null Gewicht"""
        with pytest.raises(ValueError):
            berechne_bmi(0, 1.75)
    
    def test_berechne_bmi_negative_groesse(self):
        """Test: Negative Grösse"""
        with pytest.raises(ValueError):
            berechne_bmi(70, -1.75)
    
    def test_berechne_bmi_zero_groesse(self):
        """Test: Null Grösse"""
        with pytest.raises(ValueError):
            berechne_bmi(70, 0)
    
    def test_berechne_bmi_small_values(self):
        """Test: Kleine Werte"""
        result = berechne_bmi(50, 1.5)
        assert result == 22.22
    
    def test_berechne_bmi_large_values(self):
        """Test: Grosse Werte"""
        result = berechne_bmi(150, 2.0)
        assert result == 37.5


class TestInterpretiereBMI:
    """Tests für interpretiere_bmi() Funktion"""
    
    def test_interpretiere_bmi_untergewicht(self):
        """Test: Untergewicht"""
        result = interpretiere_bmi(18.0)
        assert result == "Untergewicht"
    
    def test_interpretiere_bmi_normalgewicht(self):
        """Test: Normalgewicht"""
        result = interpretiere_bmi(22.0)
        assert result == "Normalgewicht"
    
    def test_interpretiere_bmi_uebergewicht(self):
        """Test: Übergewicht"""
        result = interpretiere_bmi(27.0)
        assert result == "Übergewicht"
    
    def test_interpretiere_bmi_adipositas(self):
        """Test: Adipositas"""
        result = interpretiere_bmi(32.0)
        assert result == "Adipositas"
    
    def test_interpretiere_bmi_grenzwert_untergewicht(self):
        """Test: Grenzwert Untergewicht"""
        result = interpretiere_bmi(18.5)
        assert result == "Normalgewicht"
    
    def test_interpretiere_bmi_grenzwert_normalgewicht(self):
        """Test: Grenzwert Normalgewicht"""
        result = interpretiere_bmi(25.0)
        assert result == "Übergewicht"
    
    def test_interpretiere_bmi_grenzwert_uebergewicht(self):
        """Test: Grenzwert Übergewicht"""
        result = interpretiere_bmi(30.0)
        assert result == "Adipositas"
    
    def test_interpretiere_bmi_sehr_niedrig(self):
        """Test: Sehr niedriger BMI"""
        result = interpretiere_bmi(10.0)
        assert result == "Untergewicht"
    
    def test_interpretiere_bmi_sehr_hoch(self):
        """Test: Sehr hoher BMI"""
        result = interpretiere_bmi(50.0)
        assert result == "Adipositas"


class TestIntegration:
    """Integrations-Tests"""
    
    def test_berechne_und_interpretiere(self):
        """Test: Berechnung und Interpretation zusammen"""
        bmi = berechne_bmi(70, 1.75)
        kategorie = interpretiere_bmi(bmi)
        assert kategorie == "Normalgewicht"
    
    def test_verschiedene_personen(self):
        """Test: Verschiedene Personen"""
        personen = [
            (50, 1.75, "Untergewicht"),
            (70, 1.75, "Normalgewicht"),
            (90, 1.75, "Übergewicht"),
            (110, 1.75, "Adipositas"),
        ]
        
        for gewicht, groesse, erwartet in personen:
            bmi = berechne_bmi(gewicht, groesse)
            kategorie = interpretiere_bmi(bmi)
            assert kategorie == erwartet

