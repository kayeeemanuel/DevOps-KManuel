# Makefile
.PHONY: clean build test

clean:
    rm -rf *.pyc __pycache__

build: clean
    python3 -m compileall .

test: build
    python3 -m unittest discover
