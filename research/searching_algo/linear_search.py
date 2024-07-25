import pandas as pd

def linear_search(data, key, search_key):
    """Perform a linear search on the provided data looking for the specified search key in the specified column."""
    for index, row in data.iterrows():
        if row[key] == search_key:
            return row.to_dict()  # Return the row as a dictionary if found
    return None  # Return None if the key is not found
