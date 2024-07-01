import pandas as pd
import time
import psutil

def custom_sort_key(s):
    """Convert a string like '1999-0001' to a tuple (1999, 1) for sorting."""
    parts = s.split('-')
    return (int(parts[0]), int(parts[1]))

def selection_sort_with_dataframe(df, key_func, column_name):
    start_time = time.time()
    process = psutil.Process()
    mem_before = process.memory_info().rss
    print("Sorting started...")

    # Extract the column to sort by and apply the key function
    a = df[column_name].apply(key_func).tolist()
    sizeOfArray = len(a)
    
    print(f"Number of elements to sort: {sizeOfArray}")

    for i in range(sizeOfArray):
        minPosition = i
        for j in range(i + 1, sizeOfArray):
            if a[j] < a[minPosition]:
                minPosition = j
        # swap in the list
        a[i], a[minPosition] = a[minPosition], a[i]
        # swap in the dataframe
        df.iloc[i], df.iloc[minPosition] = df.iloc[minPosition].copy(), df.iloc[i].copy()
        if i % 100 == 0:
            print(f"Progress: {i}/{sizeOfArray} elements sorted...")

    end_time = time.time()
    elapsed_time = end_time - start_time
    mem_after = process.memory_info().rss
    mem_used = mem_after - mem_before

    elapsed_time = round(elapsed_time, 2)
    mem_used = round(mem_used / (1024 * 1024), 2)

    print(f"Sorting completed in {elapsed_time:.2f} seconds.")
    print(f"Memory used: {mem_used:.2f} MB")

    return df, elapsed_time, mem_used

# # Test the selection sort function
# if __name__ == "__main__":
#     try:
#         # Read the file using pandas
#         print("Reading data from excel...")
#         CVE_file_path = r'CVE data\small_set_for_testing.xlsx'  # Adjust the path as needed
#         data = pd.read_excel(CVE_file_path)
#         print("Data read successfully.")

#         # Perform selection sort
#         sorted_df, elapsed_time, mem_used = selection_sort_with_dataframe(data, custom_sort_key, data.columns[0])

#         # Print the sorted DataFrame and the metrics
#         print(sorted_df.head())
#         print(f"Sorting completed in {elapsed_time:.2f} seconds.")
#         print(f"Memory used: {mem_used:.2f} MB")

#         # Save the sorted DataFrame to a new Excel file for verification
#         sorted_file_path = 'Sorted CVE/SelectionSort.xlsx'
#         sorted_df.to_excel(sorted_file_path, index=False)
#         print(f"Sorted file saved to {sorted_file_path}")

#     except Exception as e:
#         print(f'Error processing file: {str(e)}')
