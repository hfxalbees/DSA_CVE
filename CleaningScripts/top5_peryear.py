import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset from Excel
file_path = 'D:\\SIT University\\Y1T3\\Data Structure and Algorithm\\Project\\updated_CVE_Data_with_Attack_Type.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Step 2: Filter out attack type 'other'
df_filtered = df[df['Attack Type'] != 'Other']

# Step 3: Group by Year and Attack Type, count occurrences
grouped = df_filtered.groupby(['Year', 'Attack Type']).size().reset_index(name='Count')

# Step 4: Plotting top 5 attack types per year
years = sorted(df_filtered['Year'].unique())

for year in years:
    top_attacks = grouped[grouped['Year'] == year].nlargest(5, 'Count')
    plt.figure(figsize=(10, 6))
    plt.bar(top_attacks['Attack Type'], top_attacks['Count'], color='skyblue')
    plt.xlabel('Attack Type')
    plt.ylabel('Count')
    plt.title(f'Top 5 Attack Types in {year}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
