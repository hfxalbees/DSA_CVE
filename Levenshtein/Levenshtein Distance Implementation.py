import numpy
import pandas

excel_file = pandas.read_csv("C:/Users/wenzh/Downloads/Dataset.csv")


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


print("Available Columns:")
for column in excel_file.columns:
    print("-", column)

user_specified_column = input("\nSelect the column of interest: ")
user_search_string = input("\nInput the search string: ")
closely_matched_word_set = set()

exact_match_found = False

for data in excel_file[user_specified_column]:
    distance = levenshtein(user_search_string, data.lower())

    if distance == 0:
        exact_match_found = True
        break
    elif distance < 2:
        closely_matched_word_set.add(data)

if exact_match_found:
    print(f"\nYou have entered the following string:", user_search_string)
else:
    if len(closely_matched_word_set) > 0:
        print("\nIt looks like there is a typo in your input.")
        print("Did you mean any of the following?")
        print(closely_matched_word_set)
    else:
        print("\nIt looks like there are no similar words found within the dictionary.")
