#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to clean build artifacts
clean() {
    echo "Cleaning build artifacts..."
    rm -rf __pycache__
    find . -type f -name "*.pyc" -delete
}

# Function to build (compile) the application
build() {
    echo "Building the application..."
    python3 -m compileall .
}

# Function to run unit tests
test() {
    echo "Running unit tests..."
    python3 -m unittest discover
}

# Main script execution
clean
build
test

echo "Build and tests completed successfully."
