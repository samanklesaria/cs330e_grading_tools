# # Combine all the jsons into a single json file
sh mergeit.sh > merged.json

# # Calculate whether they deserve a bonus and extract names
jq -f bonuses.jq merged.json > bonuses.json

# # Grab relevant details from the test files
sh get_stats.sh > results.json

# Inner join on gitlab name
python joinfiles.py results.json bonuses.json
