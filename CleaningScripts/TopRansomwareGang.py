import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load the ransomware data
def load_data(file_path):
    return pd.read_excel(file_path)

# Count ransomware groups from the dataset
def count_ransomware_groups(data):
    ransomware_groups = []
    for group_list in data['Ransomware Group Association']:
        groups = group_list.split(", ")
        ransomware_groups.extend(groups)
    return Counter(ransomware_groups)

# Get sorted data of top ransomware groups
def get_sorted_ransomware_groups(file_path):
    df = load_data(file_path)
    group_count = count_ransomware_groups(df)
    group_count_df = pd.DataFrame(group_count.items(), columns=['Ransomware Group', 'Count'])
    group_count_df['Ransomware Group'] = group_count_df['Ransomware Group'].str.replace('\n ', '', regex=False)
    sorted_groups = group_count_df.sort_values(by='Count', ascending=False, kind='mergesort')
    return sorted_groups

def plot_top_ransomware_groups(file_path):
    sorted_groups = get_sorted_ransomware_groups(file_path)
    top_10_groups = sorted_groups.head(10)  # Select only the top 10 groups

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.bar(top_10_groups['Ransomware Group'], top_10_groups['Count'], color='blue')  # You can change the color
    plt.xlabel('Ransomware Group')
    plt.ylabel('Count')
    plt.title('Top 10 Ransomware Groups')
    plt.xticks(rotation=45, ha='right')  # Rotate the labels to prevent overlap and adjust alignment
    plt.tight_layout()  # Adjust subplots to fit into figure area
    plt.savefig('static/images/top_ransomware_groups.png')
    plt.close()  # Close the plot to free up memory
