import pandas as pd
import numpy as np
import re
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
    
    if abs(len1 - len2) > max_dist:
        return max_dist + 1

    distance = np.zeros((len1 + 1, len2 + 1), dtype=int)

    for i in range(len1 + 1):
        distance[i][0] = i
    for j in range(len2 + 1):
        distance[0][j] = j

    for i in range(1, len1 + 1):
        min_row_distance = max_dist + 1
        for j in range(1, len2 + 1):
            cost = 0 if token1[i - 1] == token2[j - 1] else 1

            distance[i][j] = min(
                distance[i - 1][j] + 1,
                distance[i][j - 1] + 1,
                distance[i - 1][j - 1] + cost
            )
            min_row_distance = min(min_row_distance, distance[i][j])
        
        if min_row_distance > max_dist:
            return max_dist + 1

    return distance[len1][len2]

def find_similar_words(df, column, search_term, threshold=1):
    clean_search_term = re.sub(r'\W+', '', search_term.strip().lower())
    for data in df[column].astype(str):
        for word in data.strip().lower().split():
            clean_word = re.sub(r'\W+', '', word)
            distance = calculate_levenshtein(clean_search_term, clean_word, threshold)
            print(f'Comparing "{clean_search_term}" with "{clean_word}": Distance = {distance}')
            if distance <= threshold:
                return {clean_word}  # Early termination if a similar word is found
    return set()

# # Example usage with a DataFrame
# data = {
#     'description': ['example) one', 'example two', 'example three', 'modules\\currencies\\index.php', 'ransomwart and the load_signed_id'],
#     'other_column': ['data1', 'data2', 'data3', 'data4', 'data5']
# }
# df = pd.DataFrame(data)

# search_term = "examplr"
# similar_words = find_similar_words(df, 'description', search_term, threshold=2)
# print("Similar words found:", similar_words)
