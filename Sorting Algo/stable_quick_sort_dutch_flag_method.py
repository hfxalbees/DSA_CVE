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

# Timing the sort operation for 'Base Score'
start_time = time.time()
base_score_sorted = stable_quick_sort(df.to_dict('records'), 'Base Score')
base_score_sorted_df = pd.DataFrame(base_score_sorted)
base_score_sorted_df.to_excel('Base_Score_Sorted.xlsx', index=False)
base_score_sort_time = time.time() - start_time

# Timing the sort operation for 'Exploitability Score'
start_time = time.time()
exploitability_score_sorted = stable_quick_sort(df.to_dict('records'), 'Exploitability Score')
exploitability_score_sorted_df = pd.DataFrame(exploitability_score_sorted)
exploitability_score_sorted_df.to_excel('Exploitability_Score_Sorted.xlsx', index=False)
exploitability_score_sort_time = time.time() - start_time

# Timing the sort operation for 'Impact Score'
start_time = time.time()
impact_score_sorted = stable_quick_sort(df.to_dict('records'), 'Impact Score')
impact_score_sorted_df = pd.DataFrame(impact_score_sorted)
impact_score_sorted_df.to_excel('Impact_Score_Sorted.xlsx', index=False)
impact_score_sort_time = time.time() - start_time

# Print the timing results
print(f"Time taken to sort by Base Score: {base_score_sort_time:.4f} seconds")
print(f"Time taken to sort by Exploitability Score: {exploitability_score_sort_time:.4f} seconds")
print(f"Time taken to sort by Impact Score: {impact_score_sort_time:.4f} seconds")
