PYTHON = python

all:
	@echo "Building Quixo..."
	@echo "author:Cherif hassan"

run:
	@$(PYTHON) main.py

clean:
	@echo "Cleaning up..."	
	@del /F /Q Controller\__pycache__ *.pyc
	@del /F /Q Model\__pycache__ *.pyc
	@del /F /Q View\__pycache__ *.pyc
	@del /F /Q Players\__pycache__ *.pyc

	@del /F /Q __pycache__ *.pyc


.PHONY: all run clean
