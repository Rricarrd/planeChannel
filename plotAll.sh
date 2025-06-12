echo "Plotting all cases"
# Iterate through all directories in the current working directory that start with a digit
for DIR_PATH in [0-9]*/; do
    # Check if it's actually a directory
    if [ -d "$DIR_PATH" ]; then

        # Into directory, execute the plotting script and exit
        echo "Plotting in directory: $DIR_PATH"
        cd "$DIR_PATH"
        python plot_all.py time skip
        cd ..
    fi
done

echo ""
echo "All specified directories processed."