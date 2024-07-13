import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/SIT University/Y1T3/Data Structure and Algorithm/Project/FINAL_DATASET.xlsx'  
sheet_name = 'Sheet1'  

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Define the scoring mapping
score_mapping = {'NONE': 0, 'PARTIAL': 0.5, 'LOW' : 0.5, 'HIGH': 1, 'COMPLETE': 1}

# Apply the mapping to calculate the scores
df['Confidentiality Score'] = df['Confidentiality Impact'].map(score_mapping)
df['Integrity Score'] = df['Integrity Impact'].map(score_mapping)
df['Availability Score'] = df['Availability Impact'].map(score_mapping)

# Sum the scores for each year and each impact factor
yearly_scores = df.groupby('Year')[['Confidentiality Score', 'Integrity Score', 'Availability Score']].sum()

# Plotting the data
yearly_scores.plot(kind='bar', stacked=True, figsize=(12, 8))

# Set the chart title and labels
plt.title('Impact Scores per Year')
plt.xlabel('Year')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.legend(title='Impact Type')
plt.tight_layout()

# Display the bar chart
plt.show()
