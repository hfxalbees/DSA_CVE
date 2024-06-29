import pandas as pd
import time

# Load the Excel file
file_path = 'updated_CVE_Data_with_Attack_Type.xlsx'
df = pd.read_excel(file_path)

# Define a function to extract the year and id from a CVE ID
def extract_year_id(cve_id):
    parts = cve_id.split('-')
    year = int(parts[1])
    cve_id = int(parts[2])
    return year, cve_id

# Define Shell Sort function for CVE IDs
def shell_sort_cve(cve_list):
    n = len(cve_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = cve_list[i]
            temp_year_id = extract_year_id(temp['CVE ID'])
            j = i
            while j >= gap and extract_year_id(cve_list[j - gap]['CVE ID']) > temp_year_id:
                cve_list[j] = cve_list[j - gap]
                j -= gap
            cve_list[j] = temp
        gap //= 2

# Timing the sort operation for CVE IDs using Shell Sort
start_time = time.time()

# Convert DataFrame to a list of dictionaries for sorting
cve_list = df.to_dict('records')

# Perform Shell Sort on CVE IDs
shell_sort_cve(cve_list)

# Convert sorted list back to DataFrame
sorted_df = pd.DataFrame(cve_list)

# Save sorted DataFrame to Excel
output_excel_file = 'CVE_ID_Sorted_Shell.xlsx'
sorted_df.to_excel(output_excel_file, index=False)

# Calculate elapsed time
shell_sort_time = time.time() - start_time

# Print the timing results
print(f"Time taken to sort by CVE ID using Shell Sort: {shell_sort_time:.4f} seconds")
print(f"Sorted Excel with all columns saved to '{output_excel_file}'")
