#!/bin/bash

# Find all default.parameters files up to 2 subdirectories deep
find . -maxdepth 3 -name "default.parameters" -type f | while read -r file; do
    echo "Processing: $file"
    
    # Check if the file contains the target string
    if grep -q "tEnd              600;" "$file"; then
        # Create a backup
        cp "$file" "$file.bak"
        
        # Replace the string
        sed -i 's/tEnd              600;/tEnd              450;/g' "$file"
        
        echo "Updated $file (backup created as $file.bak)"
    else
        echo "Target string not found in $file"
    fi
done

echo "Processing complete."