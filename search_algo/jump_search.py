import pandas as pd
import math
import time

def jump_search(arr, x, n):
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
    start_time = time.time()  # Using time.time() for timing
    df_sorted = df.sort_values(by=column_name)
    search_list = df_sorted[column_name].tolist()
    index = jump_search(search_list, search_value, len(search_list))

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds

    if index != -1:
        return "Jump Search", elapsed_time, df_sorted.iloc[index]
    else:
        return "Jump Search", elapsed_time, None

if __name__ == "__main__":
    try:
        # Read the file using pandas
        print("Reading excel file...")
        CVE_file_path = r'CVE data/FINAL_DATASET.xlsx'
        data = pd.read_excel(CVE_file_path)
        
        # Prompt the user for the value to search for
        search_value = input("Enter the CVE value to search for: ")
        
        # Perform jump search
        algorithm_type, elapsed_time, result = jump_search_dataframe(data, search_value, data.columns[0])
        
        # Display the result
        if result is not None:
            print("Match found:")
            print(result)
        else:
            print("No match found.")
        
        # Print algorithm type and time taken
        print(f"Algorithm Type: {algorithm_type}")
        print(f"Time taken: {elapsed_time:.2f} ms")

    except Exception as e:
        print(f'Error processing file: {str(e)}')
