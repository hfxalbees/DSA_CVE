import pandas as pd
import math
import time
import psutil

def jump_search(arr, x, n):
    """Performs jump search on a sorted list."""
    step = math.sqrt(n)
    prev = 0
    
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[int(prev)] == x:
        return int(prev)
    
    return -1

def jump_search_dataframe(df, search_value, column_name):
    """Performs jump search on a DataFrame column and measures time and memory usage."""
    start_time = time.time()
    process = psutil.Process()
    mem_before = process.memory_info().rss

    df_sorted = df.sort_values(by=column_name)
    search_list = df_sorted[column_name].tolist()
    index = jump_search(search_list, search_value, len(search_list))

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
        
        # Perform jump search
        result, elapsed_time, mem_used = jump_search_dataframe(data, search_value, data.columns[0])
        
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
