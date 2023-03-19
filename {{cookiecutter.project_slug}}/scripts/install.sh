#!/bin/bash -e
# 
# Instalar el repositorio en el directorio actual

# Remove already existing virtualenv
if [ -d ".venv" ]; then rm -Rf venv; fi

# Configure poetry to use venv
poetry env use python3
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

# Install poetry env with dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install

# Install pre-push hooks
echo "./scripts/test.sh unit \\nexit \$?" > .git/hooks/pre-push
chmod a+x .git/hooks/pre-push
