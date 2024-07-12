import pandas as pd

# Read the Excel file and convert it into a DataFrame
file_path = '..\\CVE data\\filtered_cve_list_USETHIS.xlsx'
df = pd.read_excel(file_path)

# Knuth-Morris-Pratt (KMP) Algorithm for pattern searching
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return True  # Pattern found
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False  # Pattern not found

# Function to search for CVE ID or description in the DataFrame
def search_cve_or_description(df, search_term):
    result = []
    search_term = search_term.lower()
    for index, row in df.iterrows():
        cve_id = row['CVE ID'].lower()
        description = row['Description'].lower()
        if kmp_search(cve_id, search_term) or kmp_search(description, search_term):
            result.append(row)
    return pd.DataFrame(result)

# Example usage
search_term = 'cros'  # Replace with the search term you want to use
search_results = search_cve_or_description(df, search_term)


# Print the search results
print(search_results)
