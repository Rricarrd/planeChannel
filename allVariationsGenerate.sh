for variation_file in variation_files/*.variations; do
    python generate_variations.py --variations "$(basename "$variation_file")"
done
