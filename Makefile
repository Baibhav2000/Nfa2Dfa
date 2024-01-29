PYTHON = python3
PIP = $(PYTHON) -m pip
SRC_DIR = src
TEST_DIR = tests
VENV_DIR = venv

PIP_REQUIREMENTS = requirements.txt

setup:
	@echo -n "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV_DIR)
	@echo "OK"

install: $(PIP_REQUIREMENTS)
	@echo "Installing necessary dependencies"
	@$(PIP) install -r $(PIP_REQUIREMENTS)

test:
	@echo "Running tests..."
	@$(PYTHON) -m unittest discover tests

run:
	@$(PYTHON) -m src.main


