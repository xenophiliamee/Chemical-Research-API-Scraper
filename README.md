# Chemical Research API Scraper

## Description

This Python script automates the process of querying the OpenAlex API to retrieve research articles related to a list of chemical names. It reads chemical names from a series of text files, searches for research papers that mention each chemical in their title or abstract, and stores the results in CSV and text files. The script uses pagination to handle large result sets and retries failed requests with exponential backoff.

## Key Features:
- Handles multiple input files containing lists of chemical names.
- Makes API requests to retrieve research articles using OpenAlex API.
- Supports pagination to collect all available research articles.
- Automatically retries failed requests with exponential backoff.
- Saves results to CSV and tracks found/not found chemicals in separate text files.
- Includes rate-limiting handling by pausing between requests to avoid hitting API rate limits.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)
- Pandas library (`pip install pandas`)

## Files:
### Input files:
The chemical names are stored in text files (`chemical_list_1.txt`, `chemical_list_2.txt`, ..., `chemical_list_24.txt`). Each line contains one chemical name.

### Output files:
- `chemical_results_{file_index}.csv`: Stores the API results in CSV format.
- `found_chemical_list_{file_index}.txt`: Stores the list of chemicals that returned results from the API.
- `not_found_chemical_list_{file_index}.txt`: Stores the list of chemicals that didn't return any results.

## How to Run:
1. Place your chemical name text files (e.g., `chemical_list_1.txt`, `chemical_list_2.txt`, etc.) in the same directory as the script.
2. Run the script:
    ```bash
    python script_name.py
    ```

## Example:
For each input file (e.g., `chemical_list_1.txt`), the script will:
- Search for each chemical in the OpenAlex API.
- Collect up to 50 articles per chemical, handling pagination.
- Save results in CSV format and track which chemicals returned results or not in separate text files.

## Notes:
- The script retries up to 5 times for each chemical if a request fails, with exponential backoff.
- To avoid API rate limits, the script pauses for 10 seconds after processing every 20 chemicals.

## License:
This project is open-source and available under the MIT License. See the LICENSE file for more details.
