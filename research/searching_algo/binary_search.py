def binary_search(data, key, search_key):
    # Ensure data is sorted by key
    data_sorted = data.sort_values(by=key).reset_index(drop=True)
    
    # Extract the column to search through
    arr = data_sorted[key].tolist()
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == search_key:
            return data_sorted.iloc[mid].to_dict()  # Return the entire row as a dictionary if found
        elif arr[mid] < search_key:
            left = mid + 1
        else:
            right = mid - 1
    return None  # If no match found
