import pandas as pd
import time

# Step 1: Load the dataset from Excel
file_path = 'shell_sorted.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Step 2: Define a function to perform ternary search
def ternary_search_cve(cve_list, target_cve):
    left, right = 0, len(cve_list) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if cve_list[mid1]['CVE ID'] == target_cve:
            return mid1
        elif cve_list[mid2]['CVE ID'] == target_cve:
            return mid2
        elif target_cve < cve_list[mid1]['CVE ID']:
            right = mid1 - 1
        elif target_cve > cve_list[mid2]['CVE ID']:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

# Step 3: Prompt user input for CVE ID
target_cve = input("Enter CVE ID (e.g., CVE-2024-1234): ")

# Step 4: Perform ternary search with timing measurement
start_time = time.time()
sorted_df = df.sort_values(by='CVE ID').reset_index(drop=True)
cve_list = sorted_df.to_dict('records')
result_index = ternary_search_cve(cve_list, target_cve)
end_time = time.time()

# Step 5: Display corresponding information if found
if result_index != -1:
    print(f"CVE {target_cve} found!")
    print("Details:")
    for key, value in cve_list[result_index].items():
        print(f"{key}: {value}")
else:
    print(f"CVE {target_cve} not found in the dataset.")

# Step 6: Print the time taken for the search
print(f"Time taken: {end_time - start_time:.6f} seconds")
