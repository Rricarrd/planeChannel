#!/bin/bash

# --- Configuration ---
REMOTE_USER="ricardarbat" # Replace with your SSH username on the remote nodes
REMOTE_HOST_PREFIX="juno"         # e.g., if your nodes are node3, node4, etc.
START_NODE=3                      # Starting node number
END_NODE=7                        # Ending node number
REMOTE_SCRIPT_PATH="./executeVariation.sh" # Path to the script on the remote node.
                                           # './' assumes it's in the remote user's home directory
                                           # or a directory added to their remote PATH.
                                           # Use a full path like '/path/to/remote/script.sh' if needed.

# --- Script Logic ---

echo "Starting directory iteration and remote execution..."

# Iterate through all directories in the current working directory that start with a digit
for DIR_PATH in [0-9]*/; do
    # Check if it's actually a directory
    if [ -d "$DIR_PATH" ]; then
        # Remove the trailing slash to get just the directory name
        DIR_NAME="${DIR_PATH%/}"

        echo ""
        echo "Processing local directory: '$DIR_NAME'"

        # Iterate through the specified range of remote nodes
        for NODE_NUM in $(seq $START_NODE $END_NODE); do
            REMOTE_HOST="${REMOTE_HOST_PREFIX}${NODE_NUM}"
            echo "  --> Connecting to ${REMOTE_USER}@${REMOTE_HOST}..."

            # Execute the remote script with the directory name as an argument
            # The directory name is quoted for robustness against spaces/special characters
            ssh "${REMOTE_USER}@${REMOTE_HOST}" "${REMOTE_SCRIPT_PATH} \"${DIR_NAME}\""

            # Check the exit status of the SSH command
            if [ $? -eq 0 ]; then
                echo "  Command executed successfully on ${REMOTE_HOST} for '$DIR_NAME'."
            else
                echo "  Error: Command failed on ${REMOTE_HOST} for '$DIR_NAME'. See above output for details."
            fi
        done
    fi
done

echo ""
echo "All specified directories processed."
