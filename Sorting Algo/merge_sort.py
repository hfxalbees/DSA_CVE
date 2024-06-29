import pandas as pd
import time

# Load the Excel file
file_path = 'CVE_Data_2015.xlsx'
df = pd.read_excel(file_path)

# Merge Sort implementation
def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:  # Change to ascending order
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Timing the sort operation for 'CVE ID'
start_time = time.time()
cve_id_sorted = df.to_dict('records')
merge_sort(cve_id_sorted, 'CVE ID')
cve_id_sorted_df = pd.DataFrame(cve_id_sorted)
cve_id_sorted_df.to_excel('CVE_ID_Sorted.xlsx', index=False)
cve_id_sort_time = time.time() - start_time

# Print the timing results
print(f"Time taken to sort by CVE ID: {cve_id_sort_time:.4f} seconds")
