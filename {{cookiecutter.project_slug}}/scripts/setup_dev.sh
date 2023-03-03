#!/bin/bash -e
# 
# Hacer setup para desarrollo local

# Configure Git entity
IFS= read -r -p "Enter entity name (e.g. John Doe): " name
IFS= read -r -p "Enter entity e-mail (e.g. john.dow@gmail.com): " email

git config entity.name "$name"
git config entity.email "$email"

# Give execution permissions to commands
chmod +x commands/*
