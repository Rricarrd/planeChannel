#!/bin/bash

# Script to copy files from scripts/variations to folders named #_*
# where # is a digit, and replace files with the same names

# Check if scripts/variations directory exists
if [ ! -d "scripts/variations" ]; then
    echo "Error: scripts/variations directory not found"
    exit 1
fi

# Find all directories that start with a digit followed by underscore
for target_dir in [0-9]*_*/; do
    if [ -d "$target_dir" ]; then
        echo "Processing directory: $target_dir"
        
        # Copy all files from scripts/variations to the target directory
        for file in scripts/variations/*; do
            if [ -f "$file" ]; then
                filename=$(basename "$file")
                cp "$file" "$target_dir"
                echo "  Copied $filename to $target_dir"
            fi
        done
    fi
done

echo "File copying completed"