# import requests
# import pandas as pd

# chemical_names = ["Beta-Penta-O-galloyl-D-glucose", "(-)-20S-Heyneanine"]
# results = []

# for chemical in chemical_names:
#     response = requests.get(f"https://api.openalex.org/works?filter=title.search:{chemical}")
#     data = response.json()
#     results.extend(data.get('results', []))

# # Save results to a CSV file
# df = pd.DataFrame(results)
# df.to_csv('chemical_results.csv', index=False)

# import requests
# import pandas as pd
# import time

# # Read chemical names from the text file
# with open('chemical_list_1.txt', 'r') as file:
#     chemical_names = [line.strip() for line in file if line.strip()]

# results = []
# not_found_chemicals = []
# found_chemicals = []

# # Process chemicals in batches of 20
# for index, chemical in enumerate(chemical_names):
#     response = requests.get(f"https://api.openalex.org/works?filter=title.search:{chemical}")
#     data = response.json()

#     if data.get('results'):
#         results.extend(data['results'])
#         found_chemicals.append(chemical)  # Add to found chemicals list
#     else:
#         not_found_chemicals.append(chemical)

#     # Wait for 10 seconds after every 20 chemicals
#     if (index + 1) % 20 == 0:
#         print(f"Processed {index + 1} chemicals. Waiting for 10 seconds...")
#         time.sleep(5)

# # Save results to a CSV file
# if results:
#     df = pd.DataFrame(results)
#     df.to_csv('chemical_results_1.csv', index=False)

# # Save found chemicals to a separate file
# if found_chemicals:
#     with open('found_chemical_list_1.txt', 'w') as f_file:
#         for chemical in found_chemicals:
#             f_file.write(chemical + '\n')

# # Save not found chemicals to a separate file
# if not_found_chemicals:
#     with open('not_found_chemical_list_1.txt', 'w') as nf_file:
#         for chemical in not_found_chemicals:
#             nf_file.write(chemical + '\n')

# print("Process completed.")

# import requests
# import pandas as pd
# import time

# chemical_files = [f'chemical_list_{i}.txt' for i in range(1, 25)]  # Adjust the range if needed

# for file_index, chemical_file in enumerate(chemical_files, start=1):
#     print(f"Processing {chemical_file}...")
    
#     with open(chemical_file, 'r') as file:
#         chemical_names = [line.strip() for line in file if line.strip()]

#     results = []
#     not_found_chemicals = []
#     found_chemicals = []

#     for index, chemical in enumerate(chemical_names):
#         attempt = 0
#         while attempt < 5:  # Retry up to 5 times
#             try:
#                 response = requests.get(f"https://api.openalex.org/works?filter=title.search:{chemical}")
#                 data = response.json()

#                 if data.get('results'):
#                     results.extend(data['results'])
#                     found_chemicals.append(chemical)
#                 else:
#                     not_found_chemicals.append(chemical)

                

#                 break  # Exit the retry loop if successful

#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching data for {chemical}: {e}")
#                 attempt += 1
#                 time.sleep(2 ** attempt)  # Exponential backoff

#         if (index + 1) % 20 == 0:
#             print(f"Processed {index + 1} chemicals. Waiting for 10 seconds...")
#             time.sleep(10)

#     if results:
#         df = pd.DataFrame(results)
#         df.to_csv(f'chemical_results_{file_index}.csv', index=False)

#     if found_chemicals:
#         with open(f'found_chemical_list_{file_index}.txt', 'w') as f_file:
#             for chemical in found_chemicals:
#                 f_file.write(chemical + '\n')

#     if not_found_chemicals:
#         with open(f'not_found_chemical_list_{file_index}.txt', 'w') as nf_file:
#             for chemical in not_found_chemicals:
#                 nf_file.write(chemical + '\n')

#     print(f"Completed processing {chemical_file}.\n")

# print("All processes completed.")

# new updtated 

# import requests
# import pandas as pd
# import time

# # List of chemical files
# chemical_files = [f'chemical_list_{i}.txt' for i in range(1, 25)]  # Adjust the range if needed

# # Loop through each file
# for file_index, chemical_file in enumerate(chemical_files, start=1):
#     print(f"Processing {chemical_file}...")
    
#     # Read chemical names from the file
#     with open(chemical_file, 'r') as file:
#         chemical_names = [line.strip() for line in file if line.strip()]

#     results = []
#     not_found_chemicals = []
#     found_chemicals = []

#     # Loop through each chemical name
#     for index, chemical in enumerate(chemical_names):
#         attempt = 0
#         page = 1
#         while attempt < 5:  # Retry up to 5 times
#             try:
#                 # Request the OpenAlex API for both title and abstract search, with pagination
#                 while True:
#                     # Construct the URL with pagination and search filters
#                     url = f"https://api.openalex.org/works?filter=title.search:{chemical},abstract.search:{chemical}&page={page}&per_page=50"
#                     response = requests.get(url)

#                     # Check if the response is valid
#                     if response.status_code == 200:
#                         data = response.json()

#                         if data.get('results'):
#                             results.extend(data['results'])  # Append results
#                             found_chemicals.append(chemical)  # Track found chemicals
#                         else:
#                             not_found_chemicals.append(chemical)  # Track not found chemicals
                        
#                         # Check if the current page has fewer than 50 results (end of pages)
#                         if len(data['results']) < 50:
#                             break
#                         else:
#                             page += 1  # Move to the next page
#                     else:
#                         print(f"Error fetching data for {chemical} on page {page}: {response.status_code}")
#                         break  # Exit the inner loop on an error
#                 break  # Exit the retry loop if successful
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching data for {chemical}: {e}")
#                 attempt += 1
#                 time.sleep(2 ** attempt)  # Exponential backoff

#         # Every 20 chemicals, wait for 10 seconds to avoid hitting rate limits
#         if (index + 1) % 20 == 0:
#             print(f"Processed {index + 1} chemicals. Waiting for 10 seconds...")
#             time.sleep(10)

#     # Save results to CSV if there are any
#     if results:
#         df = pd.DataFrame(results)
#         df.to_csv(f'chemical_results_{file_index}.csv', index=False)

#     # Save found chemicals to text file
#     if found_chemicals:
#         with open(f'found_chemical_list_{file_index}.txt', 'w') as f_file:
#             for chemical in found_chemicals:
#                 f_file.write(chemical + '\n')

#     # Save not found chemicals to text file
#     if not_found_chemicals:
#         with open(f'not_found_chemical_list_{file_index}.txt', 'w') as nf_file:
#             for chemical in not_found_chemicals:
#                 nf_file.write(chemical + '\n')

#     print(f"Completed processing {chemical_file}.\n")

# print("All processes completed.")

import requests
import pandas as pd
import time

chemical_files = [f'chemical_list_{i}.txt' for i in range(1, 25)]  # Adjust the range if needed how much bash file you want to create

for file_index, chemical_file in enumerate(chemical_files, start=1):
    print(f"Processing {chemical_file}...")
    
    with open(chemical_file, 'r') as file:
        chemical_names = [line.strip() for line in file if line.strip()]

    results = []
    not_found_chemicals = []
    found_chemicals = []

    for index, chemical in enumerate(chemical_names):
        attempt = 0
        page = 1  # Start from the first page
        while attempt < 5:  # Retry up to 5 times
            try:
                while True:  # Loop through pages
                    # Construct the API request URL with pagination and search filters (title + abstract)
                    url = f"https://api.openalex.org/works?filter=title.search:{chemical},abstract.search:{chemical}&page={page}&per_page=50"
                    response = requests.get(url)

                    # Check if the response is valid
                    if response.status_code == 200:
                        data = response.json()

                        if data.get('results'):
                            for item in data['results']:
                                item['chemical_name'] = chemical  # Add the chemical name to the result
                            results.extend(data['results'])  # Add results from this page
                            found_chemicals.append(chemical)
                        else:
                            not_found_chemicals.append(chemical)
                        
                        # If fewer than 50 results are returned, we're done
                        if len(data['results']) < 50:
                            break
                        else:
                            page += 1  # Move to the next page
                    else:
                        print(f"Error fetching data for {chemical} on page {page}: {response.status_code}")
                        break  # Exit if there's an error with the API
                break  # Exit the retry loop if successful
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data for {chemical}: {e}")
                attempt += 1
                time.sleep(2 ** attempt)  # Exponential backoff

        # Every 20 chemicals, wait for 10 seconds to avoid hitting rate limits
        if (index + 1) % 20 == 0:
            print(f"Processed {index + 1} chemicals. Waiting for 10 seconds...")
            time.sleep(10)

    # Save results to CSV if there are any
    if results:
        df = pd.DataFrame(results)
        df.to_csv(f'chemical_results_{file_index}.csv', index=False)

    # Save found chemicals to text file
    if found_chemicals:
        with open(f'found_chemical_list_{file_index}.txt', 'w') as f_file:
            for chemical in found_chemicals:
                f_file.write(chemical + '\n')

    # Save not found chemicals to text file
    if not_found_chemicals:
        with open(f'not_found_chemical_list_{file_index}.txt', 'w') as nf_file:
            for chemical in not_found_chemicals:
                nf_file.write(chemical + '\n')

    print(f"Completed processing {chemical_file}.\n")

print("All processes completed.")
