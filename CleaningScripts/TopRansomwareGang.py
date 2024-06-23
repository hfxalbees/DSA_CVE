import pandas as pd
from collections import Counter

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
