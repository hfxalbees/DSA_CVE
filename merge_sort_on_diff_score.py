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
            if left_half[i][key] > right_half[j][key]:
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

# Timing the sort operation for 'Base Score'
start_time = time.time()
base_score_sorted = df.to_dict('records')
merge_sort(base_score_sorted, 'Base Score')
base_score_sorted_df = pd.DataFrame(base_score_sorted)
base_score_sorted_df.to_excel('Base_Score_Sorted.xlsx', index=False)
base_score_sort_time = time.time() - start_time

# Timing the sort operation for 'Exploitability Score'
start_time = time.time()
exploitability_score_sorted = df.to_dict('records')
merge_sort(exploitability_score_sorted, 'Exploitability Score')
exploitability_score_sorted_df = pd.DataFrame(exploitability_score_sorted)
exploitability_score_sorted_df.to_excel('Exploitability_Score_Sorted.xlsx', index=False)
exploitability_score_sort_time = time.time() - start_time

# Timing the sort operation for 'Impact Score'
start_time = time.time()
impact_score_sorted = df.to_dict('records')
merge_sort(impact_score_sorted, 'Impact Score')
impact_score_sorted_df = pd.DataFrame(impact_score_sorted)
impact_score_sorted_df.to_excel('Impact_Score_Sorted.xlsx', index=False)
impact_score_sort_time = time.time() - start_time

# Print the timing results
print(f"Time taken to sort by Base Score: {base_score_sort_time:.4f} seconds")
print(f"Time taken to sort by Exploitability Score: {exploitability_score_sort_time:.4f} seconds")
print(f"Time taken to sort by Impact Score: {impact_score_sort_time:.4f} seconds")
