#!/bin/bash
# Test runner script for Employee Management System

echo "Running Employee Management System Tests..."
echo "=========================================="
echo ""

echo "1. Running API Tests..."
pytest tests/test_api.py -v
echo ""

echo "2. Running UI Logic Tests..."
pytest tests/test_ui_logic.py -v
echo ""

echo "3. Running All Tests..."
pytest tests/ -v
echo ""

echo "Tests completed!"


