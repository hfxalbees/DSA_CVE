import pandas as pd
import openpyxl
import time

def custom_sort_key(s):
    """Convert a string like '1999-0095' to a tuple (1999, 95) for sorting."""
    parts = s.split('-')
    return (int(parts[0]), int(parts[1]))

def pigeonhole_sort_with_dataframe(df, key_func, column_name):
    start_time = time.time()
    print("Sorting started...")

    # Extract the column to sort by
    a = df[column_name].tolist()

    # Apply the key function to convert each element to a sortable tuple
    converted = [key_func(x) for x in a]
    
    # Find the range of the values
    min_val = min(converted)
    max_val = max(converted)
    range_size = max_val[0] - min_val[0] + 1  # only considering first part of tuple for pigeonholes

    # Create pigeonholes
    holes = [[] for _ in range(range_size)]

    # Populate the pigeonholes with indices
    for i, x in enumerate(converted):
        index = x[0] - min_val[0]
        holes[index].append((x, i))

    # Sort each pigeonhole and flatten the list
    sorted_indices = []
    for hole in holes:
        hole.sort()
        sorted_indices.extend([i for _, i in hole])

    # Rearrange the DataFrame based on sorted indices
    sorted_df = df.iloc[sorted_indices]

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Sorting completed in {elapsed_time:.2f} seconds.")
    return sorted_df

# Read the Excel file
input_file = 'CVE data/updated_cve_list.xlsx'  # Path to the input Excel file
df = pd.read_excel(input_file)

# Sort the DataFrame using pigeonhole sort based on the first column
sorted_df = pigeonhole_sort_with_dataframe(df, custom_sort_key, df.columns[0])

# Write the sorted DataFrame to a new Excel file
output_file = 'Sorted CVE/PigeonHoleSort.xlsx'  # Path to the output Excel file
sorted_df.to_excel(output_file, index=False)

print(f"Sorted values saved to {output_file}")
