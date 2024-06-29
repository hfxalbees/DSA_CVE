import pandas as pd
import time
import tracemalloc

# Load the data from the uploaded Excel file
file_path = '..\\CVE data\\CveIdOnly.xlsx'
cve_data = pd.read_excel(file_path)

# Extract the CVE IDs and sort them (assuming they are not already sorted)
cve_ids = cve_data['CVE ID'].tolist()
cve_ids.sort()

# Binary search function
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example CVE ID to search for
search_id = "1999-1122"

# Measure the time taken and memory used for the binary search
tracemalloc.start()
start_time = time.time()

# Perform the binary search multiple times
iterations = 100000
for _ in range(iterations):
    result = binary_search(cve_ids, search_id)

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = (end_time - start_time) / iterations
memory_used = peak - current

# Output the results
print(f"Search result index: {result}")
print(f"Time taken: {time_taken:.10f} seconds (average over {iterations} iterations)")
print(f"Memory used: {memory_used} bytes")
print("Time complexity: O(log n)")
print("Space complexity: O(1)")
