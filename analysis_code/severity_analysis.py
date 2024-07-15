import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/SIT University/Y1T3/Data Structure and Algorithm/Project/FINAL_DATASET.xlsx'  
sheet_name = 'Sheet1'  

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the 'Base Severity' column has the desired categories, including 'Critical' if present
severity_levels = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']

# Pivot the data to get counts of severity per year
severity_counts = df.pivot_table(index='Year', columns='Base Severity', aggfunc='size', fill_value=0)

# Reorder the columns to match the desired severity levels
severity_counts = severity_counts[severity_levels].fillna(0)

# Plotting the data
severity_counts.plot(kind='bar', stacked=True, figsize=(12, 8))

# Set the chart title and labels
plt.title('CVE Severity per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Base Severity')
plt.tight_layout()

# Display the bar chart
plt.show()
