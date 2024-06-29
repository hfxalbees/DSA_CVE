# Done By Chen YiHeng
import time
import tracemalloc
import pandas as pd

# Load the data
file_path = '..\\CVE data\\CveIdOnly.xlsx'
df = pd.read_excel(file_path)
data = df['CVE ID'].tolist()

# Function to perform bucket sort
def bucket_sort(arr):
    # Create buckets
    largest = max(arr)
    length = len(arr)
    size = largest/length

    buckets = [[] for _ in range(length)]

    # Insert elements into their respective buckets
    for i in range(length):
        j = int(arr[i] / size)
        if j != length:
            buckets[j].append(arr[i])
        else:
            buckets[length - 1].append(arr[i])

    # Sort the elements of each bucket
    for i in range(length):
        buckets[i] = sorted(buckets[i])

    # Get the sorted elements
    result = []
    for i in range(length):
        result = result + buckets[i]

    return result

# Convert CVE IDs to integers for sorting
int_data = [int(cve_id.replace('-', '')) for cve_id in data]

# Measure the time taken to run the program
start_time = time.time()
tracemalloc.start()

sorted_data = bucket_sort(int_data)

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()

# Convert sorted integers back to CVE IDs
sorted_cve_ids = [f"{str(cve_id)[:4]}-{str(cve_id)[4:]}" for cve_id in sorted_data]

# Print the time and space complexity
time_complexity = "O(n + k)"
space_complexity = "O(n + k)"

print(f"Time Complexity: {time_complexity}")
print(f"Space Complexity: {space_complexity}")
print(f"Time taken to run the program: {end_time - start_time} seconds")
print(f"Memory used: Current={current / 10**6}MB; Peak={peak / 10**6}MB")

# Create a DataFrame with the sorted CVE IDs
sorted_df = pd.DataFrame(sorted_cve_ids, columns=['CVE ID'])
sorted_df.head()
