import pandas as pd
import time

# Load the Excel file
excel_file = 'updated_CVE_Data_with_Attack_Type.xlsx'  # Replace with your actual file path
sheet_name = 'Sheet1'  # Replace with your sheet name if different

# Load data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Define a function to extract the year and id from a CVE ID
def extract_year_id(cve_id):
    parts = cve_id.split('-')
    year = int(parts[1])
    cve_id = int(parts[2])
    return year, cve_id

# Define insertion sort function for CVE IDs
def insertion_sort_cve(cve_list):
    for i in range(1, len(cve_list)):
        key = cve_list[i]
        key_year_id = extract_year_id(key['CVE ID'])
        j = i - 1
        while j >= 0:
            current_cve_id = cve_list[j]
            current_year_id = extract_year_id(current_cve_id['CVE ID'])
            if current_year_id > key_year_id or (current_year_id == key_year_id and current_cve_id['CVE ID'] > key['CVE ID']):
                cve_list[j + 1] = cve_list[j]
                j -= 1
            else:
                break
        cve_list[j + 1] = key

# Timing the sort operation for CVE IDs using Insertion Sort
start_time = time.time()

# Convert DataFrame to a list of dictionaries for sorting
cve_list = df.to_dict('records')

# Perform Insertion Sort on CVE IDs
insertion_sort_cve(cve_list)

# Convert sorted list back to DataFrame
sorted_df_insertion = pd.DataFrame(cve_list)

# Save sorted DataFrame to Excel
output_excel_file_insertion = 'insertion_sorted.xlsx'  # Replace with your desired output file path for Insertion Sort
sorted_df_insertion.to_excel(output_excel_file_insertion, index=False, sheet_name='Sorted Sheet (Insertion Sort)')

# Calculate elapsed time
insertion_sort_time = time.time() - start_time

# Print the timing results
print(f"Insertion Sort completed in {insertion_sort_time:.4f} seconds.")
print(f"Sorted Excel with all columns saved to '{output_excel_file_insertion}' (Insertion Sort)")
