#!/bin/bash

# Check if a directory argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <target_directory>"
  exit 1
fi

TARGET_DIR="$1"
SCRIPT_NAME="runAllCasesTmux.sh"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory '$TARGET_DIR' not found."
  exit 1
fi

echo "Changing to directory: $TARGET_DIR"
cd "$TARGET_DIR" || { echo "Failed to change directory to $TARGET_DIR"; exit 1; }

# Add script and node info to casesRunning.txt

echo -e "\n$(date): Running $SCRIPT_NAME on node $(hostname) in directory $TARGET_DIR" >> ../casesRunning.txt || { echo "Warning: Could not write to casesRunning.txt"; }


echo "Executing $SCRIPT_NAME..."
if [ -f "./$SCRIPT_NAME" ]; then
bash ./$SCRIPT_NAME
else
  echo "Error: Script '$SCRIPT_NAME' not found in '$TARGET_DIR'."
  exit 1
fi

echo "Script execution completed."
