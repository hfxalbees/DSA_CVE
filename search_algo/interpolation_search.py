import pandas as pd
import numpy as np
import time
import tracemalloc

# Interpolation Search Function
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Load the Excel file
file_path = '..\\CVE data\\CveIdOnly.xlsx'
data = pd.read_excel(file_path)

# Convert CVE IDs to integer format for the search (e.g., remove 'CVE-' and convert to int)
data['CVE ID'] = data['CVE ID'].apply(lambda x: int(x.replace('-', '')))

# Prepare the array for searching
arr = data['CVE ID'].values
arr.sort()

# Define the target CVE ID to search for (e.g., '1999-1122')
target_cve_id = '1999-1122'
target = int(target_cve_id.replace('-', ''))

# Start measuring time
start_time = time.time()

# Start measuring memory usage
tracemalloc.start()

# Perform the search
index = interpolation_search(arr, target)

# Stop measuring memory usage
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Stop measuring time
end_time = time.time()
time_taken = end_time - start_time

# Convert memory usage to KB
memory_used = peak / 1024

# Print results
result = {
    'Index Found': index,
    'Time Taken (seconds)': time_taken,
    'Memory Used (KB)': memory_used
}

print(result)
