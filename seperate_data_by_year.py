import pandas as pd

# Load the data
file_path = 'CVE_Data from NVD database obtained on 08 July 2023.xlsx'
data = pd.read_excel(file_path)

# Define a function to extract the year from the CVE ID and convert it to an integer
def extract_year(cve_id):
    return int(cve_id.split('-')[1])

# Apply the function to the 'CVE ID' column and create a new 'Year' column
data['Year'] = data['CVE ID'].apply(extract_year)

# Filter the data to keep only rows with 'Year' >= 2016
filtered_data = data[data['Year'] >= 2015]

# Split the data by year and save each subset to a separate file
for year in filtered_data['Year'].unique():
    subset = filtered_data[filtered_data['Year'] == year]
    file_name = f'CVE_Data_{year}.xlsx'
    subset.to_excel(file_name, index=False)

# Confirming files are created
print("Files created for each year with CVE IDs from 2015 onwards.")
