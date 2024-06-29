import pandas as pd
import time
import tracemalloc

# Load the Excel file using a relative path
file_path = '..\\CVE data\\CveIdOnly.xlsx'
df = pd.read_excel(file_path)

# Extract numerical parts from the CVE ID as strings
cve_numbers = df['CVE ID'].str.replace('-', '')

# Pad the strings with leading zeros to ensure they are all the same length
max_len = cve_numbers.str.len().max()
cve_numbers = cve_numbers.str.zfill(max_len)

def counting_sort_string(arr, exp, max_len):
    n = len(arr)
    output = [""] * n
    count = [0] * 10

    for i in range(n):
        index = int(arr[i][max_len - exp])
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i][max_len - exp])
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort_string(arr):
    max_len = max(len(num) for num in arr)
    exp = 1
    while exp <= max_len:
        counting_sort_string(arr, exp, max_len)
        exp += 1

# Record start time and memory usage
start_time = time.time()
tracemalloc.start()

# Perform radix sort
radix_sort_string(cve_numbers)

# Record end time and memory usage
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Print time and space complexity, time taken, and memory used
time_taken = end_time - start_time
memory_used = peak / 10**6  # convert to MB

# Time complexity: O(d*(n+b)) where d is the number of digits in the maximum number, n is the number of elements, and b is the base (10 here).
# Space complexity: O(n+b) where n is the number of elements and b is the base.

time_complexity = "O(d*(n+b)) where d is the number of digits in the maximum number, n is the number of elements, and b is the base (10 here)."
space_complexity = "O(n+b) where n is the number of elements and b is the base."

print(f"Time Complexity: {time_complexity}")
print(f"Space Complexity: {space_complexity}")
print(f"Time Taken: {time_taken} seconds")
print(f"Memory Used: {memory_used} MB")
