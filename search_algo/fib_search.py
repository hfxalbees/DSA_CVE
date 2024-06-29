import pandas as pd
import time

# Load the Excel file
file_path = 'CVE_ID_Sorted.xlsx'
df = pd.read_excel(file_path)

# Convert the sorted DataFrame to a list of dictionaries for easier manipulation
data_list = df.to_dict(orient='records')

# Fibonacci Search implementation
def fibonacci_search(arr, x, key):
    n = len(arr)
    
    # Initialize fibonacci numbers
    fib2 = 0  # (m-2)'th Fibonacci number
    fib1 = 1  # (m-1)'th Fibonacci number
    fibM = fib1 + fib2  # m'th Fibonacci number

    # fibM is going to store the smallest Fibonacci number >= n
    while (fibM < n):
        fib2 = fib1
        fib1 = fibM
        fibM = fib1 + fib2

    # Marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected. Note that we compare arr[fib2] with x.
    while (fibM > 1):
        # Check if fib2 is a valid location
        i = min(offset + fib2, n - 1)

        # If x is greater than the value at index fib2, cut the subarray from offset to i
        if (arr[i][key] < x):
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i

        # If x is less than the value at index fib2, cut the subarray after i+1
        elif (arr[i][key] > x):
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1

        # Element found, return index
        else:
            return i

    # comparing the last element with x
    if(fib1 and arr[offset + 1][key] == x):
        return offset + 1

    # Element not found
    return -1

# Prompt the user for a CVE ID
search_key = input("Enter the CVE ID to search for: ")

# Timing the Fibonacci search operation
start_time = time.perf_counter()
index = fibonacci_search(data_list, search_key, 'CVE ID')
search_time = time.perf_counter() - start_time

# Display the result
if index != -1:
    print(f"Found {search_key}: {data_list[index]}")
else:
    print(f"{search_key} not found in the data")

# Print the timing result
print(f"Time taken to search for {search_key}: {search_time:.9f} seconds")
