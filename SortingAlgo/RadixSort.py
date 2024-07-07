import pandas as pd
import time

# Define radix sort function for the digits
def radix_sort(arr):
    max_len = len(str(max(arr)))
    for exp in range(max_len):
        bins = [[] for _ in range(10)]
        for num in arr:
            bins[(num // 10**exp) % 10].append(num)
        arr = [num for bin in bins for num in bin]
    return arr

# Define the file path for reading and writing
input_file_path = '..\\CVE data\\filtered_cve_list_USETHIS.xlsx'
output_file_path = '..\\CVE data\\sorted_cve_list.xlsx'

# Read the Excel file
df = pd.read_excel(input_file_path)

# Extract the year and the digits after the dash
df['Year'] = df['CVE ID'].apply(lambda x: int(x.split('-')[0]))
df['Digits'] = df['CVE ID'].apply(lambda x: int(x.split('-')[1]))

# Sort by year first
df = df.sort_values(by=['Year'])

# Measure the time taken to sort
start_time = time.time()

# For each year, sort the digits using radix sort
sorted_rows = []
for year in df['Year'].unique():
    year_df = df[df['Year'] == year]
    sorted_digits = radix_sort(year_df['Digits'].tolist())
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
sorting_algorithm = "Radix Sort"
time_taken, sorting_algorithm, sorted_full_df.head()  # .head() to show the first few rows
