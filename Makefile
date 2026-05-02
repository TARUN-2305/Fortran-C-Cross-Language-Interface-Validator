.PHONY: install test lint format report-lapack clean

install:
	pip install -e .[dev]

test:
	pytest -v

lint:
	flake8 fcv
	black --check fcv

format:
	black fcv

report-lapack:
	# Add lapack report generation command here later
	@echo "Not implemented yet"

clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
