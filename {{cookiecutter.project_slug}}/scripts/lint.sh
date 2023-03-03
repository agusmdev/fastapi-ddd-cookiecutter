#!/bin/bash

# Repo root directory
REPO_ROOT_DIR="$(git rev-parse --show-toplevel)"

echo "Running black!"
poetry run black "${REPO_ROOT_DIR}/app"
echo "Running ruff!"
poetry run ruff --fix "${REPO_ROOT_DIR}/app"
