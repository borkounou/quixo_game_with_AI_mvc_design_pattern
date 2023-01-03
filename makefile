PYTHON = python

all:
	@echo "Building Quixo..."

run:
	@$(PYTHON) main.py

clean:
	@echo "Cleaning up..."	
	@del /F /Q *.pyc
	@del /F /Q *.pyo
	@del /F /Q *.log

.PHONY: all run clean
