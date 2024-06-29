import pandas as pd
import time

# Load the Excel file
file_path = 'CVE_Data_2015.xlsx'
df = pd.read_excel(file_path)

# Prompt the user for a CVE ID
search_key = input("Enter the CVE ID to search for: ")

# Timing the linear search operation
start_time = time.perf_counter()
found = False
result = None

for index, row in df.iterrows():
    if row['CVE ID'] == search_key:
        result = row.to_dict()
        found = True
        break

search_time = time.perf_counter() - start_time

# Display the result
if found:
    print(f"Found {search_key}: {result}")
else:
    print(f"{search_key} not found in the data")

# Print the timing result
print(f"Time taken to search for {search_key}: {search_time:.9f} seconds")
