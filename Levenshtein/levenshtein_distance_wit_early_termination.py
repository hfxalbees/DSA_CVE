import numpy as np
from collections import defaultdict
from functools import lru_cache

levenshtein_cache = defaultdict(dict)

@lru_cache(maxsize=None)
def calculate_levenshtein(token1, token2, max_dist):
    if token1 not in levenshtein_cache[token2]:
        levenshtein_cache[token2][token1] = levenshtein(token1, token2, max_dist)
    return levenshtein_cache[token2][token1]

def levenshtein(token1, token2, max_dist):
    len1, len2 = len(token1), len(token2)
    
    # Early exit if the length difference is greater than max_dist
    if abs(len1 - len2) > max_dist:
        return max_dist + 1

    # Initialize the distance matrix
    distance = np.zeros((len1 + 1, len2 + 1), dtype=int)

    # Setup the first row and column of the matrix
    for i in range(len1 + 1):
        distance[i][0] = i
    for j in range(len2 + 1):
        distance[0][j] = j

    # Fill the distance matrix
    for i in range(1, len1 + 1):
        min_row_distance = max_dist + 1  # Start with a value larger than max_dist
        for j in range(1, len2 + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            distance[i][j] = min(
                distance[i - 1][j] + 1,  # Deletion
                distance[i][j - 1] + 1,  # Insertion
                distance[i - 1][j - 1] + cost  # Substitution
            )
            min_row_distance = min(min_row_distance, distance[i][j])
        
        # Early stopping if the minimum distance in this row exceeds max_dist
        if min_row_distance > max_dist:
            return max_dist + 1

    return distance[len1][len2]

def find_similar_words(df, column, search_term, threshold=3):
    similar_words = set()
    for data in df[column].astype(str):
        distance = calculate_levenshtein(search_term.lower(), data.lower(), threshold)
        if distance <= threshold:
            similar_words.add(data)
    return similar_words
