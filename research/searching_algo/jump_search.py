import pandas as pd
import math

def jump_search(arr, x):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0

    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

    return -1

def jump_search_dataframe(data, key, search_key):
    """Perform a jump search on the provided DataFrame for the given search_key in the specified column key."""
    # Ensure data is sorted by key
    data_sorted = data.sort_values(by=key).reset_index(drop=True)
    search_list = data_sorted[key].tolist()

    # Convert search_key to appropriate type if necessary
    try:
        search_key = type(search_list[0])(search_key)
    except ValueError:
        return "Type conversion error: Ensure search key is the correct type for comparison"

    index = jump_search(search_list, search_key)
    if index != -1:
        return data_sorted.iloc[index].to_dict()  # Return the matching row as a dictionary
    else:
        return None

