import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/SIT University/Y1T3/Data Structure and Algorithm/Project/FINAL_DATASET.xlsx'
sheet_name = 'Sheet1'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure 'Year' is of integer type
df['Year'] = df['Year'].astype(int)

# Group by 'Year' and 'Attack Type' and calculate the average Base Score
average_severity = df.groupby(['Year', 'Attack Type'])['Base Score'].mean().reset_index()

# Pivot the DataFrame to have years as index and attack types as columns
severity_pivot = average_severity.pivot(index='Year', columns='Attack Type', values='Base Score')

# Plot the results
plt.figure(figsize=(14, 8))
ax = plt.gca()

# Get a colormap directly
colors = plt.cm.tab20.colors

# Plot each line with a unique color
for idx, column in enumerate(severity_pivot.columns):
    severity_pivot[column].plot(kind='line', marker='o', ax=ax, color=colors[idx], label=column)

# Set the chart title and labels
plt.title('Change in Severity of Different Attack Types Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Base Score')
plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the line chart
plt.tight_layout()
plt.show()
