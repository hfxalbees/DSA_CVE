import pandas as pd
import time

def ternary_search(cve_list, target_cve):
    """Perform a ternary search on a list."""
    left, right = 0, len(cve_list) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if cve_list[mid1]['CVE ID'] == target_cve:
            return mid1
        elif cve_list[mid2]['CVE ID'] == target_cve:
            return mid2
        elif target_cve < cve_list[mid1]['CVE ID']:
            right = mid1 - 1
        elif target_cve > cve_list[mid2]['CVE ID']:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

def ternary_search_dataframe(data, key, search_key):
    """Perform a ternary search on the provided DataFrame for the given search_key in the specified column key."""
    # Ensure data is sorted by key
    data_sorted = data.sort_values(by=key).reset_index(drop=True)
    cve_list = data_sorted.to_dict(orient='records')
    
    index = ternary_search(cve_list, search_key)
    if index != -1:
        return data_sorted.iloc[index].to_dict()  # Return the matching row as a dictionary
    else:
        return None

