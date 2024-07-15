import numpy

dictionary_path = "Levenshtein/100_common_words.txt"

with open(dictionary_path, "r") as dictionary:
    dictionary_data = dictionary.read().splitlines()


def levenshtein(token1, token2):
    distance = numpy.zeros((len(token1) + 1, len(token2) + 1))

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

                if insert_cost <= delete_cost and insert_cost <= replace_cost:
                    distance[t1][t2] = insert_cost + 1
                elif delete_cost <= insert_cost and delete_cost <= replace_cost:
                    distance[t1][t2] = delete_cost + 1
                else:
                    distance[t1][t2] = replace_cost + 1

    return distance[len(token1)][len(token2)]


user_input = input("\nInput a string: ")
closely_matched_word_list = []

exact_match_found = False

for data in dictionary_data:
    distance = levenshtein(user_input, data)

    if distance == 0:
        exact_match_found = True
        break
    elif distance < 2:
        closely_matched_word_list.append(data)

if exact_match_found:
    print(f"\nYou have entered the following string:", user_input)
else:
    if len(closely_matched_word_list) > 0:
        print("\nIt looks like there is a typo in your input.")
        print("Did you mean any of the following?")
        print(closely_matched_word_list)
    else:
        print("\nIt looks like there are no similar words found within the dictionary.")
