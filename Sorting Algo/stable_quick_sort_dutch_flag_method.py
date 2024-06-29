import pandas as pd
import time

# Load the Excel file
file_path = 'CVE_Data_2015.xlsx'
df = pd.read_excel(file_path)

# Stable Quick Sort implementation
def stable_quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][key]
        less = [x for x in arr if x[key] < pivot]
        equal = [x for x in arr if x[key] == pivot]
        greater = [x for x in arr if x[key] > pivot]
        return stable_quick_sort(less, key) + equal + stable_quick_sort(greater, key)

# Timing the sort operation for 'CVE ID'
start_time = time.time()
cve_id_sorted = stable_quick_sort(df.to_dict('records'), 'CVE ID')
cve_id_sorted_df = pd.DataFrame(cve_id_sorted)
cve_id_sorted_df.to_excel('CVE_ID_Sorted.xlsx', index=False)
cve_id_sort_time = time.time() - start_time

# Print the timing results
print(f"Time taken to sort by CVE ID: {cve_id_sort_time:.4f} seconds")
