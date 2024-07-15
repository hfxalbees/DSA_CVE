import numpy as np

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

                distance[t1][t2] = min(insert_cost, delete_cost, replace_cost) + 1

    return distance[len(token1)][len(token2)]

def find_closest_match(search_term, column_data, threshold=2):
    min_distance = float('inf')
    closest_match = search_term
    for value in column_data:
        distance = levenshtein(search_term.lower(), str(value).lower())
        if distance < min_distance and distance <= threshold:
            min_distance = distance
            closest_match = value
    return closest_match if min_distance <= threshold else search_term
