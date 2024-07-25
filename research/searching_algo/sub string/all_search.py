import pandas as pd
import time
from kmp import search_dataframe_kmp
from brute_force import search_dataframe_brute_force
from levenshtein_distance import find_similar_words, find_all_distances

def run_and_time_search_algorithm(algorithm, data, search_term, column_name):
    start_time = time.time()
    results = algorithm(data, search_term, column_name)
    end_time = time.time()
    return results, end_time - start_time

file_path = 'cleaned.xlsx'  # Path to your CVE dataset
df = pd.read_excel(file_path)
column_name = "Description"
search_term = "html"  # Example search term

def levenshtein_search_wrapper(df, search_term, column_name):
    results_df = find_all_distances(df, column_name, search_term)
    return results_df

# List of search algorithms with the new brute force search included
search_algorithms = [
    (search_dataframe_kmp, "KMP Search"),
    (search_dataframe_brute_force, "Brute Force Search")
    
]

results = []
time_results = []

for algorithm, algo_name in search_algorithms:
    search_results, exec_time = run_and_time_search_algorithm(algorithm, df, search_term, column_name)
    results.append((search_results, exec_time))
    time_results.append((algo_name, exec_time))
    # Print the results of the search
    print(f"Results for {algo_name}:")
    print(search_results)  # Print all rows of the search results
    print(f"Execution time: {exec_time:.4f} seconds\n")

# Create a DataFrame from time results
time_df = pd.DataFrame(time_results, columns=['Algorithm', 'Execution Time'])

# Output and save results
print(time_df)
time_df.to_excel('search_timing_results.xlsx', index=False)
