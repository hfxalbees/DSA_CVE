import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/SIT University/Y1T3/Data Structure and Algorithm/Project/FINAL_DATASET.xlsx'  
sheet_name = 'Sheet1'  

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Count the number of entries for each year
year_counts = df['Year'].value_counts().sort_index()

# Create the bar chart
plt.figure(figsize=(10, 6))
year_counts.plot(kind='bar')
plt.title('CVE per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the bar chart
plt.show()
