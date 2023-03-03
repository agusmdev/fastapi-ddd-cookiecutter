#!/bin/bash -e
# 
# Remover archivos temporales

# Clear files generated on coverage reports
rm -f .coverage.*
rm -f .coverage
rm -f coverage.xml
rm -f report.xml
rm -f tests/coverage/*
rm -rf htmlcov

# Clear pytest cache files
rm -rf .pytest_cache
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
