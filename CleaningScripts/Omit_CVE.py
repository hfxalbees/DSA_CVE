import pandas as pd

# Load the data from the Excel file
file_path = 'CVE data/CVE_Data from NVD database obtained on 08 July 2023.xlsx'  # Update this path as needed
df = pd.read_excel(file_path)

# Print the original DataFrame
print("Original Data:")
print(df.head())

# Remove "CVE-" from the 'CVE ID' column
df['CVE ID'] = df['CVE ID'].str.replace('CVE-', '')

# Print the updated DataFrame to confirm changes
print("Updated Data:")
print(df.head())

# Save the updated DataFrame back to an Excel file
df.to_excel('CVE data\updated_cve_list.xlsx', index=False)
