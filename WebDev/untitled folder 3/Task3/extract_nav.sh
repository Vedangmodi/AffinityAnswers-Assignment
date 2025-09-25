#!/bin/bash

# AMFI India NAV Data Extractor
# Extracts Scheme Name and Asset Value from mutual fund data

echo "Starting AMFI NAV data extraction..."

# Correct URL (they moved to portal.amfiindia.com)
DATA_URL="https://portal.amfiindia.com/spages/NAVAll.txt"
TSV_FILE="amfi_nav_data.tsv"
JSON_FILE="amfi_nav_data.json"

echo "Downloading data from AMFI India..."
curl -s "$DATA_URL" > temp_data.txt

if [ ! -s temp_data.txt ]; then
    echo "Error: Failed to download data"
    exit 1
fi

echo "Processing data..."

# Create TSV file with header
echo -e "Scheme Name\tAsset Value" > "$TSV_FILE"

# Extract Scheme Name (field 4) and Asset Value (field 5) from semicolon-separated data
awk -F ';' '
BEGIN {
    count = 0
}
NR > 1 && NF >= 5 && $4 != "" && $5 != "" && $4 != "Scheme Name" {
    scheme_name = $4
    asset_value = $5
    gsub(/^[ \t]+|[ \t]+$/, "", scheme_name)
    gsub(/^[ \t]+|[ \t]+$/, "", asset_value)
    if (scheme_name != "" && asset_value != "") {
        print scheme_name "\t" asset_value
        count++
    }
}
END {
    if (count > 0) {
        print "Successfully extracted " count " records"
    }
}' temp_data.txt >> "$TSV_FILE"

# Create JSON version for comparison
echo "[" > "$JSON_FILE"
awk -F '\t' '
NR == 1 { next } # Skip header
{
    if (NR > 2) printf ",\n"
    printf "  {\n"
    printf "    \"scheme_name\": \"%s\",\n", $1
    printf "    \"asset_value\": \"%s\"\n", $2
    printf "  }"
}
END { print "\n]" }' "$TSV_FILE" >> "$JSON_FILE"

# Cleanup
rm temp_data.txt

echo "Extraction completed!"
echo "Files created:"
echo "- $TSV_FILE (TSV format, $(wc -l < "$TSV_FILE") lines)"
echo "- $JSON_FILE (JSON format)"

echo ""
echo "Sample of extracted data:"
echo "========================="
head -5 "$TSV_FILE"
echo "========================="

echo ""
echo "Note: JSON format would be better for:"
echo "- Web APIs and modern applications"
echo "- Structured data with proper typing" 
echo "- Easier parsing in JavaScript/Python"
echo "- Support for nested/hierarchical data"