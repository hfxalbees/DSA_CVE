import pandas as pd
import time

# Define bucket sort function for the digits
def bucket_sort(arr):
    max_val = max(arr)
    buckets = [[] for _ in range(max_val + 1)]
    for num in arr:
        buckets[num].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr

# Define the file path for reading and writing
input_file_path = '..\\CVE data\\filtered_cve_list_USETHIS.xlsx'
output_file_path = '..\\CVE data\\sorted_cve_list_bucket_sort.xlsx'

# Read the Excel file
df = pd.read_excel(input_file_path)

# Extract the year and the digits after the dash
df['Year'] = df['CVE ID'].apply(lambda x: int(x.split('-')[0]))
df['Digits'] = df['CVE ID'].apply(lambda x: int(x.split('-')[1]))

# Sort by year first
df = df.sort_values(by=['Year'])

# Measure the time taken to sort
start_time = time.time()

# For each year, sort the digits using bucket sort
sorted_rows = []
for year in df['Year'].unique():
    year_df = df[df['Year'] == year]
    sorted_digits = bucket_sort(year_df['Digits'].tolist())
    sorted_year_df = year_df.set_index('Digits').loc[sorted_digits].reset_index()
    sorted_rows.append(sorted_year_df)

# Concatenate all the sorted dataframes
sorted_full_df = pd.concat(sorted_rows, ignore_index=True).drop(columns=['Year', 'Digits'])

# Measure the end time and calculate the elapsed time
end_time = time.time()
time_taken = end_time - start_time

# Export the sorted dataframe to an Excel file
sorted_full_df.to_excel(output_file_path, index=False)

# Return the required outputs
sorting_algorithm = "Bucket Sort"
time_taken, sorting_algorithm, sorted_full_df.head()  # .head() to show the first few rows
