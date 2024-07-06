import pandas as pd

# Load the data
file_path = 'D:/SIT University/Y1T3\Data Structure and Algorithm/Project/CVE_Data/CVE_Data from NVD database obtained on 08 July 2023.xlsx'
data = pd.read_excel(file_path)

# Define a function to extract the year from the CVE ID and convert it to an integer
def extract_year(cve_id):
    return int(cve_id.split('-')[1])

# Apply the function to the 'CVE ID' column and create a new 'Year' column
data['Year'] = data['CVE ID'].apply(extract_year)

# Filter the data to keep only rows with 'Year' >= 2015
filtered_data = data[data['Year'] >= 2015]

# Filter out rows where the 'Description' column starts with '** REJECT **'
cleaned_data = filtered_data[~filtered_data['Description'].str.startswith('** REJECT **')]

# Update 'CVE ID' column format to YEAR-ID using .loc to avoid SettingWithCopyWarning
cleaned_data.loc[:, 'CVE ID'] = cleaned_data['CVE ID'].apply(lambda x: '-'.join(x.split('-')[1:]))

# Reorder columns to place 'CVE ID' as the first column
new_column_order = ['CVE ID'] + [col for col in cleaned_data.columns if col != 'CVE ID']
cleaned_data = cleaned_data[new_column_order]

# Save the cleaned data to a single Excel file
cleaned_file_path = 'CLEANED_DATASET.xlsx'
cleaned_data.to_excel(cleaned_file_path, index=False)

# Confirming file is created
print(f"Final cleaned data saved to: {cleaned_file_path}")
