import pandas as pd
import concurrent.futures
import time
from linear_search import linear_search
from fib_search import fibonacci_search
from binary_search import binary_search
from binary_tree_search import binary_tree_search
from exponential_search import exponential_search
from interpolation_search import interpolation_search_dataframe
from jump_search import jump_search_dataframe
from ternary_search import ternary_search_dataframe
from gallop_search import gallop_search_dataframe

# Load the Excel file
df = pd.read_excel('cleaned.xlsx')

def perform_search(algorithm, data, key, search_value):
    start_time = time.perf_counter()  # Start timing here
    result = algorithm(data, key, search_value)
    end_time = time.perf_counter()  # End timing here
    return result, end_time - start_time  # Return both result and time taken

# List of algorithms to run
algorithms = [
         binary_search                # Add if adapted to work with DataFrames
         # Add if adapted to work with DataFrames
]

# Target CVE ID to search for
target_cve_id = "2021-0043457"

results = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_algo = {executor.submit(perform_search, algo, df, 'CVE ID', target_cve_id): algo.__name__ for algo in algorithms}
    for future in concurrent.futures.as_completed(future_to_algo):
        algo_name = future_to_algo[future]  # Retrieve algorithm name directly from the dictionary
        search_result, search_time = future.result()
        results.append((algo_name, f"{search_time:.9f} seconds", search_result))

for result in results:
    print(result)
