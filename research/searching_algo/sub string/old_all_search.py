import pandas as pd
import time
from kmp import search_dataframe_kmp
from levenshtein_distance import find_similar_words
from brute_force import search_dataframe_brute_force

def run_and_time_search_algorithm(algorithm, data, search_term, column_name):
    start_time = time.time()
    results = algorithm(data, search_term, column_name)
    end_time = time.time()
    return results, end_time - start_time

file_path = 'small_dataset.xlsx'  # Path to your CVE dataset
df = pd.read_excel(file_path)
column_name = "Description"
search_term = "Multiple unspecified vulnerabilities in Google V8 before 4.6.85.23, as used in Google Chrome before 46.0.2490.71, allow attackers to cause a denial of service or possibly have other impact via unknown vectors."  # Example search term

# Define the Levenshtein search function to match the signature
def levenshtein_search_wrapper(df, search_term, column_name):
    similar_words = find_similar_words(df, column_name, search_term, threshold=3)
    return df[df[column_name].isin(similar_words)]

# List of search algorithms with the new brute force search included
search_algorithms = [

    (levenshtein_search_wrapper, "Levenshtein Search"),
]

results = []
time_results = []

for algorithm, algo_name in search_algorithms:
    search_results, exec_time = run_and_time_search_algorithm(algorithm, df, search_term, column_name)
    results.append((search_results, exec_time))
    time_results.append((algo_name, exec_time))

# Create a DataFrame from time results
time_df = pd.DataFrame(time_results, columns=['Algorithm', 'Execution Time'])

# Output and save results
print(time_df)
time_df.to_excel('search_timing_results.xlsx', index=False)


