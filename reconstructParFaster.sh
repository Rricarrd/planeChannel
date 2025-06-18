#!/bin/bash

# Directory to search (change '.' to your specific directory if needed)
DIR="processor0"

# Tolerance in seconds for approximate spacing
TOLERANCE=0.5
INTERVAL=5.0

# Extract directory names that start with a float, sort numerically
folders=$(find "$DIR" -maxdepth 1 -type d -regextype posix-extended -regex '.*/[0-9]+\.[0-9]+' | sed 's#.*/##' | sort -n)

selected=()
last_selected_time=""

for folder in $folders; do
    current_time=$folder

    # First folder (starting from 0 or smallest)
    if [ -z "$last_selected_time" ]; then
        selected+=("$folder")
        last_selected_time=$current_time
        continue
    fi

    # Compute time difference
    diff=$(echo "$current_time - $last_selected_time" | bc -l)

    # If difference is ~5s, within tolerance, select it
    cmp=$(echo "$diff >= $INTERVAL - $TOLERANCE && $diff <= $INTERVAL + $TOLERANCE" | bc -l)
    if [ "$cmp" -eq 1 ]; then
        selected+=("$folder")
        last_selected_time=$current_time
    fi
done

# Print the selected folder names
for folder in "${selected[@]}"; do
    echo "$folder"
done

