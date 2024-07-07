# Done By Chen YiHeng
from sorting_module import sort_cve_data

input_file_path = '..\\CVE data\\filtered_cve_list_USETHIS.xlsx'
output_file_path = '..\\CVE data\\sorted_cve_list.xlsx'

# Call the sorting function
sorting_algorithm = 'radix'  # or 'bucket'
time_taken, sorted_dataframe = sort_cve_data(input_file_path, output_file_path, sorting_algorithm)

print(f"Time taken: {time_taken} seconds")
print("Sorted DataFrame:")
print(sorted_dataframe.head())
