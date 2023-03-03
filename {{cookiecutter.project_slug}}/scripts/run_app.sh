#!/bin/bash -e
# 
# Correr app

poetry run uvicorn app.main:create_app --port 8000
