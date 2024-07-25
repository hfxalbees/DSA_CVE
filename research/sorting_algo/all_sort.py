import concurrent.futures
import pandas as pd
import time
from merge_sort import merge_sort  # Assuming merge_sort is in merge_sort.py
from stable_quick_sort import stable_quick_sort  
from PigeonHoleSort import pigeonhole_sort 
from SelectionSort import selection_sort 
from shell_sort import shell_sort  
from insertion_sort import insertion_sort 
from bubble_sort import bubble_sort 
from bucket import bucket_sort 
from comb_sort import comb_sort 
from RadixSort import radix_sort 


def run_and_time_sorting_algorithm(algorithm, data, column_name):
    start_time = time.time()
    data_list = data.to_dict('records')
    sorted_data = algorithm(data_list, column_name)
    sorted_df = pd.DataFrame(sorted_data)
    end_time = time.time()
    return sorted_df, end_time - start_time

file_path = 'cleaned.xlsx'
df = pd.read_excel(file_path)
column_name = "CVE ID"
sorting_algorithms = [merge_sort, stable_quick_sort, pigeonhole_sort, selection_sort, shell_sort, insertion_sort, bubble_sort, bucket_sort, comb_sort, radix_sort]
results = []
time_results = []  # List to store algorithm names and their execution times

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(run_and_time_sorting_algorithm, algo, df, column_name): algo.__name__ for algo in sorting_algorithms}
    for future in concurrent.futures.as_completed(futures):
        algo_name = futures[future]
        sorted_data, exec_time = future.result()
        results.append((sorted_data, exec_time))
        time_results.append((algo_name, exec_time))  # Collect algorithm name and time taken

# Create a DataFrame from time results
time_df = pd.DataFrame(time_results, columns=['Algorithm', 'Execution Time'])

# Print results
for algo_name, exec_time in time_results:
    print(f"{algo_name} took {exec_time:.6f} seconds")

# Save the sorted DataFrame to an Excel file for each algorithm
for sorted_data, _ in results:
    sorted_data.to_excel(f'sorted_{algo_name}.xlsx', index=False)

# Print and save the time results DataFrame
print(time_df)
time_df.to_excel('timing_results.xlsx', index=False)
