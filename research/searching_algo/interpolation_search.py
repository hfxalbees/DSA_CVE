import pandas as pd

def interpolation_search(arr, x):
    """Perform an interpolation search on a list."""
    low, high = 0, len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        # Prevent division by zero if the values are the same
        range_val = arr[high] - arr[low]
        if range_val == 0:
            if arr[low] == x:
                return low
            return -1

        # Calculate position using interpolation formula
        pos = low + int((high - low) * ((x - arr[low]) / range_val))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def extract_numerical_part(cve_id):
    """Extract the numerical part from a CVE ID."""
    try:
        return float(cve_id.split('-')[-1])  # Assumes the last part after the hyphen is numeric
    except ValueError:
        return None

def interpolation_search_dataframe(data, key, search_key):
    """Perform an interpolation search on the provided DataFrame for the given numerical part of search_key in the specified column key."""
    try:
        # Extract numerical parts from the CVE IDs in the DataFrame
        data[key] = data[key].apply(extract_numerical_part)
        search_key = extract_numerical_part(search_key)  # Convert the search key
        if search_key is None:
            return "Search key conversion failed: Invalid format"

        # Ensure data is sorted by the key column
        data_sorted = data.sort_values(by=key)
        search_list = data_sorted[key].dropna().tolist()

        index = interpolation_search(search_list, search_key)
        if index != -1:
            return data_sorted.iloc[index].to_dict()  # Return the matching row as a dictionary
        else:
            return None
    except Exception as e:
        return f"Error: {str(e)}"
