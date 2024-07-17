import numpy as np
from collections import defaultdict
from functools import lru_cache

levenshtein_cache = defaultdict(dict)

@lru_cache(maxsize=None)
def calculate_levenshtein(token1, token2):
    if token1 not in levenshtein_cache[token2]:
        levenshtein_cache[token2][token1] = levenshtein(token1, token2)
    return levenshtein_cache[token2][token1]

def levenshtein(token1, token2):
    distance = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distance[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distance[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distance[t1][t2] = distance[t1 - 1][t2 - 1]
            else:
                insert_cost = distance[t1][t2 - 1]
                delete_cost = distance[t1 - 1][t2]
                replace_cost = distance[t1 - 1][t2 - 1]

                distance[t1][t2] = min(insert_cost + 1, delete_cost + 1, replace_cost + 1)

    return distance[len(token1)][len(token2)]

def find_similar_words(df, column, search_term, threshold=3):
    similar_words = set()
    for data in df[column].astype(str):
        distance = calculate_levenshtein(search_term.lower(), data.lower())
        if distance < threshold:
            similar_words.add(data)
    return similar_words
