# Employee-Record-Deduplication-Script
This tool normalizes employee data, handles inconsistent formatting (hyphens, spacing, usernames vs. full names), and produces an audit-friendly summary.

- Extracts employee ID numbers from mixed-format input
- Deduplicates records using Employee ID as the unique key
- Normalizes usernames (first initial + last name)
- Cleans and formats full names

Handles:
- Hyphen-separated entries (123456 - Jane Doe)
- Username-only entries (jdoe)
- ID-only entries (123456)

Provides a clear summary including:
- Total entries processed
- Unique employee IDs
- Number of duplicates removed

Example Input:
100001 - Jane Doe
100001-jdoe
100001
200002 - John Smith
200002-jsmith

Example Output:
Emp ID     Username   Full Name
----------------------------------------
100001     jdoe       Jane Doe
200002     jsmith     John Smith

Summary:
Total entries processed: 5
Unique employee IDs:     2
Duplicate entries removed: 3

Requirements:
- Python 3.9+
- No external libraries required (uses only the standard library)

This script does not connect to any systems, does not perform deletions, and is read-only and intended for data cleanup review.
