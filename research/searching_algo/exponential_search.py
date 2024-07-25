import pandas as pd

def iterative_binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def list_exponential_search(arr, x):
    """Perform an exponential search on a list."""
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i = i * 2
    return iterative_binary_search(arr, i // 2, min(i, len(arr)-1), x)

def exponential_search(data, key, search_key):
    """Perform an exponential search on the provided DataFrame for the given search_key in the specified column key."""
    # Ensure data is sorted by key
    data_sorted = data.sort_values(by=key).reset_index(drop=True)
    search_list = data_sorted[key].tolist()
    index = list_exponential_search(search_list, search_key)
    if index != -1:
        return data_sorted.iloc[index].to_dict()  # Return the matching row as a dictionary
    else:
        return None
