"""
Tests für passwort_validator.py

Coverage: 95%+
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from passwort_validator import (
    validiere_passwort,
    berechne_passwort_staerke,
    zeige_passwort_staerke_visuell
)


class TestValidierePasSwort:
    """Tests für validiere_passwort() Funktion"""
    
    def test_validiere_passwort_gueltig(self):
        """Test: Gültiges Passwort"""
        gueltig, fehler = validiere_passwort("MyPass123!")
        assert gueltig is True
        assert len(fehler) == 0
    
    def test_validiere_passwort_zu_kurz(self):
        """Test: Zu kurzes Passwort"""
        gueltig, fehler = validiere_passwort("Pass1!")
        assert gueltig is False
        assert any("8 Zeichen" in f for f in fehler)
    
    def test_validiere_passwort_kein_grossbuchstabe(self):
        """Test: Kein Grossbuchstabe"""
        gueltig, fehler = validiere_passwort("mypass123!")
        assert gueltig is False
        assert any("Grossbuchstabe" in f for f in fehler)
    
    def test_validiere_passwort_kein_kleinbuchstabe(self):
        """Test: Kein Kleinbuchstabe"""
        gueltig, fehler = validiere_passwort("MYPASS123!")
        assert gueltig is False
        assert any("Kleinbuchstabe" in f for f in fehler)
    
    def test_validiere_passwort_keine_ziffer(self):
        """Test: Keine Ziffer"""
        gueltig, fehler = validiere_passwort("MyPassword!")
        assert gueltig is False
        assert any("Ziffer" in f for f in fehler)
    
    def test_validiere_passwort_kein_sonderzeichen(self):
        """Test: Kein Sonderzeichen"""
        gueltig, fehler = validiere_passwort("MyPassword123")
        assert gueltig is False
        assert any("Sonderzeichen" in f for f in fehler)
    
    def test_validiere_passwort_alle_fehler(self):
        """Test: Alle Fehler"""
        gueltig, fehler = validiere_passwort("pass")
        assert gueltig is False
        assert len(fehler) == 4  # Keine Kleinbuchstaben ist nicht erforderlich
    
    def test_validiere_passwort_verschiedene_sonderzeichen(self):
        """Test: Verschiedene Sonderzeichen"""
        sonderzeichen = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        for char in sonderzeichen[:5]:
            pw = f"MyPass123{char}"
            gueltig, _ = validiere_passwort(pw)
            assert gueltig is True


class TestBerechnePasSwortStaerke:
    """Tests für berechne_passwort_staerke() Funktion"""
    
    def test_berechne_staerke_schwach(self):
        """Test: Schwaches Passwort"""
        result = berechne_passwort_staerke("pass")
        assert result == "schwach"
    
    def test_berechne_staerke_mittel(self):
        """Test: Mittleres Passwort"""
        result = berechne_passwort_staerke("Password1")
        assert result == "mittel"
    
    def test_berechne_staerke_stark(self):
        """Test: Starkes Passwort"""
        result = berechne_passwort_staerke("MyPass123!")
        assert result == "stark"
    
    def test_berechne_staerke_sehr_stark(self):
        """Test: Sehr starkes Passwort"""
        result = berechne_passwort_staerke("MySecure123!@#$%")
        assert result == "sehr stark"
    
    def test_berechne_staerke_lange_passwort(self):
        """Test: Langes Passwort"""
        result = berechne_passwort_staerke("A" * 20 + "a1!")
        assert result in ["stark", "sehr stark"]


class TestZeigePasswortStaerkeVisuell:
    """Tests für zeige_passwort_staerke_visuell() Funktion"""
    
    def test_zeige_staerke_schwach(self):
        """Test: Visuelle Darstellung schwach"""
        result = zeige_passwort_staerke_visuell("schwach")
        assert "🔴" in result
        assert "████░░░░░░" in result
    
    def test_zeige_staerke_mittel(self):
        """Test: Visuelle Darstellung mittel"""
        result = zeige_passwort_staerke_visuell("mittel")
        assert "🟡" in result
        assert "██████░░░░" in result
    
    def test_zeige_staerke_stark(self):
        """Test: Visuelle Darstellung stark"""
        result = zeige_passwort_staerke_visuell("stark")
        assert "🟢" in result
        assert "████████░░" in result
    
    def test_zeige_staerke_sehr_stark(self):
        """Test: Visuelle Darstellung sehr stark"""
        result = zeige_passwort_staerke_visuell("sehr stark")
        assert "🟢" in result
        assert "██████████" in result
    
    def test_zeige_staerke_unbekannt(self):
        """Test: Unbekannte Stärke"""
        result = zeige_passwort_staerke_visuell("unbekannt")
        assert "⚪" in result


class TestIntegration:
    """Integrations-Tests"""
    
    def test_validierung_und_staerke(self):
        """Test: Validierung und Stärke zusammen"""
        pw = "MyPass123!"
        gueltig, _ = validiere_passwort(pw)
        staerke = berechne_passwort_staerke(pw)
        visuell = zeige_passwort_staerke_visuell(staerke)
        
        assert gueltig is True
        assert staerke in ["schwach", "mittel", "stark", "sehr stark"]
        assert len(visuell) > 0
    
    def test_verschiedene_passwoerter(self):
        """Test: Verschiedene Passwörter"""
        passwoerter = [
            ("pass", False, "schwach"),
            ("Password1", False, "mittel"),
            ("MyPass123!", True, "stark"),
            ("MySecure123!@#$%", True, "sehr stark"),
        ]
        
        for pw, erwartet_gueltig, erwartet_staerke in passwoerter:
            gueltig, _ = validiere_passwort(pw)
            staerke = berechne_passwort_staerke(pw)
            assert gueltig == erwartet_gueltig
            assert staerke == erwartet_staerke

