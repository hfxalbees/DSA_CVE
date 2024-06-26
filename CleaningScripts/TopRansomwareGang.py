import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import time

# Custom Merge Sort Functions
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left_half = mergeSort(array[:mid])
    right_half = mergeSort(array[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:  # Compare counts, assuming descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


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

def get_sorted_ransomware_groups(file_path):
    df = load_data(file_path)
    group_count = count_ransomware_groups(df)
    group_list = [(group, count) for group, count in group_count.items()]
    
    # Convert to list of tuples and prepare for sorting
    sort_list = [(group, count) for group, count in group_count.items()]
    
    # Start timing
    start_time = time.time()
    
    # Apply custom merge sort
    sorted_list = mergeSort(sort_list)
    
    # End timing and convert to milliseconds
    elapsed_time_ms = (time.time() - start_time) * 1000
    
    print(f"Merge sort time: {elapsed_time_ms:.2f} ms")  # This should print to the console

    # Convert list back to DataFrame
    sorted_groups = pd.DataFrame(sorted_list, columns=['Ransomware Group', 'Count'])

    return sorted_groups, elapsed_time_ms


# Plot the top 10 ransomware groups
def plot_top_ransomware_groups(file_path):
    sorted_groups, elapsed_time_ms = get_sorted_ransomware_groups(file_path)  # Unpack the tuple
    top_10_groups = sorted_groups.head(10)  # Select only the top 10 groups

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.bar(top_10_groups['Ransomware Group'], top_10_groups['Count'], color='blue')
    plt.xlabel('Ransomware Group')
    plt.ylabel('Count')
    plt.title('Top 10 Ransomware Groups')
    plt.xticks(rotation=45, ha='right')  # Rotate the labels to prevent overlap and adjust alignment
    plt.tight_layout()  # Adjust subplots to fit into figure area
    plt.savefig('static/images/top_ransomware_groups.png')
    plt.close()  # Close the plot to free up memory
