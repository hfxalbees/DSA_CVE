import pandas as pd

def brute_force_search(text, pattern):
    """Simple brute force search to find a pattern within a text."""
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return True
    return False

def search_dataframe_brute_force(df, pattern, column_name):
    """Search a DataFrame column for a pattern using brute force method."""
    try:
        matches = []
        for index, row in df.iterrows():
            if brute_force_search(str(row[column_name]), pattern):
                matches.append(row)
        if not matches:
            return "No matches found."
        return pd.DataFrame(matches)
    except Exception as e:
        return f"An error occurred: {str(e)}"
