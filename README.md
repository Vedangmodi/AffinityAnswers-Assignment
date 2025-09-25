# Task 2: SQL Queries for Rfam Database

## Database Information
- **Database**: Rfam Public Database
- **Host**: mysql-rfam-public.ebi.ac.uk
- **Port**: 4497
- **User**: rfamro
- **Password**: None required
- **Purpose**: Biological database for RNA families

## Approach & Methodology

### Exploration Phase
1. First connected to the Rfam database using MySQL client
2. Explored the database schema using `SHOW TABLES` and `DESCRIBE` commands
3. Identified key tables and their relationships through foreign key analysis
4. Tested all queries with actual data to ensure accuracy

### Key Discoveries
- Discovered that `full_region` table uses `rfam_acc` instead of `family_acc`
- Found that Sumatran Tiger (`Panthera tigris sumatrae`) is not present in current dataset
- Identified proper joining conditions between all major tables

## Notes
- All queries have been tested on the live Rfam database
- Results reflect the current state of the database
- Proper error handling and edge cases considered



# Task 3: AMFI India NAV Data Extractor

## Script Purpose
Extracts Scheme Name and Asset Value from AMFI India's mutual fund NAV data and converts it to TSV format.

## Features
- Downloads latest NAV data from AMFI India
- Extracts only Scheme Name and Asset Value fields
- Creates both TSV and JSON formats
- Includes proper error handling and validation
- Shows sample output and format comparison

## Usage
```bash
# Make script executable
chmod +x extract_nav.sh

# Run the script
./extract_nav.sh
