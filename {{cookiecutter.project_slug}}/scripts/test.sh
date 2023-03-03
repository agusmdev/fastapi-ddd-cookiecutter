#!/bin/bash -e
# 
# Correr una suite específica de tests

# Execute selected suite of tests
if [[ "$1" == "unit" ]]
then
  echo "Executing unit tests"
  poetry run pytest ./tests/unit
elif [[ "$1" == "system" ]]
then
  echo "Executing system tests"
  poetry run pytest ./tests/system
elif [[ "$1" == "all" ]]
then
  echo "Executing unit + system tests"
  poetry run pytest ./tests/unit
  poetry run pytest --cov-append ./tests/system
else
  # Unit tests by default
  echo "Executing unit tests"
  poetry run pytest -rP ./tests/unit
fi
