# Done By Chen YiHeng
import pandas as pd
import time

def sort_cve_data(input_file_path, output_file_path, sorting_algorithm='radix'):
    # Define sorting function based on algorithm choice
    def radix_sort(arr):
        max_len = len(str(max(arr)))
        for exp in range(max_len):
            bins = [[] for _ in range(10)]
            for num in arr:
                bins[(num // 10 ** exp) % 10].append(num)
            arr = [num for bin in bins for num in bin]
        return arr

    def bucket_sort(arr):
        max_val = max(arr)
        buckets = [[] for _ in range(max_val + 1)]
        for num in arr:
            buckets[num].append(num)
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(bucket)
        return sorted_arr

    # Read the Excel file
    df = pd.read_excel(input_file_path)

    # Extract the year and the digits after the dash
    df['Year'] = df['CVE ID'].apply(lambda x: int(x.split('-')[0]))
    df['Digits'] = df['CVE ID'].apply(lambda x: int(x.split('-')[1]))

    # Sort by year first
    df = df.sort_values(by=['Year'])

    # Measure the time taken to sort
    start_time = time.time()

    # Choose sorting algorithm based on input
    if sorting_algorithm == 'radix':
        sort_function = radix_sort
    elif sorting_algorithm == 'bucket':
        sort_function = bucket_sort
    else:
        raise ValueError("Sorting algorithm not supported.")

    # For each year, sort the digits using the chosen algorithm
    sorted_rows = []
    for year in df['Year'].unique():
        year_df = df[df['Year'] == year]
        sorted_digits = sort_function(year_df['Digits'].tolist())
        sorted_year_df = year_df.set_index('Digits').loc[sorted_digits].reset_index()
        sorted_rows.append(sorted_year_df)

    # Concatenate all the sorted dataframes
    sorted_full_df = pd.concat(sorted_rows, ignore_index=True).drop(columns=['Year', 'Digits'])

    # Measure the end time and calculate the elapsed time
    end_time = time.time()
    time_taken = end_time - start_time

    # Export the sorted dataframe to an Excel file
    sorted_full_df.to_excel(output_file_path, index=False)

    # Return the time taken and sorted dataframe
    return time_taken, sorted_full_df
