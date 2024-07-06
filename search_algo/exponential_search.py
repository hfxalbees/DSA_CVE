import pandas as pd
import time

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
    start_time = time.time()  # Start timer for performance measurement

    df_sorted = df.sort_values(by=column_name)
    search_list = df_sorted[column_name].tolist()
    index = exponential_search(search_list, len(search_list), search_value)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds for consistency


    if index != -1:
        return "Exponential Search", elapsed_time, df_sorted.iloc[index]
    else:
        return "Exponential Search", elapsed_time, None

if __name__ == "__main__":
    try:
        # Read the file using pandas
        CVE_file_path = r'CVE data\small_set_for_testing.xlsx'  # Adjust the path as needed
        data = pd.read_excel(CVE_file_path)
        
        # Prompt the user for the value to search for
        search_value = input("Enter the CVE value to search for: ")
        
        # Perform exponential search
        algorithm_type, elapsed_time, result = exponential_search_dataframe(data, search_value, data.columns[0])
        
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
