import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/SIT University/Y1T3/Data Structure and Algorithm/Project/FINAL_DATASET.xlsx'  
sheet_name = 'Sheet1'  

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Calculate the average Impact Score for each Attack Type
average_scores = df.groupby('Attack Type')['Impact Score'].mean().sort_values()

# Plotting the average Impact Score for each Attack Type
plt.figure(figsize=(12, 8))
average_scores.plot(kind='barh', color='skyblue')

# Set the chart title and labels
plt.title('Average Impact Score per Attack Type')
plt.xlabel('Average Impact Score')
plt.ylabel('Attack Type')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the bar chart
plt.tight_layout()
plt.show()
