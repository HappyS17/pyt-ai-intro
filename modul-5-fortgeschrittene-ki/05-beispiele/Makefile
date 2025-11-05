.PHONY: help test test-verbose test-coverage test-fast test-unit test-integration clean install lint format

help:
	@echo "Verfügbare Befehle:"
	@echo "  make install          - Installiere Test-Dependencies"
	@echo "  make test             - Führe alle Tests aus"
	@echo "  make test-verbose     - Tests mit ausführlicher Ausgabe"
	@echo "  make test-coverage    - Tests mit Coverage Report"
	@echo "  make test-fast        - Schnelle Tests (parallel)"
	@echo "  make test-unit        - Nur Unit Tests"
	@echo "  make test-integration - Nur Integration Tests"
	@echo "  make lint             - Code Quality Checks"
	@echo "  make format           - Code formatieren"
	@echo "  make clean            - Cleanup"

install:
	uv sync --group test

test:
	pytest tests/

test-verbose:
	pytest tests/ -v

test-coverage:
	pytest tests/ --cov=. --cov-report=html --cov-report=term-missing
	@echo "Coverage Report: htmlcov/index.html"

test-fast:
	pytest tests/ -n auto

test-unit:
	pytest tests/ -m unit

test-integration:
	pytest tests/ -m integration

lint:
	flake8 *.py tests/
	pylint *.py tests/
	mypy *.py tests/

format:
	black *.py tests/

clean:
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf __pycache__
	rm -rf tests/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

