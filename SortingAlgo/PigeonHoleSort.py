import pandas as pd
import time
import psutil

def custom_sort_key(s):
    """Convert a string like '1999-0095' to a tuple (1999, 95) for sorting."""
    parts = s.split('-')
    return (int(parts[0]), int(parts[1]))

def pigeonhole_sort_with_dataframe(df, key_func, column_name):
    start_time = time.time()
    process = psutil.Process()
    mem_before = process.memory_info().rss
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
    mem_after = process.memory_info().rss
    mem_used = mem_after - mem_before

    elapsed_time = round(elapsed_time, 2)
    mem_used = round(mem_used / (1024 * 1024), 2)

    print(f"Sorting completed in {elapsed_time:.2f} seconds.")
    print(f"Memory used: {mem_used:.2f} MB")
    
    return sorted_df, elapsed_time, mem_used

if __name__ == "__main__":
    try:
        # Read the file using pandas
        print("Reading data from excel...")
        CVE_file_path = r'CVE data\small_set_for_testing.xlsx'  # Adjust the path as needed
        data = pd.read_excel(CVE_file_path)

        # Perform selection sort
        sorted_df, elapsed_time, mem_used = pigeonhole_sort_with_dataframe(data, custom_sort_key, data.columns[0])

        # Print the sorted DataFrame and the metrics
        print(sorted_df.head())
        print(f"Sorting completed in {elapsed_time:.2f} seconds.")
        print(f"Memory used: {mem_used:.2f} MB")

        # Save the sorted DataFrame to a new Excel file for verification
        sorted_file_path = 'Sorted CVE/PigeonHoleSort.xlsx'
        sorted_df.to_excel(sorted_file_path, index=False)
        print(f"Sorted file saved to {sorted_file_path}")

    except Exception as e:
        print(f'Error processing file: {str(e)}')