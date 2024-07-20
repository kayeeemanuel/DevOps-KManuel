#!/bin/bash

# Compile the application (syntax check for Python)
echo "Compiling the application..."
python -m py_compile hello.py
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

# Run unit tests
echo "Running unit tests..."
python -m unittest discover -s . -p "test_*.py"
if [ $? -ne 0 ]; then
    echo "Unit tests failed."
    exit 1
fi

# Package the application
echo "Packaging the application..."
zip -r hello_app.zip hello.py
if [ $? -ne 0 ]; then
    echo "Packaging failed."
    exit 1
fi

echo "Build and packaging completed successfully."
exit 0
