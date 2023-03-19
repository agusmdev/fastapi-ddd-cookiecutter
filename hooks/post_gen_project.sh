#!/bin/bash -e
# 


if [ "$(uname)" == "Darwin" ]; then ## Check if we are in MacOS
    find . -type f -exec sed -i '' -e 's/entity/{{cookiecutter.first_entity | lower}}/g' {} \;
    find . -type f -exec sed -i '' -e 's/Entity/{{cookiecutter.first_entity | capitalize}}/g' {} \;
else
    find . -type f -exec sed -i 's/entity/{{cookiecutter.first_entity | lower}}/g' {} \;
    find . -type f -exec sed -i 's/Entity/{{cookiecutter.first_entity | capitalize}}/g' {} \;
fi

git init --initial-branch=main
./scripts/install.sh