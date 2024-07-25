import pandas as pd

def compute_lps(pattern):
    """
    Compute the LPS array (Longest Prefix Suffix) for the given pattern.
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
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
    """
    Perform KMP search on the given text for the specified pattern.
    Returns True if the pattern is found, else False.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return True  # Pattern found
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False  # Pattern not found

def search_dataframe_kmp(df, pattern, column_name):
    """
    Search a DataFrame column for a pattern using the KMP search algorithm.
    """
    pattern = pattern.lower()

    def kmp_apply(text):
        return kmp_search(text.lower(), pattern)

    matches = df[df[column_name].apply(kmp_apply)]
    return matches
