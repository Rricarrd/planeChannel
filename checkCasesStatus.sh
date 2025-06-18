#!/bin/bash

# Clear or create the not-finished list
echo "Creating/clearing not_finished_list.txt"
> not_finished_list.txt

echo "Searching for top-level directories matching pattern ##_*..."

# Loop over top-level directories matching pattern like 5_test or 12_case
for top_dir in [0-9][0-9]_* [0-9]_*; do
    # Remove trailing slash if any
    top_dir=${top_dir%/}

    # Skip non-directories
    if [ ! -d "$top_dir" ]; then
        echo "Skipping $top_dir (not a directory)"
        continue
    fi

    echo "Processing top-level directory: $top_dir"

    # Look for subdirectories that start with the same name
    for sub_dir in "$top_dir"/[0-9]_*; do
        if [ ! -d "$sub_dir" ]; then
            echo "Skipping $sub_dir (not a directory)"
            continue
        fi

        echo "  Checking subdirectory: $sub_dir"

        float_dirs=()
        # Loop over potential float-named subdirectories
        for fdir in "$sub_dir"/*; do
            fname=$(basename "$fdir")
            if [[ -d "$fdir" && "$fname" =~ ^[0-9]+\.[0-9]+$ ]]; then
                float_dirs+=("$fname")
            fi
        done

        if [ ${#float_dirs[@]} -eq 0 ]; then
            echo "    No float directories found in $sub_dir — marking as not finished"
            echo "$sub_dir" >> not_finished_list.txt
            continue
        fi

        # Find the maximum float
        max_float=$(printf "%s\n" "${float_dirs[@]}" | sort -g | tail -n 1)
        echo "    Max float found: $max_float"

        # Compare max float against threshold (440)
        if (( $(echo "$max_float > 440" | bc -l) )); then
            echo "$sub_dir → finished ✅ (max = $max_float)"
        else
            echo "$sub_dir → not finished (max = $max_float)"
            echo "$sub_dir" >> not_finished_list.txt
        fi
    done
done

echo "Script complete. Check not_finished_list.txt for unfinished cases."

