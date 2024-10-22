#!/bin/bash

size_limit=$((99 * 1024 * 1024))

find . -type f -size +99M | while read file; do

    if ! grep -qxF "$file" .gitignore; then

        echo "$file" >> .gitignore
        echo "Added $file to .gitignore"
    else
        echo "$file is already in .gitignore"
    fi
done

