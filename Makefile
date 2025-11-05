.PHONY: test test-coverage test-fast test-modul1 test-modul2 test-modul3 test-modul4 test-modul5 install help

help:
	@echo "🧪 Test-Befehle für pyt-ai-intro"
	@echo ""
	@echo "Setup:"
	@echo "  make install           - Test-Dependencies mit uv installieren"
	@echo ""
	@echo "Alle Tests:"
	@echo "  make test              - Alle Tests ausführen"
	@echo "  make test-coverage     - Tests mit Coverage-Report"
	@echo "  make test-fast         - Tests parallel (schneller)"
	@echo ""
	@echo "Modul-spezifische Tests:"
	@echo "  make test-modul1       - Tests für Modul 1 (Mindset & Setup)"
	@echo "  make test-modul2       - Tests für Modul 2 (Python Grundlagen)"
	@echo "  make test-modul3       - Tests für Modul 3 (Datenverarbeitung)"
	@echo "  make test-modul4       - Tests für Modul 4 (Agentic Coding)"
	@echo "  make test-modul5       - Tests für Modul 5 (Fortgeschrittene KI)"
	@echo ""
	@echo "Weitere:"
	@echo "  make clean             - Cleanup (__pycache__, .pytest_cache)"
	@echo "  make help              - Diese Hilfe anzeigen"

install:
	@echo "📦 Installiere Test-Dependencies mit uv..."
	uv sync --group test

test:
	@echo "🧪 Führe alle Tests aus..."
	pytest

test-coverage:
	@echo "📊 Führe Tests mit Coverage aus..."
	pytest --cov=. --cov-report=html --cov-report=term-missing
	@echo ""
	@echo "✅ Coverage Report: htmlcov/index.html"

test-fast:
	@echo "⚡ Führe Tests parallel aus..."
	pytest -n auto

test-modul1:
	@echo "🧪 Tests für Modul 1..."
	pytest modul-1-mindset-setup/05-beispiele/tests -v

test-modul2:
	@echo "🧪 Tests für Modul 2..."
	pytest modul-2-python-grundlagen/05-beispiele/tests -v

test-modul3:
	@echo "🧪 Tests für Modul 3..."
	pytest modul-3-datenverarbeitung-dateien/05-beispiele/tests -v

test-modul4:
	@echo "🧪 Tests für Modul 4..."
	pytest modul-4-agentic-coding/05-beispiele/tests -v

test-modul5:
	@echo "🧪 Tests für Modul 5..."
	pytest modul-5-fortgeschrittene-ki/05-beispiele/tests -v

clean:
	@echo "🧹 Cleanup..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .coverage -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleanup abgeschlossen"

