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

## File Structure
- `exploration.sql` - Initial database exploration queries
- `solutions.sql` - Final answers to all questions
- `results.md` - Actual output from running the queries

## Notes
- All queries have been tested on the live Rfam database
- Results reflect the current state of the database
- Proper error handling and edge cases considered
