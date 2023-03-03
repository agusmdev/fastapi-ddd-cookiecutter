#!/bin/bash -e
# 
# Activar el entorno creado con virtualenv

source .venv/bin/activate

export PATH=$PATH:$(pwd)

# Load environment variables
if test -f ".env"; then
    set -o allexport && source .env && set +o allexport > /dev/null
fi