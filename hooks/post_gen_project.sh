#!/bin/bash -e
# 


if [ "$(uname)" == "Darwin" ]; then ## Check if we are in MacOS
    find . -type f -exec sed -i '' -e 's/entity/asd/g' {} \;
    find . -type f -exec sed -i '' -e 's/Entity/Asd/g' {} \;
else
    find . -type f -exec sed -i 's/entity/asd/g' {} \;
    find . -type f -exec sed -i 's/Entity/Asd/g' {} \;
fi

git init --initial-branch=main