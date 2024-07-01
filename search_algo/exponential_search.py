import pandas as pd
import math
import time
import psutil

def iterative_binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1

def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0
    
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    
    return iterative_binary_search(arr, i // 2, min(i, n-1), x)

def exponential_search_dataframe(df, search_value, column_name):
    start_time = time.time()
    process = psutil.Process()
    mem_before = process.memory_info().rss

    df_sorted = df.sort_values(by=column_name)
    search_list = df_sorted[column_name].tolist()
    index = exponential_search(search_list, len(search_list), search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time
    mem_after = process.memory_info().rss
    mem_used = mem_after - mem_before

    elapsed_time = round(elapsed_time, 2)
    mem_used = round(mem_used / (1024 * 1024), 2)

    if index != -1:
        return df_sorted.iloc[index], elapsed_time, mem_used
    else:
        return None, elapsed_time, mem_used

if __name__ == "__main__":
    try:
        # Read the file using pandas
        CVE_file_path = r'CVE data\small_set_for_testing.xlsx'  # Adjust the path as needed
        data = pd.read_excel(CVE_file_path)
        
        # Prompt the user for the value to search for
        search_value = input("Enter the CVE value to search for: ")
        
        # Perform exponential search
        result, elapsed_time, mem_used = exponential_search_dataframe(data, search_value, data.columns[0])
        
        # Display the result
        if result is not None:
            print("Match found:")
            print(result)
        else:
            print("No match found.")

        # Print time and memory usage
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Memory used: {mem_used:.2f} MB")

    except Exception as e:
        print(f'Error processing file: {str(e)}')
